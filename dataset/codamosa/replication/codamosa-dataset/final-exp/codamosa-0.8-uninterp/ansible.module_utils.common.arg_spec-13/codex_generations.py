

# Generated at 2022-06-12 22:56:25.520455
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
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

    assert result._validated_parameters['name'] == 'bo', 'expected string'
    assert result._validated_parameters['age'] == 42, 'expected int'

# Generated at 2022-06-12 22:56:26.592225
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    assert False, "No tests for this class yet"

# Generated at 2022-06-12 22:56:36.020787
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
        'tshirt_size': {
            'type': 'str',
            'default': 'M',
            'choices': ['S', 'M', 'L', 'XL'],
        },
    }

    parameters = {
        'name': 'bo',
        'age': '42'
    }

    validator = ArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)

    assert not result.errors

    assert result.validated_parameters['name'] == 'bo'
    assert result.validated_parameters['age'] == 42
    assert result.validated_parameters['tshirt_size'] == 'M'


# Generated at 2022-06-12 22:56:46.163778
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():

    from ansible.module_utils.six import PY3


# Generated at 2022-06-12 22:56:56.974497
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    class Result:

        def __init__(self, parameters):
            self._deprecations=[]
            self._unsupported_parameters = []
            self._validated_parameters={}
            self._warnings=[]
            self.errors = []

    # Patch super class to return valid Result object
    def validate(self, parameters):
        return Result(parameters)

    validator = ModuleArgumentSpecValidator('')
    validator.validate = validate       # Patch super method
    result = validator.validate('')
    assert isinstance(result, Result)
    assert hasattr(result, '_deprecations')
    assert hasattr(result, '_unsupported_parameters')
    assert hasattr(result, '_validated_parameters')
    assert hasattr(result, '_warnings')


# Generated at 2022-06-12 22:57:04.765767
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    # Arrange
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
        'aliases': {
            'aliases': ['alias1', 'alias2'],
            'type': 'list'
        }
    }

    mutually_exclusive = [['name', 'alias1'], ['age', 'alias2']]
    required_together = [['name', 'age']]
    required_one_of = [['name', 'age']]
    required_by = {'name': ['alias2']}
    required_if = {'name': {'state': ['present', 'absent'], 'parameters': ['alias1']}}


# Generated at 2022-06-12 22:57:15.222219
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    import pytest
    from ansible.module_utils.common.parameters import sanitize_keys


# Generated at 2022-06-12 22:57:20.576833
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

    assert not result.errors
    assert "bo" == result.validated_parameters['name']
    assert 42 == result.validated_parameters['age']

# Generated at 2022-06-12 22:57:31.280365
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    example_argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
        'aliases': {'type': 'list', 'aliases': ['nicknames', 'nicks']},
    }
    example_parameters = {
        'name': 'bo',
        'age': '42',
        'aliases': ['bobo', 'bob'],
    }
    example_validator = ModuleArgumentSpecValidator(example_argument_spec,
                                                    mutually_exclusive=None,
                                                    required_together=None,
                                                    required_one_of=None,
                                                    required_if=None,
                                                    required_by=None,
                                                    )

# Generated at 2022-06-12 22:57:35.176997
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():

    def test_validator(parameters):
        validator = ArgumentSpecValidator({'name': {'type': 'int'}})

        result = validator.validate(parameters)

        assert result.validated_parameters == parameters

    test_validator({'name': '2'})

# Generated at 2022-06-12 22:57:48.146726
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    from ansible.module_utils.common._collections_compat import Mapping, MutableMapping, MappingView
    from ansible.module_utils.common._collections_compat import MutableSequence, MutableSet
    from ansible.module_utils.common._collections_compat import Sequence, Set
    from ansible.module_utils.common._text_compat import ensure_text
    from ansible.module_utils.common.text.converters import to_text
    Mapping.register(dict)
    MutableMapping.register(dict)
    Sequence.register(tuple)
    MutableSequence.register(list)
    Set.register(set)
    MutableSet.register(set)
    ensure_text.register(type(None), to_text)

