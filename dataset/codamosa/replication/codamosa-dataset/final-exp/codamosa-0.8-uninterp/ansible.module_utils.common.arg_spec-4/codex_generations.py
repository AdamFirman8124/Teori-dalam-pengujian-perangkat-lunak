

# Generated at 2022-06-12 22:56:20.862042
# Unit test for constructor of class ArgumentSpecValidator
def test_ArgumentSpecValidator():
    from ansible.module_utils.common import REMOVED_IF_GTE_34
    argument_spec = dict(
        name=dict(type='str'),
        age=dict(type='int'),
        banana=dict(type='int', removed_in_version=2.9, removed_from_collection='community.aws')
    )
    mutually_exclusive = [['name', 'age']]
    required_together = [['name', 'age']]
    required_one_of = [['name', 'age']]
    required_if = [['name', 'age', 'banana']]
    required_by = {'name': 'age'}
    validator = ArgumentSpecValidator(argument_spec, mutually_exclusive, required_together, required_one_of,
                                      required_if, required_by)

   

# Generated at 2022-06-12 22:56:31.547146
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    test_argument_spec = {
        'name': {'type': 'str', 'aliases': ['name_alias']},
        'age': {'type': 'int'},
    }

    test_parameters = {
        'name': 'bo',
        'age': '42',
    }

    validator = ModuleArgumentSpecValidator(test_argument_spec)

    # ensure our get_warnings function properly calls the warn function
    from ansible.module_utils import warnings as a_warning
    a_warning.warn = lambda m: 'called with %s' % m

    # ensure our get_deprecation function properly calls the deprecate function
    from ansible.module_utils import deprecation as a_deprecation

# Generated at 2022-06-12 22:56:39.043596
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():

    from ansible.module_utils.basic import AnsibleModule

    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int', 'deprecated': {'version': '2.13', 'removed_in': '2.15', 'why': 'existing_why',
                                              'collection_name': 'collection_name', 'alt': 'new_name'}},
    }

    parameters = {
        'name': 'bo',
        'age': '42',
    }

    module = AnsibleModule(argument_spec=argument_spec)

    validator = ModuleArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)

    assert result.validated_parameters['name'] == 'bo'
    assert result.validated_

# Generated at 2022-06-12 22:56:49.890291
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    legal_inputs = [
        [1, 2, 3],
        [2, 3, 4],
        [3, 4, 5],
        [4, 5, 6],
        ['a', 'b', 'c'],
        ['b', 'c', 'd'],
        ['c', 'd', 'e'],
        ['d', 'e', 'f']]
    mutually_exclusive = [['a', 'b'], ['b', 'c'], ['c', 'd'], ['d', 'a'], ['a', 'f', 'g']]
    required_together = [['a', 'b', 'c'], ['b', 'c', 'd', 'e'], ['c', 'd', 'e', 'f']]

# Generated at 2022-06-12 22:56:56.882498
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    """Check if validate method of class
    ModuleArgumentSpecValidator is working correctly.
    """

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

# Generated at 2022-06-12 22:57:03.020387
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
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


# Generated at 2022-06-12 22:57:13.732084
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    from collections import namedtuple
    from ansible.module_utils.six import PY3

    Deprecation = namedtuple('deprecation', ['name', 'version', 'date', 'collection_name'])
    deprecation_01 = Deprecation(name='boo', version=None, date=None, collection_name=None)
    deprecation_02 = Deprecation(name='boo', version='2.13', date='2019-12-01', collection_name='deprecated_collection')

    Warning = namedtuple('warning', ['option', 'alias'])
    warning_01 = Warning(option='foo', alias='boo')
    warning_02 = Warning(option='foo', alias='boo')


# Generated at 2022-06-12 22:57:18.736268
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    argument_spec = {
        "name": {"type": "str"},
        "age": {"type": "int"},
    }

    parameters = {
        "name": "bo",
        "age": "42",
    }

    return_value = {
        "name": "bo",
        "age": 42,
    }

    validator = ArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)

    assert result.validated_parameters == return_value



