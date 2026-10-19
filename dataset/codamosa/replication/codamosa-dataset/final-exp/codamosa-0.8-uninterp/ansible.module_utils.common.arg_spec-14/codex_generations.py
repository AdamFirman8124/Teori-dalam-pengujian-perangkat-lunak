

# Generated at 2022-06-12 22:56:17.134496
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    params = {'test_param_one': 'param_one', 'test_param_two': 'param_two'}
    arg_spec = {'test_param_one': {'type': 'str'},
                'test_param_two': {'type': 'str'}}
    ave = ArgumentSpecValidator(arg_spec)
    result = ave.validate(params)
    assert result.validated_parameters == params
    assert result.error_messages == []
    assert result.unsupported_parameters == set()
    assert result._deprecations == []
    assert result._warnings == []

# Generated at 2022-06-12 22:56:27.869169
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    example_argument_spec_validator_with_deprecation = ModuleArgumentSpecValidator(
        argument_spec={'deprecated_option': {'aliases': ['deprecated_alias'], 'type': 'str',
                                             'deprecated': {'version': '2.10', 'date': '2020-01-01'}}})
    example_argument_spec_validator_with_alias = ModuleArgumentSpecValidator(
        argument_spec={'option': {'aliases': ['alias'],
                                  'type': 'str'}})

# Generated at 2022-06-12 22:56:36.866986
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    argument_spec = {"test1": {"type": "str", "default": "foo", "aliases": ["test2", "test3"]}}
    mutually_exclusive = []
    required_together = []
    required_one_of = []
    required_if = []
    required_by = {}

    validator = ModuleArgumentSpecValidator(argument_spec=argument_spec,
                                            mutually_exclusive=mutually_exclusive,
                                            required_together=required_together,
                                            required_one_of=required_one_of,
                                            required_if=required_if,
                                            required_by=required_by
                                            )
    parameters = {"test2": "bar"}
    result = validator.validate(parameters=parameters)


# Generated at 2022-06-12 22:56:39.958660
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    validator = ModuleArgumentSpecValidator({'arg': {'type': 'str'}})
    result = validator.validate(dict(arg='test'))
    assert result._validated_parameters == {'arg': 'test'}

# Generated at 2022-06-12 22:56:47.109236
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

    assert bool(result.errors) is False
    assert result.validated_parameters == {'name': 'bo', 'age': 42}



# Generated at 2022-06-12 22:56:57.804949
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    }

    mutually_exclusive = [['age', 'name']]
    required_together = [['age', 'name']]
    required_on_of = [['age', 'name']]
    required_if = [['age', 'name', ['age']]]
    required_by = {'age': ['name']}

    parameters = {
        'name': 'bo',
        'age': '42',
    }


# Generated at 2022-06-12 22:57:06.524067
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    """ 
    Unit test driver for method validate of class ArgumentSpecValidator
    """

    # generic parameters to test
    params = {'name': 'bo', 'age': '42', 'answer': 'True', 'ansible_check_mode': False}

    legal_inputs = set(['age', 'answer', 'name'])

    for obj in (ArgumentSpecValidator, ModuleArgumentSpecValidator):
        # Test argument spec:
        # {'name': {'type': 'str'}, 'age': {'type': 'int'}, 'answer': {'type': 'bool'}}
        assert(obj({'name': {'type': 'str'}, 'age': {'type': 'int'}, 'answer': {'type': 'bool'}}).validate(params) == None)

        # Test argument spec:
       

# Generated at 2022-06-12 22:57:16.635764
# Unit test for method validate of class ModuleArgumentSpecValidator

# Generated at 2022-06-12 22:57:22.893363
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    def test_deprecate(msg, version=None, date=None, collection_name=None):
        if (deprecated_msgs_L == []):
            deprecated_msgs_L.append({'msg':msg, 'version':version, 'date':date, 'collection_name':collection_name})

    def test_warn(msg):
        warnings_L.append(msg)

    def test_validate(parameters):
        validator = ModuleArgumentSpecValidator(argument_spec,
                                                mutually_exclusive=mutually_exclusive,
                                                required_together=required_together,
                                                required_one_of=required_one_of,
                                                required_if=required_if,
                                                required_by=required_by)
        deprecate = test_deprecate

