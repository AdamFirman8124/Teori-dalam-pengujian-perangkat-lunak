

# Generated at 2022-06-12 22:56:14.034639
# Unit test for constructor of class ArgumentSpecValidator
def test_ArgumentSpecValidator():
    argument_spec = {'name': {'type': 'str'}}
    validator = ArgumentSpecValidator(argument_spec)
    param = {'name': 'bob'}
    result = validator.validate({'name': 'bob'})
    assert param == result.validated_parameters
    assert not result.errors

# Generated at 2022-06-12 22:56:24.307563
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    argument_spec = {'name': {
        'required': True,
        'type': 'str'
    }, 'age': {
        'type': 'int',
        'default': 20
    }, 'color': {
        'type': 'list',
        'default': ['red', 'green', 'blue'],
        'aliases': ['colour']
    }}
    mutually_exclusive = [['color', 'colour']]
    required_together = [['color', 'name']]
    required_one_of = [['color', 'age']]
    required_if = [['color', 'red', ['name']]]
    required_by = {'color': ['name']}

# Generated at 2022-06-12 22:56:25.021589
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    pass

# Generated at 2022-06-12 22:56:34.960731
# Unit test for constructor of class ArgumentSpecValidator
def test_ArgumentSpecValidator():
    # test_init_with_valid_args
    mutually_exclusive = [['a', 'b'], ['c', 'd']]
    required_together = [['a', 'b'], ['c', 'd']]
    required_one_of = [['a', 'b'], ['c', 'd']]
    required_if = [['a', 'b']]
    required_by = {'a': ['b','c'], 'b': ['d','e'], 'c':['f']}
    argument_spec = {'a': {'type': 'str'}, 'b': {'type': 'str'}}


# Generated at 2022-06-12 22:56:36.002527
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    ModuleArgumentSpecValidator("argumentspec").validate("parameters")

# Generated at 2022-06-12 22:56:46.163714
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
        'address': {'type': 'dict', 'options': {'place': {'type': 'str'}, 'number': {'type': 'int', 'required': True}}},
    }
    parameters = {
        'name': 'bo',
        'age': '42',
        'address': {'place': 'neverland'}
    }
    validator = ArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)
    assert result.error_messages == ["address.number is required"]
    assert result.validated_parameters == {'name': 'bo', 'age': 42, 'address': {'place': 'neverland'}}

# Generated at 2022-06-12 22:56:56.975437
# Unit test for constructor of class ArgumentSpecValidator
def test_ArgumentSpecValidator():
    # Initialization
    test_spec = {
        'prop1': {
            'type': 'str'
        },
        'prop2': {
            'type': 'str'
        },
        'prop3': {
            'type': 'str'
        },
        'prop4': {
            'type': 'str'
        }
    }
    test_mutually_exclusive = [['prop1', 'prop2', 'prop3']]
    test_required_together = [['prop1', 'prop2']]
    test_required_one_of = [['prop1', 'prop2']]
    test_required_if = [['prop2', '1', ['prop3', 'prop4']]]

    # Call the constructor

# Generated at 2022-06-12 22:57:01.679921
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    # Define test data
    argument_spec = {'param1': {'type': 'str', 'default': 'test'}, 'param2': {'type': 'dict', 'default': 'test'}}
    parameters = {'param1': 'test'}
    result = ValidationResult(parameters)
    result._deprecations = []
    result._warnings = []
    result.errors = AnsibleValidationErrorMultiple()

    # Start test
    validator = ModuleArgumentSpecValidator(argument_spec)
    validator.validate(parameters)

# Generated at 2022-06-12 22:57:12.588070
# Unit test for constructor of class ArgumentSpecValidator
def test_ArgumentSpecValidator():
    #
    # This is expected to succeed.
    # The constructor of class ArgumentSpecValidator should
    # accept various combinations of mutually exclusive and
    # other arguments
    #
    validator = ArgumentSpecValidator(argument_spec={})
    assert validator
    validator = ArgumentSpecValidator(argument_spec={}, mutually_exclusive=[])
    assert validator
    validator = ArgumentSpecValidator(argument_spec={}, mutually_exclusive=None)
    assert validator
    validator = ArgumentSpecValidator(argument_spec={}, mutually_exclusive=None,
                                      required_together=None, required_one_of=None,
                                      required_if=None, required_by=None)
    assert validator

