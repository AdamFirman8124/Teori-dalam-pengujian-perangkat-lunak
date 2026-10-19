

# Generated at 2022-06-13 15:28:13.859487
# Unit test for function safe_eval
def test_safe_eval():
    test_vars = dict(
        foo='foo',
        bar='bar',
        baz='baz',
        num=99,
        array=[1, 2, 3],
        dict={'foo': 'bar'}
    )

    def assert_result_error(expr, expected_result, expected_error):
        result, error = safe_eval(expr, test_vars, include_exceptions=True)
        assert result == expected_result
        assert error == expected_error

    assert_result_error('foo', 'foo', None)
    assert_result_error('foo == "foo"', True, None)
    assert_result_error('foo == "bar"', False, None)
    assert_result_error('foo == bar', 'foobar', None)

# Generated at 2022-06-13 15:28:22.331394
# Unit test for function safe_eval
def test_safe_eval():
    # test safe_evals (EXPECTED)
    evaluate = safe_eval
    assert [] == evaluate('[]')
    assert {} == evaluate('{}')
    assert 1 == evaluate('1')
    assert 1.1 == evaluate('1.1')
    assert [1, 2] == evaluate('[1,2]')
    assert {'a': 1} == evaluate('{"a":1}')
    assert 1 == evaluate('1')
    assert 1.1 == evaluate('1.1')
    assert True == evaluate('true')
    assert True == evaluate('True')
    assert False == evaluate('false')
    assert False == evaluate('False')
    assert None == evaluate('null')
    assert None == evaluate('None')
    assert 'foo' == evaluate('"foo"')
    assert 'foo bar' == evaluate("'foo bar'")

# Generated at 2022-06-13 15:28:26.747989
# Unit test for function safe_eval
def test_safe_eval():
    tests = [
        {'expr': '2 + 2', 'result': 4},
        {'expr': '[2, 2]', 'result': [2, 2]},
        {'expr': '{"a": 2, "b": "foo"}', 'result': {u'a': 2, u'b': u'foo'}},
        {'expr': '!True', 'result': False},
        {'expr': 'true', 'result': True},
        {'expr': 'null', 'result': None},
    ]


# Generated at 2022-06-13 15:28:35.865348
# Unit test for function safe_eval
def test_safe_eval():
    test_values = (
        ('1', 1),
        ('1+2', 3),
        ('false', False),
        ('true', True),
        ('null', None),
        ('[1, 2, 3]', [1, 2, 3]),
        ('{"k1": "v1"}', {'k1': 'v1'}),
    )
    for value, expected in test_values:
        assert expected == safe_eval(value)

    syntax_error_values = (
        "'",
        "import os",
        "__import__('os').system('ls')",
        "[1, 2, "
    )
    for value in syntax_error_values:
        try:
            safe_eval(value)
        except SyntaxError as e:
            assert True

# Generated at 2022-06-13 15:28:44.963690
# Unit test for function safe_eval
def test_safe_eval():
    # call with a fully-compliant expression
    test_expression = '12 + 7'
    test_result = safe_eval(test_expression)
    assert test_result == 19

    # call with a JSON-compliant expression
    test_expression_json = 'true and false'
    test_result_json = safe_eval(test_expression_json)
    assert test_result_json is False

    # call with an expression containing a builtin function call
    test_expression_function = 'str(12)'
    test_result_function = safe_eval(test_expression_function)
    assert test_result_function == '12'

    # call with an expression containing a builtin function call that is not
    # allowed
    test_expression_function_not_allowed = 'compile(12)'

# Generated at 2022-06-13 15:28:53.012729
# Unit test for function safe_eval
def test_safe_eval():
    # Load enough globals to cover all tests
    OUR_GLOBALS = {}
    OUR_GLOBALS['container_to_text'] = container_to_text
    OUR_GLOBALS['__builtins__'] = __builtins__

    failed = False


# Generated at 2022-06-13 15:29:00.087188
# Unit test for function safe_eval
def test_safe_eval():

    (result, exception) = safe_eval('3+3', include_exceptions=True)
    assert result == 6
    assert exception is None

    (result, exception) = safe_eval('True', include_exceptions=True)
    assert result is True
    assert exception is None

    (result, exception) = safe_eval('False', include_exceptions=True)
    assert result is False
    assert exception is None

    (result, exception) = safe_eval('None', include_exceptions=True)
    assert result is None
    assert exception is None

    (result, exception) = safe_eval('none', include_exceptions=True)
    assert result is None
    assert exception is None

    # test sequences
    (result, exception) = safe_eval('[3,4]', include_exceptions=True)