# Generated at 2022-06-12 22:57:31.541221
# Unit test for constructor of class ArgumentSpecValidator
def test_ArgumentSpecValidator():
    argument_spec = {'host': {'required': False, 'default': 'localhost'},
                     'port': {'required': True, 'type': 'int'}}
    mutually_exclusive = [['host', 'cat']]
    mutually_exclusive_required = [['port', 'cat']]
    required_together = [['host', 'port']]
    required_if = [['host', 'localhost', ['port']]]
    required_one_of = [['host', 'password']]
    required_by = {'port': ['host']}

    argument_spec_validator = ArgumentSpecValidator(argument_spec)
    assert()

# Generated at 2022-06-12 22:57:44.995984
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    # A normal spec with no defined conditions
    arg_spec = dict(
        foo=dict(required=True, type='str'),
        bar=dict(required=False, type='int'),
        baz=dict(required=False, type='list'),
    )

    # Parameters with no conditions
    parameters = dict(
        foo='qux',
        bar=42,
        baz=[1, 2, 3],
    )

    validator = ArgumentSpecValidator(arg_spec)
    result = validator.validate(parameters)

    assert not result.error_messages

    # Parameters with no conditions but some extra unsupported parameters

# Generated at 2022-06-12 22:57:52.648908
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    argument_spec = {
        'name': {'type': 'str', 'required': True},
        'age': {'type': 'int', 'required': True},
        'cloud': {
            'type': 'dict',
            'options': {
                'id': {'type': 'str'},
                'name': {'type': 'str'},
            },
        },
    }

    parameters = {
        'name': 'bo',
        'cloud': {
            'name': 'aws',
        },
    }

    validator = ArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)

    assert result.error_messages == ['age (int) is required']

# Generated at 2022-06-12 22:58:02.514922
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    # TODO: Remove this function when validation_checker is introduced
    def set_os_family(family):
        import os
        os.environ['ANSIBLE_OS_FAMILY'] = family

    UPPER_FAMILY = 'UPPER_FAMILY'
    LOWER_FAMILY = 'lower_family'
    FAMILY_FROM_FILE = 'family_from_file'


# Generated at 2022-06-12 22:58:11.835103
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    """Test :func:`ArgumentSpecValidator.validate() <ansible.module_utils.common.arg_spec.ArgumentSpecValidator.validate()>`."""
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

# Generated at 2022-06-12 22:58:23.095313
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    from ansible.module_utils.common.json_utils import jsonify

    def json_validator(argument_spec, parameters):
        try:
            result = ModuleArgumentSpecValidator(argument_spec).validate(parameters)
            return (result.validated_parameters,
                    result.error_messages,
                    result.unsupported_parameters)
        except Exception as e:
            return str(e)


# Generated at 2022-06-12 22:58:32.050421
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    # Tests of the alias error detection
    validator_alias_error_1 = ArgumentSpecValidator({'name': {'type': 'str'}}, required_if=[['name', 'is_present', ['full_name']]])
    result_alias_error_1 = validator_alias_error_1.validate({'name': 'bo', 'full_name': 'bo'})
    assert "Found both original and alias name(s) for name" in result_alias_error_1.error_messages[0]

    # Tests of the validate method
    validator = ArgumentSpecValidator({'name': {'type': 'str'}, 'age': {'type': 'int'}})
    result = validator.validate({'name': 'bo', 'age': '42'})
    assert result.error_messages == []

# Generated at 2022-06-12 22:58:38.131821
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    # argument_spec
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'}
    }

    # parameters
    parameters = {
        'name': 'bo',
        'age': '42',
    }

    # Arguments
    mutually_exclusive = None
    required_together = None
    required_one_of = None
    required_if = None
    required_by = None

    validator = ArgumentSpecValidator(argument_spec,
                 mutually_exclusive=mutually_exclusive,
                 required_together=required_together,
                 required_one_of=required_one_of,
                 required_if=required_if,
                 required_by=required_by
                 )

    run_result = validator.validate(parameters)
   

# Generated at 2022-06-12 22:58:49.222698
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    # setup
    argument_spec = {}
    mutually_exclusive = []
    required_together = []
    required_one_of = []
    required_if = []
    required_by = []

    validator = ModuleArgumentSpecValidator(argument_spec, mutually_exclusive, required_together, required_one_of, required_if, required_by)

    expected = ValidationResult(parameters={})
    expected._no_log_values = set()
    expected._validated_parameters = {}
    expected._deprecations = []
    expected._warnings = []
    expected.errors = AnsibleValidationErrorMultiple()
    expected.error_messages = []

    # test
    actual = validator.validate(parameters={})

    # assert
    assert expected.validated_parameters == actual.validated_param

