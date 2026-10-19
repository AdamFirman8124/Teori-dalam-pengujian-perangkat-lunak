

# Generated at 2022-06-12 22:56:19.359529
# Unit test for method validate of class ArgumentSpecValidator

# Generated at 2022-06-12 22:56:26.855368
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

    # the age parameter should have been validated and coerced to an int
    assert result._validated_parameters['age'] == 42

    assert not result.errors.messages



# Generated at 2022-06-12 22:56:36.202218
# Unit test for constructor of class ArgumentSpecValidator
def test_ArgumentSpecValidator():
    argument_spec = {
        "provider": {
            "type": "dict",
            "options": {
                "hostname": {"type": "str"},
                "port": {"type": "int"},
                "username": {"type": "str"},
                "password": {"type": "str", "no_log": True},
                "timeout": {"type": "int"},
                "aliases": ["pass"],
            },
            "aliases": ["rest"],
        },
        "transport": {"type": "str", "required": True, "choices": ["cli", "eapi"]},
        "port": {"type": "int", "default": 22},
        "username": {"type": "str"},
        "password": {"type": "str", "no_log": True},
    }


# Generated at 2022-06-12 22:56:46.486087
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    """ArgumentSpecValidator.validate() returns ValidationResult
    """
    base_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
        'sub': {
            'type': 'dict',
            'subspec': {
                'name': {'type': 'str'},
                'version': {'type': 'int'},
            }
        }
    }

    parameters = {
        'name': 'bo',
        'age': '42',
        'sub': {
            'name': 'module',
            'version': '0.2.2',
        },
    }

    validator = ArgumentSpecValidator(base_spec)
    result = validator.validate(parameters)
    assert isinstance(result, ValidationResult)

# Generated at 2022-06-12 22:56:54.186049
# Unit test for constructor of class ArgumentSpecValidator
def test_ArgumentSpecValidator():
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    }

    mutually_exclusive = None
    required_together = None
    required_one_of = None
    required_if = None
    required_by = None

    validator = ArgumentSpecValidator(argument_spec, mutually_exclusive, required_together, required_one_of, required_if, required_by)
    assert isinstance(validator, ArgumentSpecValidator)



# Generated at 2022-06-12 22:57:02.767154
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    argument_spec = {
                    'name': {'type': 'str'},
                    'age': {'type': 'int'},
                    'sub_spec': {'type': 'dict', 'options': {
                        'friend': {'type': 'str'},
                        'sub_sub_spec': {'type': 'dict', 'options': {
                            'dog': {'type': 'literal'},
                        }}
                    }}
                }


# Generated at 2022-06-12 22:57:13.625387
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    mutually_exclusive = [['mutually_exclusive1', 'mutually_exclusive2']]
    required_together = [['required_together1', 'required_together2']]
    required_one_of = [['required_one_of1', 'required_one_of2']]
    required_if = [['required_if1', 'required_if1', ['required_if2']]]
    required_by = {'required_by1': ['required_by2']}

    argument_spec = {'test_option': {'required': True, 'type': 'bool'},
                     'test_required_together1': {'required': True},
                     'test_required_together2': {'required': True}}

# Generated at 2022-06-12 22:57:21.532249
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    # Setup initial state
    mutually_exclusive1 = [['name', 'deprecated_name']]
    required_together1 = [['name']]
    argument_spec1 = {
        "name": {
            "type": "str"
        },
        "deprecated_name": {
            "type": "str",
            "removed_version": "2.10",
            "removed_at_date": "2021-01-01T00:00:00Z",
            "collection_name": "community.general",
            "aliases": ["name"],
        },
    }
    validator1 = ModuleArgumentSpecValidator(argument_spec1, mutually_exclusive1, required_together1)

    parameters1 = {
        "name": "bo",
        "deprecated_name": "bo",
    }