# Generated at 2022-06-13 15:29:08.924008
# Unit test for function safe_eval
def test_safe_eval():
    # Covers literals, basic math and variables
    assert safe_eval("1 + 1") == 2
    assert safe_eval("1 + 1", dict(x=1), True) == (2, None)
    assert safe_eval("1 + x", dict(x=1), True) == (2, None)

    # Ensure dicts, lists and tuples are allowed
    assert safe_eval("{'a': 1}") == {'a': 1}
    assert safe_eval("{'a': 1}", dict(x=1), True) == ({'a': 1}, None)
    assert safe_eval("[1, 2]") == [1, 2]
    assert safe_eval("[1, 2]", dict(x=1), True) == ([1, 2], None)

# Generated at 2022-06-13 15:29:18.449273
# Unit test for function safe_eval
def test_safe_eval():
    # most of these tests are documented in test/units/module_utils/test_safe_eval.py
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    import ast
    import random

    def do_test(expr, expected_result, locals=None):
        # this test intentionally calls 'safe_eval' twice to verify both cases
        (_, err) = safe_eval(expr, locals=locals, include_exceptions=True)
        if err is not None:
            raise AssertionError("Expected %s to be allowed, but got %s" % (expr, err))
        result = safe_eval(expr, locals=locals, include_exceptions=False)

# Generated at 2022-06-13 15:29:29.898684
# Unit test for function safe_eval
def test_safe_eval():
    # assert container_to_text(safe_eval('{{ ansible_date_time.epoch }}')) == container_to_text(safe_eval('{{ ansible_date_time.epoch }}'))
    assert container_to_text(safe_eval('{{ ansible_date_time.epoch }}')) == safe_eval('{{ ansible_date_time.epoch }}')
    assert safe_eval('{{ ansible_date_time.epoch }}') is not None
    assert safe_eval('{{ ansible_date_time.epoch }}', dict(ansible_date_time=dict(epoch=123456)), include_exceptions=True) == (123456, None)

# Generated at 2022-06-13 15:29:41.565962
# Unit test for function safe_eval
def test_safe_eval():
    my_vars = dict(
        a_string="foo",
        b_string="bar",
        c_list=[1, 2, 3, 4],
        d_dict=dict(a=1, b=2),
        e_num=4,
        f_bool=True,
        g_none=None,
    )
    assert(safe_eval("a_string", my_vars) == "foo")
    assert(safe_eval("b_string", my_vars) == "bar")
    assert(safe_eval("c_list", my_vars) == [1, 2, 3, 4])
    assert(safe_eval("d_dict", my_vars) == dict(a=1, b=2))
    assert(safe_eval("e_num", my_vars) == 4)


# Generated at 2022-06-13 15:29:52.577291
# Unit test for function safe_eval
def test_safe_eval():
    # Test basic type handling
    result = safe_eval('3 + 6')
    assert result == 9, "safe_eval should do math (1)"

    result = safe_eval(u'3 + 6')
    assert result == 9, "safe_eval should do math (2)"

    result = safe_eval('foo_bar')
    assert result == "foo_bar", "safe_eval should pass through unknown variables (1)"

    result = safe_eval(u'foo_bar')
    assert result == "foo_bar", "safe_eval should pass through unknown variables (2)"

    result = safe_eval('"foo_bar"')
    assert result == "foo_bar", "safe_eval should pass through simple strings"

    result = safe_eval(u'"foo_bar"')

# Generated at 2022-06-13 15:30:00.469670
# Unit test for function safe_eval
def test_safe_eval():
    # usage: safe_eval(expr, locals=None, include_exceptions=False)
    # The expr passed in is an expression and should be valid Python code
    # locals is a dict of local variables that may be referenced by the expr
    # include_exceptions is optional and when True will return a tuple with
    # the result and any exception (see the test code below for examples)

    # Examples:
    print(safe_eval("['a', 'b', 'c']"))
    print(safe_eval("{'a': 1, 'b': 2, 'c': 3}"))
    print(safe_eval("['a', 'b', 'c'] + {'a': 1, 'b': 2, 'c': 3}"))