# Generated at 2022-06-12 22:58:55.240114
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    '''
    This function tests the validity of the `validate` method of class ModuleArgumentSpecValidator
    '''
    # Initialize the class
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
        }
    m = ModuleArgumentSpecValidator(argument_spec)
    parameters = {'name' : 'bo', 'age' : '43'}
    result = m.validate(parameters)
    assert type(result) == ValidationResult

# Generated at 2022-06-12 22:59:06.819314
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    def _test_module_argument_spec_validator_validate():
        import ansible.module_utils.common.arg_spec
        ansible.module_utils.common.arg_spec.ArgumentSpecValidator = ModuleArgumentSpecValidator
        import ansible.modules.cloud.amazon.ec2_snapshot
        ec2_snapshot = ansible.modules.cloud.amazon.ec2_snapshot.Ec2Snapshot()
        result = ec2_snapshot.validate()
        if result.error_messages:
            sys.exit("Validation failed: {0}".format(", ".join(result.error_messages)))
        valid_params = result.validated_parameters

    # import ansible.module_utils.common.arg_spec
    # ansible.module_utils.common.arg_spec.

# Generated at 2022-06-12 22:59:12.672727
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    validator = ArgumentSpecValidator({})
    result = validator.validate({})
    assert not result.errors
    assert not result._no_log_values
    assert not result._unsupported_parameters
    assert result._validated_parameters == {}

# Generated at 2022-06-12 22:59:16.069416
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    validator = ModuleArgumentSpecValidator({'name': {'type': 'str', 'aliases': ['full_name']}})
    result = validator.validate({'name': 'username', 'full_name': 'Mr.Username'})
    assert result.error_messages == [
        'Both option name and its alias full_name are set.']

# Generated at 2022-06-12 22:59:23.774488
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    argument_spec = {
        "name": {"type": "str"},
        "age": {"type": "int", "deprecated": {"version": "2.14", "date": "2020-03-01"}},
    }

    validator = ModuleArgumentSpecValidator(argument_spec)
    parameters = {"name": "bo", "age": "42"}
    result = validator.validate(parameters)

    assert len(result.error_messages) == 0
    assert result.validated_parameters == {"name": "bo", "age": 42}



# Generated at 2022-06-12 22:59:30.185970
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    argument_spec={'age': {'type': 'int'}, 'name': {'type': 'str'}}
    validator = ArgumentSpecValidator(argument_spec)
    parameters = {'name': 'bo', 'age': '42'}
    result = validator.validate(parameters)
    assert not result.error_messages
    assert result.validated_parameters['age'] == 42
    assert result.validated_parameters['name'] == 'bo'

# Generated at 2022-06-12 22:59:36.402015
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    spec = {'name': {'type': 'str'}, 'age': {'type': 'int'}}
    parameters = {'name': 'bo', 'age': '42'}
    validator = ModuleArgumentSpecValidator(spec)
    result = validator.validate(parameters)
    assert result.error_messages == []
    assert result.validated_parameters == {'name': 'bo', 'age': '42'}


# Generated at 2022-06-12 22:59:44.225460
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    import ansible.module_utils.common.arg_spec as arg_spec_module

    def _test(argument_spec, parameters, mutually_exclusive=None, required_together=None, required_one_of=None, required_if=None, required_by=None):
        # SUT
        validator = arg_spec_module.ModuleArgumentSpecValidator(argument_spec, mutually_exclusive, required_together, required_one_of, required_if, required_by)
        result = validator.validate(parameters)
        return result

    parameters = {
        'name': 'Ansible',
        'age': 42,
        'subspec': {
            'subname': 'subspec.subname',
            'subdeprecated': 'subspec.subdeprecated',
        }
    }

# Generated at 2022-06-12 22:59:46.093582
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    with pytest.raises(AnsibleValidationError):
        ModuleArgumentSpecValidator({'test': {'type': 'str'}}).validate({'test': 1})