# Generated at 2022-06-12 22:57:49.965550
# Unit test for constructor of class ArgumentSpecValidator
def test_ArgumentSpecValidator():

    assert ArgumentSpecValidator({'name': {'type': 'str'}, 'age': {'type': 'int'}})



# Generated at 2022-06-12 22:57:59.752179
# Unit test for constructor of class ArgumentSpecValidator
def test_ArgumentSpecValidator():

    assert ArgumentSpecValidator(
        None,
        mutually_exclusive=[['a', 'b']]
    )._mutually_exclusive == [['a', 'b']]

    assert ArgumentSpecValidator(
        None,
        mutually_exclusive=[['a', 'b']],
        required_together=[['c', 'd']]
    )._mutually_exclusive == [['a', 'b']]

    assert ArgumentSpecValidator(
        None,
        mutually_exclusive=[['a', 'b']],
        required_together=[['c', 'd']]
    )._required_together == [['c', 'd']]


# Generated at 2022-06-12 22:58:07.069381
# Unit test for constructor of class ArgumentSpecValidator
def test_ArgumentSpecValidator():
    argument_spec = {
        'argument_one': {'type': 'str'},
        'argument_two': {'type': 'str'},
        'argument_three': {
            'type': 'dict',
            'options': {
                'argument_four': {'type': 'str'}
            }
        }
    }
    mutually_exclusive = [ ['argument_one', 'argument_two'] ]
    required_together = [ ['argument_one', 'argument_three'] ]
    required_one_of = [ ['argument_one', 'argument_two'] ]
    required_if = [ ['argument_one', '1', 'argument_three.argument_four'] ]
    required_by = { 'argument_one': ['argument_three'] }

# Generated at 2022-06-12 22:58:18.304147
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    }

    # check parameters dict
    parameters = {
        'name': 'bo',
        'age': '42',
    }
    validator = ModuleArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)
    assert len(result.errors) == 0
    assert result.validated_parameters['name'] == 'bo'
    assert result.validated_parameters['age'] == 42

    # check parameters dict
    parameters = {
        'name': 'bo',
        'age': '42',
    }
    validator = ModuleArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)

# Generated at 2022-06-12 22:58:28.920366
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    # Unit test for method validate of class ArgumentSpecValidator

    from ansible.module_utils.common._collections_compat import Mapping

    import sys
    import unittest
    from contextlib import contextmanager

    from ansible.module_utils.six import StringIO

    class TestException(Exception):
        def __init__(self, *args, **kwargs):
            super(TestException, self).__init__(*args, **kwargs)

        def __repr__(self):
            return 'My exception'

    @contextmanager
    def captured_conf_stdout():
        new_stdout, new_stderr = StringIO(), StringIO()
        old_stdout, old_stderr = sys.stdout, sys.stderr

# Generated at 2022-06-12 22:58:35.453182
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    argument_spec = {
        'name': {
            'type': 'str',
        },
        'age': {
            'type': 'int',
        },
        'friends': {
            'type': 'list',
        },
    }

    parameters = {
        'name': 'bo',
        'age': '42',
        'friends': '[]',
    }

    validator = ArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)

    if result.error_messages:
        sys.exit("Validation failed: {0}".format(", ".join(result.error_messages)))

    valid_params = result.validated_parameters

    assert valid_params['name'] == 'bo'
    assert valid_params['age'] == 42
    assert valid_params

# Generated at 2022-06-12 22:58:46.482267
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    '''Unit test for method validate of class ArgumentSpecValidator'''
    from ansible.module_utils.common.text.converters import to_bytes, to_text

    # convert unicode to bytes
    argumentspec = {
        to_bytes("name", encoding="ascii"):
            {'type': 'str'},
        to_bytes("age", encoding="ascii"):
            {'type': 'int'},
    }
    parameters = {
        to_bytes("name", encoding="ascii"): to_bytes("bo", encoding="ascii"),
        to_bytes("age", encoding="ascii"): to_bytes("42", encoding="ascii"),
    }

    validator = ArgumentSpecValidator(argument_spec=argumentspec)

# Generated at 2022-06-12 22:58:47.512252
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    ModuleArgumentSpecValidator()