# Generated at 2022-06-12 22:57:20.424719
# Unit test for method validate of class ModuleArgumentSpecValidator

# Generated at 2022-06-12 22:57:33.911397
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    from ansible.module_utils.common.validation import MutuallyExclusiveError
    from ansible.module_utils.common.warnings import deprecate, warn
    import io
    import sys
    import pytest


    class FakeDeprecationClass:
        def __init__(self):
            self.deprecations = []
        def __call__(self, msg, version=None, date=None, collection_name=None):
            self.deprecations.append({'msg': msg, 'version': version, 'date': date, 'collection_name': collection_name})


    class FakeWarnClass:
        def __init__(self):
            self.warns = []

# Generated at 2022-06-12 22:57:40.881153
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    """
    Unit test function for class ModuleArgumentSpecValidator
    """
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    }
    mutually_exclusive=(['name', 'age'])
    parameters = {
        'name': 'bo',
        'age': 42,
    }
    module_argument_spec_validator = ModuleArgumentSpecValidator(argument_spec, mutually_exclusive=mutually_exclusive)
    module_argument_spec_validator.validate(parameters)

# Generated at 2022-06-12 22:57:46.027853
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

    assert result.errors.messages == []
    assert result.validated_parameters == {'name': 'bo', 'age': 42}

# Generated at 2022-06-12 22:57:51.023457
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    argument_spec = {}
    
    mutually_exclusive = None

    required_together = None

    required_one_of = None

    required_if = None

    required_by = None


    parameters = {}


    ModuleArgumentSpecValidator(argument_spec,mutually_exclusive=mutually_exclusive,required_together=required_together,required_one_of=required_one_of,required_if=required_if,required_by=required_by).validate(parameters)

# Generated at 2022-06-12 22:57:51.926553
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    pass


# Generated at 2022-06-12 22:58:01.876011
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    from ansible.module_utils.basic import AnsibleModule
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
        'address': {'type': 'dict', 'keys': {'street': {}}},
    }

    parameters1 = {
        'name': 'bo',
        'age': 42,
        'address': {'street': 'Preet vihar'},
    }

    parameters2 = {
        'name': 'bo',
        'age': '42',
        'address': {'street': 'Preet vihar'},
    }

    parameters3 = {
        'name': 'bo',
        'age': 42,
    }


# Generated at 2022-06-12 22:58:06.867172
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
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
    assert result.validated_parameters == parameters

# Generated at 2022-06-12 22:58:15.927561
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    from ansible.module_utils.common.arg_spec import ArgumentSpecValidator
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
    assert len(result.error_messages) == 0

# Generated at 2022-06-12 22:58:17.829107
# Unit test for constructor of class ArgumentSpecValidator
def test_ArgumentSpecValidator():
    assert ArgumentSpecValidator({}, [], [], [], [], {})



# Generated at 2022-06-12 22:58:25.911033
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    argument_spec = {}
    mutually_exclusive = []
    required_together = []
    required_one_of = []
    required_if = []
    required_by = {}

    parameters = {}

    validator = ModuleArgumentSpecValidator(argument_spec, mutually_exclusive, required_together,
                                           required_one_of, required_if, required_by)
    result = validator.validate(parameters)

    assert isinstance(validator, ModuleArgumentSpecValidator)
    assert isinstance(parameters, dict)
    assert isinstance(result, ValidationResult)

# Generated at 2022-06-12 22:58:35.676137
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():

    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.six import string_types

    # Create AnsibleModule object
    module = AnsibleModule(
        argument_spec={
            'test': {'type': 'list', 'elements': 'str', 'required': True, 'default': ['a']},
            'no_log': {'type': 'bool', 'required': False, 'default': True, 'no_log': True}
        },
        mutually_exclusive=[],
        required_together=[],
        required_one_of=[],
        required_if=[],
        required_by=[]
    )

    # Test valid input
    parameters = dict(test=['a', 'b'])
    # Create validator