# Generated at 2022-06-12 22:59:55.536030
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    argument_spec = {
        'name': {
            'type': 'str',
            'required': True,
        },
        'age': {
            'type': 'int',
            'required': True,
        },
        'gender': {
            'type': 'str',
            'choices': ['Male', 'Female'],
            'required': True,
        },
    }

    parameters = {
        'name': 'bo',
        'age': '5',
        'gender': 'Female',
    }

    validator = ModuleArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)

    assert result.error_messages == []

# Generated at 2022-06-12 22:59:59.905557
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    from ansible.module_utils import basic

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

    # apply fixup to the module_utils.basic
    basic.MODULE_ARGUMENT_SPEC = {}
    basic.MODULE_COMPLEX_ARGS = {}

    # call basic._load_params() to update the MODULE_ARGUMENT_SPEC and
    # MODULE_COMPLEX_ARGS
    basic._load_params()

    # get the copy of the MODULE_ARGUMENT_SPEC and MODULE

# Generated at 2022-06-12 23:00:10.144112
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    parameters = dict(
        name=dict(value="", type=dict),
        age=dict(value="", type=dict),
        acct=dict(value="", type=dict),
        icount=dict(value="", type=dict),
    )
    argument_spec = dict(
        name=dict(type="str"),
        age=dict(type="int"),
        acct=dict(type="float"),
        icount=dict(type="int"),
        state=dict(default="present", choices=["present", "absent", "latest"]),
    )
    mutually_exclusive = [['name', 'age'], ['icount', 'acct']]
    required_together = (
        [["name", "age"], ["acct", "icount"]]
    )

# Generated at 2022-06-12 23:00:23.254710
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    """Unit test for method validate of class ModuleArgumentSpecValidator"""
    # pylint: disable=unused-variable
    from ansible.module_utils.common.arg_spec import ModuleArgumentSpecValidator
    from ansible.module_utils.common.validation import check_required_together

    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
        'nested': {'type': 'dict', 'argument_spec': {'a': {'type': 'int'}, 'b': {'type': 'int'}, 'c': {'type': 'int', 'version_added': '2.12'}}},
    }


# Generated at 2022-06-12 23:00:33.506157
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():

    # module has no alias error is found
    def validate_no_alias_error():
        from ansible.module_utils._text import to_text
        param = dict()
        param['module'] = dict()
        param['module']['value'] = 'setup'
        param['module']['type'] = 'str'
        params = {'module': 'setup'}
        arg_spec = dict()
        arg_spec['module'] = param
        validator = ModuleArgumentSpecValidator(arg_spec)
        result = validator.validate(params)
        assert isinstance(result, ValidationResult)
        assert isinstance(result.errors, AnsibleValidationErrorMultiple)
        assert len(result.errors) == 1
        assert isinstance(result.errors[0], AliasError)

# Generated at 2022-06-12 23:00:40.641768
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    result = {}

    exec_params={
        'name': 'bo',
        'age': '42',
        'connection': 'netconf'
    }

    argument_spec = {
            'name': {'type': 'str'},
            'age': {'type': 'int'},
            'connection': {'type': 'str', 'default': 'ssh'}
        }


    validator = ModuleArgumentSpecValidator(argument_spec)
    result = validator.validate(exec_params)

    assert len(result.error_messages) == 0

# Generated at 2022-06-12 23:00:51.484548
# Unit test for method validate of class ModuleArgumentSpecValidator

# Generated at 2022-06-12 23:01:02.393975
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    """
    This is a test function for the method validate of class ArgumentSpecValidator.
    """
    # Initializing a simple argument_spec and parameters
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    }
    parameters = {
        'name': 'bo',
        'age': '42',
    }

    # Initializing class ArgumentSpecValidator using the argument_spec
    validator = ArgumentSpecValidator(argument_spec)

    # Calling method validate of class ArgumentSpecValidator using the parameters
    result = validator.validate(parameters)

    if result.error_messages:
        raise Exception("Validation failed: {0}".format(", ".join(result.error_messages)))

    valid_params = result.validated_

