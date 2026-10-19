

# Generated at 2022-06-12 22:56:24.669127
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    argument_spec={
        'name': {'type': 'str'},
        'age': {'type': 'int'},
        'age_alias': {'type': 'int', 'aliases': ['alt_age']},
        'date': {'type': 'str', 'default': 'today', 'aliases': ['deprecated_date']},
    }
    parameters = {
        'name': 'bo',
        'age': '42',
        'alt_age': '42',
        'deprecated_date': 'yesterday',
    }

    validator = ModuleArgumentSpecValidator(argument_spec)
    # result = validator.validate(parameters)
    # assert result.error_messages == []
    # assert result.validated_parameters == {'name': 'bo',
    #                                       

# Generated at 2022-06-12 22:56:34.670845
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    mod_arg_validator = ModuleArgumentSpecValidator({"name" : {"type" : "str"}, "age" : {"type" : "int"}})
    assert mod_arg_validator != None
    params = {"name" : "bo", "age" : 42}
    result = mod_arg_validator.validate(params)
    assert result != None
    assert result.validated_parameters == params
    assert len(result.errors) == 0
    assert len(result._warnings) == 0
    assert len(result._deprecations) == 0

    # --------------------------------------------------------

    params = {"name" : "bo", "age" : 42, "age_" : 24}
    result = mod_arg_validator.validate(params)
    assert result != None

# Generated at 2022-06-12 22:56:44.119344
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():

    argument_spec = {'test': {'type': 'dict', 'required': True,
                              'options': {'name': {'type': 'str'},
                                          'age': {'type': 'int'}}
                              }
                     }

    mutually_exclusive = []
    required_together = []
    required_one_of = []
    required_if = []
    required_by = []

    validator = ArgumentSpecValidator(argument_spec,
                                      mutually_exclusive=mutually_exclusive)

    result = validator.validate({})

    assert isinstance(result, ValidationResult)
    assert isinstance(result.errors, AnsibleValidationErrorMultiple)
    assert result.error_messages == ["argument of type 'dict' is required and not found for 'test'"]

    result = validator.valid

# Generated at 2022-06-12 22:56:55.141895
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    from ansible.module_utils._text import to_text
    from ansible.module_utils.common.validation import check_mutually_exclusive, check_required_arguments
    from ansible.module_utils.common.warnings import deprecate, warn

    class FakeModule:
        def __init__(self):
            pass
        def fail_json(self, *args, **kwargs):
            raise AssertionError("fail_json called with args = {0} and kwargs = {1}".format(args, kwargs))

    def fake_check_mutually_exclusive(*args, **kwargs):
        raise TypeError("fake_check_mutually_exclusive called with args = {0} and kwargs = {1}".format(args, kwargs))

# Generated at 2022-06-12 22:57:03.347622
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    mutually_exclusive = None
    required_together = None
    required_one_of = None
    required_if = None
    required_by = None

    def test_spec():
        return {
            'test': {'type': 'str', 'required': True},
        }

    validator = ModuleArgumentSpecValidator(test_spec(),
                                            mutually_exclusive=mutually_exclusive,
                                            required_together=required_together,
                                            required_one_of=required_one_of,
                                            required_if=required_if,
                                            required_by=required_by)

    empty_params = {}
    empty_result = validator.validate(empty_params)
    assert len(empty_result.error_messages) == 1

# Generated at 2022-06-12 22:57:10.230000
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    import pytest

    params = {'src': 'test', 'dest': 'test'}
    argument_spec = {'src': {'type': 'str'}, 'dest': {'type': 'str'}}
    validator = ModuleArgumentSpecValidator(argument_spec)

    result = validator.validate(params)

    assert result.validated_parameters == params
    assert result.errors == []
    assert result.warnings == []
    assert result.deprecations == []

# Generated at 2022-06-12 22:57:11.661114
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    validator = ModuleArgumentSpecValidator({})
    assert validator is not None