# Generated at 2022-06-13 15:30:08.285503
# Unit test for function safe_eval
def test_safe_eval():
    # The expression passed to safe_eval can be anything
    # that Python can evaluate with eval, as long as it's simple enough.
    #
    # For example, these expressions should all evaluate successfully:
    #
    #    1 + 2
    #    foo[3]
    #    'foo ' + 42
    #    (True if False else False)
    #    (False or False)
    #
    # These, however, should all fail:
    #
    #    1 + 2 + foo[bar]
    #    foo(bar)

    # 1 + 2    # This should be evaluated to 3
    expr = '1 + 2'
    assert safe_eval(expr) == 3

    # 'foo ' + 42    # This should be evaluated to 'foo 42'
    expr = '"foo " + 42'
    assert safe_

# Generated at 2022-06-13 15:30:18.709486
# Unit test for function safe_eval
def test_safe_eval():
    def verify(expr, expected, include_exceptions=False):
        expr, exception = safe_eval(expr, include_exceptions=include_exceptions)
        if include_exceptions:
            assert expr == expected[0]
        else:
            assert expr == expected

    # simple variable (in a list)
    verify('[a]', ['a'])
    # simple variable (in a dict)
    verify("{'b': b}", {"b": "b"})
    # simple variable (in a set)
    verify("{c}", {"c"})
    # simple variable (in a list comprehension)
    verify("[d['e'] for d in [{'e': 'f'}]]", ['f'])
    # simple variable (in a dict comprehension)

# Generated at 2022-06-13 15:30:26.963839
# Unit test for function safe_eval
def test_safe_eval():
    # Test OK
    assert safe_eval("2+2") == 4
    assert safe_eval("null") is None
    assert safe_eval("true") is True
    assert safe_eval("false") is False
    assert safe_eval("true and false") is False
    assert safe_eval("2*2") == 4
    assert safe_eval("['a', 'b']") == ['a', 'b']
    assert safe_eval("{'a':'b'}") == {'a': 'b'}

    # Test Invalid
    if C.DEFAULT_DEBUG:
        # this is the real error but the error message is not very pretty
        assert safe_eval('[    "a", "b" ]') == "[    \"a\", \"b\" ]"
        # the following is a more human-readable error, but it is
       

# Generated at 2022-06-13 15:30:33.303563
# Unit test for function safe_eval

# Generated at 2022-06-13 15:30:42.384721
# Unit test for function safe_eval
def test_safe_eval():
    def validate(expr, expected, include_exceptions=False, debug=False):
        if debug:
            print("testing: %s" % expr)

        if include_exceptions:
            (result, err) = safe_eval(expr, include_exceptions=True)
            if debug:
                print("err: %s" % err)
        else:
            result = safe_eval(expr, include_exceptions=False)
        if debug:
            print("result: %s" % result)
        assert result == expected

    validate("a and b", 'a and b')
    validate("a in b", 'a in b')
    validate("a + b", 'a + b')
    validate("a + b == 1", 'a + b == 1')

# Generated at 2022-06-13 15:30:48.435731
# Unit test for function safe_eval
def test_safe_eval():
    import datetime

    # valid expressions to evaluate

# Generated at 2022-06-13 15:30:52.674890
# Unit test for function safe_eval

# Generated at 2022-06-13 15:31:10.790439
# Unit test for function safe_eval
def test_safe_eval():
    """
    ansible jinja2 filters test utility
    ~~~~~

        $ python test_safe_eval.py
    """
    import sys, os
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + '../../')
    import ansible
    from ansible import constants as C
    from ansible.module_utils.common.text.converters import container_to_text, to_native

    # check if Jinja2 filters are properly installed
    if not ansible.__file__.endswith('__init__.py'):
        sys.path.append(os.path.dirname(ansible.__file__))
    from ansible.template import Templar

    # allow user to pass custom test expressions on the command line
    # eg: test_