# Generated at 2022-06-12 22:57:19.312998
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    pass

# Generated at 2022-06-12 22:57:25.848726
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    # setup
    data_in = {
        'b': {}
    }
    argument_spec = {
        'a': {'type': 'str'},
        'b': {'type': 'dict'},
    }
    a = ModuleArgumentSpecValidator(argument_spec)

    # action
    result = a.validate(data_in)

    # assert
    assert result.errors == []
    assert result.validated_parameters == {'a': '', 'b': {}}

# Generated at 2022-06-12 22:57:44.259437
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    '''test for method validate of class ModuleArgumentSpecValidator'''
    import sys
    import os
    sys.path.append(os.path.dirname(__file__).replace('lib/ansible/module_utils/common/arg_spec', 'lib/ansible'))
    from ansible.module_utils.common.warnings import DeprecationWarning
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
    warn_msg = 'Both option name and its alias name are set.'
    assert result.error

# Generated at 2022-06-12 22:57:52.207270
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    from six.moves import StringIO
    from ansible.module_utils.six import PY3
    from ansible.module_utils.basic import AnsibleModule

    def _get_warnings(out, warn_regex):
        for line in out:
            if warn_regex.search(line):
                yield line

    class TestAnsibleModule(AnsibleModule):
        def exit_json(self, *args, **kwargs):
            return args, kwargs

        def fail_json(self, *args, **kwargs):
            self.exit_args = args
            self.exit_kwargs = kwargs
            raise Exception('FAIL')


# Generated at 2022-06-12 22:58:02.121899
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    """Unit test for method validate of class ArgumentSpecValidator"""

    argument_spec={
        'age': {'type': 'int'},
        'name': {'type': 'str'},
        'job': {'type': 'str', 'choices': ['pilot', 'janitor', 'sailor', 'spy']},
        'siblings': {'type': 'list', 'elements': 'str'},
        'has_mole': {'type': 'bool'},
        'info': {'type': 'dict'}
    }

# Generated at 2022-06-12 22:58:12.106103
# Unit test for constructor of class ArgumentSpecValidator
def test_ArgumentSpecValidator():
    """ArgumentSpecValidator class constructor."""


# Generated at 2022-06-12 22:58:18.093813
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    }

    parameters = {
        'age': '42',
    }

    validator = ModuleArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)
    assert result.error_messages == ['name is required']

# Generated at 2022-06-12 22:58:28.805407
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    import sys
    sys.path.append('/home/ansible/ansible/lib/ansible/module_utils/common')
    sys.path.append('/home/ansible/ansible/lib/ansible/module_utils/common/arg_spec')
    from ansible.module_utils.common.arg_spec import ModuleArgumentSpecValidator
    arguments_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'}
    }
    parameters = {
        'name': 'bo',
        'age': '42',
    }
    validator = ModuleArgumentSpecValidator(arguments_spec)
    result = validator.validate(parameters)

    assert len(result.errors) == 0
    assert len(result._deprecations) == 0

# Generated at 2022-06-12 22:58:30.957573
# Unit test for constructor of class ArgumentSpecValidator
def test_ArgumentSpecValidator():
    res = ArgumentSpecValidator({
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    })

    assert isinstance(res, ArgumentSpecValidator)

# Generated at 2022-06-12 22:58:36.832234
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    argument_spec = {
        'age': {'type': 'int'},
        'name': {'type': 'str'},
    }

    # test_parameters_with_age_as_string_raises_error
    parameters = {
        'age': '42',
        'name': 'bo'
    }
    validator = ModuleArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)
    assert result.error_messages[0] == 'age: value must be type int but got str'
    assert len(result.error_messages) == 1

    # test_parameters_with_name_as_integer_raises_error
    parameters = {
        'name': 42
    }
    result = validator.validate(parameters)