# Generated at 2022-06-12 22:57:19.842739
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    # to check if deprecate is logging the right message
    def deprecate(msg, version, date, collection_name):
        msg_one = "Alias 'name' is deprecated. See the module docs for more information"
        msg_two = "Alias 'age' is deprecated. See the module docs for more information"
        if msg == msg_one or msg == msg_two:
           return True
        else:
           return False

    # to check if warn is logging the right message
    def warn(msg):
        if msg == "Both option name and its alias nickname are set.":
            return True
        else:
           return False

    # to check if alias_deprecations are appending the right values

# Generated at 2022-06-12 22:57:30.357000
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    # test with all options
    argument_spec = {
        'name': {'required': True, 'type': 'str'},
        'age': {'type': 'int', 'default': 42},
        'hobbies': {'type': 'list', 'default': ['golf', 'long walks on the beach'], 'aliases': ['interests']},
    }
    parameters = {
        'name': 'Bob',
        'age': '42',
        'hobbies': ['golf', 'long walks on the beach'],
        'interests': ['golf', 'long walks on the beach'],
    }
    mutually_exclusive = [
        ['name', 'job'],
    ]
    required_together = [
        ['name', 'age'],
    ]

# Generated at 2022-06-12 22:57:40.036399
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    def dummy(*args):
        return None

    errors = [{'func': dummy, 'err': dummy}]
    argument_spec = {'bo': {'type': 'int', 'required': False}}
    mutually_exclusive = []
    required_together = []
    required_one_of = []
    required_if = []
    required_by = []
    parameters = {'bo': 1}
    module_argument_spec_validator = ModuleArgumentSpecValidator(argument_spec,
                                                                 mutually_exclusive=mutually_exclusive,
                                                                 required_together=required_together,
                                                                 required_one_of=required_one_of,
                                                                 required_if=required_if,
                                                                 required_by=required_by)

    result = module_argument_spec_valid

# Generated at 2022-06-12 22:57:49.614699
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    argument_spec = {'test_arg': {'type': 'bool'}}
    validator = ModuleArgumentSpecValidator(argument_spec)

    parameters = {'test_arg': True}
    result = validator.validate(parameters)

    assert result.validated_parameters['test_arg'] == True
    assert result.unsupported_parameters == set()
    assert result.deprecations == []
    assert result.warnings == []
    assert result.errors.messages == []

# Generated at 2022-06-12 22:57:59.306118
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    # create a function to set a value for debugging
    def get_value(result, value):
        result['value'] = value

    test_spec = {
        'foo': {
            'type': 'str',
            'default': 'bar',
            'no_log': True,
        },
        'baz': dict(
            type='int',
            aliases=['bar'],
        ),
    }

    # test ArgumentSpecValidator.validate()
    result_dict1 = {
        'foo': 'bar',
        'baz': '42',
    }
    validator1 = ArgumentSpecValidator(test_spec)
    result1 = validator1.validate(result_dict1)
    get_value(result1.validated_parameters, 'bar')

# Generated at 2022-06-12 22:58:01.789962
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    validator = ModuleArgumentSpecValidator({})
    parameters = {'name': 'bo', 'age': 42}
    result = validator.validate(parameters)

    assert result.validated_parameters == parameters
    assert not result.errors.messages
    assert not result._deprecations
    assert not result._warnings

# Generated at 2022-06-12 22:58:11.581201
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    """Test the validate method of ModuleArgumentSpecValidator"""
    args = {
        'version': {'type': 'int', 'aliases': ['ver']},
        'timeout': {'type': 'int', 'aliases': ['tmout']},
        'age': {'type': 'int'},
    }
    parameters = {
        'ver': 1,
        'timeout': 10,
        'age': "hello",
        'unsupported': 1234,
        'wrong_type': "abc",
    }
    # Mock warn and deprecate
    import mock
    import warnings
    warnings.warn = mock.Mock(side_effect=warn)
    deprecate = mock.Mock(side_effect=deprecate)

# Generated at 2022-06-12 22:58:17.542165
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    """Unit test for method validate of class ModuleArgumentSpecValidator"""

    param = dict(name='bo', age='42')
    arg_spec = dict(name=dict(type='str'), age=dict(type='int'))
    # Test with no exceptions
    result = ModuleArgumentSpecValidator(argument_spec=arg_spec).validate(param)
    assert not result.error_messages