# Generated at 2022-06-13 15:31:15.039506
# Unit test for function safe_eval
def test_safe_eval():
    # dictionary and list creation
    assert safe_eval('{"a": 1, "b": 2}') == {"a": 1, "b": 2}
    assert safe_eval('{"a": 1, "b": 2}') == {"a": 1, "b": 2}
    assert safe_eval('[1, 2, 3]') == [1, 2, 3]
    assert safe_eval('(1, 2, 3)') == (1, 2, 3)

    # string
    assert safe_eval('"foo"') == 'foo'

    # simple math
    assert safe_eval('1 + 2') == 3
    assert safe_eval('2 * 3') == 6
    assert safe_eval('6 / 2') == 3

    # number
    assert safe_eval('3') == 3

    # dict lookup
    assert safe_eval

# Generated at 2022-06-13 15:31:26.788409
# Unit test for function safe_eval
def test_safe_eval():
    # Test various combinations of builtins and other functions
    builtin_names = [name for name, obj in builtins.__dict__.items() if callable(obj)]
    methods = ['join', 'split', 'strip', 'keys', 'items', 'values']


# Generated at 2022-06-13 15:31:35.140262
# Unit test for function safe_eval
def test_safe_eval():
    """
    Unit test for safe_eval().
    """

# Generated at 2022-06-13 15:31:44.240565
# Unit test for function safe_eval
def test_safe_eval():
    # fails for all the right reasons
    assert safe_eval("", include_exceptions=True)[0] is None

    assert safe_eval("", include_exceptions=True)[0] == ""
    assert safe_eval("a_list_variable", dict(a_list_variable=[1, 2, 3]), include_exceptions=True)[0] == [1, 2, 3]
    assert safe_eval("a_list_variable", dict(a_list_variable={"foo": "bar"}), include_exceptions=True)[0] == {"foo": "bar"}
    assert safe_eval("a_list_variable", dict(a_list_variable="foo"), include_exceptions=True)[0] == "foo"

# Generated at 2022-06-13 15:31:54.889976
# Unit test for function safe_eval
def test_safe_eval():
    # Make sure that safe_eval is not affected by changes to
    # builtins.__dict__, so we make the builtins dict a regular
    # dict rather than a module dict.
    my_builtins = {'__builtins__': dict((k, v) for k, v in builtins.__dict__.items() if k in ('False', 'True', 'int', 'str'))}
    my_builtins['__builtins__']['custom_func'] = lambda x, y: None
    my_builtins['__builtins__']['unknown_func'] = lambda x, y: None
    my_builtins['__builtins__']['list'] = lambda x: None
    my_builtins['__builtins__']['dict'] = lambda x: None

# Generated at 2022-06-13 15:32:05.675194
# Unit test for function safe_eval
def test_safe_eval():
    from ansible.module_utils.common._collections_compat import Mapping, Sequence
    from ansible.utils.unsafe_proxy import wrap_var

    # the following strings should evaluate to 1

    # basic arithmetic
    assert safe_eval('1+0') == 1
    assert safe_eval('1+1') == 2

    # dicts and lists
    assert safe_eval('{"a":1}') == {"a": 1}
    assert safe_eval('[1]') == [1]

    # comparisons with numbers
    assert safe_eval('2 > 1') is True
    assert safe_eval('2 < 1') is False
    assert safe_eval('2 == 2') is True
    assert safe_eval('2 != 2') is False
    assert safe_eval('2 >= 3') is False

# Generated at 2022-06-13 15:32:17.771424
# Unit test for function safe_eval

# Generated at 2022-06-13 15:32:29.720984
# Unit test for function safe_eval
def test_safe_eval():
    # eval('a_list_variable') returns a string, so it's not safe to do
    # this as Ansible would try to evaluate the string as a python object
    # and fail.  We only want to unwrap this in the case where it's just
    # a data structure, hence safe_eval.
    assert safe_eval('a_list_variable') == 'a_list_variable'
    assert safe_eval(['a_list_variable']) == ['a_list_variable']

    # we only want to do this for literals, not things like 'var.split()'
    # or other functions
    if C.DEFAULT_SUDO_EXE == '/usr/bin/sudo':
        assert safe_eval('var.split()') == 'var.split()'

    # this is a basic mathematical expression which is valid and safe