# Generated at 2022-06-12 23:01:10.789633
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    # Create Aliases in Argument Spec
    argument_spec = dict(name={'type': 'str', 'aliases': ['full_name']},
                         age={'type': 'int', 'aliases': ['dog_years']},
                         height={'type': 'int', 'aliases': ['dog_height']})

    # Create dictionary with data for valid parameters
    parameters = dict(name='bo', age=42, height=5)

    validator = ModuleArgumentSpecValidator(argument_spec)

    # Run method under test
    result = validator.validate(parameters)
    
    assert result.validated_parameters == {'name': 'bo', 'age': 42, 'height': 5}
    assert result.unsupported_parameters == set()
    assert result.errors == AnsibleValidationErrorMultiple()
    assert result

# Generated at 2022-06-12 23:01:21.275774
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    from ansible.module_utils.common.warnings import Warning
    import warnings
    import pytest
    from ansible.errors import AnsibleModuleError

    argument_spec = {
        "name": {"type": "str"},
        "age": {"type": "int", "required": True},
    }
    validator = ArgumentSpecValidator(argument_spec)

    # make sure required parameters are checked
    parameters = {'name': 'bo'}
    with pytest.raises(AnsibleModuleError):
        result = validator.validate(parameters)

    parameters = {'age': '42'}
    with pytest.raises(AnsibleModuleError):
        result = validator.validate(parameters)

    # make sure parameter types are checked

# Generated at 2022-06-12 23:01:27.655602
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    """
    Make the test idempotent
    """
    # Setup
    module_argument_spec_validator = ModuleArgumentSpecValidator({})
    parameters = {
        'name': 'bo',
        'age': '42',
    }

    # Run
    result = module_argument_spec_validator.validate(parameters)

    # Assert
    assert result.errors == []

    # Cleanup - none necessary

# Generated at 2022-06-12 23:01:36.126135
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    from ansible.module_utils.common.parameters import NO_LOG_PARAMETERS
    from ansible.module_utils.common.validation import DeprecationWarning
    from ansible.module_utils.common.warnings import AnsibleDeprecationWarning

    class TestModuleArgumentSpecValidator(ModuleArgumentSpecValidator):
        def __init__(self, *args, **kwargs):
            super(TestModuleArgumentSpecValidator, self).__init__(*args, **kwargs)

    class TestParameters(dict):
        def __init__(self, *args, **kwargs):
            self.warnings = []
            self.deprecations = []
            super(TestParameters, self).__init__(*args, **kwargs)


# Generated at 2022-06-12 23:01:36.773028
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    assert(False)

# Generated at 2022-06-12 23:01:40.914794
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    assert True

# Generated at 2022-06-12 23:01:48.820939
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    # The test is just copied from test_ArgumentSpecValidator.py
    # but with an addition of one argument "warnings"

    from ansible.module_utils.common.compat import HAS_LOCALIZED_ANSIBLE_GETTEXT
    from ansible.module_utils.common.parameters import NO_LOG_PARAMETERS

    argument_spec = dict(
        name=dict(type='str'),
        state=dict(type='str', default='present', choices=['absent', 'present']),
    )

    mutually_exclusive = [
        ['name', 'state'],
        ['name', 'state'],
        ['name', 'state', 'msg'],
    ]


# Generated at 2022-06-12 23:01:58.147377
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    module_name = 'test_module'
    mutually_exclusive = [['one', 'two', 'three']]
    required_together = [['four', 'five', 'six']]
    required_one_of = [['seven', 'eight', 'nine']]
    required_if = [
        ['ten', 'eleven', ['twelve', 'thirteen', 'fourteen']],
        ['fifteen', 'sixteen', ['seventeen', 'eighteen', 'nineteen']],
    ]
    required_by = {
        'twenty': ['twenty_one', 'twenty_two'],
        'twenty_one': ['twenty_three'],
        'twenty_four': ['twenty_five'],
    }

# Generated at 2022-06-12 23:02:05.236641
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    """Test validate of ModuleArgumentSpecValidator"""
    import warnings
    argspec_validator = ModuleArgumentSpecValidator(None)
    assert argspec_validator.validate(None) is None
    with warnings.catch_warnings(record=True) as w:
        # Cause all warnings to always be triggered.
        warnings.simplefilter("always")
        argspec_validator = ModuleArgumentSpecValidator({'name': {'aliases': ['name1']}})
        argspec_validator.validate({'name1': 'test', 'name': 'test'})
        assert len(w) == 1
        assert str(w[-1].message) == 'Both option name and its alias name1 are set.'

    # Should not fail when _mutually_exclusive, _required_together, _required_one_of,