# Generated at 2022-06-12 22:58:28.355185
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    from ansible.module_utils.six import StringIO
    from ansible.module_utils._text import to_text

    bad_arg_spec_msg = "Bad argument_spec."
    none_arg_spec_msg = "None argument_spec."
    none_parameters_msg = "None parameters."
    spec = {'name':{'required':'yes', 'type':'str', 'aliases':['answer']}}
    parameters = {'name':'bo'}

    argumentSpec = {"argument_spec":{},
                    "mutually_exclusive": [],
                    "required_together": [],
                    "required_one_of": [],
                    "required_if": [],
                    "required_by": {}}

    result = ModuleArgumentSpecValidator(argumentSpec)

    #Test for bad argument_spec
   

# Generated at 2022-06-12 22:58:34.492114
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    # example spec and parameters
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    }
    parameters = {
        'name': 'bo',
        'age': '42',
    }

    # test
    validator = ArgumentSpecValidator(
        argument_spec,
        mutually_exclusive=[],
        required_together=[],
        required_one_of=[],
        required_if=[],
        required_by={}
    )
    result = validator.validate(parameters)

    assert len(result.error_messages) == 0
    assert result.validated_parameters == {'name': 'bo', 'age': 42}

# Generated at 2022-06-12 22:58:45.143130
# Unit test for constructor of class ArgumentSpecValidator
def test_ArgumentSpecValidator():
    required_parameter = {'required': True}
    optional_parameter = {}
    argument_spec = {
        'required_parameter': required_parameter,
        'optional_parameter': optional_parameter
    }

    mutually_exclusive = [['required_parameter', 'optional_parameter']]
    required_together = [['required_parameter', 'optional_parameter']]
    required_one_of = [['required_parameter', 'optional_parameter']]
    required_if = [
        ['required_parameter', 'a', ['optional_parameter']],
        ['required_parameter', 'b', ['optional_parameter']],
    ]
    required_by = {
        'required_parameter': ['optional_parameter']
    }


# Generated at 2022-06-12 22:58:52.859315
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():

    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.common.arg_spec import ModuleArgumentSpecValidator

    expected_result = b'no_log: [\'plain text\']'
    parameter = to_bytes({"no_log": "plain text"})
    argument_spec = {
        'no_log': {'type': 'bool'}
    }
    validator = ModuleArgumentSpecValidator(argument_spec)
    result = validator.validate(parameter)

    assert expected_result == result.validated_parameters["no_log"]

# Generated at 2022-06-12 22:59:03.137005
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    validator = ArgumentSpecValidator({'a': dict(type='int')})

    result = validator.validate({'a': '42'})
    assert result.errors == []
    assert result.validated_parameters == {'a': 42}
    assert result.error_messages == []
    assert result.unsupported_parameters == set()

    validator = ArgumentSpecValidator({'a': dict(type='int')})
    result = validator.validate({'a': 'nope'})
    assert result.errors == [AnsibleValidationError('a', '42', 'int', 'nope')]
    assert result.validated_parameters == {'a': 'nope'}
    assert result.error_messages == ['a must be an instance of int but got "nope"']

# Generated at 2022-06-12 22:59:08.312139
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():

    validator = ModuleArgumentSpecValidator(argument_spec={})
    assert validator.validate({})

# Generated at 2022-06-12 22:59:16.976200
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():

    '''
    Unit test for method validate of class ArgumentSpecValidator
    '''

    import os
    import sys
    import tempfile
    import shutil
    import json

    from ansible.module_utils import basic
    from ansible.module_utils.basic import AnsibleModule

    from ansible.module_utils._text import to_bytes

    from ansible.module_utils.connection import Connection
    from ansible.module_utils.common.parameters import list_no_log_values

    # create a temporary directory and write two test yaml files
    temp_directory = tempfile.mkdtemp()

# Generated at 2022-06-12 22:59:24.403734
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    from ansible.module_utils.six import iteritems
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
    assert result.validated_parameters == parameters