# Generated at 2022-06-12 22:58:56.178459
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    def _assert_warnings_called(module_mock, *args, **kwargs):
        assert module_mock.warn.called
        assert module_mock.warn.call_count == len(args)

        for (warn_arg,), _ in module_mock.warn.call_args_list:
            assert warn_arg in args

    def _assert_deprecation_called(module_mock, *args, **kwargs):
        assert module_mock.deprecate.called
        assert module_mock.deprecate.call_count == len(args)

        for (warn_arg,), _ in module_mock.deprecate.call_args_list:
            assert warn_arg in args


# Generated at 2022-06-12 22:59:06.721920
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    from .test_common_arg_spec import argument_spec

    result = ModuleArgumentSpecValidator('test', argument_spec).validate({'src': 'A', 'dest': 'B'})
    assert not result.errors
    assert result.validated_parameters == {'src': 'A', 'dest': 'B'}



# Generated at 2022-06-12 22:59:13.330304
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

    assert result._validated_parameters['name'] == 'bo'
    assert result._validated_parameters['age'] == 42

# Generated at 2022-06-12 22:59:19.972217
# Unit test for method validate of class ArgumentSpecValidator

# Generated at 2022-06-12 22:59:30.990602
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    from ansible.module_utils.basic import AnsibleModule
    import sys

    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    }

    parameters = {
        'name': 'example',
        'age': 42,
    }

    argument_spec_validator = ModuleArgumentSpecValidator(argument_spec)
    result = argument_spec_validator.validate(parameters)

    if result.error_messages:
        sys.exit("Validation failed: {0}".format(", ".join(result.error_messages)))

    valid_params = result.validated_parameters

    assert valid_params['name'] == 'example'
    assert valid_params['age'] == 42


# Generated at 2022-06-12 22:59:40.445134
# Unit test for constructor of class ArgumentSpecValidator
def test_ArgumentSpecValidator():
    argument_spec = {
        'name': {'type': 'str', 'aliases': ['username']},
        'age': {'type': 'int'},
        'task': {'type': 'dict', 'options': {
            'item': {'type': 'str'},
            'username': {'type': 'str'},
        }},
    }

    mutually_exclusive = [['name', 'age']]
    required_one_of = [['name', 'age']]
    required_together = [['name', 'age']]
    required_if = [['name', 'new', ['item']]]
    required_by = {'name': ['item']}
    ArgumentSpecValidator(argument_spec, mutually_exclusive, required_together, required_one_of, required_if, required_by)



# Generated at 2022-06-12 22:59:48.126366
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():

    class StubMessage:
        def __init__(self, the_message):
            self.the_message = the_message
        def __str__(self):
            return self.the_message

    STUB = StubMessage('STUB')

    check = {
        'func': check_mutually_exclusive,
        'attr': '_mutually_exclusive',
        'err': MutuallyExclusiveError
    }

    def _func_a(check, validated_parameters):
        raise TypeError(STUB)

    _ADDITIONAL_CHECKS.append({'func': _func_a, 'attr': None})

    args = (
        {},
        {'mutually_exclusive': None}
    ), 

# Generated at 2022-06-12 22:59:55.171471
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    argspec_validator = ArgumentSpecValidator(argument_spec={
                                    'option': {'type': 'str', 'default': 0},
                                    'version': {'type': 'int', 'default': '3'},
                                    'aliases': {'type': 'list', 'default': list}
                                })

    parameters = {'version': '3', 'aliases': [], 'option': 0}
    result = argspec_validator.validate(parameters)

    assert result.validated_parameters == parameters
    assert result.error_messages == []

# Generated at 2022-06-12 23:00:00.727313
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

    assert result.validated_parameters == {'name': 'bo', 'age': 42}
    assert result.unsupported_parameters == set()
    assert not result.error_messages

# Generated at 2022-06-12 23:00:11.409618
# Unit test for method validate of class ArgumentSpecValidator

# Generated at 2022-06-12 23:00:21.236346
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    mutually_exclusive_values_list = [
        'mut1',
        ['mut2'],
        ['mut3_1', 'mut3_2'],
        ['mut4_1', 'mut4_2'],
    ]
    required_together_values_list = [
        ['rt1'],
        ['rt2_1', 'rt2_2'],
        ['rt3_1', 'rt3_2'],
    ]
    required_one_of_values_list = [
        ['roo1'],
        ['roo2_1', 'roo2_2'],
        ['roo3_1', 'roo3_2'],
        ['roo4_1', 'roo4_2'],
    ]