# Generated at 2022-06-12 23:02:16.108520
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    """Unit test for method validate of class ModuleArgumentSpecValidator"""
    from ansible.module_utils.common.warnings import AnsibleDeprecationWarning
    from ansible.module_utils.common.warnings import AnsibleFilterDeprecationWarning
    from ansible.module_utils.common.warnings import AnsibleIteratorDeprecationWarning

    import warnings
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")

# Generated at 2022-06-12 23:02:24.736100
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    name = dict(type='str')
    age = dict(type='int')
    valid_parameter_names = {'name', 'age'}

    argument_spec = {
        'name': name,
        'age': age,
    }

    result = ModuleArgumentSpecValidator(argument_spec).validate({'name': 'bo', 'age': '42'})

    assert len(result.errors) == 0
    assert result.validated_parameters == {'name': 'bo', 'age': 42}
    assert result._valid_parameter_names == valid_parameter_names

# Generated at 2022-06-12 23:02:30.257034
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

    assert not result.errors.has_errors()

# Generated at 2022-06-12 23:02:36.795212
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    from ..basic import AnsibleModule

    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    }

    def main():
        module = AnsibleModule(argument_spec=argument_spec)
        module.exit_json(changed=False, meta=module.params)

    parameters = {
        'name': 'bo',
        'age': '42',
    }

    with AnsibleModule(argument_spec=argument_spec, check_invalid_arguments=False) as module:
        module.params = parameters
        module.validate_parameters()

    assert module.params == {'name': 'bo', 'age': 42}

# Generated at 2022-06-12 23:02:47.224022
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    from ansible.module_utils.common import AnsibleModule, AnsibleModuleError
    params = {'state':'present', 'name':'test-ansible-validation-module', 'item_name':'test item'}
    state_to_be_validated = ['present','absent','disabled','enabled','suspended','locked']
    def test_module_validate_params(AnsibleModule):
        state = params['state']
        if state not in state_to_be_validated:
            raise AnsibleModuleError('state is not one of the list of states to be validated')
        return True

# Generated at 2022-06-12 23:02:52.508435
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    # Given
    argument_spec =  {
                        'name': {'type': 'str'},
                        'age': {'type': 'int'},
    }

    parameters = {
                    'name': 'bo',
                    'age': '42',
    }
    validator = ModuleArgumentSpecValidator(argument_spec)
    # When
    result = validator.validate(parameters)
    # Then
    assert result.error_messages == []
    assert result.validated_parameters == {'age': 42, 'name': 'bo'}
    assert result.unsupported_parameters == set()


# Generated at 2022-06-12 23:03:06.217209
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
  # create a validator with argument_spec
  argument_spec = {'str_arg': {'type': 'str'}, 'int_arg': {'type': 'int'}, 'bool_arg': {'type': 'bool'}, 'list_arg': {'type': 'list'}}
  validator = ArgumentSpecValidator(argument_spec)
  # test valid parameters
  parameters = {'str_arg': 'string', 'int_arg': 42, 'bool_arg': True, 'list_arg': []}
  valid_params = validator.validate(parameters)
  assert valid_params.errors == []
  assert valid_params.validated_parameters == parameters
  # test invalid parameters

# Generated at 2022-06-12 23:03:09.438416
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    import unittest

    class FakeArgSpecValidator:

        def validate(self, parameters):
            return None

    class TestModuleArgumentSpecValidator(unittest.TestCase):

        def test_ModuleArgumentSpecValidator_validate(self):
            validator = ModuleArgumentSpecValidator('validator')
            validator.validate = FakeArgSpecValidator().validate
            validator.validate('parameters')
            self.assertEqual(1, 1)

    unittest.main()



# Generated at 2022-06-12 23:03:10.347750
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    # TODO: Implement unit test
    pass

# Generated at 2022-06-12 23:03:15.297854
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    """
    This test class checks if the method validate of class ModuleArgumentSpecValidator works properly
    """

    class TestModuleArgumentSpecValidator(ModuleArgumentSpecValidator):
        """
        Mock Class for ModuleArgumentSpecValidator to enable testing
        """
        def __init__(self, *args, **kwargs):
            super(TestModuleArgumentSpecValidator, self).__init__(*args, **kwargs)

        def validate(self, parameters):
            """
            Method validate of class ModuleArgumentSpecValidator
            """
            result = super(TestModuleArgumentSpecValidator, self).validate(parameters)
            return result

    # initialize argument_spec with test values