# Generated at 2022-06-12 22:59:34.976498
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    # Setup
    spec = {
        'name': {
            'type': 'str',
        },
        'age': {
            'type': 'int',
        },
    }
    validator = ArgumentSpecValidator(spec)

    # Functionality
    parameters1 = {
        'name': 'bo',
        'age': '42',
    }
    result1 = validator.validate(parameters1)
    parameters2 = {
        'name': 'bo',
        'input': '42',
    }
    result2 = validator.validate(parameters2)
    parameters3 = {
        'name': 'bo',
        'age': '42',
        'foo': 'baz',
    }
    result3 = validator.validate(parameters3)

    assert result1.validate

# Generated at 2022-06-12 22:59:43.049209
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
        'gender': {'type': 'str', 'choices': ['male', 'female']},
        'married': {'type': 'bool'},
        'hobbies': {'type': 'list', 'elements': 'str'},
        'friends': {'type': 'dict', 'keys': {'name': {'type': 'str'}, 'age': {'type': 'int'}}}
    }


# Generated at 2022-06-12 22:59:49.739527
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    """Test that the deprecations of validate are called correctly and super() is called."""
    parameters = {"key": "value"}
    instance = ModuleArgumentSpecValidator("my_spec")

# Generated at 2022-06-12 22:59:59.056359
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():

    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.module_utils.common.validation import check_required_together

    def check_method(item, name, options):
        if item[name] is not None:
            check_required_together(item['required_together'], options)

    def check_cidr(item, name, options):
        if item['ip'] is not None:
            check_required_together([['ip', 'netmask'], ['ip', 'prefix']], options)

    #
    # required_if is not checked because it is tested elsewhere
    #
    # required_by is not checked because it is tested elsewhere
    #
    # mutually_exclusive is not checked because it is tested elsewhere
    #
    # unsupported_parameters is not checked because the values it

# Generated at 2022-06-12 23:00:09.054497
# Unit test for method validate of class ArgumentSpecValidator

# Generated at 2022-06-12 23:00:10.866580
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    pass
# vim: expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4

# Generated at 2022-06-12 23:00:19.501401
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    # Test 1: Deprecations
    arg_spec_validator = ModuleArgumentSpecValidator(
        argument_spec={
            'name': {'type': 'str'},
            'age': {'type': 'int'},
        },
        mutually_exclusive=None,
        required_together=None,
        required_one_of=None,
        required_if=None,
        required_by=None,
    )
    parameters = {
        'name': 'bo',
        'age': '42',
    }
    result = arg_spec_validator.validate(parameters)
    print(result.validated_parameters)


# Generated at 2022-06-12 23:00:37.198698
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():

    # define test data
    argument_spec = {
        "username": {"type": "str", "required": True},
        "password": {"type": "str", "required": True, "no_log": True},
        "age": {"type": "int"},
        "group": {"type": "list"}
    }
    parameters = {
        "username": "bo",
        "password": "secret",
        "age": 42,
        "group": "wheel"
    }
    no_log_values = set(["secret"])
    unsupported_parameters = set()
    deprecations_info = []
    warnings_info = []

    # create validator
    validator = ModuleArgumentSpecValidator(argument_spec)

    # invoke method
    result = validator.validate(parameters)

    # validate the

# Generated at 2022-06-12 23:00:41.733083
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    result = ModuleArgumentSpecValidator(
        argument_spec={
            'option': {'type': 'str', 'aliases': ['alias']},
        },
    ).validate({'option': 'value'})

    assert result.validated_parameters == {'option': 'value'}


if __name__ == '__main__':
    test_ModuleArgumentSpecValidator_validate()

# Generated at 2022-06-12 23:00:45.870434
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
    assert not result.unsupported_parameters
    assert not result.errors
    assert not result.error_messages

# Generated at 2022-06-12 23:00:54.441372
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    """
    Unit test for method validate of class ModuleArgumentSpecValidator
    """
    v = ModuleArgumentSpecValidator(
        argument_spec={'a': {'type': 'int'}},
        mutually_exclusive=None,
        required_together=None,
        required_one_of=None,
        required_if=None,
        required_by=None,
    )
    parameters = {'a':1}
    result = v.validate(parameters)
    assert not result.errors.messages
    assert result.validated_parameters['a'] == 1