# Generated at 2022-06-12 23:00:35.265412
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    # Test case #1
    result = {}

    try:
        ModuleArgumentSpecValidator(argument_spec=[], mutually_exclusive=[], required_together=[],
                                    required_one_of=[], required_if=[], required_by=[]).validate(parameters=result)

    except Exception as e:
        pass
    else:
        assert False

    # Test case #2
    result = {}

    try:
        ModuleArgumentSpecValidator(argument_spec={}, mutually_exclusive=[], required_together=[],
                                    required_one_of=[], required_if=[], required_by=[]).validate(parameters=result)

    except Exception as e:
        assert False
    else:
        assert isinstance(result, ValidationResult)

    # Test case #3
    result = {}


# Generated at 2022-06-12 23:00:37.864501
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    validator = ModuleArgumentSpecValidator({}, deprecations=[{'name': 'a', 'version': '9999.99.99'}], warnings=[['a', 'b']])
    result = validator.validate({})
    assert result.validated_parameters == {}
    assert len(result.error_messages) == 0
    assert result.unsupported_parameters == set()

# Generated at 2022-06-12 23:00:42.710827
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    argument_spec = {
        "param1": {"type": "str", "default": "foobar", "no_log": True},
        "param2": {"type": "str", "aliases": ["foo"]},
        "param3": {"type": "str", "aliases": ["bar"]},
    }

    parameters = {"param1": "foo"}

    deprecations = []
    warnings = []

    validator = ModuleArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)

    assert result.error_messages == []
    assert result.validated_parameters == {"param1": "foo"}
    assert result.unsupported_parameters == []

    assert deprecations == []
    assert warnings == []

    parameters = {"param2": "foo"}


# Generated at 2022-06-12 23:00:54.000417
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    argument_spec = {
        'name': {'type': 'str'},
        'username': {'type': 'str'},
        'password': {'type': 'str', 'no_log': True}
    }

    mutually_exclusive = [
        ['name', 'username'],
        ['password', 'username']
    ]

    args = [argument_spec, mutually_exclusive]

    assert len(args[0]) == 3
    assert len(args[0]['name']) == 1
    assert len(args[0]['username']) == 1
    assert len(args[0]['password']) == 2

    assert len(args[1]) == 2
    assert len(args[1][0]) == 2
    assert len(args[1][1]) == 2


# Generated at 2022-06-12 23:01:02.054569
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    # Create instance of class ModuleArgumentSpecValidator with its argument
    argument_spec = {}
    my_obj = ModuleArgumentSpecValidator(argument_spec)

    # Create a mock for the method validate of class ArgumentSpecValidator
    mock_validate = Mock(return_value=ValidationResult({}))
    my_obj._validate = mock_validate

    # Unit test for method validate of class ModuleArgumentSpecValidator
    my_obj.validate({})

    # Assert that the mock was called once
    mock_validate.assert_called_once_with({})

# Generated at 2022-06-12 23:01:08.254116
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    module_argument_spec = {
        'name': {
            'type': 'str',
            'required': True,
        },
        'age': {
            'type': 'int',
            'required': False,
        },
    }

    parameters = {
        'name': 'Bob',
        'age': '42'
    }

    validator = ModuleArgumentSpecValidator(module_argument_spec)
    result = validator.validate(parameters)

    assert result.validated_parameters == {
        u'name': u'Bob',
        u'age': 42,
    }, "Values are not set to their type"

# Generated at 2022-06-12 23:01:09.572557
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    "Test validate method of ArgumentSpecValidator class"
    pass

# Generated at 2022-06-12 23:01:19.913801
# Unit test for method validate of class ArgumentSpecValidator

# Generated at 2022-06-12 23:01:27.258795
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    # Set up
    parameters = {"name": "bo", "age": "42"}
    argument_spec = {'name': {'type': 'str'}, 'age': {'type': 'int'}}

    # Test
    validator = ModuleArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)

    # Assert
    assert not result.error_messages
    assert result.validated_parameters == {"name": "bo", "age": 42}