# Generated at 2022-06-12 22:58:41.985471
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    argument_spec = {
        "name": {
            "required": True,
            "type": "str"
        },
    }
    parameters = {
        "name": "bo"
    }
    validator = ArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)
    assert isinstance(result, ValidationResult)
    assert result.validated_parameters == parameters


# Generated at 2022-06-12 22:58:52.433840
# Unit test for constructor of class ArgumentSpecValidator
def test_ArgumentSpecValidator():
    """
    Test for the constructor of class ArgumentSpecValidator

    :return:
    """
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    }

    mutually_exclusive = [['name', 'age']]
    required_together = [['name', 'age']]
    required_one_of = [['name', 'age']]
    required_if = ['name', 'foobar', ['name', 'age']]
    required_by = {'name': ['age']}

    asv = ArgumentSpecValidator(argument_spec, mutually_exclusive, required_together, required_one_of, required_if,
                                required_by)

    assert isinstance(asv, ArgumentSpecValidator)



# Generated at 2022-06-12 22:58:58.497084
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
    assert result.validated_parameters == {'name': 'bo', 'age': 42}

    result = ModuleArgumentSpecValidator(argument_spec).validate(parameters)
    assert result.validated_parameters == {'name': 'bo', 'age': 42}



# Generated at 2022-06-12 22:59:10.688291
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():

    def run_validate(validator, parameters):
        # fake validate_for_remove function
        validator._validate_for_remove = lambda parameters:parameters
        return validator.validate(parameters)

    argument_spec = {
        'param1': {'type': 'str'},
        'param2': {'type': 'str'},
        'param3': {'type': 'str', 'no_log': True}
    }

    parameters = {
        'param1': 'value1',
        'param2': 'value2',
        'param3': 'value3',
        'param4': 'value4'
    }

    validator = ArgumentSpecValidator(argument_spec)

    # Deprecations

# Generated at 2022-06-12 22:59:18.431504
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    mutually_exclusive = [
        ['a', 'b'],
        ['c', 'd'],
    ]
    required_together = [
        ['e', 'f'],
        ['g', 'h'],
    ]
    required_one_of = [
        ['j', 'k'],
        ['l', 'm'],
    ]
    required_if = [
        ['n', 'p', ['o']]
    ]
    required_by = {
        'q': ['r'],
        's': ['t']
    }

# Generated at 2022-06-12 22:59:29.334246
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    from ansible.module_utils.common.parameters import generate_params_spec

    # Some modules like mod_info don't have any parameters so we needn't test for that
    # However some modules do have required parameters, so we need to test for that
    argument_spec = {
        'file': {'required': True, 'type': 'path'},
        'name': {'required': True, 'type': 'str'},
        'state': {'default': 'present', 'choices': ['present', 'absent']},
    }

    check_required_args = {'file': '/etc/hosts', 'name': 'aliased_host'}

    mutually_exclusive = [
        ['file', 'inline'],
    ]


# Generated at 2022-06-12 22:59:39.148644
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    argument_spec = {'name': {'type': 'str'},
                     'age': {'type': 'int'},
                     'description': {'type': 'str'},
                     'enabled': {'type': 'bool', 'default': False},
                     'account_type': {'type': 'str', 'choices': ['standard', 'admin'], 'aliases': ['type', 'accttype']}
                     }

    parameters = {'name': 'bo',
                  'age': '42',
                  'description': 'age'
                  }

    validator = ArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)

    # test that no error was thrown
    assert not result.error_messages

    # test that enabled is defaulted
    assert result.validated_parameters['enabled']

# Generated at 2022-06-12 22:59:44.441528
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

    assert result.error_messages == ['The following are mutually exclusive parameters: age, name']
    assert result.validated_parameters == {}

# Generated at 2022-06-12 22:59:53.276012
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    """ Test the validate method of class ModuleArgumentSpecValidator. """

    class ClassForTesting():
        """ Test class with fake methods. """

        def deprecate(self, *args, **kwargs):
            pass

        def warn(self, *args, **kwargs):
            pass

    class_for_testing = ClassForTesting()
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
    assert isinstance(result, ValidationResult)
    assert result._no_log_values == set()
    assert result

# Generated at 2022-06-12 23:00:02.077962
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    # object type
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
    assert result.error_messages is None
    assert result.validated_parameters == {'name': 'bo', 'age': 42}

