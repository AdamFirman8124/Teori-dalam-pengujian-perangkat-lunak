

# Generated at 2022-06-12 22:56:18.766893
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
    assert result.validated_parameters == {
        'name': 'bo',
        'age': 42,
    }

# Generated at 2022-06-12 22:56:29.498615
# Unit test for constructor of class ArgumentSpecValidator
def test_ArgumentSpecValidator():
    mutually_exclusive = []
    required_together = []
    required_one_of = []
    required_if = []
    required_by = []
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    }
    validator = ArgumentSpecValidator(argument_spec,
                 mutually_exclusive=mutually_exclusive,
                 required_together=required_together,
                 required_one_of=required_one_of,
                 required_if=required_if,
                 required_by=required_by
                 )
    assert(validator._mutually_exclusive == mutually_exclusive)
    assert(validator._required_together == required_together)
    assert(validator._required_one_of == required_one_of)

# Generated at 2022-06-12 22:56:37.963697
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    """Test validation of `deprecated` argument spec."""

    def fake_warn(msg):
        warnings.append(msg)

    def fake_deprecate(msg):
        deprecations.append(msg)

    # Save real functions
    real_warn = warn
    real_deprecate = deprecate
    # Replace with fake ones
    warn = fake_warn
    deprecate = fake_deprecate

    warnings = []
    deprecations = []


# Generated at 2022-06-12 22:56:38.910584
# Unit test for constructor of class ArgumentSpecValidator
def test_ArgumentSpecValidator():
    assert ArgumentSpecValidator


# Generated at 2022-06-12 22:56:42.955976
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    issues = ModuleArgumentSpecValidator({'name': {'type': 'str'}}, None, None, None, None, None).validate({'name': 'name'})
    assert issues.validated_parameters == {'name': 'name'}
    assert issues.errors.messages == []



# Generated at 2022-06-12 22:56:54.391396
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    # create a validation result object
    class ValidationResult:
        def __init__(self):
            self._validated_parameters = dict()
            self._no_log_values = list()
            self._unsupported_parameters = list()
            self._warnings = list()
            self._deprecations = list()
            self.errors = AnsibleValidationErrorMultiple()

    result = ValidationResult()
    result._no_log_values = [{'param': 'p', 'value': 'v'}]
    result._deprecations = [{'name': 'dn', 'version': 'v', 'date': 'd', 'collection_name': 'c'}]
    result._warnings = [{'option': 'o', 'alias': 'a'}]

    from ansible.module_utils._text import to

# Generated at 2022-06-12 22:57:02.926945
# Unit test for method validate of class ArgumentSpecValidator

# Generated at 2022-06-12 22:57:13.669070
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():

    # Test one required param, one optional param
    argument_spec = {'req_param': {'required': True, 'type': 'str'},
                     'opt_param': {'required': False, 'type': 'str'}}
    required_params_set = {'req_param': 'hello'}
    optional_params_set = {'opt_param': 'hi'}
    validator = ArgumentSpecValidator(argument_spec)
    required_param_result = validator.validate(required_params_set)
    optional_param_result = validator.validate(optional_params_set)
    assert not required_param_result.error_messages
    assert not optional_param_result.error_messages

    # Test alias for a param

# Generated at 2022-06-12 22:57:21.574991
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    result = None
    test_args = [
        {
            'argument_spec': {
                'name': {'type': 'str'},
                'age': {'type': 'int'},
            },
            'parameters': {
                'name': 'bo',
                'age': '42',
            },
        },
    ]
    for test_data in test_args:
        try:
            validator = ArgumentSpecValidator(test_data['argument_spec'])
            result = validator.validate(test_data['parameters'])
        except Exception as e:
            print(e)
            assert False, "AnsibleValidationError was raised"

        assert result.errors == [], result.errors
        assert result.unsupported_parameters == set(), result.unsupported_parameters


# Unit

# Generated at 2022-06-12 22:57:26.581411
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    argument_spec = {'name': {'type': 'str'}, 'age': {'type': 'int'}}
    parameters = {'name': 'bo', 'age': '42'}
    validator = ModuleArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)
    assert not result.error_messages