# Generated at 2022-06-12 23:01:04.864561
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    def validate():
        validator = ModuleArgumentSpecValidator(argument_spec, required_if=required_if)
        result = validator.validate(parameters)
        assert result.error_messages == expected_errors

    argument_spec = dict(
        backend=dict(type='str', default='local', choices=['local', 'external']),
        context=dict(type='str', default='', aliases=['ctx'])
    )
    required_if = [['backend', 'external', ['context']]]
    parameters = dict(backend='external')
    expected_errors = ['context is required by backend when backend is external']
    validate()

    parameters = dict(backend='external', context='abc')
    expected_errors = []
    validate()

    parameters = dict(backend='external', context='')

# Generated at 2022-06-12 23:01:07.748765
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    ModuleArgumentSpecValidator_instance = ModuleArgumentSpecValidator()
    parameters = {}
    result = ModuleArgumentSpecValidator_instance.validate(parameters)

    assert result
    assert result.errors
    assert result.validated_parameters
    assert result.error_messages

# Generated at 2022-06-12 23:01:13.503430
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    class TestModuleArgumentSpecValidator(ModuleArgumentSpecValidator):
        def __init__(self, *args, **kwargs):
            super(TestModuleArgumentSpecValidator, self).__init__(*args, **kwargs)

        def _get_no_log_values(self, validated_params):
            return validated_params.get('no_log_values')

    spec = {'a': {'type': 'bool', 'no_log': True}, 'b': {'type': 'bool'}}
    mutually_exclusive = [['a', 'b']]
    required_together = [['a', 'b']]
    required_one_of = [['a', 'b']]
    required_if = [['a', 'a', ['b']]]
    required_by = {'a': ['b']}

# Generated at 2022-06-12 23:01:24.444234
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    sut = ModuleArgumentSpecValidator({'name': {'default': 'Tom', 'type': 'str'},
                                'age': {'default': 34, 'type': 'int'},
                                'date_joined': {'type': 'datetime'},
                                'attrs': {'type': 'dict'},
                                'hobbies': {'type': 'list'},
                                'state': {'type': 'str', 'choices': ['present', 'absent', 'disabled'], 'default': 'present'},
                                'is_good': {'type': 'bool', 'default': False},
                                'friends': {'type': 'list'},
                                })

    err = sut.validate({})

    assert 'age' in err.validated_parameters

# Generated at 2022-06-12 23:01:31.723022
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    parameters = {'name': 'bo', 'age': '42'}
    argument_spec = {'name': {'type': 'str'}, 'age': {'type': 'int'}}

    validator = ModuleArgumentSpecValidator(argument_spec, required_if=[['age', 22, ['name']]])
    result = validator.validate(parameters)

    assert result.error_messages == []
    assert result.validated_parameters == {'name': 'bo', 'age': 42}
    assert result.unsupported_parameters == set()

# Generated at 2022-06-12 23:01:36.094365
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    v = ArgumentSpecValidator({}, mutually_exclusive=[['state', 'force']])

    parameters = {'state': 'present'}
    assert not v.validate(parameters).error_messages

    parameters = {'force': 'yes'}
    assert not v.validate(parameters).error_messages

    parameters = {'state': 'present', 'force': 'yes'}
    assert v.validate(parameters).error_messages

# Generated at 2022-06-12 23:02:01.124340
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    mutually_exclusive = [('name', 'age')]
    required_together = [('name', 'age')]
    required_one_of = [('name', 'age')]
    required_if = [('name', 'age')]
    required_by = [('name', 'age')]

    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    }

    parameters = {
        'name': 'bo',
        'age': '42',
    }

    validator = ModuleArgumentSpecValidator(argument_spec, mutually_exclusive, required_together,
                                            required_one_of, required_if, required_by)
    result = validator.validate(parameters)

    assert isinstance(result, ValidationResult)