# Generated at 2022-06-12 23:03:24.770450
# Unit test for constructor of class ArgumentSpecValidator
def test_ArgumentSpecValidator():
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    }
    mutually_exclusive = [['name', 'age']]
    required_together = [['name', 'age']]
    required_one_of = [['name', 'age']]
    required_if = [['name', 'age', ['age', 'name']]]
    required_by = {
        'name': ['name'],
        'age': ['age']
    }

    # create a validator

# Generated at 2022-06-12 23:03:30.119973
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    validator = ArgumentSpecValidator({
        'virtual_host': {'type': 'str', 'required': True},
        'port': {'type': 'int'},
    })

    parameters = {
        'virtual_host': 'www.ansible.com',
        'port': '8080',
    }

    result = validator.validate(parameters)
    assert result.validated_parameters['port'] == 8080

# Generated at 2022-06-12 23:03:35.880822
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    # valid_parameters = {'name': 'bo', 'age': '42'}
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


# Generated at 2022-06-12 23:03:42.339763
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

# Generated at 2022-06-12 23:03:49.970866
# Unit test for constructor of class ArgumentSpecValidator
def test_ArgumentSpecValidator():
    # Argspec is valid
    val = ArgumentSpecValidator(
        argument_spec={
            'atype1': {
                'type': 'str',
            }
        }
    )
    assert isinstance(val, ArgumentSpecValidator)

    # Argspec is invalid
    try:
        val = ArgumentSpecValidator(
            argument_spec={
                'atype1': {
                    'type': 'str',
                    'default': 'val1'
                }
            },
            mutually_exclusive=[['atype1']],
            required_together=[['atype1']]
        )
    except ValueError:
        pass



# Generated at 2022-06-12 23:03:58.892917
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    from ansible.module_utils.common.parameters import sanitize_keys
    from ansible.module_utils.common.text.converters import to_bytes
    import json
    import os


# Generated at 2022-06-12 23:04:18.073716
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    from ansible.module_utils.common.arg_spec import ArgumentSpecValidator
    argument_spec = {
        'name': {'type': 'str', 'default': 'bo'},
        'age': {'type': 'int', 'default': 42},
        'obj': {'type': 'dict', 'options': {
            'color': {'type': 'str', 'default': 'red'},
            'sides': {'type': 'int', 'default': 5},
        }, 'default': {
            'color': 'blue',
            'sides': 6,
        }}
    }
    parameters = {
    }
    validator = ArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)
    assert 'color' in result.validated_parameters['obj']

# Generated at 2022-06-12 23:04:27.492808
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    def _do_test(parameters, argument_spec, required_if, required_by, result):
        validator = ModuleArgumentSpecValidator(argument_spec, required_if=required_if, required_by=required_by)
        x = validator.validate(parameters)
        assert x.validated_parameters == result['validated_parameters']
        assert x.error_messages == result['error_messages']
        assert x.unsupported_parameters == result['unsupported_parameters']

    argument_spec = {
        'a': {'type': 'int'},
        'b': {'type': 'int'},
        'c': {'type': 'int'},
        'd': {'type': 'int'},
    }

# Generated at 2022-06-12 23:04:37.411241
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    argument_spec = {"path": {"type": "path", "required": True}}
    mutually_exclusive = []
    required_together = []
    required_one_of = []
    required_if = []
    required_by = {}
    validator = ArgumentSpecValidator(argument_spec, mutually_exclusive, required_together, required_one_of, required_if, required_by)
    parameters = {"path": "/tmp"}
    result = validator.validate(parameters)
    assert result.validated_parameters == {"path": "/tmp"}
    assert result.error_messages == []
    parameters = {"path": 42}
    result = validator.validate(parameters)
    assert result.validated_parameters == {"path": 42}

# Generated at 2022-06-12 23:04:43.122155
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    from ansible.module_utils.six import PY3

    # Create a validator object
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
        'workingdir': {'type': 'str', 'default': '~'},
        'logged_in': {'type': 'bool', 'default': False, 'no_log': True}
    }
    # Simple valid parameters
    parameters = {
        'name': 'bo',
        'age': '42',
    }
    validator = ModuleArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)
    # Validated parameters should be same as input parameters
    assert result.validated_parameters == parameters
    # Validates should be empty

