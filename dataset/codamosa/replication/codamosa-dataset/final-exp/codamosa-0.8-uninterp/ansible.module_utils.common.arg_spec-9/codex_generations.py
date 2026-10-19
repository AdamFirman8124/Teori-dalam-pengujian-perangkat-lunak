

# Generated at 2022-06-12 22:56:13.728068
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    # ModuleArgumentSpecValidator is not meant to be used outside of AnsibleModule. Use ArgumentSpecValidator instead
    pass

# Generated at 2022-06-12 22:56:18.464670
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():

    def run_test(method, parameters):
        # pylint: disable=protected-access
        if method is 'validate':
            return method(parameters)

        assert False

    for method, parameters in [
        ('validate', {'name': 'bo', 'age': '42'}),
    ]:
        yield (run_test, method, parameters)

# Generated at 2022-06-12 22:56:25.893903
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    """

    :return: True if the test succeed, False otherwise
    """

    argument_spec = {
        "name": {"type": "str"},
        "age": {"type": "int"},
    }

    parameters = {
        "name": "bo",
        "age": "42",
    }

    validator = ArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)
    return result.validated_parameters["name"] == "bo" and result.validated_parameters["age"] == 42

# Generated at 2022-06-12 22:56:33.550593
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
    assert result
    assert len(result.errors) == 0
    assert result.error_messages == []
    assert result.validated_parameters.get('age') == 42
    assert result.unsupported_parameters == set()

# Generated at 2022-06-12 22:56:42.166540
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():

    from ansible.module_utils.common.validation import check_required_one_of
    from ansible.module_utils.common.validation import check_required_together


# Generated at 2022-06-12 22:56:53.616639
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    class MockArgs:
        def __init__(self, d):
            self.__dict__.update(d)
    class MockDeprecated:
        def __init__(self, d):
            self.__dict__.update(d)

    mock_arg_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    }
    mock_args = {
        'name': 'bo',
        'age': '42',
    }
    mock_mock_deprecated = MockDeprecated({
        'name': 'bo',
        'version': '1.1',
        'date': '2021-11-10',
        'collection_name': 'collection_name_value'
    })


# Generated at 2022-06-12 22:57:02.425466
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():

    def mocked_deprecate(message, version=None, date=None, collection_name=None):
        pass

    def mocked_warn(message):
        pass

    from ansible.module_utils.six import PY3
    from unittest.mock import patch

    from ansible.module_utils.common.arg_spec import _validate_sub_spec
    from ansible.module_utils.common.parameters import set_fallbacks

    def func(u):
        assert u == 'u_value'

    def func2(z):
        assert z == 'z_value'


# Generated at 2022-06-12 22:57:11.511637
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    from ansible.module_utils._text import to_text
    argument_spec = {
        'name': {'type': 'str', 'aliases': ['metadata_name']},
        'age': {'type': 'str', 'aliases': ['metadata_age']},
    }
    parameters = {
        'name': 'bo',
        'age': '42',
    }
    validator = ModuleArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)

    assert result.error_messages == []
    assert set(result.validated_parameters) == set(parameters)

# Generated at 2022-06-12 22:57:19.220925
# Unit test for method validate of class ArgumentSpecValidator

# Generated at 2022-06-12 22:57:29.517369
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    import pytest
    from ansible.module_utils.common.data_loader import DataLoader
    from ansible.module_args.common import log
    from ansible.module_utils.common.arg_spec import ModuleArgumentSpecValidator

    loader = DataLoader()
    log.terminal = log.terminal_true

    # This is the json data
    sample_json = loader.load_from_file('/home/caduser/code/ansible_devel/lib/ansible/module_utils/f5/bigip_irule_module.py')
    # This is the argument_spec
    argument_spec = sample_json['argument_spec']

    parameters = {
        'name': 'bo',
        'age': '42',
    }

    validator = ModuleArgumentSpecValidator(argument_spec)

# Generated at 2022-06-12 22:57:40.799028
# Unit test for constructor of class ArgumentSpecValidator
def test_ArgumentSpecValidator():
    # mutually_exclusive, required_together, required_one_of, required_if, required_by
    validator = ArgumentSpecValidator({}, None, None, None, None, None)
    assert validator._mutually_exclusive is None
    assert validator._required_together is None
    assert validator._required_one_of is None
    assert validator._required_if is None
    assert validator._required_by is None
    assert validator._valid_parameter_names == set()
    assert validator.argument_spec is not None
    assert validator._valid_parameter_names == set()