# Generated at 2022-06-12 22:57:29.930655
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    from ansible.module_utils.common.arg_spec import ModuleArgumentSpecValidator
    from ansible.module_utils.common.warnings import hide_deprecations, hide_errors

    validator = ModuleArgumentSpecValidator({'name': {'type': 'str', 'aliases': ['new_name']}, 'age': {'type': 'int'}})
    parameters = {'name': 'Alice', 'new_name': 'Bob'}

    with hide_deprecations():
        with hide_errors():
            result = validator.validate(parameters)

    assert result.error_messages == []

# Generated at 2022-06-12 22:57:39.683673
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
        'height': {'type': 'str'},
        'deprecated_field': {'type': 'str', 'deprecated': 'This field is deprecated'},
        'aliased_field': {'type': 'str', 'aliases': ['alias_field']},
        'parent_field': {'type': 'dict',
                         'options': {
                             'child_field': {'type': 'str'}
                         }}
    }

    parameters = {'name': 'bo', 'age': '42', 'height': '5\'10"'}


# Generated at 2022-06-12 22:57:53.060563
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
    assert(result.error_messages == []), \
        "Validation failed by producing an error: %s" % (", ".join(result.error_messages))
    expected_validated_params = {'name': 'bo', 'age': 42}

# Generated at 2022-06-12 22:58:00.528866
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


# Generated at 2022-06-12 22:58:00.935519
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    assert True

# Generated at 2022-06-12 22:58:08.096302
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    """Test ArgumentSpecValidator.validate"""

    # Test simple example.
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

    # Test mutually exclusive
    argument_spec = {
        'a': {'type': 'str'},
        'b': {'type': 'str'},
    }
    mutually_exclusive = [
        ['a', 'b']
    ]

    parameters_a = {
        'a': 'foo'
    }


# Generated at 2022-06-12 22:58:19.437497
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
        'validated_parameters': {'type': 'dict'},
    }
    mutually_exclusive = None
    required_together = None
    required_one_of = None
    required_if = None
    required_by = None

    validator = ArgumentSpecValidator(argument_spec,
        mutually_exclusive,
        required_together,
        required_one_of,
        required_if,
        required_by,
    )

    for i in range(1, 6):
        parameters = {
            'name': 'bo' + str(i),
            'age': str(i),
            'validated_parameters': {}
        }


# Generated at 2022-06-12 22:58:27.411968
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    my_argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    }

    parameters = {
        'name': 'bo',
        'age': '42',
    }

    validator = ModuleArgumentSpecValidator(my_argument_spec)
    result = validator.validate(parameters)

    if result.error_messages:
        sys.exit("Validation failed: {0}".format(", ".join(result.error_messages)))

    valid_params = result.validated_parameters

# Generated at 2022-06-12 22:58:34.132172
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    class MockResult:
        error_messages = ['mock error message']
        validated_parameters = {'mock parameter': 'mock value'}
        def __init__(self, validated_parameters):
            self._validated_parameters = validated_parameters
            self._deprecations = []
            self._warnings = []
        def __getattribute__(self, attr):
            return super(MockResult, self).__getattribute__(attr)
        @property
        def deprecations(self):
            return self._deprecations
        @property
        def warnings(self):
            return self._warnings

    module_argspec_validator = ModuleArgumentSpecValidator(dict())
    mock_validation_result = MockResult({'mock parameter': 'mock value'})
    module_arg

# Generated at 2022-06-12 22:58:44.583305
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    argument_spec = {'name': {'type': 'str', 'aliases': ['fn']}}
    parameters = {'name': 'bo', 'alias': 'fred'}
    validator = ModuleArgumentSpecValidator(argument_spec)

    class MockModule(object):
        deprecations = []

    class MockDeprecation(object):
        def __init__(self, deprecated_name, version, date, collection_name=None):
            self.deprecated_name = deprecated_name
            self.version = version
            self.date = date
            self.collection_name = collection_name

        def __eq__(self, other):
            if self.deprecated_name != other.deprecated_name:
                return False
            elif self.version != other.version:
                return False