# Generated at 2022-06-12 23:00:13.039434
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    # test case 1
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
    assert result.unsupported_parameters == set()
    assert result.validated_parameters == {'name': 'bo', 'age': 42}

    # test case 2
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    }

# Generated at 2022-06-12 23:00:19.630739
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    a = ModuleArgumentSpecValidator(
        argument_spec={'arg1': {'type': 'str'}, 'arg2': {'type': 'str', 'aliases': ['arg3']}},
        mutually_exclusive=None,
        required_together=None,
        required_one_of=None,
        required_if=None,
        required_by=None,
    )
    assert a.validate({'arg1': 'val1', 'arg2': 'val2'})

# Generated at 2022-06-12 23:00:28.333832
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

    mutually_exclusive = [
        ['name', 'age'],
    ]

    required_together = [
        ['name'],
    ]

    required_one_of = [
        ['name'],
    ]

    required_if = [
        ['name', 'age'],
    ]

    required_by = {
        'name': ['age'],
    }


# Generated at 2022-06-12 23:00:37.958289
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    import sys
    # Input parameters
    argument_spec = {
      "foo": {
        "type": "str",
      }
    }
    parameters = {
      "foo": "bar",
    }

    # Call the method to test
    validator = ArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)

    # Output results
    if result.error_messages:
      sys.exit("Validation failed: {0}".format(", ".join(result.error_messages)))

    valid_params = result.validated_parameters

    if valid_params["foo"] != "bar":
      sys.exit("Parameters validation failed")


# Generated at 2022-06-12 23:00:44.250314
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

    if result.errors:
        sys.exit("Validation failed: {0}".format(", ".join(result.errors)))

    valid_params = result.validated_parameters
    print(valid_params)


# Generated at 2022-06-12 23:00:52.852511
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


# Generated at 2022-06-12 23:01:03.615348
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    from ansible.module_utils.six import iteritems

    expected_error_message = "Validation failed: "
    expected_no_log_values = {'password': 'hidden_password', 'api_key': 'hidden_api_key'}

    parameters = {
        'username': 'bobos',
        'password': 'secret',
        'api_key': '12345'
    }

    argument_spec = {
        'username': {'type': 'str'},
        'password': {'type': 'str', 'no_log': True},
        'api_key': {'type': 'str', 'no_log': True}
    }

    validator = ModuleArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)


# Generated at 2022-06-12 23:01:13.321641
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    mutually_exclusive = [['a', 'b']]
    required_together = [('c', 'd')]
    required_one_of = [['a', 'b']]
    required_if = [('a', 'b', ['c'])]
    required_by = {'c': ['a']}

    argument_spec = {
        'a': {'type': 'str', 'required': True},
        'b': {'type': 'str'},
        'c': {'type': 'str'},
        'd': {'type': 'str'},
    }

    parameters = {
        'a': 'a',
        'b': 'b',
        'c': 'c',
        'd': 'd',
    }


# Generated at 2022-06-12 23:01:24.244032
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    spec = {
        'age': {'type': 'int'},
        'foo': {'type': 'list', 'elements': 'dict', 'options': {'key': {'type': 'str'}, 'value': {'type': 'str'}}},
        'name': {'type': 'str'},
        'no_log_value': {'type': 'str', 'no_log': True},
        'email_address': {'type': 'str', 'aliases': ['email']},
        'user': {'type': 'dict', 'options': {'age': {'type': 'int'}, 'first': {'type': 'str'},
                                             'last': {'type': 'str'}, 'no_log_value': {'type': 'str', 'no_log': True}}},
    }

# Generated at 2022-06-12 23:01:36.480485
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    class DummyModuleArgumentSpecValidator(ModuleArgumentSpecValidator):
        def __init__(self, args, **kwargs):
            super(DummyModuleArgumentSpecValidator, self).__init__(args, **kwargs)

    validator = DummyModuleArgumentSpecValidator({'name': {'type': 'str', 'deprecated': {'version': '2.13', 'date': '2020-01-01', 'collection_name': 'community.general'}}})

    parameters = dict(name='test')

    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter('always')
        result = validator.validate(parameters)
        assert len(w) == 1
        assert issubclass(w[0].category, DeprecationWarning)
        assert 'Alias'