# Generated at 2022-06-12 22:57:39.393686
# Unit test for constructor of class ArgumentSpecValidator
def test_ArgumentSpecValidator():
    argument_spec = {'name': {'type': 'str'}, 'age': {'type': 'int'}}
    mutually_exclusive = ['name', 'age']
    required_together = [['name', 'age']]
    required_one_of = [['name', 'age']]
    required_if = [['name', 'age', ['name', 'age']]]
    required_by = {'name': ['name', 'age']}

    ArgumentSpecValidator(argument_spec,
                          mutually_exclusive=mutually_exclusive,
                          required_together=required_together,
                          required_one_of=required_one_of,
                          required_if=required_if,
                          required_by=required_by,
                          )

    # missing argument_spec

# Generated at 2022-06-12 22:57:47.898041
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    # Create an object of class ArgumentSpecValidator
    validator_object = ArgumentSpecValidator(argument_spec={'name': {'type': 'str'}, 'age': {'type': 'int'}})

    # Test validate method without any errors
    result = validator_object.validate({'name': 'bo', 'age': '42'})
    assert result.validated_parameters == {'name': 'bo', 'age': 42}
    assert len(result.error_messages) == 0

    # Test validate method with alias error
    result = validator_object.validate({'name': 'bo', 'age': '42', 'foo': 'bar', 'bar': 'baz'},
                                       aliases={'foo': 'bar'})
    assert result.unsupported_parameters == set(['bar'])
   

# Generated at 2022-06-12 22:57:54.231855
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    """Unit test for method validate of class ArgumentSpecValidator"""

    from ansible.module_utils.basic import AnsibleModule

    argument_spec = {'name': {'type': 'str'},
                     'age': {'type': 'int', 'default': 42},
                     'files': {'type': 'list'},
                     'size': {'type': 'dict', 'required': True},
                     'cities': {'type': 'dict', 'no_log': True, 'default': {'A': 'a'}},
                     'subspec': {'type': 'dict', 'default': {}, 'subspec': {
                         'subsubspec': {'type': 'list', 'suboptions': {'subsuboption': {'type': 'str'}}}}}}

    # test success

# Generated at 2022-06-12 22:57:58.523189
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():

    class A(object):
        pass

    a = A()
    a.argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    }

    a.validate({'name': 'bo', 'age': 42})

# Generated at 2022-06-12 22:58:06.700299
# Unit test for constructor of class ArgumentSpecValidator
def test_ArgumentSpecValidator():
    '''
    Argument Spec Validation class:

    argument_spec:
        - name
        - age
    '''
    argument_spec = {'name': {'type': 'str'},
                     'age': {'type': 'int'}}

    mutually_exclusive = [['name', 'age']]
    required_together = [['name', 'age']]
    required_one_of = [['name', 'age']]
    required_if = [["name", "age"]]
    required_by = {"name": ["age"]}


# Generated at 2022-06-12 22:58:09.661245
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    spec = dict(foo=dict(type='str'))
    specification = ModuleArgumentSpecValidator(spec)
    assert specification.validate({'foo': 'bar'})

# Generated at 2022-06-12 22:58:19.006093
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():  # pylint: disable=missing-param-doc,missing-type-doc
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


# Generated at 2022-06-12 22:58:20.946735
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    v = ModuleArgumentSpecValidator({}, [])

    assert isinstance(v.validate({}), ValidationResult)

# Generated at 2022-06-12 22:58:21.618850
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    pass

# Generated at 2022-06-12 22:58:24.657290
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    params = {'validated_parameters': {}}
    result = ModuleArgumentSpecValidator.validate(params)
    assert(result == params.get('validated_parameters'))

# Generated at 2022-06-12 22:58:32.936141
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    module_argument_spec = {
        "parameter1": {
            "type": "str",
            "default": "value1",
            "aliases": ["alias1", "alias2"],
        },
    }

    parameters = {"parameter1": "value1"}

    validator = ModuleArgumentSpecValidator(module_argument_spec)
    result = validator.validate(parameters)
    assert result.validated_parameters['parameter1'] == 'value1'
    assert result.errors == []
    assert result.unsupported_parameters == set()
    assert result.error_messages == []