# Generated at 2022-06-12 22:58:51.063392
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    parameters = {'name': 'bo', 'age': '42'}
    expected_result = {'name': 'bo', 'age': 42}
    argument_spec = {'name': {'type': 'str'}, 'age': {'type': 'int'}}

    try:
        validator = ArgumentSpecValidator(argument_spec)
        result = validator.validate(parameters)
    except:
        raise

    assert result.validated_parameters == expected_result

# Generated at 2022-06-12 22:58:58.042270
# Unit test for constructor of class ArgumentSpecValidator
def test_ArgumentSpecValidator():
    argument_spec = {
    "name": {
        "type": "str",
        "default": "bo",
        "required": True,
        "choices": ["bo", "ro"],
    },
    "age": {
        "type": "int",
        "default": 0,
        "required": True,
    },
    }
    mutually_exclusive = [
        ["name"],
        ["age"]
    ]
    required_together = [
        ["name", "age"],
        ["age"]
    ]

    required_one_of = [
        ["name", "age"]
    ] 

    required_if = [
        ["name", "bo", "age"]
    ] 

    required_by = {
        "name": ["age"]
    }


# Generated at 2022-06-12 22:59:09.499619
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    """
    Condition:
        - Check that ArgSpecValidator.validate raises exception with specified message
    """
    validator = ArgumentSpecValidator({}, required_if=[['a', 'b', ['c']]])
    parameters = {'a': 'b'}
    result = validator.validate(parameters)
    assert len(result.errors) == 1
    assert result.errors[0].args[0] == 'a (b) is required when c is set'

# Generated at 2022-06-12 22:59:17.669287
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    #test deprecate
    class DeprecateWarn:
        def __init__(self):
            self.last_warn = None
            self.warn_count = 0

        def deprecate(self, thing, version, date, collection_name):
            self.last_warn = thing
            self.warn_count += 1

    deprecate_warn = DeprecateWarn()

    #test warn
    class Warn:
        def __init__(self):
            self.last_warn = None
            self.warn_count = 0

        def warn(self, thing):
            self.last_warn = thing
            self.warn_count += 1

    warn = Warn()
    #test validate

# Generated at 2022-06-12 22:59:26.418274
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    '''Test validate method of class ModuleArgumentSpecValidator'''

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


# Generated at 2022-06-12 22:59:36.754946
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    from ansible.module_utils.common.parameters import ansible_deprecate
    from ansible.module_utils.common.warnings import AnsibleDeprecationWarning


# Generated at 2022-06-12 22:59:44.550483
# Unit test for method validate of class ModuleArgumentSpecValidator

# Generated at 2022-06-12 22:59:53.413760
# Unit test for constructor of class ArgumentSpecValidator
def test_ArgumentSpecValidator():

    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    }

    mutually_exclusive = [
        ['water', 'land'],
        ['deep', 'shallow'],
    ]

    required_together = [
        ['name', 'age']
    ]

    required_one_of = [
        ['name', 'age'],
        ['water', 'land']
    ]

    required_if = [
        ['name', 'bo', ['age']],
        ['water', 'no', ['land']],
    ]

    required_by = {
        'name': ['age'],
        'water': ['land'],
    }


# Generated at 2022-06-12 23:00:01.586249
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    # Scenario: Warnings and deprecations are issued after validation.
    # Given that a ModuleArgumentSpecValidator object is created with
    #  argument_spec and a parameter
    # When validate method is called for the parameter
    # Then there is no error
    #  And warnings and deprecations are issued after validation

    class ModuleArgumentSpecValidatorMock(ModuleArgumentSpecValidator):
        def __init__(self, *args, **kwargs):
            super(ModuleArgumentSpecValidatorMock, self).__init__(*args, **kwargs)

    class TestClass:
        def __init__(self):
            self.warnings = 0
            self.deprecations = 0

        def warn(self, msg):
            self.warnings += 1