# Generated at 2022-06-12 22:57:46.334301
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    argspec = {
        'assert': {'type': 'str'},
        'name': {'type': 'str'},
        'age': {'type': 'int'}
    }

    parameters = {
        'name': 'bo',
        'age': '42',
        'assert': 'true'
    }

    validator = ArgumentSpecValidator(argspec)
    result = validator.validate(parameters)
    assert isinstance(result, ValidationResult)
    assert result.errors == []


# Generated at 2022-06-12 22:57:53.404317
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    from ansible.module_utils.common.validation import check_required_one_of
    from ansible.module_utils.common.validation import check_required_together
    from ansible.module_utils.common.validation import check_required_if

    spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
        'nicknames': {'type': 'list'},
    }

    arguments = {
        'name': 'bo',
        'age': '42',
        'nicknames': 'not a list'
    }

    validator = ArgumentSpecValidator(spec)
    result = validator.validate(arguments)

    assert isinstance(result, ValidationResult)
    assert isinstance(result.errors, AnsibleValidationErrorMultiple)



# Generated at 2022-06-12 22:57:54.507125
# Unit test for constructor of class ArgumentSpecValidator
def test_ArgumentSpecValidator():
    assert ArgumentSpecValidator is not None

# Generated at 2022-06-12 22:58:04.036973
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    from ansible.module_utils.common.arg_spec import MutuallyExclusiveError
    from ansible.module_utils.common.validation import (
        check_mutually_exclusive, check_required_arguments,
        check_required_if, check_required_one_of,
        check_required_together,
    )
    result = ValidationResult({})
    if result._mutually_exclusive or result._required_if or result._required_one_of or result._required_together:
        raise AssertionError('result._mutually_exclusive | result._required_if | result._required_one_of | result._required_together')
    if result._valid_parameter_names:
        raise AssertionError('result._valid_parameter_names')

# Generated at 2022-06-12 22:58:14.473756
# Unit test for method validate of class ModuleArgumentSpecValidator

# Generated at 2022-06-12 22:58:21.813918
# Unit test for constructor of class ArgumentSpecValidator
def test_ArgumentSpecValidator():
    # create a ArgumentSpecValidator object
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
        'aliases': {'type': 'str',
                    'aliases': ['apple', 'ball']}
    }

    validator = ArgumentSpecValidator(argument_spec)

    assert validator._valid_parameter_names == {'aliases (apple, ball)', 'age', 'name'}


# Generated at 2022-06-12 22:58:31.304757
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

    # If result.error_messages is not empty, validation fails

# Generated at 2022-06-12 22:58:40.153331
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    """Unit test for method validate of class ModuleArgumentSpecValidator"""
    from ansible.module_utils.common.warnings import MockDeprecationClass, MockWarningClass
    from ansible.module_utils.common.arg_spec import ModuleArgumentSpecValidator
    validation_result = ModuleArgumentSpecValidator(
        {
            'name': {'type': 'str'},
            'age': {'type': 'int'},
        },
        mutually_exclusive=[['name', 'age']]
    ).validate({'name': 'bo', 'age': '42'})

    assert "int" in validation_result.error_messages[0]
    assert len(validation_result.error_messages) == 1
    assert validation_result.validated_parameters['name'] == 'bo'
    assert validation_result

# Generated at 2022-06-12 22:58:41.047187
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    pass

# Generated at 2022-06-12 22:58:50.536218
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    argument_spec = {'name': {'type': 'str'}, 'age': {'type': 'int'}}
    parameters = {'name': 'bo', 'age': '42'}

    validator = ModuleArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)

    assert result.validated_parameters == {'name': 'bo', 'age': 42}