# Generated at 2022-06-12 23:01:46.167275
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    # initialize
    class UnitTest:
        def __init__(self, name):
            self.name = name
        def __str__(self):
            return self._module.name

    # test case
    result = UnitTest('ansible_module_utils.common.arg_spec')
    result._module = result
    result._mutually_exclusive = None
    result._required_together = None
    result._required_one_of = None
    result._required_if = None
    result._required_by = None
    result._valid_parameter_names = set()
    result._validated_parameters = {'name': 'bo', 'age': '42'}
    result._no_log_values = set()
    result._unsupported_parameters = set()

# Generated at 2022-06-12 23:01:54.881279
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    from ansible_collections.notstdlib.moveitallout.plugins.module_utils.common.arg_spec import ArgumentSpec
    from ansible_collections.notstdlib.moveitallout.plugins.module_utils.common.validation import check_mutually_exclusive, check_required_arguments, check_required_one_of, check_required_together, check_required_if, check_required_by
    from ansible_collections.notstdlib.moveitallout.plugins.module_utils.common.parameters import _get_unsupported_parameters, _set_defaults
    from ansible_collections.notstdlib.moveitallout.plugins.module_utils.common.text.converters import to_native

# Generated at 2022-06-12 23:01:59.583725
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    parameters = { "name" : "foo", "age" : "42" }
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'}
    }
    validator = ArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)

    return (len(result.error_messages) == 0)

# Generated at 2022-06-12 23:02:06.113424
# Unit test for method validate of class ModuleArgumentSpecValidator

# Generated at 2022-06-12 23:02:14.192295
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    # TestCase: deprecations
    spec = {
        'name': {
            'type': 'str',
            'aliases': ['username'],
            'deprecated': {'version': '2.7', 'collection_name': 'my_collection', 'date': '2022-12-31'},
        },
    }
    # Create the validator
    validator = ModuleArgumentSpecValidator(spec)
    # Run validation
    result = validator.validate({'name': 'root'})
    assert result.errors is not None

# Generated at 2022-06-12 23:02:25.310372
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
    assert result.validated_parameters == {'age': 42, 'name': 'bo'}

    required_if = [['state', 'present', ['foo', 'bar']]]

    validator = ArgumentSpecValidator(argument_spec,
                                      required_if=required_if)

    result = validator.validate(parameters)


# Generated at 2022-06-12 23:02:34.679337
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    args = dict(name=dict(type='str'),
                age=dict(type='int'),
                )
    params = dict(name=['bo'], age=[42])
    validator = ModuleArgumentSpecValidator(args)
    result = validator.validate(params)
    assert dict == type(result.errors)
    assert dict == type(result.warnings)
    assert dict == type(result.deprecations)
    assert dict == type(result.validated_parameters)

    args = dict(name=dict(type='str'),
                age=dict(type='int'),
                )
    params = dict(name=['bo'], age=['42'])
    validator = ModuleArgumentSpecValidator(args)
    result = validator.validate(params)

# Generated at 2022-06-12 23:02:45.324738
# Unit test for method validate of class ModuleArgumentSpecValidator

# Generated at 2022-06-12 23:02:53.566659
# Unit test for method validate of class ModuleArgumentSpecValidator

# Generated at 2022-06-12 23:03:10.968112
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():

    from ansible.module_utils.six import iteritems
    from ansible.module_utils.common.missing_lib_warnings import MissingLibWarning

    import warnings

    warnings.filterwarnings("always", category=MissingLibWarning)

    try:
        from __main__ import display
    except ImportError:
        from ansible.utils.display import Display
        display = Display()

    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    }

    # Checking if no errors
    parameters = {
        'name': 'bo',
        'age': '42',
    }

    validator = ModuleArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)

    assert not result.error_messages

    #

# Generated at 2022-06-12 23:03:16.008278
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    """ Test validate method of class ArgumentSpecValidator """
    # validator = ArgumentSpecValidator(argument_spec,
    #         mutually_exclusive=None,
    #         required_together=None,
    #         required_one_of=None,
    #         required_if=None,
    #         required_by=None,
    #         )
    # result = validator.validate(parameters)