# Generated at 2022-06-12 23:00:12.437160
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    def deprecate(self, msg, version=None, date=None, collection_name=None):
        msg_list.append(msg)
        date_list.append(date)
        version_list.append(version)
        collection_list.append(collection_name)

    msg_list = []
    version_list = []
    date_list = []
    collection_list = []
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    }
    mutually_exclusive = [["name", "age"]]
    required_together = []
    required_one_of = []
    required_if = []
    required_by = []

    parameters = {
        'name': 'bo',
        'age': '42',
    }



# Generated at 2022-06-12 23:00:13.491272
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    assert False, "No tests for this object yet"

# Generated at 2022-06-12 23:00:22.986530
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    # Test 001 validate function return value type
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    }
    parameters = {
        'age': '42',
    }
    validator = ArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)
    assert isinstance(result, ValidationResult)
    assert result.errors

    # Test 002 validate function return value type
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    }
    parameters = {
        'name': 'bo',
        'age': '42',
    }
    validator = ArgumentSpecValidator(argument_spec)

# Generated at 2022-06-12 23:00:34.162579
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    parameters = {
        'name': 'bo',
        'age': '42',
    }
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    }
    validator = ModuleArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)

    assert result.unsupported_parameters == set()
    assert result.validated_parameters == {'name': 'bo', 'age': 42}

# Generated at 2022-06-12 23:00:36.623156
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    validator = ModuleArgumentSpecValidator({})
    result = validator.validate({})

    assert isinstance(result, ValidationResult)

# Generated at 2022-06-12 23:00:42.273729
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    argument_spec = {
        'name': {'type': 'str', 'required': True},
        'age': {'type': 'int', 'required': True},
    }

    parameters = {
        'name': 'bo',
        'age': '42',
    }

    validator = ModuleArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)

    if result.error_messages:
        raise AssertionError(", ".join(result.error_messages))

    valid_params = result.validated_parameters


# Generated at 2022-06-12 23:00:53.464902
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    class MyError(Exception):

        def __init__(self, msg, **kwargs):
            self.msg = msg
            self.kwargs = kwargs

        def __str__(self):
            return "'msg': {msg}, 'kwargs': {kwargs}".format(msg=self.msg, kwargs=self.kwargs)

    class DeprecationError(Exception):

        def __init__(self, msg, **kwargs):
            self.msg = msg
            self.kwargs = kwargs

        def __str__(self):
            return "'msg': {msg}, 'kwargs': {kwargs}".format(msg=self.msg, kwargs=self.kwargs)

    class WarningError(Exception):

        def __init__(self, msg, **kwargs):
            self.msg = msg

# Generated at 2022-06-12 23:01:04.134200
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    parameters = {'module': 'testmodule', 'argument_spec': {'name': {'type': 'str'}, 'age': {'type': 'int'}},
                  'mutually_exclusive': None, 'required_together': None, 'required_one_of': None, 'required_if': None,
                  'required_by': None, 'required_if_value': None}

    parameters = {'name': 'bo', 'age': '42'}


# Generated at 2022-06-12 23:01:11.150488
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    #
    # Should not raise exceptions
    #
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    }

    parameters = {
        'name': 'bo',
        'age': 42,
    }

    validator = ArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)
    assert not result.error_messages


    #
    # Should raise exceptions
    #
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    }

    parameters = {
        'name': 'bo',
        'age': '42',
    }

    validator = ArgumentSpecValidator(argument_spec)

# Generated at 2022-06-12 23:01:21.590946
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    # Test simple argument spec
    validator = ArgumentSpecValidator(argument_spec={"name": {"type": "str"}})
    result = validator.validate({'name': 'bo'})
    assert result.validated_parameters == {'name': 'bo'}
    assert result.erro_messages == []

    # Test mutually exclusive error
    validator = ArgumentSpecValidator(argument_spec={"name": {"type": "str"}}, mutually_exclusive={'name', 'age'})
    result = validator.validate({'name': 'bo', 'age': '42'})
    assert result.validated_parameters == {'name': 'bo', 'age': '42'}