# Generated at 2022-06-12 23:01:32.240746
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    ''' Unit test for method validate of class ModuleArgumentSpecValidator '''
    result = ModuleArgumentSpecValidator(argument_spec = { 'param1': { 'type': 'str'}}).validate( {'param1': 'abc'})
    assert len( result.error_messages) == 0
    assert result.validated_parameters == { 'param1': 'abc'}

# Generated at 2022-06-12 23:01:47.298873
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    from ansible.module_utils.six import iteritems

    argument_spec = {
        'name': {'type': 'str', 'required': True, 'aliases': ['foo']},
        'age': {'type': 'int', 'default': 10, 'aliases': ['bar']},
        'validate': {"type": 'str', 'choices': ['foo', 'bar']}
    }

    mutually_exclusive = [['name', 'age']]
    mutually_exclusive_empty = []
    required_if = [['name', 'foo', ['validate']]]
    required_if_empty = []
    required_one_of = [['name', 'age', 'validate']]
    required_one_of_empty = []


# Generated at 2022-06-12 23:01:56.455791
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
        'aliased': {'type': 'str', 'aliases': ['alias']},
        'nested': {
            'type': 'dict',
            'aliases': ['alt'],
            'options': {
                'name': {'type': 'str'},
                'age': {'type': 'int'}
            }
        }
    }
    mutually_exclusive = [['name', 'alias']]
    required_together = []
    required_one_of = []
    required_if = []
    required_by = []

# Generated at 2022-06-12 23:01:59.790633
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    validator = ModuleArgumentSpecValidator({'arg1': {'type': 'str'}})
    assert validator.validate({'arg1': 42}).error_messages[0] == "arg1 was expected to be a string, got <type 'int'>"
    assert validator.validate({'arg1': '42'}).validated_parameters == {'arg1': '42'}

# Generated at 2022-06-12 23:02:09.551778
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    result = ModuleArgumentSpecValidator(None).validate({})
    assert not result._deprecations
    assert not result._warnings
    assert not result._errors

    result = ModuleArgumentSpecValidator(None).validate({'ansible_check_mode': True})
    assert result.deprecations
    assert result.deprecations[0]['name'] == 'ansible_check_mode'
    assert result.warnings
    assert result.warnings[0]['option'] == 'ansible_check_mode'
    assert result.warnings[0]['alias'] == 'check_mode'

    result = ModuleArgumentSpecValidator(None).validate({'ansible_check_mode': True, 'check_mode': True})
    assert result.deprecations

# Generated at 2022-06-12 23:02:11.214956
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    # TODO: Write unit test
    pass


# Generated at 2022-06-12 23:02:22.299975
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    from unit_tests.module_utils.module_arg_spec_validator import mock_ansible_module

    argument_spec = dict(
        test_str=dict(type='str'),
        test_str_required=dict(type='str', required=True),
        test_str_required_default=dict(type='str', required=True, default='default_value'),
        test_str_no_default=dict(type='str'),
        test_dict=dict(type='dict', default=dict(a=1)),
        test_list=dict(type='list', default=list()),
    )


# Generated at 2022-06-12 23:02:28.276253
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    argument_spec = {
        'foo': {'type': 'str'},
        'bar': {'type': 'int'}
    }

    parameters = {
        'foo': 'test',
        'bar': 42,
    }

    validator = ArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)

    assert not result.error_messages



# Generated at 2022-06-12 23:02:36.364054
# Unit test for method validate of class ModuleArgumentSpecValidator

# Generated at 2022-06-12 23:02:46.930791
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
        'phone': {'type': 'str'},
    }
    parameters = {
        'name': 'bo',
        'age': '42',
        'phone': 123,
    }
    validator = ArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)
    assert len(result.errors) == 1 and result.errors[0].issue == 'Invalid type for argument phone'
    assert result.validated_parameters['age'] == 42
    assert result.validated_parameters['name'] == 'bo'