# Generated at 2022-06-13 15:32:39.913746
# Unit test for function safe_eval
def test_safe_eval():
    def t(s, expected, expected_error=None, force_no_error=False):
        actual, error = safe_eval(s, include_exceptions=True)
        if isinstance(expected, type):
            assert isinstance(actual, expected)
        else:
            assert expected == actual
        if force_no_error:
            assert error is None
        else:
            assert expected_error == error

    t('true', True)
    t('false', False)
    t('[]', [])
    t('[1]', [1])
    t('[1, 2]', [1, 2])
    t('foo', 'foo', expected_error=exceptions.NameError)
    t('{"foo": "bar"}', {"foo": "bar"})

# Generated at 2022-06-13 15:32:55.916781
# Unit test for function safe_eval
def test_safe_eval():
    from ansible.module_utils.six import PY3

    print("Running safe_eval unit tests")
    # We should be able to eval these safely

# Generated at 2022-06-13 15:33:05.145337
# Unit test for function safe_eval
def test_safe_eval():
    # Success cases
    assert safe_eval("2 + 2") == 4
    assert safe_eval("'abc'.join(['a','b','c'])") == 'abc'
    assert safe_eval("['a','b','c']") == ['a','b','c']
    assert safe_eval("{'a': 'b'}") == {'a': 'b'}
    assert safe_eval("{'a': 'b', 'c': 'd'}") == {'a': 'b', 'c': 'd'}
    assert safe_eval("()") == ()
    assert safe_eval("(1, 2)") == (1, 2)
    assert safe_eval("(1, 2, 3)") == (1, 2, 3)
    assert safe_eval("None") is None

# Generated at 2022-06-13 15:33:16.095379
# Unit test for function safe_eval
def test_safe_eval():
    '''
    This is intended for allowing things like:
    with_items: a_list_variable

    Where Jinja2 would return a string but we do not want to allow it to
    call functions (outside of Jinja2, where the env is constrained).
    '''

    # Test some valid expressions

# Generated at 2022-06-13 15:33:27.032057
# Unit test for function safe_eval
def test_safe_eval():
    '''
    Test the safe_eval function directly.
    '''
    from ansible.module_utils.common.text.converters import to_text
    from ansible.module_utils.parsing.convert_bool import boolean

    def _test(expr, result, locals=None, exception=None):
        if locals is not None:
            new_locals = locals.copy()
            result2, exception2 = safe_eval(expr, new_locals, include_exceptions=True)
            result2 = container_to_text(result2)
        else:
            result2, exception2 = safe_eval(expr, include_exceptions=True)
            result2 = container_to_text(result2)


# Generated at 2022-06-13 15:33:38.048994
# Unit test for function safe_eval

# Generated at 2022-06-13 15:33:43.975557
# Unit test for function safe_eval
def test_safe_eval():
    import doctest
    import sys
    results = doctest.testmod(sys.modules[__name__])
    asserts = 0
    failures = 0
    for result in results:
        asserts += results[result]
        if not results[result]:
            failures += 1
    if failures > 0:
        raise Exception('Doctests failed: %i failures out of %i asserts' % (failures, asserts))

# Generated at 2022-06-13 15:33:55.128162
# Unit test for function safe_eval
def test_safe_eval():
    # Expected to succeed
    assert safe_eval("1") == 1
    assert safe_eval("1.1") == 1.1
    assert safe_eval("True") is True
    assert safe_eval("True and False") is False
    assert safe_eval("True and True") is True
    assert safe_eval("True and None") is None
    assert safe_eval("True or None") is True
    assert safe_eval("True or False") is True
    assert safe_eval("True or False and None") is True
    assert safe_eval("True or (False and None)") is True
    assert safe_eval("False or (True and False)") is False
    assert safe_eval("None or (True and False)") is False
    assert safe_eval("False and (True or False)") is False

# Generated at 2022-06-13 15:34:05.769664
# Unit test for function safe_eval
def test_safe_eval():
    sandbox = {
        'foo': 'bar',
        'true': True,
        'false': False,
        'null': None,
        'int_val': 1,
        'float_val': 1.1,
        'list_val': [1, 2, 3],
        'dict_val': {'a': 1, 'b': 2},
        'tuple_val': (1, 2, 3),
    }