# Generated at 2022-06-12 23:01:30.988310
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
    assert not result.error_messages
    valid_params = result.validated_parameters
    assert 'name' in valid_params
    assert 'age' in valid_params
    assert isinstance(valid_params['name'], str)
    assert isinstance(valid_params['age'], int)

# Unit tests for class ModuleArgumentSpecValidator

# Generated at 2022-06-12 23:01:33.252751
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    ModuleArgumentSpecValidator(argument_spec={}, mutually_exclusive=[], required_together=[], required_one_of=[], required_if=[], required_by={}).validate({})

# Generated at 2022-06-12 23:01:40.200131
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

    assert not result.error_messages

# Generated at 2022-06-12 23:01:46.217911
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    val = ArgumentSpecValidator({})
    assert isinstance(val.validate({}), ValidationResult)
    assert isinstance(val.validate({}), ValidationResult)

# Generated at 2022-06-12 23:01:52.747689
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    parameter = {'name': 'bo', 'age': '42', 'state': 'present'}
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
        'state': {'type': 'str', 'default': 'present'}
    }

    result = ModuleArgumentSpecValidator(argument_spec).validate(parameter)

    assert result.validated_parameters['name'] == 'bo'
    assert result.validated_parameters['age'] == 42
    assert result.validated_parameters['state'] == 'present'

# Generated at 2022-06-12 23:02:00.313555
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    class TestModuleArgumentSpecValidator(ModuleArgumentSpecValidator):
        def __init__(self, *args, **kwargs):
            super(TestModuleArgumentSpecValidator, self).__init__(*args, **kwargs)

    module_argument_spec_validator = TestModuleArgumentSpecValidator({'name': {'type': 'str'},
                                                                      'age': {'type': 'int'}},
                                                                     mutually_exclusive=[['name', 'age']],
                                                                     required_together=[['name', 'age']])

    assert module_argument_spec_validator.validate({'name': 'bo'}) is not None

# Generated at 2022-06-12 23:02:10.560415
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    from ansible.module_utils.common.warnings import AnsibleDeprecationWarning
    from ansible.module_utils.common.warnings import AnsibleDeprecationWarning, AnsibleFilterDeprecationWarning
    from ansible.module_utils.common.warnings import AnsibleUndefinedVariableWarning

    import mock

    import pytest

    import sys

    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
        'money': {'type': 'float'},
        'groups': {'type': 'list'},
        'aliases': {'type': 'list'},
        'address': {'type': 'dict'},
    }


# Generated at 2022-06-12 23:02:18.333477
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
    assert result.validated_parameters == {
        'name': 'bo',
        'age': 42,
    }

# Generated at 2022-06-12 23:02:29.312429
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    """Unit test for method validate of class ModuleArgumentSpecValidator"""
    deprecations = []
    warnings = []

    # Test for deprecations and warnings
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
        'color': {'type': 'str', 'aliases': ['colour']},
        'fruit': {'type': 'str', 'aliases': ['fruit', 'vegetable']},
    }

    # test deprecation
    parameters = {
        'name': 'bo',
        'age': '42',
        'color': 'blue',
        'colour': 'red',
        'fruit': 'apple',
        'vegetable': 'carrot',
    }

# Generated at 2022-06-12 23:02:36.677409
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    """Test Module ArgumentSpecValidator.

    Note:
        This function executes the code to be tested and makes assertions about the results.

    Args:
        None

    Returns:
        None

    Raises:
        None
    """
    # Arrange
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    }
    parameters = {
        'name': 'bo',
        'age': '42',
    }
    expected = {'name': 'bo', 'age': 42}
    validator = ArgumentSpecValidator(argument_spec)

    # Act

    result = validator.validate(parameters)

    # Assert
    assert result.validated_parameters == expected