# Generated at 2022-06-12 23:02:11.520563
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    from ansible.module_utils.common._collections_compat import MutableMapping
    from ansible.module_utils.common.validation import check_mutually_exclusive, check_required_arguments

    # Create dummy validator
    class DummyModuleArgumentSpecValidator(ModuleArgumentSpecValidator):
        def __init__(self, *args, **kwargs):
            super(DummyModuleArgumentSpecValidator, self).__init__(*args, **kwargs)

        def _get_legal_inputs(self, argument_spec, parameters, aliases):
            raise NotImplementedError()

        def _list_no_log_values(self, argument_spec, parameters):
            raise NotImplementedError()


# Generated at 2022-06-12 23:02:17.394990
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    # Create a test object
    module_argument_spec_validator = ModuleArgumentSpecValidator(None)
    # Get a test result
    result = module_argument_spec_validator.validate(None)
    # Set a correct result value
    correct_result = ValidationResult(None)
    # Compare
    assert result.__dict__ == correct_result.__dict__



# Generated at 2022-06-12 23:02:20.828782
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

    assert result.unsupported_parameters == set()
    assert result.error_messages == []
    assert result.validated_parameters['name'] == 'bo'
    assert result.validated_parameters['age'] == 42

# Generated at 2022-06-12 23:02:31.449555
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    argument_spec = {
        'age': {'type': 'int'},
        'list': {'type': 'list'},
        'name': {'type': 'str'},
        'neck_size': {'type': 'int', 'aliases': ['neck-size']},
        'neck_size1': {'type': 'int', 'aliases': ['neck-size1']},
    }

    parameters = {
        'age': '30',
        'list': '',
        'name': 'bo',
        'neck_size': '50',
        'neck_size1': '50',
    }

    result = ModuleArgumentSpecValidator(argument_spec).validate(parameters)

    assert result._unsupported_parameters == set(['list'])
    assert len(result.errors) == 2

# Generated at 2022-06-12 23:02:41.628283
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    from ansible.module_utils.network.common.utils import transform_dict
    from ansible.module_utils.common.parameters import _handle_aliases
    from ansible.module_utils.common.validation import _get_validated_parameters

    import pytest

    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
        'details': {
            'type': 'dict',
            'options': {
                'height': {'type': 'int'},
                'drinks': {'type': 'bool'},
            },
        },
    }


# Generated at 2022-06-12 23:02:48.703368
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    mutually_exclusive = [['name', 'age']]
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
        }
    parameters = {
        'name': 'bo',
        'age': '42',
    }
    validator = ModuleArgumentSpecValidator(argument_spec, mutually_exclusive)
    result = validator.validate(parameters)
    assert result.validated_parameters == {'name': 'bo', 'age': 42}
    assert result.error_messages == []

# Generated at 2022-06-12 23:02:49.235975
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    pass

# Generated at 2022-06-12 23:02:55.910508
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():

    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int', 'default': 42},
    }

    mutually_exclusive = [['name', 'age']]

    validator = ArgumentSpecValidator(argument_spec, mutually_exclusive=mutually_exclusive)

    # no errors
    parameters = {
        'name': 'bo',
        'age': '42',
    }
    result = validator.validate(parameters)
    assert not result.errors
    assert result.validated_parameters == {'name': 'bo', 'age': 42}

    # mutually exclusive
    parameters = {
        'name': 'bo',
        'age': 'bo',
    }
    result = validator.validate(parameters)
    assert result.errors

# Generated at 2022-06-12 23:03:02.966940
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

    module_argument_spec_validator = ModuleArgumentSpecValidator(argument_spec)

    result = module_argument_spec_validator.validate(parameters)

    assert result.validated_parameters['name'] == 'bo'
    assert result.validated_parameters['age'] == 42

# Generated at 2022-06-12 23:03:16.554675
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    argument_spec = {
        'foo': {'type': 'str'},
        'bar': {'type': 'int'},
        'baz': {'type': 'list', 'version_added': '1.3'},
    }

    # Test with no arguments
    validator = ArgumentSpecValidator(argument_spec)
    result = validator.validate({})
    assert result.validated_parameters == {}
    assert len(result.error_messages) == 0

    # Test with valid arguments
    parameters = {
        'foo': 'boo',
        'bar': 42,
    }
    result = validator.validate(parameters)
    assert result.validated_parameters == parameters
    assert len(result.error_messages) == 0

    # Test with extra arguments