# Generated at 2022-06-12 22:58:40.397176
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    validator = ModuleArgumentSpecValidator({'a': {'type': 'bool'}})
    sut = validator.validate({'a': True})

    assert sut.validated_parameters['a'] == True

# Generated at 2022-06-12 22:58:51.246444
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    """
    unit tests for method ModuleArgumentSpecValidator.validate()
    """
    from ansible.module_utils.common.arg_spec import ModuleArgumentSpecValidator

    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int', 'required': True},
        'options': {'type': 'dict', 'required': False},
        'state': {'type': 'str', 'required': True, 'choices': ['present', 'absent']}
    }

    parameters = {
        'name': 'bo',
        'age': '42',
        'state': 'present',
        'options': {'a': 1}
    }

    validator = ModuleArgumentSpecValidator(argument_spec)

# Generated at 2022-06-12 22:59:09.825301
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    parameters = {
        'name': 'bo',
        'age': '42',
    }

    # Required and non required value
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int', 'required': False},
    }

    validator = ArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)

    assert(not result.error_messages and result.validated_parameters == {'name': 'bo', 'age': 42})

    # Multiple errors
    argument_spec = {
        'name': {'type': 'str', 'required': True},
        'age': {'type': 'int', 'required': False},
    }

    validator = ArgumentSpecValidator(argument_spec)
    result = validator

# Generated at 2022-06-12 22:59:14.906827
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    result = ModuleArgumentSpecValidator(
        mutually_exclusive=['a', 'b']
    ).validate({
        'a': True,
        'b': True
    })

    assert len(result.errors) == 1
    assert isinstance(result.errors[0], MutuallyExclusiveError)

__all__ = (
    'ArgumentSpecValidator',
    'ModuleArgumentSpecValidator',
    'ValidationResult',
)

# Generated at 2022-06-12 22:59:16.031902
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    parameter = {}
    ModuleArgumentSpecValidator({}).validate(parameter)

# Generated at 2022-06-12 22:59:26.571516
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    # test each of the exception conditions
    args = (
        ('mutually_exclusive', MutuallyExclusiveError),
        ('required_together', RequiredError),
        ('required_one_of', RequiredError),
        ('required_if', RequiredError),
        ('required_by', RequiredError),
        ('type', TypeError),
        ('choices', TypeError),
        ('aliases', ValueError),
    )


# Generated at 2022-06-12 22:59:36.929927
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    from ansible.module_utils.common._collections_compat import Mapping, MutableMapping
    from ansible.module_utils.basic import AnsibleModule
    from sys import version_info

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
    assert isinstance(result._validated_parameters, MutableMapping)
    assert isinstance(result._no_log_values, set)
    assert isinstance(result._unsupported_parameters, set)

# Generated at 2022-06-12 22:59:40.960348
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
    assert type(result.validated_parameters['name']) == str
    assert type(result.validated_parameters['age']) == int
    assert result.error_messages == []



# Generated at 2022-06-12 22:59:42.040429
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    # TODO: write unit test for method validate
    assert True


# Generated at 2022-06-12 22:59:49.227376
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
        'deprecated_name' : {'type': 'dict', 'aliases': ['deprecated_name_alias']},
        'dict_with_defaults' :
            {'type' : 'dict',
             'default': {'name': 'dict_default_name',
                         'age': 'dict_default_age'},
             'options': {'city': {'type': 'str'}}},
    }

    parameters = {'name': 'bo', 'age': '42', 'deprecated_name_alias': '42'}
    validator = ModuleArgumentSpecValidator(argument_spec, support_check_mode=False)
    result = validator.validate(parameters)



# Generated at 2022-06-12 22:59:57.020205
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    parameters = {
        "name": "bo",
        "age": "42",
    }
    argument_spec = {
        "name": {"type": "str"},
        "age": {"type": "int"},
    }
    validator = ModuleArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)
    assert result.validated_parameters == parameters
    assert result._no_log_values == set()
    assert result._unsupported_parameters == set()
    assert result._deprecations == []
    assert result._warnings == []
    assert result.error_messages == []