# Generated at 2022-06-13 15:34:14.119216
# Unit test for function safe_eval
def test_safe_eval():
    """
    Test function safe_eval() in module ansible.utils.unsafe_proxy
    """

    fact_dict = { 'fact' : 'valid_var' }
    template_var = '{{valid_template}}'
    test_list = ['test_string', '{{invalid_template}}', ['test_list'],
                 { 'test_dict': '{{invalid_template}}'}]
    test_dict = { 'test_string': 'test_string', 'test_list':
        ['{{invalid_template}}'], 'test_dict': { 'test_string': 123 }}
    test_dict_var = { 'test_string_var': '{{valid_var}}'}

# Generated at 2022-06-13 15:34:18.647687
# Unit test for function safe_eval
def test_safe_eval():
    # empty string should return an empty string
    assert safe_eval('') == ''

    # basic python expressions should work
    assert safe_eval('1+1') == 2
    assert safe_eval('(1+1, 2+2)') == (2, 4)
    assert safe_eval('[1+1, 2+2]') == [2, 4]
    assert safe_eval('{1+1: 2+2}') == {2: 4}

    # builtin functions should not work
    result = safe_eval('__import__("os").getcwd()')
    assert result == '__import__("os").getcwd()'

    # items in the CALL_ENABLED list should work
    result = safe_eval('set([1,2,3]) == set([3,2,1])')
    assert result

# Generated at 2022-06-13 15:34:42.849690
# Unit test for function safe_eval
def test_safe_eval():
    def assert_safe_eval(expression, expected_result, should_raise=False):
        try:
            result = safe_eval(expression)
        except Exception as e:
            if should_raise:
                return
            else:
                raise AssertionError("safe_eval(%s) raised unexpectedly: %s" % (expression, e))
        if should_raise:
            raise AssertionError("safe_eval did not raise exception on expression: %s" % expression)
        if result != expected_result:
            raise AssertionError("safe_eval(%s) returned %s instead of %s" % (expression, result, expected_result))

    assert_safe_eval('1 + 1', 2)
    assert_safe_eval('2 * 3', 6)
    assert_safe_eval('2 ** 3', 8)
   

# Generated at 2022-06-13 15:34:51.516738
# Unit test for function safe_eval

# Generated at 2022-06-13 15:35:01.467291
# Unit test for function safe_eval
def test_safe_eval():
    # Passes
    assert safe_eval(None) is None
    assert safe_eval('foo') == 'foo'
    assert safe_eval('foo') == 'foo'
    assert safe_eval('"foo"') == 'foo'
    assert safe_eval('"foo"') == 'foo'
    assert safe_eval('"foo"') == 'foo'
    assert safe_eval('None') is None
    assert safe_eval('False') is False
    assert safe_eval('True') is True
    assert safe_eval('1+1') == 2
    assert safe_eval('-1') == -1
    assert safe_eval('1.0/2') == 0.5
    assert safe_eval('1/2') == 0.5
    assert safe_eval('-1/2') == -0.5
    assert safe_

# Generated at 2022-06-13 15:35:09.421527
# Unit test for function safe_eval
def test_safe_eval():
    # Check for a valid expression
    expr = "{{ ansible_hostname }} == 'host1'"
    result = safe_eval(expr, dict(ansible_hostname='host1'))
    assert result is True

    # Check for an invalid expression
    expr = "{{ ansible_hostname }} | upper == 'HOST1'"
    result = safe_eval(expr, dict(ansible_hostname='host1'))
    assert result == expr

    # Check for an invalid expression
    expr = "{{ ansible_hostname }} | upper"
    result = safe_eval(expr, dict(ansible_hostname='host1'))
    assert result == expr

    # Check for an invalid expression
    expr = "{{ ansible_hostname }} == 'host1' | upper"

# Generated at 2022-06-13 15:35:18.678145
# Unit test for function safe_eval
def test_safe_eval():
    def assert_exception(value, expected_exception=None, **kwargs):
        result, exception = safe_eval(value, include_exceptions=True, **kwargs)
        assert result == value
        assert (exception is not None) == (expected_exception is not None)
        if expected_exception is not None:
            assert isinstance(exception, expected_exception)

    assert safe_eval(None) is None
    assert safe_eval(True) is True
    assert safe_eval(False) is False
    assert safe_eval(1) == 1
    assert safe_eval(1.0) == 1.0
    assert safe_eval(-1) == -1
    assert safe_eval(-1.0) == -1.0
    assert safe_eval(1 + 2 + 3) == 6