# Generated at 2022-06-12 23:03:26.424688
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    class TestModule:
        _CHECKS_DEPRECATIONS_WARNINGS = ('deprecate', 'warn')

    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
        'nested': {'type': 'dict', 'options': {'addr': {'type': 'str'}}},
        'a1': {'type': 'str', 'aliases': ['a2']},
        'b1': {'type': 'str', 'aliases': ['b2'], 'no_log': True},
        'c1': {'type': 'str', 'aliases': ['c2', 'c3'], 'aliases_no_log': ['c2']},
    }
    parameters = None
    validator = None
    result = None

   

# Generated at 2022-06-12 23:03:34.912818
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    # Test that super class validate is called
    mock_module_argument_spec_validator = ModuleArgumentSpecValidator("argument_spec", "mutually_exclusive", "required_together", "required_one_of", "required_if", "required_by")
    mock_module_argument_spec_validator.super = MagicMock()
    mock_module_argument_spec_validator.validate("parameters")
    assert mock_module_argument_spec_validator.super.validate.called
    # Test that deprecate method is called
    mock_module_argument_spec_validator.validate("parameters")
    assert mock_module_argument_spec_validator.deprecate.called
    # Test that warn method is called
    mock_module_argument_spec_validator.validate("parameters")

# Generated at 2022-06-12 23:03:46.029140
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():

    def no_op(*args, **kwargs):
        pass

    def fail_on_true(parameters):
        raise ValueError

    argument_spec = dict(boolean_options=dict(type='bool'))

    parameters = dict(boolean_options=True)

    validator = ModuleArgumentSpecValidator(argument_spec, warn=no_op)
    try:
        result = validator.validate(parameters)
        assert result.validated_parameters == parameters
    except AnsibleValidationErrorMultiple:
        assert False

    validator = ModuleArgumentSpecValidator(argument_spec, warn=fail_on_true)
    try:
        result = validator.validate(parameters)
        assert result.validated_parameters == parameters
    except AnsibleValidationErrorMultiple:
        assert False

   

# Generated at 2022-06-12 23:03:55.318272
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    def validate(self, parameters):
        result = super(ModuleArgumentSpecValidator, self).validate(parameters)

        for d in result._deprecations:
            deprecate("Alias '{name}' is deprecated. See the module docs for more information".format(name=d['name']),
                      version=d.get('version'), date=d.get('date'),
                      collection_name=d.get('collection_name'))

        for w in result._warnings:
            warn('Both option {option} and its alias {alias} are set.'.format(option=w['option'], alias=w['alias']))

        return result

    from ansible.module_utils._text import to_native
    from ansible.module_utils.common.validation import check_mutually_exclusive

# Generated at 2022-06-12 23:04:02.641530
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    """Test validate calls deprecate and warn when appropriate."""
    argument_spec = {'_test_deprecate': dict(aliases=['test_deprecate', {'test_deprecate': 'test_deprecate_alias'}]),
                     'test_warn': dict(aliases=['test_warn_alias'])}
    mutually_exclusive = None
    required_together = None
    required_one_of = None
    required_if = None
    required_by = None
    test_params = {'_test_deprecate': "true", 'test_deprecate_alias': "true", 'test_warn': "true", 'test_warn_alias': "true"}

# Generated at 2022-06-12 23:04:12.565084
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

    assert result.validated_parameters == parameters
    assert result.validated_parameters['age'] == 42

    # test for a validator that has a choice spec
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
        'category': {
            'type': 'list',
            'choices': ['one', 'two']
        },
    }


# Generated at 2022-06-12 23:04:17.943510
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

    if result.error_messages:
        sys.exit("Validation failed: {0}".format(result.error_messages))

    valid_params = result.validated_parameters
    # assert valid_params == {'name': 'bo', 'age': 42}  # uncomment below
    assert valid_params == {'name': 'bo', 'age': '42'}

# Generated at 2022-06-12 23:04:27.357398
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    }

    mutually_exclusive = [
        ["name", "age"]
    ]

    required_together = [
        ["name", "age"]
    ]

    required_one_of = [
        ["name", "age"]
    ]

    required_if = [
        ["name", "age"]
    ]

    required_by = {
        'name': 'age'
    }

    parameters = {
        'name': 'bo',
        'age': '42',
    }