# Generated at 2022-06-12 23:00:06.339672
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():

    module = MagicMock()
    module.params = {'option_1': 'value', 'option_2': 'value'}
    module.mutually_exclusive = [
        ['option_1', 'option_2'],
    ]
    module.required_together = [
        ['option_1', 'option_2'],
    ]
    module.required_one_of = [
        ['option_1', 'option_2'],
    ]
    module.required_if = [
        ['option_1', 'value', ['option_2']],
        ['option_2', 'value', ['option_1']],
    ]
    module.required_by = {'option_1': ['option_2'], 'option_2': ['option_1']}

# Generated at 2022-06-12 23:00:23.875230
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    pass

# Generated at 2022-06-12 23:00:32.645066
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():

    module_argument_spec_validator = ModuleArgumentSpecValidator(argument_spec={'name': {'type': 'str'},
                                                                                'age': {'type': 'int'}},
                                                                mutually_exclusive=[['name', 'age']],
                                                                required_together=[['name', 'age']])

    parameters = {'name': 'bo',
                  'age': '42'}
    result = module_argument_spec_validator.validate(parameters)
    assert result.validated_parameters == {'name': 'bo', 'age': 42}
    assert result.errors == AnsibleValidationErrorMultiple()

# Generated at 2022-06-12 23:00:42.128287
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    argument_spec = { 'test_param': {
                                      'type': 'bool',
                                      'aliases': ['test_alias'],
                                      'required': True
                                     }
                    }
    mutually_exclusive = [
                            ['mutual_param1', 'mutual_param2']
                         ]
    required_together = [
                            ['required_param1', 'required_param2']
                         ]
    required_one_of = [
                            ['required_one_param1', 'required_one_param2']
                         ]

# Generated at 2022-06-12 23:00:53.470830
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.common._collections_compat import Mapping

    argument_spec = {
        'age': {
            'type': 'int',
            'default': 42,
        },
        'name': {
            'type': 'str',
            'default': 'Bob',
        },
        'subspec': {
            'sub_name': {
                'type': 'int',
                'default': 42,
            },
        },
        'subspec_list': {
            'sub_list': {
                'sub_list_item': {
                    'type': 'int',
                    'default': 42,
                },
            },
        },
    }


# Generated at 2022-06-12 23:01:04.177378
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    def _args(x): return x

# Generated at 2022-06-12 23:01:14.170953
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    import sys
    import binascii

    def test_function(result):
        assert(result.validated_parameters == {'name': 'bo', 'age': 42})
        assert(result.error_messages == [])


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

    test_function(result)

    parameters = {
        'name': [b'1', b'2'],
        'age': '42',
    }


# Generated at 2022-06-12 23:01:23.029261
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

    assert result.error_messages == []

    assert result.unsupported_parameters == set()

    assert result.validated_parameters == {
        'name': 'bo',
        'age': 42,
    }

# Generated at 2022-06-12 23:01:33.175354
# Unit test for method validate of class ArgumentSpecValidator

# Generated at 2022-06-12 23:01:44.479765
# Unit test for constructor of class ArgumentSpecValidator
def test_ArgumentSpecValidator():
    argument_spec = {'name': {'type': 'str'}, 'age': {'type': 'int'}}
    mutually_exclusive = [['a', 'b']]
    required_together = [['c', 'd']]
    required_one_of = [['e', 'f']]
    required_if = [{'parameter': 'g', 'value': 1, 'required': ['h']}, {'parameter': 'i', 'value': 2, 'required': ['j']}]
    required_by = {'k': ['l']}
    # THIS IS THE FUNCTION UNDER TEST