# Generated at 2022-06-12 22:58:42.650968
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

    assert result.validated_parameters == {'name': 'bo', 'age': 42}, \
        "result.validated_parameters return should be {'name': 'bo', 'age': 42}"

    assert result.error_messages == [], "result.error_messages should be []"
    assert result.unsupported_parameters == set(), "result.unsupported_parameters should be []"



# Generated at 2022-06-12 22:58:52.946298
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    """Test validate method of class ArgumentSpecValidator"""
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
        'ips': {'type': 'list', 'elements': 'str'},
    }
    parameters = {
        'name': 'bo',
        'age': 40,
    }
    validator = ArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)
    assert result.error_messages == []
    assert isinstance(result.validated_parameters.get('name'), str)
    assert isinstance(result.validated_parameters.get('age'), int)
    assert result.validated_parameters.get('name') == 'bo'

# Generated at 2022-06-12 22:58:56.886208
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



# Generated at 2022-06-12 22:59:06.819890
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

    expected = {
        'age': 42,
        'name': 'bo',
    }

    assert result.validated_parameters == expected
    assert result.error_messages == []
    assert result._deprecations == []
    assert result._warnings == []

# Generated at 2022-06-12 22:59:14.327219
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    # TODO: review this test
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

    assert not result.errors
    assert not result.error_messages
    assert result.validated_parameters == {
        'name': 'bo',
        'age': 42,
    }

# Generated at 2022-06-12 22:59:24.353110
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
        'aliased': {'type': 'str', 'aliases': ['aliased_alias', 'alias3']},
    }
    mutually_exclusive = [['name', 'age']]
    required_together = [['name', 'aliased']]
    required_one_of = [['name', 'age']]
    required_if = [["name", None, ["aliased"]], ["name", "foo", ["age"]]]
    required_by = {"name": ["aliased"]}


# Generated at 2022-06-12 22:59:31.592620
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    arg_spec = {
                 'name': {'type': 'str'},
                 'age': {'type': 'int'}
               }

    parameters = {
                    'name': 'bo',
                    'age': '42'
                }

    validator = ModuleArgumentSpecValidator(arg_spec)
    result = validator.validate(parameters)

    assert not result.error_messages

    assert result.validated_parameters['name'] == 'bo'
    assert result.validated_parameters['age'] == 42

# Generated at 2022-06-12 22:59:37.142504
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    """
    The purpose of this test is to verify that the deprecations are printed and the warnings are returned
    """
    from ansible.module_utils.common.arg_spec import ModuleArgumentSpecValidator
    from ansible.module_utils._text import to_text

    argument_spec = {'name': {'type': 'str'},
                     'age': {'type': 'int'},
                     }

    parameters = {'name': 'bo',
                  'age': '42',
                  }

    validator = ModuleArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)

    assert result._deprecations == [], "Deprecations were generated"
    assert result._warnings == [], "Warnings were generated"


# Generated at 2022-06-12 22:59:42.539270
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    from collections import namedtuple
    from ansible.module_utils.common.text.converters import to_text
    TupleMappingProxyType = namedtuple('mappingproxy', 'keys')
    Deprecation = namedtuple('Deprecation', ('name', 'version', 'date', 'collection_name'))

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

    # expectation
    no_log_values = []
    error = None
    error_messages = []
    deprecations = []

# Generated at 2022-06-12 22:59:55.125016
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    from ansible.module_utils.common import ModuleLoggerAdapter
    from ansible.module_utils.common.warnings import ModuleDeprecationWarning

    from ansible.module_utils.common.parameters import sanitize_keys
    from ansible.module_utils.common.warnings import deprecate


    VALIDATED_PARAMETER = {'name': 'bo', 'age': 42}


# Generated at 2022-06-12 23:00:00.691055
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    msg = "Both option 'name' and its alias 'alias' are set."
    result = ValidationResult({'name': 'bo', 'alias': 'miles'})
    result._warnings.append({'option': 'name', 'alias': 'alias'})
    assert [w['option'] for w in result._warnings] == ['name']
    assert w['alias'] == 'alias'
    assert w['option'] == 'name'
    assert w['alias'] == 'alias'
    assert msg in str(result._warnings)