# Generated at 2022-06-12 23:02:47.141030
# Unit test for method validate of class ModuleArgumentSpecValidator

# Generated at 2022-06-12 23:02:52.247387
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    result = {}
    result['warning'] = None

# Generated at 2022-06-12 23:03:02.531483
# Unit test for constructor of class ArgumentSpecValidator
def test_ArgumentSpecValidator():
    argument_spec = {
        'src': {'required': True, 'type': 'str'},
        'dest': {'required': True, 'type': 'str'},
        'delegate_to': {'type': 'str'},
        'become_method': {'type': 'str', 'choices': ['sudo', 'su']},
        'remote_user': {'type': 'str'},
        'become_user': {'type': 'str'},
        'validate_certs': {'type': 'bool'},
    }
    mutually_exclusive = ['become_method', 'become_user']

# Generated at 2022-06-12 23:03:10.343040
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    from ansible.module_utils.common.arg_spec import MODULE_ARGUMENT_SPEC_VALIDATOR
    argument_spec = {'name': {'type': 'str'}, 'age': {'type': 'int'}, 'list': {'type': 'list'}}
    parameters = {'name': 'bo', 'age': '42', 'list': ['nested_list']}
    validator = MODULE_ARGUMENT_SPEC_VALIDATOR(argument_spec)
    result = validator.validate(parameters)
    assert result.validated_parameters['name'] == 'bo'
    assert result.validated_parameters['age'] == 42
    assert result.validated_parameters['list'] == ['nested_list']

# Generated at 2022-06-12 23:03:18.003006
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    from ansible.module_utils.six import PY3
    from ansible.module_utils._text import to_text

    ps = {'name': 'bo', 'age': '123'}
    spec = {'name': {'type': 'str'}, 'age': {'type': 'int'}}

    v = ArgumentSpecValidator(spec)
    result = v.validate(ps)
    assert result.validated_parameters == {"name": "bo", "age": 123}
    assert result.errors == AnsibleValidationErrorMultiple()

    ps = {'name': 'bo', 'age': '123', 'cats': ['fluffy', 'garfield']}

# Generated at 2022-06-12 23:03:22.510143
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    """Validate that the metadata for the ArgumentSpecValidator validate function is correct."""
    expected_return_result = ValidationResult
    assert ArgumentSpecValidator.validate.__annotations__['return'] == expected_return_result
    assert ArgumentSpecValidator.validate.__qualname__ == 'ArgumentSpecValidator.validate'

# Generated at 2022-06-12 23:03:29.251104
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

    assert not len(result.errors)

    assert result.validated_parameters['name'] == 'bo'
    assert result.validated_parameters['age'] == 42


# Generated at 2022-06-12 23:03:36.961033
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    class Validator(ModuleArgumentSpecValidator):
        def __init__(self, *args, **kwargs):
            super(Validator, self).__init__(*args, **kwargs)

        def validate(self, parameters):
            return super(Validator, self).validate(parameters)

    # Empty spec
    spec = {}

    # Empty parameters
    parameters = {}
    validator = Validator(spec)
    result = validator.validate(parameters)
    assert result.error_messages == []

    # No spec
    spec = None

    # Empty parameters
    parameters = {}
    validator = Validator(spec)
    result = validator.validate(parameters)
    assert result.error_messages == []

    #
    # Example 1
    #

    # Add spec
    spec

# Generated at 2022-06-12 23:03:43.460881
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    from ansible.module_utils.common.parameters import COMPLEX_ARGUMENT_SPECS
    from ansible.module_utils.common.arg_spec import ModuleArgumentSpecValidator

    result = ModuleArgumentSpecValidator(COMPLEX_ARGUMENT_SPECS).validate({
        'arg1': 'bar'
    })

    assert not result.errors
    assert result.validated_parameters['arg1'] == 'bar'