# Generated at 2022-06-12 23:02:54.017824
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    # check that deprecations and warnings can be emitted
    argument_spec = {
        'name': {
            'type': 'str',
            'aliases': ['name_alias']
        },
        'other_name': {
            'type': 'str',
            'aliases': ['other_name_alias'],
            'deprecated': {'version': '2.10', 'date': '2020-06-12', 'collection_name': 'my_collection', 'removed_in': '2.12', "removal_reason": "it is to be removed"}
        }
    }
    parameters = {
        'other_name_alias': 1,
        'other_name': 2
    }
    validator = ModuleArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)


# Generated at 2022-06-12 23:03:13.409726
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    validator = ModuleArgumentSpecValidator({
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    })
    result = validator.validate({'name': 'bo', 'age': 42})
    assert not result.error_messages, "Validation failed with messages: {0}".format(", ".join(result.error_messages))
    assert result.validated_parameters['name'] == 'bo' and result.validated_parameters['age'] == 42, \
        "Validated parameters were not assigned to the result"

# Generated at 2022-06-12 23:03:17.247735
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    from ansible.module_utils.common.arg_spec import MODULE_ARGUMENT_SPEC

    v = ModuleArgumentSpecValidator(MODULE_ARGUMENT_SPEC)
    result = v.validate({'_ansible_module_name': 'ansible.module_utils.common.arg_spec'})

    assert not result._deprecations
    assert not result._warnings

# Generated at 2022-06-12 23:03:27.243820
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    argument_spec = {
        'a': {'type': 'str', 'aliases': ['b'], 'default': 'aaaaa'},
        'c': {'type': 'str', 'aliases': ['d'], 'default': 'bbb'},
        'e': {'type': 'str'},
    }

    parameters = {
        'a': '1',
        'b': '2',
        'c': '3',
        'd': '4',
        'e': '5',
    }

    validator = ModuleArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)

    assert result.errors == []
    assert result.validated_parameters['a'] == '2'
    assert result.validated_parameters['c'] == '3'
   

# Generated at 2022-06-12 23:03:35.551600
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    from ansible.module_utils import basic
    import mock

    # Mocking fail_json

    original_fail_json = basic.AnsibleModule.fail_json

    def mocked_fail_json(*args, **kwargs):
        mocked_fail_json.fail_json_count += 1
        mocked_fail_json.fail_json_calls.append((args, kwargs))
        original_fail_json(*args, **kwargs)
    mocked_fail_json.fail_json_count = 0
    mocked_fail_json.fail_json_calls = []

    basic.AnsibleModule.fail_json = mocked_fail_json

    # Mocking warning

    original_warn = basic.AnsibleModule.warning

    def mocked_warn(msg):
        original_warn(msg)

# Generated at 2022-06-12 23:03:37.097193
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    ModuleArgumentSpecValidator()

# Generated at 2022-06-12 23:03:47.707778
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
        'file': {'type': 'str', 'no_log': True},
    }

    parameters = {
        'name': 'bo',
        'age': '42',
        'file': 'secret.txt',
    }

    validator = ArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)

    assert not result.error_messages
    assert result.validated_parameters == {
        'name': 'bo',
        'age': 42,
        'file': 'secret.txt',
    }
    assert result.unsupported_parameters == set()


# Unit test to verify that mutually exclusive arguments are properly validated

# Generated at 2022-06-12 23:03:56.213430
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    }
    validator = ArgumentSpecValidator(argument_spec)
    parameters = {
        'name': 'bo',
        'age': '42',
    }
    result = validator.validate(parameters)
    assert type(result) is ValidationResult
    assert result.errors
    assert result.error_messages
    assert result.error_messages[0] == '"age" is of type string but expected to be of type int'
    assert result.validated_parameters == {
        'name': 'bo',
        'age': 42,
    }
    assert not result.unsupported_parameters

# Generated at 2022-06-12 23:04:03.257357
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():

    class MockAnsibleValidationErrorMultiple():

        def __init__(self, messages=None):
            self.messages = messages

    class MockArgumentSpecValidator(ArgumentSpecValidator):

        def __init__(self, argument_spec, required_if=None):
            self._required_if = required_if
            self._valid_parameter_names = set()
            self.argument_spec = argument_spec

        def validate(self, parameters):
            result = ValidationResult(parameters)
            result._no_log_values.update(set_fallbacks(self.argument_spec, result._validated_parameters))
            alias_warnings = []
            alias_deprecations = []