# Generated at 2022-06-12 23:00:06.126164
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    """Just checks if ModuleArgumentSpecValidator class validate method works well.
    Not a true unit test, only some basic checks.
    """
    from ansible.module_utils.common.text.converters import to_text
    from ansible.module_utils.common.parameters import sanitize_keys
    import json

    # case: custom arg_spec and valid parameters
    arg_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    }

    parameters = {
        'name': 'bo',
        'age': 42,
    }

    validator = ModuleArgumentSpecValidator(arg_spec)
    result = validator.validate(parameters)

    assert result.validated_parameters == parameters
    assert result.errors.get_

# Generated at 2022-06-12 23:00:16.575485
# Unit test for method validate of class ModuleArgumentSpecValidator

# Generated at 2022-06-12 23:00:23.902979
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    args = {
        'ip': {'type': 'str', 'required': True},
        'netmask': {'type': 'int', 'required': True},
        'gateway': {'type': 'str'},
        'state': {'type': 'str'},
        'dns': {'type': 'list', 'elements': 'str'},
        'aliases': {'type': 'list', 'elements': 'str'}
    }


# Generated at 2022-06-12 23:00:34.279354
# Unit test for constructor of class ArgumentSpecValidator
def test_ArgumentSpecValidator():
    # test init
    validator = ArgumentSpecValidator({}, ['a', 'b'], [], [], [], {})
    validator.arguments = []
    validator.no_log_values = set()
    validator.unsupported_parameters = set()
    validator.warnings = []
    validator.deprecations = []
    validator.errors = AnsibleValidationErrorMultiple()
    assert validator.mutually_exclusive == ['a', 'b']
    assert validator.required_together == []
    assert validator.required_one_of == []
    assert validator.required_if == []
    assert validator.required_by == {}
    assert validator.no_log_values == set()
    assert validator.unsupported_parameters == set()
    assert validator.warnings == []

# Generated at 2022-06-12 23:00:43.169844
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    # Mock warn to capture it in test
    def mock_warn(message):
        mock_warn.message = message
    mock_warn.message = ''
    original_warn = warn
    warn = mock_warn

    # Mock deprecate to capture it in test
    def mock_deprecate(message, version=None, date=None, collection_name=None, collection_requirement=None):
        mock_deprecate.message = message
    mock_deprecate.message = ''
    original_deprecate = deprecate
    deprecate = mock_deprecate