# Generated at 2022-06-12 23:03:52.964003
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    from ansible_collections.ansible.foo.tests.unit.compat import unittest

    class MockDeprecation:
        def __init__(self):
            self.call_count = 0

        def __call__(self, *args, **kwargs):
            self.call_count += 1
            self.args = args
            self.kwargs = kwargs

    class MockWarn:
        def __init__(self):
            self.call_count = 0

        def __call__(self, *args, **kwargs):
            self.call_count += 1
            self.args = args
            self.kwargs = kwargs


# Generated at 2022-06-12 23:04:00.601341
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    }
    mutually_exclusive = [['name', 'age']]
    required_one_of = [['name', 'age']]
    validator = ArgumentSpecValidator(argument_spec, mutually_exclusive=mutually_exclusive, required_one_of=required_one_of)

    parameters = {
        'name': 'bo',
        'age': '42',
    }

    result = validator.validate(parameters)
    assert result.error_messages == []
    assert result.validated_parameters['name'] == 'bo'
    assert result.validated_parameters['age'] == 42

# Generated at 2022-06-12 23:04:11.656868
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    from ansible.module_utils.six import PY3

    import types
    import sys
    if not PY3:
        import inspect
        getfullargspec = inspect.getargspec
    else:
        from inspect import getfullargspec

    # Initiation
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    }
    mutually_exclusive = [['name', 'age'], ['name']]
    required_together = [['name']]
    required_one_of = [['name']]

    parameters = {
        'name': 'bo',
        'age': '42',
    }

    # Test validate

# Generated at 2022-06-12 23:04:18.673412
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    # Test function to validate that deprecate and warn are correctly called
    my_deprecations = list()
    my_warnings = list()

    def deprecate_mock(msg, version=None, date=None, collection_name=None):
        my_deprecations.append(msg)

    def warn_mock(msg):
        my_warnings.append(msg)

    # Mocking calls to deprecate and warn
    ModuleArgumentSpecValidator.deprecate = deprecate_mock
    ModuleArgumentSpecValidator.warn = warn_mock

    argument_spec = {
        'name': {
            'type': 'str',
            'aliases': ['foo']
        }
    }

    parameters = {
        'foo': 'bar',
    }

    validator = ModuleArgument

# Generated at 2022-06-12 23:04:32.789615
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    module_spec= {"a": {'type': 'bool'},
                  "b": {'type': 'bool'},
                  "c": {'type': 'int'},
                  "d": {'type': 'int'},
                  "e": {'type': 'int', 'required': True},
                  "f": {'type': 'int', 'default': '7'},
                  "g": {'type': 'int', 'default': '8'},
                  "h": {'type': 'dict', 'suboptions': {'i': {'type': 'int'}}}}

    mutually_exclusive=[["a", "b"]]
    required_if=[["c", "1", ["d"]]]
    required_one_of= [["e", "f"]]


# Generated at 2022-06-12 23:04:39.156199
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    from ansible.module_utils.ansible_module import _load_params as validate

    # pylint: disable=protected-access
    msg = validate.__doc__.split('\n')
    assert isinstance(msg[1], str)  # check the first parameter given to validate is a string
    assert isinstance(msg[2], str)  # check the second parameter given to validate is a string
    assert isinstance(msg[3], str)  # check the third parameter given to validate is a string
    # pylint: enable=protected-access

# Generated at 2022-06-12 23:04:46.030635
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

    assert isinstance(result, ValidationResult)
    assert isinstance(result.error_messages, list)
    assert result.error_messages == []
    assert isinstance(result.validated_parameters, dict)
    assert result.validated_parameters == {'name': 'bo', 'age': 42}



# Generated at 2022-06-12 23:04:54.106366
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():

    # test simple argument_spec
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
    assert result.validated_parameters['name'] == 'bo'
    assert result.validated_parameters['age'] == 42

    # test argument_spec with list
    argument_spec = {
        'name': {'type': 'list'},
    }
    parameters = {
        'name': 'bo',
    }