# Generated at 2022-06-12 22:58:57.817640
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    """
    Test for ArgumentSpecValidator.validate()
    """
    argument_spec = {
        "age": {"type": "int"},
        "name": {"type": "dict"}
    }
    mutually_exclusive = [["age", "name"]]
    result = ValidationResult({"name": "bo", "age": 12})
    result._no_log_values.update(set_fallbacks(argument_spec, result._validated_parameters))
    aliases = None
    legal_inputs = _get_legal_inputs(argument_spec, result._validated_parameters, aliases)
    result._unsupported_parameters.update(_get_unsupported_parameters(argument_spec, result._validated_parameters, legal_inputs))

# Generated at 2022-06-12 22:59:10.143147
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    from ansible.module_utils.common.arg_spec import ModuleArgumentSpecValidator
    argument_spec = {
        'foo': {'type': 'str', 'default': 'bar'},
        'test': {'type': 'str', 'aliases': ['testing']},
        'what': {'type': 'str', 'aliases': ['whatever']}
    }
    mutually_exclusive = [('foo', 'bar'), ('test', 'what')]
    parameters = {'foo': 'baz', 'bar': 'quux'}
    validator = ModuleArgumentSpecValidator(argument_spec, mutually_exclusive)
    result = validator.validate(parameters)
    assert len(result.validated_parameters) == 1
    assert result.validated_parameters['foo'] == 'baz'

# Generated at 2022-06-12 22:59:16.298542
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    validator = ModuleArgumentSpecValidator('argument_spec', 'mutually_exclusive',
                                            'required_together', 'required_one_of'
                                            , 'required_if', 'required_by')

    validator.validate({'name': 'bo',
                        'age': '42'})
    assert validator.validate({'name': 'bo',
                               'age': '42'}) != ""
    assert validator.validate({'name': 'bo',
                               'age': '42'}) is not None



# Generated at 2022-06-12 22:59:21.268254
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    test_spec = dict(option=dict(type='str'))
    test_parameters = dict(option='value')
    validator = ModuleArgumentSpecValidator(argument_spec=test_spec)
    result = validator.validate(parameters=test_parameters)
    assert not result.errors
    assert result.validated_parameters == test_parameters



# Generated at 2022-06-12 22:59:32.231225
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    validator = ModuleArgumentSpecValidator(argument_spec={'parameter_a': {'type': 'str'},
                                                           'parameter_b': {'type': 'str'},
                                                           'parameter_c': {'type': 'str'}})
    parameters = {'parameter_a': 'value_a', 'parameter_b': 'value_b'}

    result = validator.validate(parameters)

    assert result.validated_parameters == parameters

    parameters = {'parameter_a': 'value_a', 'alias_parameter_b': 'value_b'}

# Generated at 2022-06-12 22:59:40.967696
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    test_args = {
        "argument_spec": {
            "name": {
                "type": "str"
            },
        }
    }

    test_args['mutually_exclusive'] = ['name', 'age']

    test_args['required_together'] = ['name', 'age']

    test_args['required_one_of'] = ['name', 'age']

    test_args['required_if'] = ['name', 'age', 'test']

    test_args['required_by'] = {'name': 'test', 'age': 'test2'}

    parameters = {}

    result = ModuleArgumentSpecValidator(**test_args).validate(parameters)

    print("Errors: " + str(result.errors))

    if result.errors:
        raise Exception

# Generated at 2022-06-12 22:59:48.574761
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    validator = ModuleArgumentSpecValidator(
        argument_spec={
            'required_one_of': {'type': 'list', 'default': []},
            'required_together': {'type': 'list', 'default': []},
            'required_if': {'type': 'list', 'default': []},
            'required_by': {'type': 'dict', 'default': {}},
            'mutually_exclusive': {'type': 'list', 'default': []},
        },
        mutually_exclusive=[['a', 'b']],
        required_together=[['c', 'd']],
        required_one_of=[['e', 'f']],
        required_if=[['e', 'g', ['d', 'h']]],
        required_by={'i': ['j']},
    )

    assert valid

# Generated at 2022-06-12 22:59:54.940390
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
    assert result.validated_parameters == {'name': 'bo', 'age': 42}



# Generated at 2022-06-12 23:00:02.573903
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    # Have to mock dateutil.parser.parse so that deprecate doesn't fail if
    # dateutil.parser cannot be imported
    import mock
    from dateutil.parser import parse

    with mock.patch('dateutil.parser.parse', parse):
        from ansible.module_utils.common.text.converters import to_native
        import json
        import sys

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