# Generated at 2022-06-13 15:35:28.337804
# Unit test for function safe_eval
def test_safe_eval():
    # simple checks
    assert safe_eval('1 + 1') == 2
    assert safe_eval('2 - 1') == 1
    assert safe_eval('2 * 2') == 4
    assert safe_eval('8 / 2') == 4
    assert safe_eval('3 * 2 + 1') == 7
    assert safe_eval('3 * (2 + 1)') == 9
    assert safe_eval('10 - 2 * 3') == 4
    assert safe_eval('- (6 + 2)') == -8
    assert safe_eval('6 + -2') == 4
    assert safe_eval('(5 - 1) * ((7 + 1) / (3 - 1))') == 10
    assert safe_eval('foo', {'foo': 'bar'}) == 'bar'

# Generated at 2022-06-13 15:35:32.982690
# Unit test for function safe_eval
def test_safe_eval():
    eval_string = '"a" + "b" + "c"'
    result = safe_eval(eval_string)
    assert result == "abc"

    eval_string = '"a" + "b" + "c" + somevar'
    result = safe_eval(eval_string, dict(somevar=1))
    assert result == "abc1"

    eval_string = '"a" + "b" + "c" + somevar'
    result = safe_eval(eval_string, dict(somevar="hi"), True)
    assert result[0] == "abchi"
    assert result[1] == None

    # test that the callables are not enabled by default
    eval_string = 'abs(-3)'
    result = safe_eval(eval_string, dict(locals()), True)
    assert result

# Generated at 2022-06-13 15:35:40.279484
# Unit test for function safe_eval
def test_safe_eval():
    # Pass in dict
    # this will eval to a constant (dict)
    assert {'foo': 'bar'} == safe_eval("{'foo': 'bar'}", include_exceptions=True)

    # Pass in dict
    # this will eval to a variable (dict)
    assert {'foo': 'bar'} == safe_eval("a", {'a': {'foo': 'bar'}}, include_exceptions=True)

    # this is simple math, should eval to a number
    assert 2 == safe_eval("1+1", include_exceptions=True)

    # this is simple a string, should eval to a string
    assert "foobar" == safe_eval("'foobar'", include_exceptions=True)

    # this is hard python code, should eval to nothing

# Generated at 2022-06-13 15:35:50.322611
# Unit test for function safe_eval
def test_safe_eval():
    import sys
    import os
    import json
    import ast
    import traceback
    import tempfile

    """
    This performs a set of unit tests of the safe_eval function.
    """
    # the list of tuples of unevaluated strings and their eval'd results

# Generated at 2022-06-13 15:35:57.585161
# Unit test for function safe_eval
def test_safe_eval():
    import ansible.playbook.role.includeroad as iroad

    # check safe evaluation of a list
    assert safe_eval('[1, "foo", {"a": "b"}]') == [1, "foo", {"a": "b"}]
    # check safe evaluation of a dict
    assert safe_eval('{"a": "b", "c": "d"}') == {"a": "b", "c": "d"}
    # check invalid expression
    try:
        safe_eval('[1, "foo", {"a": "b"}, import os]')
    except:
        assert True
    # check for json types
    assert safe_eval('[1, "foo", false, true, null]') == [1, "foo", False, True, None]



# Generated at 2022-06-13 15:36:30.249477
# Unit test for function safe_eval
def test_safe_eval():
    #Test 1:
    # test safe_eval with a valid python expression not calling builtin functions
    valid_expr = "a + b"
    a = 1
    b = 3
    # test safe_eval with a valid python expression not calling builtin functions
    assert safe_eval(valid_expr, locals={'a': a, 'b': b}) == a + b

    #Test 2:
    # test safe_eval with an invalid python expression
    invalid_expr = "a * f()"
    try:
        # test safe_eval with an invalid python expression
        safe_eval(invalid_expr, locals={'a': a, 'b': b})
        failed = False
    except Exception:
        failed = True
    assert failed

    #Test 3:
    # test safe_eval with a valid python expression calling builtin functions not in