# Generated at 2022-06-12 23:05:04.670622
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():

    argument_spec = {
        'one': {'type': 'str', 'required': True, 'allow_empty': True, 'aliases': ['other']},
        'two': {'type': 'int', 'required': True, 'aliases': ['last']},
        'three': {'type': 'list', 'required': False}
    }

    mutually_exclusive = [["three", "two"]]

    required_together = [["three"]]

    required_one_of = [["one", "two"]]

    required_if = [["one", "a", ["two"]]]

    required_by = {"one": ["two"]}

    parameters = {'one': 'a', 'two': 1, 'three': [1, 2, 3]}


# Generated at 2022-06-12 23:05:13.974819
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    # test_ArgumentSpecValidator_validate_name_str
    example_argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    }
    example_parameters = {
        'name': 'bo',
        'age': '42',
    }

    validator = ArgumentSpecValidator(example_argument_spec)
    result = validator.validate(example_parameters)

    assert result.error_messages == []

    # test_ArgumentSpecValidator_validate_age_int_error
    example_argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    }

# Generated at 2022-06-12 23:05:22.936434
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    def _compare_results(result, expected_result, expected_error_messages):
        assert result == expected_result
        assert result.error_messages == expected_error_messages

    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
        'gender': {'type': 'str', 'default': 'male'},
    }

    parameters = {
        'name': 'bo',
        'age': 11,
    }
    validator = ModuleArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)
    _compare_results(result,
                     expected_result={'age': 11, 'name': 'bo', 'gender': 'male'},
                     expected_error_messages=[])

    parameters

# Generated at 2022-06-12 23:05:29.270853
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    parameter = {'name': 'bo', 'age': '42'}
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    }
    validator = ModuleArgumentSpecValidator(argument_spec)
    result = validator.validate(parameter)
    assert result.error_messages == []
    assert result.validated_parameters == {'name': 'bo', 'age': 42}

# Generated at 2022-06-12 23:05:38.877201
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    """This is the unit test of method validate of the class ModuleArgumentSpecValidator."""

    # Testing the signature of the function
    assert inspect.getargspec(ModuleArgumentSpecValidator.validate) == inspect.ArgSpec(args=['self', 'parameters'],
                                                                                        varargs=None, keywords=None,
                                                                                        defaults=None)

    # Define the test values
    module_params = {'valid_param': 'abc'}
    module_name = 'valid_module'
    argument_spec = {'valid_param': {'type': 'str'}}

    # Instanciate a ModuleArgumentSpecValidator object
    validator = ModuleArgumentSpecValidator(argument_spec)

    # Test the function
    assert validator.validate(module_params) == None

   

# Generated at 2022-06-12 23:05:40.921096
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    obj = ModuleArgumentSpecValidator()
    result = obj.validate('arg1')
    assert result == 'arg1'

# Generated at 2022-06-12 23:05:53.702095
# Unit test for constructor of class ArgumentSpecValidator
def test_ArgumentSpecValidator():
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
        'aliases': {'type': 'list', 'elements': 'str'},
    }

    parameters = {
        'name': 'bo',
        'age': '42',
        'aliases': 'bo',
    }

    validator = ArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)

    assert result.error_messages == ['age was given as "42" but the actual value is 42'], \
        "Expected error messages are not in result.error_messages"


# Generated at 2022-06-12 23:06:02.714948
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    mutually_exclusive = ["a", "b", "c", ["d", "e"], ["f", "g", "h"]]
    required_together = [['i', 'j'], ['k', 'l']]
    required_one_of = [['m', 'n'], ['o', 'p']]
    required_if = [["q", "r", ["s", "t"]], ["u", "v", ["w", "x", "y"]]]
    required_by = {"z": ["bb", "cc", "dd", "ee"], "ff": ["gg", "hh", "ii"]}