# Generated at 2022-06-12 23:00:16.721309
# Unit test for method validate of class ArgumentSpecValidator

# Generated at 2022-06-12 23:00:25.286199
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():

    from ansible_collections.notstdlib.moveitallout.plugins.module_utils.common.arg_spec import ModuleArgumentSpecValidator
    from ansible_collections.notstdlib.moveitallout.tests.unit.compat.mock import patch, PropertyMock


# Generated at 2022-06-12 23:00:33.966204
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

    assert isinstance(result.validated_parameters, dict)
    assert result.validated_parameters['name'] == 'bo'
    assert result.validated_parameters['age'] == 42

    assert len(result.error_messages) == 0



# Generated at 2022-06-12 23:00:43.010384
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():

    import datetime

    date = datetime.date(2012, 12, 12)
    today = datetime.date(2013, 12, 12)
    date2 = datetime.date(2014, 12, 12)

    # Complex dict as input

# Generated at 2022-06-12 23:00:54.389877
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    ''' Unit test for method validate of class ModuleArgumentSpecValidator '''
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.basic import AnsibleModule

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

    expected_valid_params = {
        'name': 'bo',
        'age': 42,
    }

# Generated at 2022-06-12 23:01:04.827876
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    class MockModule:
        def __init__(self):
            self.warnings = []
            self.deprecations = []

        def deprecate(self, msg, version, collection_name=None):
            self.deprecations.append({
                'msg': msg,
                'version': version,
                'collection_name': collection_name,
            })

        def warn(self, msg):
            self.warnings.append(msg)

    module = MockModule()
    parameters = dict(
        name='name',
        age='42',
        the_key='the value',
    )
    mutually_exclusive = [
        ['not_both', 'not_this'],
        ['not_this_either'],
    ]

# Generated at 2022-06-12 23:01:11.588662
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    class test_Result:
        def __init__(self):
            self._deprecations = []
            self._warnings = []

    class test_AnsibleModule:
        def __init__(self):
            self.params = {'a': 'b'}
            self.result = test_Result()

        def warning(self, msg):
            self.result._warnings.append(msg)

        def deprecated(self, msg, version=None, collection_name=None, date=None):
            deprecation = {'name': msg}
            if version is not None:
                deprecation['version'] = version
            if collection_name is not None:
                deprecation['collection_name'] = collection_name
            if date is not None:
                deprecation['date'] = date
            self.result._dep

# Generated at 2022-06-12 23:01:21.980906
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    from ansible.module_utils.common.arg_spec import ModuleArgumentSpecValidator
    from ansible.module_utils.common.validation import ArgumentError
    import sys

    if sys.version_info[0] == 2:
        try:
            from mock import patch
        except ImportError:
            try:
                from unittest.mock import patch
            except ImportError:
                raise ImportError(
                    'Unable to load mock module, please install the mock module or python-mock package')
    else:
        from unittest.mock import patch


# Generated at 2022-06-12 23:01:22.667005
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    pass

# Generated at 2022-06-12 23:01:32.895361
# Unit test for method validate of class ModuleArgumentSpecValidator

# Generated at 2022-06-12 23:01:46.399901
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    from ansible.module_utils.common.arg_spec import ArgumentSpecValidator
    from ansible.module_utils import basic
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.six.moves import StringIO
    from ansible.module_utils.six import iteritems
    from ansible.module_utils.common.parameters import sanitize_keys
    import json
    import sys

    # arg_spec = {}
    # parameters = {}
    # validator = ArgumentSpecValidator(arg_spec)
    # result = validator.validate(parameters)

    # results = {}
    # results['valid_params'] = result.validated_parameters
    # results['no_log_vals'] = result.no_log_values
    # results['unsupported_params']

# Generated at 2022-06-12 23:01:54.117847
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    from ansible.module_utils.common.arg_spec import ModuleArgumentSpecValidator
    # test deprecate
    result = ModuleArgumentSpecValidator({"name": {"aliases": ['name_alias'], "type": "str"}}).validate({"name": "kevin", "name_alias": "kevin_alias"})
    assert len(result.errors) == 0
    assert len(result._warnings) == 1
    assert len(result._deprecations) == 1
    assert "Both option name and its alias name_alias are set." == result._warnings[0]['option'] + " and its alias " + result._warnings[0]['alias'] + " are set."