# Generated at 2022-06-12 23:00:52.904979
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    """Unit test for method validate of class ArgumentSpecValidator

    Raises:
        AssertionError: If the test case fails
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

    assert not result.error_messages
    assert result.validated_parameters == {
        'name': 'bo',
        'age': 42,
    }

# Generated at 2022-06-12 23:01:01.398806
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

    #assert result.error_messages == [], result.error_messages
    assert result.validated_parameters == {'name': 'bo', 'age': 42}
    assert result.unsupported_parameters == set()



# Generated at 2022-06-12 23:01:06.151814
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    result = None
    module_argument_spec = {}

    def get_module_argument_spec():
        """Get module_argument_spec"""
        return module_argument_spec

    module_argument_spec_validator_instance = ArgumentSpecValidator(get_module_argument_spec())
    module_argument_spec = {"name": {"type": "str", "default": "bo", "aliases": ["name"]}}
    parameters = {"name": "bo"}
    result = module_argument_spec_validator_instance.validate(parameters)
    assert result.error_messages == []
    assert result.validated_parameters == {"name": "bo"}

    def get_module_argument_spec():
        """Get module_argument_spec"""
        return module_argument_spec

    module_argument_spec_validator_instance

# Generated at 2022-06-12 23:01:17.299432
# Unit test for constructor of class ArgumentSpecValidator
def test_ArgumentSpecValidator():
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    }

    validator = ArgumentSpecValidator(argument_spec)

    assert validator
    assert validator._mutually_exclusive is None
    assert validator._required_together is None
    assert validator._required_one_of is None
    assert validator._required_if is None
    assert validator._required_by is None
    assert validator._valid_parameter_names == {'age', 'name'}
    assert validator.argument_spec == argument_spec

# Generated at 2022-06-12 23:01:28.162516
# Unit test for constructor of class ArgumentSpecValidator
def test_ArgumentSpecValidator():
    test_data = {
        'argument_spec': {
            'name': {'type': 'str'},
            'age': {'type': 'int'},
        },
        'mutually_exclusive': [['name', 'age']],
        'required_together': [('name', 'age')],
        'required_one_of': [['name', 'age']],
        'required_if': [('name', 'age', 'age')],
        'required_by': {'name': 'age'}
    }


# Generated at 2022-06-12 23:01:36.422218
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.common.text.converters import to_str
    from ansible.module_utils.common.validation import check_required_if
    from ansible.module_utils.common.warnings import warn

    # init
    argument_spec = {
        "name": {"type": "str"},
        "age": {"type": "int"},
    }

    parameters = {
        "name": "bo",
        "age": "42",
    }

    validator = ArgumentSpecValidator(
        argument_spec,
        required_if=[
            ("name", "bo", ["age"]),
        ],
        required_together=[
            ["age", "name"],
        ],
    )

    # run code
    result = validator

# Generated at 2022-06-12 23:01:43.671754
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

    assert result.error_messages == ['Parameter age expects an integer value, received 42 (type=str)']
    assert result.validated_parameters == {'name': 'bo', 'age': 42}

# Generated at 2022-06-12 23:01:50.513182
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    """Unit test for :meth:`ModuleArgumentSpecValidator.validate()
    <ansible.module_utils.common.arg_spec.ModuleArgumentSpecValidator.validate()>`

    Ensures that the module-specific validations are run during validation. For example,
    a deprecation warning for a parameter should be emitted by :class:`ModuleArgumentSpecValidator`
    but not by :class:`ArgumentSpecValidator`.

    Additionaly, unit tests must be added for any new module-specific validations added to
    :class:`ModuleArgumentSpecValidator`.validate() to ensure they are only run in the
    module-specific version.
    """
    import sys
    import unittest

    # Ensure the deprecation warning is emitted by ModuleArgumentSpecValidator.validate()

# Generated at 2022-06-12 23:01:56.673438
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    validator = ArgumentSpecValidator({'answer': {'type': 'str', 'choices': ['yes', 'no', 'maybe']}})
    parameters = {'answer': 'yes'}
    result = validator.validate(parameters)
    assert len(result.errors) == 0
    assert result.validated_parameters['answer'] == 'yes'
    assert result._no_log_values == set()
    assert result._unsupported_parameters == set()
    assert result.error_messages == []

# Generated at 2022-06-12 23:02:04.650605
# Unit test for constructor of class ArgumentSpecValidator
def test_ArgumentSpecValidator():
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    }
    mutually_exclusive = [["name", "age"]]
    required_together = [["name", "age"]]
    required_one_of = [["name", "age"]]
    required_if = [["name", "age", []]]
    required_by = {"name": [], "age": []}
    validator = ArgumentSpecValidator(argument_spec, mutually_exclusive, required_together,
                                      required_one_of, required_if, required_by)

    assert validator.argument_spec == argument_spec
    assert validator._mutually_exclusive == mutually_exclusive
    assert validator._required_together == required_together
    assert validator._required_one

# Generated at 2022-06-12 23:02:12.930567
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    # Prepare the test
    validator = ModuleArgumentSpecValidator(argument_spec={
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    })
    parameters = {
        'name': 'bo',
        'age': '42',
    }

    # Run the test
    result = validator.validate(parameters)

    # Verify the results
    assert result.error_messages == []
    assert result.validated_parameters == {'name': 'bo', 'age': 42}
    assert result.unsupported_parameters == set()

# Generated at 2022-06-12 23:02:23.980840
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    # test for method validate of class ModuleArgumentSpecValidator
    # scenario: validation fails with alias deprecation
    argument_spec = {
        'first': {'type': 'str', 'aliases': ['second']},
    }
    validator = ModuleArgumentSpecValidator(argument_spec)
    result = validator.validate({'first': 'first_val', 'second': 'second_val'})
    assert result.error_messages == []
    assert result.deprecations == ['Alias \'second\' is deprecated. See the module docs for more information']
    assert result.warnings == []

    # scenario: validation fails
    argument_spec = {
        'first': {'type': 'int'},
    }
    validator = ModuleArgumentSpecValidator(argument_spec)
    result = validator.validate

# Generated at 2022-06-12 23:02:33.850418
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():

    # parameter spec of both lib/ansible/module_utils/network/common/utils.py and
    # lib/ansible/modules/network/ios/ios_interfaces.py are used as parameters
    argument_spec = {
        "provider": {
            "type": "dict",
            "required": True,
            "options": {
                "username": {
                    "type": "str"
                },
                "password": {
                    "type": "str",
                    "no_log": True,
                },
            }
        },
        "port": {
            "type": "dict",
            "required": True,
            "subspec": {
                "name": {
                    "type": "str",
                    "required": True,
                    "default": None,
                },
            }
        },
    }

# Generated at 2022-06-12 23:02:43.020291
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

    validator = ArgumentSpecValidator(argument_spec=argument_spec)
    result = validator.validate(parameters)

    assert parameters == result.validated_parameters

# Generated at 2022-06-12 23:02:52.072526
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    }

    validator = ArgumentSpecValidator(argument_spec)

    """
    Valid parameters
    """
    params = {
        'name': 'bo',
        'age': 42,
    }

    result = validator.validate(params)
    assert result.errors == []
    assert result.validated_parameters == params

    """
    Reason: Invalid type
    """
    params = {
        'name': 'bo',
        'age': "seven",
    }

    result = validator.validate(params)
    assert result.errors != []
    assert result.validated_parameters != params

    """
    Reason: Invalid value
    """
    argument_spec

# Generated at 2022-06-12 23:03:02.116881
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    from ansible.module_utils.common.text.converters import to_native


# Generated at 2022-06-12 23:03:05.124029
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
    assert len(result.errors) == 0
    assert result.validated_parameters == {'name': 'bo', 'age': 42}



# Generated at 2022-06-12 23:03:12.596438
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
    # Passing the arguments
    validator = ModuleArgumentSpecValidator(argument_spec)
    # validate the arguments
    result = validator.validate(parameters)
    # To check the result
    assert len(result.errors) == 1
    assert result.errors[0].message == "Unsupported parameters for (ansible_module) module: 'age'. Supported parameters include: 'age', 'name'."



# Generated at 2022-06-12 23:03:17.531401
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    # pylint: disable=too-many-locals,import-error
    # pylint: disable=import-error,no-name-in-module
    from ansible.module_utils.basic import AnsibleModule
    import os
    import tempfile
    from ansible.module_utils.six import BytesIO

    temp_file = tempfile.mkstemp()
    module_name = 'test_module'


# Generated at 2022-06-12 23:03:24.906430
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


# Generated at 2022-06-12 23:03:33.762932
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    # Arrange
    import ansible.module_utils.common.arg_spec as arg_spec
    import ansible.module_utils.common.validation as validation
    import ansible.module_utils.common.warnings as warnings

    def mock_check_mutually_exclusive(mutually_exclusive, params):
        raise TypeError("")

    def mock_check_required_arguments(*args, **kwargs):
        raise TypeError("")

    def mock_check_required_one_of(required_one_of, params):
        raise TypeError("")

    def mock_check_required_together(required_together, params):
        raise TypeError("")

    def mock_check_required_if(required_if, params):
        raise TypeError("")

    def mock_warn(msg):
        module_warnings.append

# Generated at 2022-06-12 23:03:42.901041
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    module_argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    }
    parameters = {
        'name': 'bo',
        'age': '42',
    }
    validator = ArgumentSpecValidator(module_argument_spec)
    result = validator.validate(parameters)

    if result.error_messages:
        sys.exit("Validation failed: {0}".format(", ".join(result.error_messages)))

    valid_params = result.validated_parameters
    assert valid_params['name'] == 'bo'
    assert valid_params['age'] == 42

# Generated at 2022-06-12 23:03:52.431674
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    # test with no warnings/deprecations
    module_args = {
        'name': 'bo',
        'age': '42',
        'no_log': 'some_no_log_value'
    }
    argument_spec = {
        'name': {
            'type': 'str',
        },
        'age': {
            'type': 'int'
        },
        'no_log': {
            'type': 'str',
            'no_log': True
        }
    }

    validator = ModuleArgumentSpecValidator(argument_spec)
    result = validator.validate(module_args)

    assert not result._deprecations
    assert not result._warnings
    assert result.validated_parameters['name'] == 'bo'

# Generated at 2022-06-12 23:04:00.472058
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    #Test for issue #70698
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

# Generated at 2022-06-12 23:04:09.952997
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    result = dict(
        deprecations=[],
        warnings=[],
        validated_parameters={},
        unsupported_parameters=set(),
        error_messages=[]
    )

    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    }

    parameters = {
        'name': 'bo',
        'age': '42',
    }

    validator = ModuleArgumentSpecValidator(argument_spec)
    result_validate = validator.validate(parameters)

    assert (result == result_validate._asdict())

# Generated at 2022-06-12 23:04:15.306308
# Unit test for method validate of class ArgumentSpecValidator

# Generated at 2022-06-12 23:04:15.669124
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    pass

# Generated at 2022-06-12 23:04:16.572574
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    result = ArgumentSpecValidator.validate(self, parameters)

# Generated at 2022-06-12 23:04:21.815100
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    import sys
    import unittest
    sys_exit = sys.exit

    def sys_exit_mock(val):
        # Unittest can't check the value of sys.exit
        # So, raise a custom exception, so we can catch it
        raise SystemExit(val)

    def mock_warn(warning):
        warnings.append(warning)

    def mock_deprecate(message, version=None, date=None, collection_name=None):
        deprecations.append(dict(
            name=message,
            version=version,
            date=date,
            collection_name=collection_name,
        ))

    warnings = []
    deprecations = []
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    }

# Generated at 2022-06-12 23:04:24.318723
# Unit test for constructor of class ArgumentSpecValidator
def test_ArgumentSpecValidator():
    argument_spec = {'name': {'type': 'str'}}
    validator = ArgumentSpecValidator(argument_spec)
    assert validator


# Generated at 2022-06-12 23:04:34.626815
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    """Unit test for method `validate` of class `ModuleArgumentSpecValidator`."""
    # test when no_log is set to true in the argument_spec
    class MockResult(ValidationResult):
        def __init__(self, no_log_values, validated_parameters):
            self._no_log_values = no_log_values
            self._validated_parameters = deepcopy(validated_parameters)
            self.errors = AnsibleValidationErrorMultiple()

    class MockValidator(ModuleArgumentSpecValidator):
        def __init__(self, no_log_values, validated_parameters):
            self._no_log_values = no_log_values
            self._validated_parameters = deepcopy(validated_parameters)
            self.errors = AnsibleValidationErrorMultiple()

       

# Generated at 2022-06-12 23:04:42.672884
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    """Test validate method of class ArgumentSpecValidator"""

    # All argument_spec entries have 'type': 'str' and no valid choices
    def validate_arguments_returned(argument_spec, parameters, requested_arguments):
        """
        Validate arguments are returned from ArgumentSpecValidator.validate().

        :arg argument_spec: Specification of valid parameters and their type. May
            include nested argument specs.
        :type argument_spec: dict[str, dict]

        :arg parameters: Parameters to validate against the argument spec
        :type parameters: dict[str, dict]

        :arg requested_arguments: the arguments to be tested
        :type requested_arguments: list[dict]

        :return: boolean
        """
        validator = ArgumentSpecValidator(argument_spec)
        result = validator.validate(parameters)

# Generated at 2022-06-12 23:04:50.349890
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    class Test:
        """
        Simple class with parameter deprecate.
        """
        def __init__(self):
            self.deprecations = []
        def deprecate(self, msg, version=None, date=None, collection_name=None):
            self.deprecations.append({msg: dict(version=version, date=date, collection_name=collection_name)})

    test = Test()

    validator = ModuleArgumentSpecValidator({'_test_deprecate_alias': {'type': 'str', 'aliases': ['test_deprecate_alias']}}, mutually_exclusive=[])
    result = validator.validate({'_test_deprecate_alias': True})

    assert len(test.deprecations) == 1
    assert len(result.errors) == 0



# Generated at 2022-06-12 23:05:00.849421
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    module_tuple = ModuleArgumentSpecValidator
    ansible_module_tuple = AnsibleModule
    args = [{'name': {'type': 'str'}, 'age': {'type': 'int'}}, None, None, None, None, None]
    parameters = {'name': 'bo', 'age': '42'}
    result = module_tuple.validate(module_tuple, parameters)
    assert result.error_messages == []
    assert result.validated_parameters == {'name': 'bo', 'age': 42}

# Generated at 2022-06-12 23:05:10.782239
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    # mock imports
    import sys
    sys.modules['ansible'] = mock.MagicMock()
    sys.modules['ansible.module_utils'] = mock.MagicMock()
    sys.modules['ansible.module_utils.common'] = mock.MagicMock()
    sys.modules['ansible.module_utils.common.warnings'] = mock.MagicMock()
    sys.modules['ansible.module_utils.common.validation'] = mock.MagicMock()
    sys.modules['ansible.module_utils.common.errors'] = mock.MagicMock()

    # mock ansible.module_utils.common.warnings.deprecate to call the original function
    orig_deprecate = ansible.module_utils.common.warnings.deprecate
    ansible.module_utils.common.warn

# Generated at 2022-06-12 23:05:16.733821
# Unit test for constructor of class ArgumentSpecValidator
def test_ArgumentSpecValidator():
    argument_spec = {'name':{'type':'str'}, 'age':{'type':'int'}}
    validator = ArgumentSpecValidator(argument_spec)
    assert len(validator.argument_spec) == 2
    assert sorted(validator.argument_spec.keys()) == ['age','name']
    assert validator.argument_spec['name']['type'] == 'str'
    assert validator.argument_spec['age']['type'] == 'int'
    assert isinstance(validator, ArgumentSpecValidator)


# Generated at 2022-06-12 23:05:25.165373
# Unit test for constructor of class ArgumentSpecValidator
def test_ArgumentSpecValidator():
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    }

    mutually_exclusive = ['name', 'age']

    required_together = [['name', 'age']]

    required_one_of = [['name', 'age']]

    required_if = []

    required_by = {}

    validator = ArgumentSpecValidator(argument_spec,
                                      mutually_exclusive,
                                      required_together,
                                      required_one_of,
                                      required_if,
                                      required_by)
    assert validator is not None



# Generated at 2022-06-12 23:05:35.343232
# Unit test for constructor of class ArgumentSpecValidator
def test_ArgumentSpecValidator():
    # Test for argument_spec
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    }
    # Test for mutually_exclusive
    mutually_exclusive = [
        ['name', 'age'],
        ['name', 'age'],
    ]

    # Test for required_together
    required_together = [
        ['name', 'age'],
        ['name', 'age'],
    ]

    # Test for required_one_of
    required_one_of = [
        ['name', 'age'],
        ['name', 'age'],
    ]

    # Test for required_if
    required_if = [
        ['name', 'age'],
        ['name', 'age'],
    ]

    # Test for required_by

# Generated at 2022-06-12 23:05:43.230367
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
    assert result.error_messages == [], "Unexpected errors {e}".format(e=result.error_messages)

    parameters = {
        'name': 'bo',
        'age': 'abc',
    }
    result = validator.validate(parameters)

# Generated at 2022-06-12 23:05:52.287121
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    from ansible.module_utils.common.validation import check_mutually_exclusive
    from ansible.module_utils._text import to_native
    # Test mutually_exclusive
    argument_spec = dict(a=dict(type='bool'),
                         b=dict(type='bool'),
                         mutually_exclusive=[['a', 'b']])
    validator = ModuleArgumentSpecValidator(argument_spec)
    parameters = dict(a=True, b=True)
    result = validator.validate(parameters)
    assert len(result.errors) == 1
    assert isinstance(result.errors[0], MutuallyExclusiveError)
    assert "are mutually exclusive" in result.errors[0].message
    # Test RequiredError
    argument_spec = dict(a=dict(type='bool', required=True))
    valid

# Generated at 2022-06-12 23:05:59.260542
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

    assert not result.errors
    assert not result._deprecations
    assert not result._warnings
    assert result._validated_parameters == {'name': 'bo', 'age': 42}
    assert not result._unsupported_parameters
    assert not result._no_log_values