# Generated at 2022-06-13 15:36:34.914516
# Unit test for function safe_eval
def test_safe_eval():
    '''
    This is the test for function safe_eval, which ensures
    that it only evaluates expressions that do not contain
    dangerous AST nodes or functions.
    '''

    # test that basic expressions are evaluated properly
    assert safe_eval('True') == True
    assert safe_eval('False') == False
    assert safe_eval('"abc"') == "abc"
    assert safe_eval('9') == 9

    # test that invalid expressions are not evaluated
    assert safe_eval('__import__') == '__import__'
    assert safe_eval('[].append') == '[].append'
    assert safe_eval('[].clear()') == '[].clear()'
    assert safe_eval('{}.clear()') == '{}.clear()'
    assert safe_eval('{}.copy()') == '{}.copy()'
   

# Generated at 2022-06-13 15:36:40.165095
# Unit test for function safe_eval

# Generated at 2022-06-13 15:36:46.656170
# Unit test for function safe_eval

# Generated at 2022-06-13 15:36:58.630264
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval('foo') == 'foo'
    assert safe_eval('1 + 1') == 2
    assert safe_eval('(1 - 1)') == 0
    assert safe_eval('"foo" * 3') == 'foofoofoo'
    assert safe_eval('["foo", "foo", "foo"]') == ['foo', 'foo', 'foo']
    assert safe_eval('[1, 2, 3]') == [1, 2, 3]
    assert safe_eval('["foo", 1, {"bar": "baz"}]') == ['foo', 1, {'bar': 'baz'}]
    assert safe_eval('{"foo": "bar"}') == {'foo': 'bar'}
    assert safe_eval('True') is True
    assert safe_eval('False') is False

# Generated at 2022-06-13 15:37:05.153696
# Unit test for function safe_eval
def test_safe_eval():
    if sys.version_info >= (3, 0):
        expr_list = [
            "a_string",
            "True",
            "False",
            "{'k1': 'v1', 'k2': 'v2'}",
            "['v1', 'v2', 'v3']",
        ]
    else:
        expr_list = [
            "a_string",
            "True",
            "False",
            "{u'k1': u'v1', u'k2': u'v2'}",
            "[u'v1', u'v2', u'v3']",
        ]

    for expr in expr_list:
        result, exception = safe_eval(expr, include_exceptions=True)
        msg = "safe_eval('%s'): %s"

# Generated at 2022-06-13 15:37:12.761372
# Unit test for function safe_eval
def test_safe_eval():
    # Test that safe_eval detects and rejects AST nodes not in SAFE_NODES
    # (which includes AST nodes for lambdas, subroutines, and other stuff
    # we don't want to allow in our code).
    expr = 'lambda x: x'
    try:
        print(safe_eval(expr))
        assert False, "safe_eval should not have allowed the lambda expression"
    except Exception as e:
        pass

    expr = '[x for x in y]'
    try:
        print(safe_eval(expr))
        assert False, "safe_eval should not have allowed the list comprehension"
    except Exception as e:
        pass

    expr = 'True and False'
    result = safe_eval(expr)
    assert result == False

    expr = 'True or False'

# Generated at 2022-06-13 15:37:17.635105
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval("True") == True
    assert safe_eval("False") == False
    assert safe_eval("None") is None
    assert safe_eval("1") == 1
    assert safe_eval("2*5") == 10
    assert safe_eval("'1'") == '1'
    assert safe_eval('"1"') == '1'
    assert safe_eval("True and False and None") is None
    assert safe_eval("2*5+1") == 11
    assert safe_eval("True or False") == True
    assert safe_eval("'1' == '1'") == True
    assert safe_eval("('1' != '2')") == True
    assert safe_eval("1 > 2") == False
    assert safe_eval("2 > 1") == True

# Generated at 2022-06-13 15:37:22.594592
# Unit test for function safe_eval
def test_safe_eval():
    # Test simple invalid expressions
    assert safe_eval("{{foo}}", include_exceptions=True) == ("{{foo}}", None)
    assert safe_eval("{{ foo }}", include_exceptions=True) == ("{{ foo }}", None)
    assert safe_eval("{{ foo }", include_exceptions=True) == ("{{ foo }", None)

    # Test invalid expressions
    assert "invalid expression" in safe_eval("1+foo()", include_exceptions=True)[1].message
    assert "invalid expression" in safe_eval("1+[1,2,3]", include_exceptions=True)[1].message
    assert "invalid expression" in safe_eval("1+{1:2}", include_exceptions=True)[1].message

# Generated at 2022-06-13 15:37:34.076561
# Unit test for function safe_eval