# Generated at 2022-06-12 23:01:55.213348
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    pass


# Generated at 2022-06-12 23:02:03.144703
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    doc = """
    ---
        parameter1: "%s"
        parameter2: "%s"
        parameter3: "%s"
        option1: "%s"

        aliases:
            parameter2: ['alias1', 'alias2']
            option2: 'option3'
    """

# Generated at 2022-06-12 23:02:09.607487
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    module_arg_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int', 'default': 20},
    }
    parameters = {
        'name': 'bo',
        'age': 42,
    }

    validator = ModuleArgumentSpecValidator(module_arg_spec)
    result = validator.validate(parameters)
    assert result.errors == []
    assert result.validated_parameters == {'name': 'bo', 'age': 42}

# Generated at 2022-06-12 23:02:20.977824
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    from ansible.module_utils.ansible_nxos_common import ModuleNxosCommon
    import os
    import sys
    import pytest

    # Since we are forced to take in the parameters as a dictionary,
    # it is important to ensure that the parameters are validated to
    # ensure that there are no duplicate keys
    with pytest.raises(RuntimeError) as e:
        sys.argv = [os.getcwd() + '/testing.py', 'host=localhost', 'host=localhost']  # duplicated key
        module = ModuleNxosCommon()
    assert "Duplicated key: 'host'" in to_native(e)

    # further ensure that the same key is not duplicated using a duplicate key
    # at the end of the argument list

# Generated at 2022-06-12 23:02:29.811840
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    """Unit test for validating the validate method of ArgumentSpecValidator class."""

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

    assert result._warnings == []

    valid_params = result.validated_parameters
    assert valid_params['name'] == 'bo'
    assert valid_params['age'] == 42

# Generated at 2022-06-12 23:02:37.084236
# Unit test for method validate of class ArgumentSpecValidator

# Generated at 2022-06-12 23:02:47.462254
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    """Unit test for method validate of class ArgumentSpecValidator."""
    result = ValidationResult(parameters=None)
    result.errors = AnsibleValidationErrorMultiple()
    cases = [
        ("parameters is not of type dict", None, result),
        ("parameters is not of type dict", [{'key': 'value'}], result),
        ("parameters is not of type dict", dict(key=dict(subkey='subvalue')), result),
        ("parameters is not of type dict", dict(key='value'), result),
        ("parameters is not of type dict", dict(subkey='subvalue'), result),
        ("parameters is not of type dict", dict(key=dict(subkey='subvalue')), result),
    ]

# Generated at 2022-06-12 23:02:48.815824
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    """
    This test validates the method "validate" from the class "ArgumentSpecValidator"
    """
    assert False

# Generated at 2022-06-12 23:03:06.073271
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    arguments_spec = {
        "name": {
            "type": "str",
            "required": True,
            "choices": [
                "bo",
                "sally",
                "mike",
                "sue"
            ],
            "aliases": ['first_name']
        },
        "age": {
            "type": "int",
            "required": False,
            "default": 30
        }
    }

    parameters = {
        # validates against argument spec
        "name": "bo",
        "age": 42,
        # unsupported
        "height": '178',
        # no_log
        "password": 'abc123'
    }

    module_argument_spec_validator = ModuleArgumentSpecValidator(arguments_spec)
    error_on_module_argument_spec

# Generated at 2022-06-12 23:03:13.680618
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():

    # Test code
    import sys
    sys.path.append(r'/home/lx/PycharmProjects/ansible/lib/ansible/module_utils/common')
    from arg_spec import ModuleArgumentSpecValidator
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

    # Check code
    assert isinstance(result, ValidationResult)

# Generated at 2022-06-12 23:03:19.224048
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    parameters = {
        'name': 'bo',
        'age': '42',
    }

    argument_spec = {
        'name': {'type': 'str', 'aliases': ['alias']},
        'age': {'type': 'int'},
    }

    validator = ModuleArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)

    assert result.validated_parameters == {u'age': 42, u'name': u'bo'}
    assert not result.error_messages