# Generated at 2022-06-12 23:01:49.648590
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    p = {'a':'msg', 'a1':'msg1'}
    m = ModuleArgumentSpecValidator({'a': {'type': 'str','aliases': ['a1']}})
    assert m.validate(p).error_messages == []
    p = {'a': 'msg', 'a2': 'msg'}
    m = ModuleArgumentSpecValidator({'a': {'type': 'str', 'aliases': ['a1']}})
    assert m.validate(p).error_messages == ['Both option a and its alias a2 are set.']

# Generated at 2022-06-12 23:02:23.013648
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    module_argument_spec_validator = ModuleArgumentSpecValidator(argument_spec={}, mutually_exclusive=[], required_together=[], required_one_of=[], required_if=[], required_by={})
    parameters = {"bo_name": "bo"}
    module_argument_spec_validator.validate(parameters)

# Generated at 2022-06-12 23:02:26.204870
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

    assert result.validated_parameters == {'age': 42, 'name': 'bo'}

    assert result.errors == []

# Generated at 2022-06-12 23:02:33.578507
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    validator = ModuleArgumentSpecValidator(
        argument_spec = {
            'name': {'type': 'str'},
            'age': {'type': 'int', 'default': 18},
        },
        mutually_exclusive = [
            ['name', 'age']
        ])

    parameters = {
        'name': 'bo',
        'age': '42',
    }
    try:
        result = validator.validate(parameters)
        assert result.errors[0].args[0] == "name, age"
    except MutuallyExclusiveError as e:
        print(e.args[0])

# Generated at 2022-06-12 23:02:44.023041
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    """Test validate method of ArgumentSpecValidator"""

    # Given

# Generated at 2022-06-12 23:02:52.738416
# Unit test for method validate of class ArgumentSpecValidator

# Generated at 2022-06-12 23:03:03.080030
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    """Unit test for method validate of class ModuleArgumentSpecValidator

    Unittest of validate method of ModuleArgumentSpecValidator in
    common/arg_spec.py: validate data for each error message for API
    and validate errors list

    :param parameters: Parameters to validate against the argument spec
    :type parameters: dict[str, dict]

    :return: validated parameters and errors list
    :rtype: dict
    """
    class Test:
        def __init__(self):
            self.error_messages = []

        def append(self, error):
            self.error_messages.append(error)


# Generated at 2022-06-12 23:03:11.434766
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():

    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
        'favorite_number': {'type': 'int'},
    }

    parameters = {
        'name': 'bo',
        'age': '42',
        'favorite_number': '42',
    }

    validator = ArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)

    assert result.validated_parameters['name'] == 'bo'
    assert result.validated_parameters['age'] == 42
    assert result.validated_parameters['favorite_number'] == 42
    assert not result.error_messages



# Generated at 2022-06-12 23:03:18.677820
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    """Verify ModuleArgumentSpecValidator.validate calls deprecate and warn at most once for each unique message.

    This method must be called directly by pytest, as import will be prevented by the ansible_collections namespace package.
    """
    deprecate_calls = 0
    warn_calls = 0
    m = ModuleArgumentSpecValidator({})
    m._valid_parameter_names = ['a']

    def my_deprecate(msg, **kwargs):
        nonlocal deprecate_calls
        if msg.startswith('Alias'):
            deprecate_calls += 1
            assert kwargs['collection_name'] == 'Ansible.foo'

    def my_warn(msg):
        nonlocal warn_calls
        if msg.startswith('Both'):
            warn

# Generated at 2022-06-12 23:03:28.548977
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    module_parameters = {
        'option1': 'value1',
        'option2': 'value2',
        'option3': 'value3',
    }
    argument_spec = {
        'option1': {
            'type': 'str',
            'required': True,
        },
        'option2': {
            'type': 'str',
            'required': True,
        },
        'option3': {
            'type': 'str',
            'aliases': ['option4'],
        },
    }
    mutually_exclusive = [
        ['option1', 'option2']
    ]

    validator = ModuleArgumentSpecValidator(argument_spec, [mutually_exclusive])
    r = validator.validate(module_parameters)

    assert not r.error_messages