# Generated at 2022-06-12 23:04:12.918330
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    import sys as _sys
    
    # Simple example of validation with simple types
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
    

# Generated at 2022-06-12 23:04:18.765410
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

    validator = ModuleArgumentSpecValidator(argument_spec=arg_spec)
    result = validator.validate(parameters)

    if result.error_messages:
        sys.exit("Validation failed: {0}".format(", ".join(result.error_messages)))

    valid_params = result.validated_parameters

    print(valid_params)



# Generated at 2022-06-12 23:04:43.846510
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    argument_spec = {'foo': {'type': 'str', 'default': 'bar', 'required': True, 'aliases': ['the_foo', 'the_foo_alias']},
                     'bar': {'type': 'int', 'required': True, 'aliases': ['the_bar', 'the_bar_alias']},
                     'baz': {'type': 'list', 'required': False},
                     'qux': {'type': 'bool', 'required': False}}

    parameters = {'foo': 'new value', 'bar': 42, 'qux': True}
    validator = ModuleArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)
    assert result.validated_parameters == parameters
    assert result.unsupported_parameters == set([])
    assert result._deprec

# Generated at 2022-06-12 23:04:44.431801
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    pass

# Generated at 2022-06-12 23:04:52.622707
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    import unittest
    import sys
    from ansible.module_utils._text import to_bytes

    class TestCase(unittest.TestCase):
        def test_alias(self):
            argument_spec = {
                'name': {'type': 'str'},
                'age': {'type': 'int', 'aliases': ['years']},
            }

            parameters = {
                'name': 'bo',
                'age': '42',
            }

            validator = ModuleArgumentSpecValidator(argument_spec)
            result = validator.validate(parameters)

            #print(result.results, file=sys.stderr)

            self.assertTrue(result.validated_parameters['age'] == 42)


    if __name__ == '__main__':
        unittest.main

# Generated at 2022-06-12 23:05:02.756789
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    from ansible.module_utils.common.text.converters import to_bytes
    from ansible.module_utils.common.parameters import _is_boolean_value
    from ansible.module_utils.common.validation import boolean
    from ansible.module_utils.compat.ipaddress import ip_address, ip_network
    from ansible.module_utils.six import PY2, PY3
    import sys


# Generated at 2022-06-12 23:05:12.347597
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    # Testing for the test case of successful descriptor
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
        'nest': {
            'spec': {
                'nested_key': {'type': 'str'}
            },
            'type': 'dict'
        }
    }

    parameters = {
        'name': 'bo',
        'age': '42',
        'nest': {
            'nested_key': 'test'
        }
    }

    validator = ModuleArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)
    assert len(result.errors) == 0, "validation failed: {0}".format(", ".join(result.error_messages))
   

# Generated at 2022-06-12 23:05:12.794930
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    assert True == True

# Generated at 2022-06-12 23:05:13.269462
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    assert True

# Generated at 2022-06-12 23:05:16.916233
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



# Generated at 2022-06-12 23:05:27.388681
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    from ansible.module_utils import basic
    from ansible.module_utils.common.arg_spec import _validate_spec

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

    # Assert ValidationResult for successful validation
    basic.assert_equals({'age': 42, 'name': 'bo'}, result.validated_parameters)
    basic.assert_equals([], result.errors)
    basic.assert_equals([], result.error_messages)

# Generated at 2022-06-12 23:05:37.264311
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    argument_spec = {
        'name': {'type': 'str',
                 'required': True},
        'age': {'type': 'int',
                'default': 42},
        'other_required': {'type': 'str',
                           'required': True},
        'type': {'type': 'str',
                 'required': True,
                 'choices': ['a', 'b']},
        'no_log': {'type': 'str',
                   'no_log': True},

    }

    mutually_exclusive = [['name', 'other_required']]

    required_together = [['other_required', 'type']]

    required_one_of = [['other_required', 'name'], ['age']]

    required_if = [['other_required', 'a', ['type']]]