# Generated at 2022-06-12 23:03:28.423352
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    # Setup
    from ansible.module_utils.common.arg_spec import ModuleArgumentSpecValidator
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'}
    }

    parameters = {
        'name': 'bo',
        'age': '42',
        'not_in_spec': 'value'
    }

    # Exercise
    validator = ModuleArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)

    # Verify
    assert result.validated_parameters == {'name': 'bo', 'age': 42}
    assert result.error_messages == ["Extra parameters: not_in_spec"]

# Generated at 2022-06-12 23:03:36.402819
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():

    parameters = {
        'name': 'bo',
        'age': '42',
        '_ansible_no_log': True
    }

    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
        '_ansible_no_log': {'type': 'bool'}
    }

    mutually_exclusive = []
    required_together = []
    required_one_of = []
    required_if = []
    required_by = []

    validator = ModuleArgumentSpecValidator(argument_spec, mutually_exclusive, required_together, required_one_of, required_if, required_by)
    result = validator.validate(parameters)


# Generated at 2022-06-12 23:03:47.298744
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    from ansible.module_utils.common.parameters import ModuleParameters
    from ansible.module_utils.netcommon import ModuleDeprecationWarning
    from ansible.module_utils.six import string_types

    def assert_raise_deprecationwarning(module):
        try:
            module.fail_json(msg='hello world.')
        except ModuleDeprecationWarning as e:
            assert isinstance(e.message, string_types)
        else:
            assert False

    def assert_raise_warning(module):
        try:
            module.fail_json(msg='hello world.')
        except UserWarning as e:
            assert isinstance(e.message, string_types)
        else:
            assert False

    # The argument spec contains an alias 'age' to 'years' and they are both set in parameters.
   

# Generated at 2022-06-12 23:03:54.549209
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
    assert 'bo' == result.validated_parameters['name']
    assert 42 == result.validated_parameters['age']
    assert 'bo' != result.validated_parameters['name']


# Generated at 2022-06-12 23:04:03.706089
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():

    # Create a fake class that has a deprecate method.
    class fake_ansiblemodule:
        @staticmethod
        def waring(m):
            print(m)

        @staticmethod
        def deprecate(m):
            print(m)

    # Create a fake class that has a warn method.
    class fake_ansible_module_utils:
        @staticmethod
        def warn(m):
            print(m)

    # Create a fake class that has a to_native method.
    class fake_ansible_module_utils_errors:
        @staticmethod
        def to_native(m):
            return m

    # Generate a fake argument spec that has a deprecate and warn.

# Generated at 2022-06-12 23:04:13.227405
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    """Check if the ArgumentSpecValidator class method parse_params works as expected"""
    valid_params = {
        'name': 'bo',
        'age': 42,
    }
    invalid_params = {
        'name': 'bo',
        #'age': 42, # uncomment to generate a RequiredError()
        'age': 'fouty two', # uncomment to generate an ArgumentError()
    }
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    }
    validator = ArgumentSpecValidator(argument_spec)
    result = validator.validate(invalid_params)
    assert result.error_messages is not None
    result = validator.validate(valid_params)

# Generated at 2022-06-12 23:04:17.296943
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    import ansible.module_utils.common.arg_spec as arg_spec
    
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    }

    parameters = {
        'name': 'bo',
        'age': '42',
    }

    validator = arg_spec.ModuleArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)

    assert len(result.errors) == 0



# Generated at 2022-06-12 23:04:37.543462
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    v = ModuleArgumentSpecValidator(argument_spec={})
    parameters = {}
    result = v.validate(parameters)
    assert result.errors.count() == 0
    assert result.validated_parameters == parameters
    assert result.unsupported_parameters == set()

# Generated at 2022-06-12 23:04:44.652924
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():

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

    validator = ModuleArgumentSpecValidator(argument_spec,
                                            mutually_exclusive=mutually_exclusive)
    result = validator.validate(parameters)

    assert result.error_messages[0] == "Options 'age' and 'name' are mutually exclusive"

    parameters = {
        'name': 'bo',
    }

    result = validator.validate(parameters)

    assert len(result.error_messages) == 0