# Generated at 2022-06-12 23:04:50.727043
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    # Testing with no_log
    argument_spec = dict(
        http_agent=dict(type='str', no_log=True)
    )
    result = ModuleArgumentSpecValidator(argument_spec).validate(dict(http_agent='User-Agent: Ansible'))
    assert not result.error_messages
    assert 'http_agent' in result.no_log_values

    # Testing with alias
    argument_spec = dict(
        funny_name=dict(type='str', aliases=['funny_alias']),
        funny_alias=dict(type='str'),
    )
    result = ModuleArgumentSpecValidator(argument_spec).validate(dict(funny_name='funnyname', funny_alias='funnyalias'))
    assert not result.error_messages

# Generated at 2022-06-12 23:04:55.416056
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    # Simulate a module using this class
    p = {
        'name': 'bo',
        'age': 42,
    }

    arg_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    }

    validator = ArgumentSpecValidator(argument_spec=arg_spec)
    result = validator.validate(parameters=p)
    assert result.error_messages == []

# Generated at 2022-06-12 23:05:06.501351
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    from ansible.module_utils.six.moves import StringIO

    class MyModule():
        def __init__(self, argument_spec=None, mutually_exclusive=None, required_together=None,
                     required_one_of=None, required_if=None, required_by=None):
            self.argument_spec = argument_spec
            self.mutually_exclusive = mutually_exclusive
            self.required_together = required_together
            self.required_one_of = required_one_of
            self.required_if = required_if
            self.required_by = required_by
            self.warnings = []
            self.deprecations = []

        @classmethod
        def create_argument_spec(cls, argument_spec, bypass_checks=False):
            return cls(argument_spec)


# Generated at 2022-06-12 23:05:09.235715
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    m_arg_spec_validator = ModuleArgumentSpecValidator({})
    result = m_arg_spec_validator.validate({})

    assert isinstance(result, ValidationResult)

# Generated at 2022-06-12 23:05:15.535528
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    from ansible.module_utils.common.warnings import AnsibleDeprecationWarning

    def deprecate(msg, version=None, date=None, collection_name=None):
        raise AnsibleDeprecationWarning("Deprecated {0}".format(msg))

    def warn(msg):
        raise AnsibleDeprecationWarning("Warning {0}".format(msg))

    a = {'name': {'type': 'str'}, 'age': {'type': 'int'}}
    p = {'name': 'bo', 'age': '42'}

    ats = ArgumentSpecValidator(a)
    result_ats = ats.validate(p)

    assert any(isinstance(e, AnsibleValidationErrorMultiple) for e in [result_ats.errors])


# Generated at 2022-06-12 23:05:25.417720
# Unit test for method validate of class ArgumentSpecValidator

# Generated at 2022-06-12 23:05:46.934908
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    import sys
    import pytest
    from ansible.module_utils._text import to_bytes

    # TEST 1 - exception if parameters is not a dict
    validator = ModuleArgumentSpecValidator({})

    with pytest.raises(TypeError) as excinfo:
        validator.validate([])
    assert 'parameters must be a dict' in to_native(excinfo.value)

    # TEST 2 - exception if argument_spec is not a dict
    validator = ModuleArgumentSpecValidator([])

    with pytest.raises(TypeError) as excinfo:
        validator.validate({})
    assert 'argument_spec must be a dict' in to_native(excinfo.value)

    # TEST 3 - exception if argument_spec contains unknown type

# Generated at 2022-06-12 23:05:55.794326
# Unit test for constructor of class ArgumentSpecValidator
def test_ArgumentSpecValidator():

    '''
    Unit test for constructor of class ArgumentSpecValidator
    '''

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

    required_one_of = [
        ['name', 'age'],
    ]

    required_if = [
        ['always', 'is_authed', ['name']],
    ]

    required_by = {
        'name': ['age'],
    }


# Generated at 2022-06-12 23:05:58.457627
# Unit test for constructor of class ArgumentSpecValidator
def test_ArgumentSpecValidator():
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    }

    validator = ArgumentSpecValidator(argument_spec)

    return validator


# Generated at 2022-06-12 23:06:02.026310
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
        'age': 42
    }