# Generated at 2022-06-12 23:04:32.740311
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    validator = ModuleArgumentSpecValidator(argument_spec={"b": {"type": "str"}, "ansible_deprecations": []})
    parameters = {"b": "hello"}
    result = validator.validate(parameters)

    assert len(result._deprecations) == 0
    assert len(result._warnings) == 0
    assert result._validated_parameters == {"b": "hello"}

# Generated at 2022-06-12 23:04:56.091834
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    """ Unit test for method validate of class ModuleArgumentSpecValidator """
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

    assert result.validated_parameters["name"] == 'bo'
    assert result.validated_parameters["age"] == 42

# Generated at 2022-06-12 23:05:07.125693
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    from ansible.module_utils.common.warnings import AnsibleModuleWarning

    parameter = {
        'foo': 'bar'
    }

    spec = {
        'foo': {'type': 'str'}
    }

    mutually_exclusive = [
        ['a', 'b'],
        ['c', 'd'],
    ]
    required_together = [
        ['a', 'b'],
        ['c', 'd'],
    ]
    required_one_of = [
        ['a', 'b'],
        ['c', 'd'],
    ]
    required_if = [['a', 'b', ['c']]]
    required_by = {'a': ['b']}


# Generated at 2022-06-12 23:05:11.125259
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
    validator.validate(parameters)

# Generated at 2022-06-12 23:05:16.732006
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    # Script
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

# Test for method validate of class ModuleArgumentSpecValidator
if __name__ == '__main__':
    test_ModuleArgumentSpecValidator_validate()

# Generated at 2022-06-12 23:05:27.190489
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    # --------------
    # Test with simple argument spec and no 'deprecated' and/or 'removed' keys
    # Test with a simple spec with one parameter

    argument_spec = dict(parameter1=dict(type='str'))
    parameters = dict(parameter1='foo')

    validator = ModuleArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)

    assert set(result._validated_parameters.keys()) == {'parameter1'}
    assert result._validated_parameters.get('parameter1') == 'foo'
    assert result.errors == []
    assert result._deprecations == []
    assert result._warnings == []

    # Test with a simple spec with multiple parameters


# Generated at 2022-06-12 23:05:27.861134
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
     pass

# Generated at 2022-06-12 23:05:30.507042
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    parameters = {}
    validator = ModuleArgumentSpecValidator({})
    result = validator.validate(parameters)
    assert result.validated_parameters == {}

# Generated at 2022-06-12 23:05:38.197773
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    }
    mutually_exclusive = [
        ['name', 'age'],
    ]
    validator = ModuleArgumentSpecValidator(argument_spec, mutually_exclusive=mutually_exclusive)
    parameters = {
        'name': 'bo',
        'age': '42',
    }
    # If a mutually exclusive group is violated, then TypeError will be thrown.
    # If all mutually exclusive groups are met, then no Exception will be thrown.
    assert validator.validate(parameters)

# Generated at 2022-06-12 23:05:47.230513
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    input_argument_spec = {
        'bo': {'type': 'boolean'},
        'int': {'type': 'int'},
        'float': {'type': 'float'},
        'str': {'type': 'str'},
        'list': {'type': 'list'},
        'dict': {'type': 'dict'},
        'complex': {'type': 'complex'},
        'none': {'type': 'none'},
    }

# Generated at 2022-06-12 23:05:55.996986
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    validator = ModuleArgumentSpecValidator({
        'test_parameter': {
            'type': 'str',
            'aliases': ['test_alias'],
            'required': True,
        },
        'test_no_log': {
            'type': 'bool',
            'no_log': True,
            'default': False,
        },
        'test_deprecation': {
            'type': 'str',
            'default': 'test_value',
            'deprecated': {
                'version': '2.11',
                'collection_name': 'my_collection',
                'date': '2021-01-01',
            }
        },
    })
    
    # Case when parameters and spec are correct
    parameters = {'test_parameter': 'test_value'}