# Generated at 2022-06-12 23:04:51.988384
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    from datetime import datetime
    from textwrap import dedent

    result = ModuleArgumentSpecValidator({
        "url": {
            "type": "str"
        }
    }).validate(dict(
        url="http://www.example.com"
    ))

    assert len(result.error_messages) == 0
    assert result.validated_parameters == {
        "url": "http://www.example.com"
    }

    result = ModuleArgumentSpecValidator({
        "url": {
            "type": "str"
        }
    }).validate(dict(
        url="http://www.example.com",
        url_1="http://www.example.com"
    ))

    assert len(result.error_messages) == 1
    assert result.error_messages

# Generated at 2022-06-12 23:05:01.872902
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():

    # 'test_alias_deprecated': [
    #     {'deprecations': [{'version': 'v3.3', 'name': 'test_alias'}],
    #      'argument_spec': {'test_alias': {'aliases': ['test'], 'type': 'str'}},
    #      'params': {},
    #      'check': {'warnings': [], 'errors': [], 'deprecations': [], 'unsupported': [], 'no_log': []}
    #      },
    # ],

    argument_spec = {'test_alias': {'aliases': ['test'], 'type': 'str'}}
    params = {}
    validator = ModuleArgumentSpecValidator(argument_spec)
    result = validator.validate(params)
    assert result.error_

# Generated at 2022-06-12 23:05:11.691795
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    # Create a mock argument_spec
    argument_spec = {'name': {'type': 'str'}, 'password': {'no_log': 'yes'}, 'age': {'type': 'int', 'required': False}}

    # Create a mock parameters
    parameters = {'name': 'bo', 'age': '42'}
    parameters2 = {'name': 'bobo', 'age': '43'}

    # Create a new Instance of ArgumentSpecValidator
    instance1 = ModuleArgumentSpecValidator(argument_spec=argument_spec)
    instance2 = ModuleArgumentSpecValidator(argument_spec=argument_spec)

    # call the method validate
    result1 = instance1.validate(parameters)
    result2 = instance2.validate(parameters2)

    # check if the result value is correct


# Generated at 2022-06-12 23:05:16.990161
# Unit test for method validate of class ArgumentSpecValidator
def test_ArgumentSpecValidator_validate():
    """ Unit test for method validate of class ArgumentSpecValidator
    """
    assert ArgumentSpecValidator({'name': {}}).validate(
        {'name': 'bo'},
    ).validated_parameters == {'name': 'bo'}

    assert ArgumentSpecValidator({'name': {}}).validate(
        {'name': 'bo'},
    ).error_messages == []

    assert ArgumentSpecValidator({'name': {}}).validate(
        {'name': 'bo'},
    ).validated_parameters == {'name': 'bo'}

    assert ArgumentSpecValidator({'name': {}}).validate(
        {'name': 'bo'},
    ).error_messages == []


# Generated at 2022-06-12 23:05:27.548186
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    import ansible.module_utils.common.arg_spec as arg_spec
    from ansible.module_utils.common.arg_spec import DeprecatedAlias
    from ansible.module_utils.common.text.converters import to_native
    import ansible.module_utils.common.warnings as warnings
    import ansible.module_utils.common.validation as validation
    import ansible.module_utils.errors as errors
    import unittest
    import unittest.mock as mock

    class UnitTest(unittest.TestCase):
        def setUp(self):
            self.module_args = {'arg1': 'arg1'}
            self.argument_spec = {'arg1': {'type': 'str'}}

# Generated at 2022-06-12 23:05:34.897986
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    module_spec = {'param_name': {'alias': 'param_alias'}}
    module_arguments = {'param_name': 'value_1', 'param_alias': 'value_2'}
    my_validator = ModuleArgumentSpecValidator(module_spec)
    result = my_validator.validate(module_arguments)
    assert result.error_messages == []
    assert result.validated_parameters == {'param_name': 'value_2'}
    assert result._unsupported_parameters == set()

# Generated at 2022-06-12 23:05:37.491505
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

# Generated at 2022-06-12 23:05:43.228660
# Unit test for method validate of class ModuleArgumentSpecValidator
def test_ModuleArgumentSpecValidator_validate():
    # Argument spec with a warning and a deprecation
    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int', 'default': 42, 'aliases': ['old']},
    }
    # Parameters with both an option and its alias set
    parameters = {
        'name': 'bo',
        'age': 24,
        'old': 32,
    }

    validator = ModuleArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)
    assert result.validated_parameters.get('age') == 32