# Generated at 2022-06-12 23:03:25.704753
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    from ansible_collections.other.not_a_real_collection.plugins.module_utils.common.arg_spec import ModuleArgumentSpecValidator
    from ansible_collections.other.not_a_real_collection.plugins.module_utils.common.validation import MutuallyExclusiveError, RequiredError
    argument_spec = {
        'force': {'type': 'bool', 'default': False},
        'name': {'type': 'str', 'required': True},
    }
    mutually_exclusive = [['name', 'force']]
    validator = ModuleArgumentSpecValidator(argument_spec, mutually_exclusive=mutually_exclusive)

    # test mutually exclusive
    # fail: mutually exclusive
    parameters = {'name': 'bo', 'force': True}
    result = validator.validate(parameters)

# Generated at 2022-06-12 23:03:29.400164
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    """
    Unit test for method validate of class ArgumentSpecValidator
    """

    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    }

    mutually_exclusive = [
        ['name', 'age']
    ]

    parameters = {
        'name': 'bo',
        'age': '42',
    }

    validator = ArgumentSpecValidator(argument_spec, mutually_exclusive=mutually_exclusive)
    result = validator.validate(parameters)

    assert result.error_messages == ['Parameters name and age are mutually exclusive']
    assert result.validated_parameters == {}


# Generated at 2022-06-12 23:03:37.076478
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
        'pets': {'type': 'list', 'elements': 'str'},
        'state': {
            'type': 'str',
            'choices': ['absent', 'present'],
            'default': 'present',
        },
        'aliases': {'type': 'list', 'elements': 'str'},
    }

    parameters = {
        'name': 'bo',
        'age': '42',
        'pets': ['dog', 'cat', 'parrot'],
    }

    mutually_exclusive = [
        ['name', 'age'],
        ['state', 'pets'],
    ]


# Generated at 2022-06-12 23:03:47.705803
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    import sys
    sys.path.insert(0, '../../lib/ansible')
    from arg_spec import ModuleArgumentSpecValidator
    import pytest

    # testing if the method validate in class ModuleArgumentSpecValidator
    # works as expected
    # also testing if the method _validate_argument_types works as expected
    # also testing if the method _validate_argument_values works as expected
    # also testing if the method _validate_sub_spec works as expected
    # testing if the method _set_defaults works as expected
    # also testing some of the methods inside the method _set_defaults
    # also testing if the method _validate_sub_spec_list works as expected
    # also testing if the method _validate_sub_spec_dict works as expected
    # also testing if the method _list_no

# Generated at 2022-06-12 23:03:56.892950
# Unit test for method validate of class ModuleArgumentSpecValidator

# Generated at 2022-06-12 23:04:03.859277
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    argument_spec = {
        'b': {'type': 'bool'},
        'w': {'type': 'bool'},
    }

    mutually_exclusive = [
        ['b', 'w']
    ]

    parameters = {
        'w': True
    }

    validator = ModuleArgumentSpecValidator(argument_spec, mutually_exclusive=mutually_exclusive)
    result = validator.validate(parameters)

    assert result.error_messages == []

# Generated at 2022-06-12 23:04:13.376151
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    import unittest
    from ansible.module_utils.common.parameters import ModuleParameters
    from ansible.module_utils.common.text.converters import to_bytes

    class TestModuleArgumentSpecValidator(unittest.TestCase):
        def setUp(self):
            self.argument_spec = {'name': {'type': 'str'}}
            self.parameters = {'name': 'bo'}
            self.validator = ModuleArgumentSpecValidator(self.argument_spec)

        def test_no_errors(self):
            result = self.validator.validate(self.parameters)
            self.assertIsInstance(result, ModuleParameters, msg="validator.validate() did not return a ModuleParameters instance.")

# Generated at 2022-06-12 23:04:14.932618
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    validator = ArgumentSpecValidator({})
    r = validator.validate({})
    assert r is not None