# Generated at 2022-06-12 23:03:30.830814
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    # validate should fail with name not found
    # validate should fail with age not found
    # validate should fail with dob not found
    # validate should fail with name not of type str
    pass

# Generated at 2022-06-12 23:04:36.354130
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    #alias deprecation message
    class Test:
        called = False
        def __init__(self, message, version=None, date=None, collection_name=None):
            pass
        def __call__(self, message, version=None, date=None, collection_name=None):
            self.called = True


    #alias deprecation message
    class Test2:
        called = False
        def __init__(self, message, version=None, date=None, collection_name=None):
            pass
        def __call__(self, message, version=None, date=None, collection_name=None):
            self.called = True

    class Test3:
        def __init__(self, message, version=None, date=None, collection_name=None):
            pass

    deprecate = Test()

# Generated at 2022-06-12 23:04:43.881806
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    from ansible.module_utils.common.arg_spec import ModuleArgumentSpecValidator
    from ansible.module_utils.common.text.converters import to_text
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.module_utils.common.warnings import _deprecation_warning


# Generated at 2022-06-12 23:04:51.374294
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    # Invalid argument_spec
    invalid_argument_spec = [
        "argument_spec",
        {
            "a": {
                "one": {
                    "two": "argument_spec"
                }
            },
            "b": {
                "type": "str"
            },
        }
    ]
    for invalid_argument_spec in invalid_argument_spec:
        with pytest.raises(AnsibleValidationErrorMultiple):
            ModuleArgumentSpecValidator(invalid_argument_spec).validate({})

    # Valid argument_spec

# Generated at 2022-06-12 23:05:00.849416
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    # Unit test for method validate of class ModuleArgumentSpecValidator
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int', 'deprecated': {'collection_name': 'core', 'date': '2021-06-01', 'version': '2.12', 'removed_in': '22.0'}},
        'position': {'type': 'list', 'elements': 'str', 'aliases': ['role']},
        'no_log': {'type': 'bool'},
        'mood': {'type': 'str', 'choices': ["happy", "sad"]},
    }


# Generated at 2022-06-12 23:05:06.592643
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

# Generated at 2022-06-12 23:05:14.404210
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
        print("Validation failed: {0}".format(", ".join(result.error_messages)))

    valid_params = result.validated_parameters
    print(valid_params)


if __name__ == "__main__":
    test_ArgumentSpecValidator_validate()

# Generated at 2022-06-12 23:05:23.601215
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    mutually_exclusive_list = ['name', ['age', 'height']]
    required_together_list = [['name', 'age'], ['name', 'height']]
    required_one_of_list = [['name', 'age'], ['name', 'height']]
    required_if_list = [['name', 'bo', ['age', 'height']]]
    required_by_dict = dict(age=['name'], height=['name'])

    argument_spec_dict = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
        'height': {'type': 'int'},
    }
    parameters_dict = {
        'name': 'ba',
        'age': '42',
        'height': '180',
    }

    validator

# Generated at 2022-06-12 23:05:33.960899
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
        'state': {'type': 'str', 'default': 'present', 'choices': ['present', 'absent']},
        'registered': {'type': 'bool', 'default': True, 'no_log': True},
        'vars': {'type': 'dict', 'default': {}},
    }

    mutually_exclusive = [
        ['name', 'registered'],
        ['state', 'registered'],
    ]

    required_if = [
        ('state', 'present', ['name']),
        ('state', 'present', ['name', 'age']),
    ]

    parameters = {'name': 'bo', 'age': '42'}

    validator = ArgumentSpecValidator

# Generated at 2022-06-12 23:05:34.897468
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    assert False, "Test not implemented"

# Generated at 2022-06-12 23:05:38.320903
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    args = dict(argument_spec=dict(name=dict(type='str')))
    result = ModuleArgumentSpecValidator(**args).validate(parameters=dict(name='foo'))
    assert result.validated_parameters == dict(name='foo')