# Generated at 2022-06-12 23:04:34.881845
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    parameter_spec = {"parameter1": "value1", "parameter2": "value2"}
    mutually_exclusive = ["parameter1", ["parameter2", "parameter3"]]
    required_together = [["parameter1", "parameter2"]]
    required_one_of = [["parameter1", "parameter2"]]
    required_if = [["parameter1", "value1", ["parameter2"]]]
    required_by = {"parameter1": ["parameter2"]}

    argument_spec_validator_test = ModuleArgumentSpecValidator(parameter_spec, mutually_exclusive, required_together, required_one_of, required_if, required_by)

    parameters = {"parameter1": "value1", "parameter2": "value2"}

    result = argument_spec_validator

# Generated at 2022-06-12 23:04:42.861065
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
  import sys
  from ansible.module_utils.common.parameters import _get_unsupported_parameters
  
  argument_spec = {
    'name': {
      'type': 'str',
    },
    'age': {
      'type': 'int',
    },
  }
  mutually_exclusive = [
    [
      'name',
      'age',
    ]
  ]
  required_together = [
    [
      'name',
      'age',
    ]
  ]
  required_one_of = [
    [
      'name',
      'age',
    ]
  ]
  required_if = [
    [
      'name',
      '1',
      [
        'age',
      ]
    ]
  ]

# Generated at 2022-06-12 23:04:49.605047
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    arg_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    }

    parameters = {
        'name': 'bo',
        'age': '42',
    }

    validator = ModuleArgumentSpecValidator(arg_spec)
    result = validator.validate(parameters)

    if result.error_messages:
        raise AssertionError("Validation failed: {0}".format(", ".join(result.error_messages)))

    valid_params = result.validated_parameters
    assert valid_params == {'name': 'bo', 'age': 42}

# Generated at 2022-06-12 23:04:51.463175
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():

    assert hasattr(ArgumentSpecValidator, 'validate')
    assert callable(ArgumentSpecValidator.validate)



# Generated at 2022-06-12 23:04:55.056072
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    validator = ArgumentSpecValidator('spec', mutually_exclusive=['a', 'b'], required_together=['c', 'd'], required_one_of=['e', 'f'],
                                      required_if='g', required_by='h')
    result = validator.validate('params')
    assert isinstance(result, ValidationResult)

# Generated at 2022-06-12 23:05:06.090037
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    import pytest

    # Unit test for the warning check
    class warn_string(str):
        pass

    dict_warn_string = dict()
    dict_warn_string['arguments'] = ['test_option', 'test_alias']

    def mock_warn(msg):
        return 'test method warn'

    param_validator = ModuleArgumentSpecValidator(arguments={'test_option':{'aliases': ['test_alias']}})

    # with patch('ansible.module_utils.common.warnings.warn', mock_validate_warning):
    with pytest.warns(warn_string) as record:
        param_validator.validate({'test_option': 'value', 'test_alias': 'value'})

    assert len(record) == 1

# Generated at 2022-06-12 23:05:07.432821
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    assert False, "TODO: Write me."

# Generated at 2022-06-12 23:05:12.835020
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

    assert result.validated_parameters['name'] == 'bo'
    assert result.validated_parameters['age'] == 42

# Generated at 2022-06-12 23:05:15.244754
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():

    # Instantiate class object with parameters and run test
    # AnsibleModule.fail_json will be called if test fails
    b = ModuleArgumentSpecValidator()
    b.validate(parameters)



# Generated at 2022-06-12 23:05:21.232157
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    import json
    import sys
    import tempfile
    import textwrap

    sys.path.append(tempfile.mkdtemp())  # Noqa: 402
    import ansible.module_utils.common.arg_spec as arg_spec  # NOQA: 402, E402

    #
    # example of a module using a nested ansible_facts.data.foo.bar nested spec

# Generated at 2022-06-12 23:05:54.631775
# Unit test for method validate of class ModuleArgumentSpecValidator

# Generated at 2022-06-12 23:06:03.626985
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    # Test valid parameters, no errors should be present
    validator = ArgumentSpecValidator({'name': {'type': 'str', 'required': True},
                                       'age': {'type': 'int', 'required': True}},
                                      mutually_exclusive=[['name', 'age']])
    parameters = {'name': 'bo', 'age': 42}
    result = validator.validate(parameters)
    assert not result.errors
    assert result.validated_parameters == {'name': 'bo', 'age': 42}

    # Test invalid parameters, type error should be present