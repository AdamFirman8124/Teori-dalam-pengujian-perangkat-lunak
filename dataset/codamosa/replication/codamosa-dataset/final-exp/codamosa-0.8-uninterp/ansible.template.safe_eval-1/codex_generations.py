

# Generated at 2022-06-13 15:28:15.987428
# Unit test for function safe_eval

# Generated at 2022-06-13 15:28:21.571091
# Unit test for function safe_eval
def test_safe_eval():
    # This is for backwards compat with modules that rely on this library.
    import ansible.module_utils.common.text.converters as converters

    converters.safe_eval = safe_eval


# Generated at 2022-06-13 15:28:25.693226
# Unit test for function safe_eval
def test_safe_eval():
    # A simple test to check the behavior of safe_eval with more complex data structures
    complex_data = [{'foo': 'bar'}]
    # We expect an exception when trying to parse the complex data since we are passing it in as a string and not a dict
    try:
        complex_data_parse = ast.literal_eval(complex_data)
    except Exception as e:
        assert isinstance(e, ValueError)
        print("Exception caught as expected: ", e)
    # When using safe_eval, we expect the data to parse to a dict
    safe_data_parse = safe_eval(complex_data, include_exceptions=True)[0]
    assert isinstance(safe_data_parse, dict)


# Generated at 2022-06-13 15:28:35.060089
# Unit test for function safe_eval

# Generated at 2022-06-13 15:28:44.482924
# Unit test for function safe_eval

# Generated at 2022-06-13 15:28:52.743235
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval('[1, 2, 3]') == [1, 2, 3]
    assert safe_eval('{"foo": 1, "bar": 2}') == {"foo": 1, "bar": 2}
    assert safe_eval('foo') == 'foo'
    assert safe_eval('1 + 1') == 2
    assert safe_eval('a_list_variable', dict(a_list_variable=[1, 2, 3])) == [1, 2, 3]
    assert safe_eval('a_list_variable', dict(a_list_variable=[1, 2, 3])) == [1, 2, 3]
    assert safe_eval('foo.bar()', dict(foo=dict(bar=lambda: 42))) == 42

# Generated at 2022-06-13 15:28:59.996216
# Unit test for function safe_eval
def test_safe_eval():
    # simple expressions
    assert safe_eval('1 + 1') == 2
    assert safe_eval('True') is True
    assert safe_eval('true') is True
    assert safe_eval('false') is False
    assert safe_eval('False') is False
    assert safe_eval('null') is None
    assert safe_eval('[1, 2, 3]') == [1, 2, 3]
    assert safe_eval('[1, foo, 3]', locals={'foo': 2}) == [1, 2, 3]
    assert safe_eval('(7,)') == (7,)
    assert safe_eval('"some"') == "some"
    assert safe_eval('None') is None

# Generated at 2022-06-13 15:29:08.887345
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval('foo') == 'foo'
    assert safe_eval(42) == 42
    assert safe_eval('[1, 2]') == [1, 2]
    assert safe_eval('[1, 2] + [3, 4]') == [1, 2, 3, 4]
    assert safe_eval('["a", "b"] + ["c", "d"]') == ["a", "b", "c", "d"]
    assert safe_eval('[1, 2, 3, 4][2]') == 3
    assert safe_eval('foo[1]', {'foo': [0, 100]}) == 100
    assert safe_eval('foo.bar', {'foo': {'bar': 'baz'}}) == 'baz'
    assert safe_eval('false') is False

# Generated at 2022-06-13 15:29:18.411997
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval("1 + 2") == 3
    assert safe_eval("True") == True
    assert safe_eval("None") == None

    assert safe_eval("1 + 2", include_exceptions=True) == (3, None)
    assert safe_eval("True", include_exceptions=True) == (True, None)
    assert safe_eval("None", include_exceptions=True) == (None, None)

    assert safe_eval("a") == "a"
    assert safe_eval("a", include_exceptions=True) == ("a", None)
    assert safe_eval("True and a") == "a"
    assert safe_eval("True and a", include_exceptions=True) == ("a", None)
    assert safe_eval("a", dict(a=1)) == 1
    assert safe_eval

# Generated at 2022-06-13 15:29:29.899702
# Unit test for function safe_eval

# Generated at 2022-06-13 15:29:40.535730
# Unit test for function safe_eval
def test_safe_eval():
    class TestModule:
        def __init__(self, module_name, module_args, check_invalid_arguments=False, use_cache=True):
            self.params = module_args
            self.check_invalid_arguments = check_invalid_arguments
            self.argument_spec = dict()

    from ansible.module_utils.facts import ModuleReplacer
    from ansible.parsing.plugin_docs import read_docstring

    m = TestModule('test_module', dict())
    module = ModuleReplacer(m)

    def test_eval(expr_str, expected, fail_on_error=False, base_expr=None):
        if base_expr is None:
            base_expr = expr_str


# Generated at 2022-06-13 15:29:52.081346
# Unit test for function safe_eval

# Generated at 2022-06-13 15:30:00.109615
# Unit test for function safe_eval

# Generated at 2022-06-13 15:30:08.146120
# Unit test for function safe_eval
def test_safe_eval():

    # Test data and results.
    test_data = []
    # Note that this test_data will not actually be parsed, because
    # CleansingNodeVisitor will reject any ast node that is not
    # known to be safe
    test_data.append(('"test"', 'test'))
    test_data.append(('["test", "test2"]', ['test', 'test2']))
    test_data.append(('2+2', 4))
    test_data.append(('true', True))
    test_data.append(('false', False))
    test_data.append(('null', None))
    test_data.append(('true and false', False))
    test_data.append(('true or false', True))
    test_data.append(('true or false and true', True))
   

# Generated at 2022-06-13 15:30:18.561856
# Unit test for function safe_eval
def test_safe_eval():
    def _test_safe_eval(data, should_be_safe, should_raise=False):
        e = None

# Generated at 2022-06-13 15:30:26.681711
# Unit test for function safe_eval

# Generated at 2022-06-13 15:30:33.131603
# Unit test for function safe_eval
def test_safe_eval():
    assert 10 == safe_eval("08 * 2")
    assert 10 == safe_eval("8 * 2")
    assert 8 == safe_eval("8")
    assert False == safe_eval("false")
    assert None == safe_eval("null")
    assert True == safe_eval("true")
    assert 33 == safe_eval("'33'")
    assert 33 == safe_eval("True + '3'")
    assert [] == safe_eval("[]")
    assert [1, 2] == safe_eval("[1,2]")
    assert ('foo', 'bar') == safe_eval("('foo','bar')")
    assert {'foo': 'bar'} == safe_eval("{'foo':'bar'}")
    assert None == safe_eval("None")
    assert 5 == safe_eval("5")

# Generated at 2022-06-13 15:30:42.278725
# Unit test for function safe_eval
def test_safe_eval():
    # This test is only run if the module is called directly
    # To run this test, type:
    # python ansible/module_utils/common/text/__init__.py
    print()
    print('TESTING TEXT MODULE')
    print('==================')
    print()

    def test_eval(expression, expected_result):
        expression = expression.strip()
        # Call safe_eval with a string expression and check that it produces
        # the expected result.
        result = safe_eval(expression)
        print('string: %s' % expression)
        print('result: %s' % container_to_text(result))
        print()
        assert result == expected_result, \
            'safe_eval(%s) should be %s but is %s' % (expression, expected_result, result)
        # The

# Generated at 2022-06-13 15:30:48.362256
# Unit test for function safe_eval

# Generated at 2022-06-13 15:30:54.085868
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval('1 + 2') == 3
    assert safe_eval('1 + 2 * 3') == 7
    assert safe_eval('(1 + 2) * 3') == 9

    assert safe_eval("'foo'") == 'foo'
    assert safe_eval("'foo' + 'bar'") == 'foobar'

    assert safe_eval("['a', 'b']") == ['a', 'b']
    assert safe_eval("['a', 'b'] + ['c', 'd']") == ['a', 'b', 'c', 'd']

    assert safe_eval("{'a': 1, 'b': 2}") == {'a': 1, 'b': 2}
    assert safe_eval("dict(a=1, b=2)") == {'a': 1, 'b': 2}

    assert safe

# Generated at 2022-06-13 15:31:07.482809
# Unit test for function safe_eval
def test_safe_eval():
    safe_eval('[]')
    safe_eval('{"foo": "bar"}')
    safe_eval('{"foo": "bar", "blam": [1, 2, 3]}')
    safe_eval('bar')
    safe_eval('()')
    safe_eval('(1,)')
    safe_eval('(1,2)')
    safe_eval('(1,2,3)')
    safe_eval('"foo"')
    safe_eval('"foo" + "bar"')
    safe_eval('"foo" + bar')

    # Safe strings
    assert safe_eval("'foo bar'") == 'foo bar'
    assert safe_eval("'foo bar' + 'baz'") == 'foo barbaz'
    assert safe_eval("'foo' 'bar'") == 'foobar'

    #

# Generated at 2022-06-13 15:31:12.266610
# Unit test for function safe_eval
def test_safe_eval():
    tests = [
        # Addition
        '5 + 4',
        # Simple dictionary
        'dict(c=4, a=1)',
        # Nested dictionary
        'dict(a=1, b=dict(q=3, w=4))',
        # Dictionary with boolean
        'dict(a=1, b=True)',
        # List
        'list(range(4))',
        # String
        '"a string"',

        # Invalid expressions
        '5 *',
        '5 + a',
        'list(range(4)) + dict(a=1, b=2)',
        'len("123")',
    ]


# Generated at 2022-06-13 15:31:21.625676
# Unit test for function safe_eval
def test_safe_eval():
    """
    This test evaluates a list of expressions as strings and compares them
    to the expected result.
    If the test is successful, it prints "ok"
    If the test fails, it prints the expression and the expected result.
    If the test fails due to an exception, it prints the expression and the
    exception message.
    """

    # list of tests
    # each item is a tuple with three elements:
    # the input expression, the expected result, the expected type
    # (None if the input expression should raise an exception)

# Generated at 2022-06-13 15:31:31.756303
# Unit test for function safe_eval
def test_safe_eval():
    import ast
    import sys
    t_eval_doc = '''
    This is intended for allowing things like:
    with_items: a_list_variable

    Where Jinja2 would return a string but we do not want to allow it to
    call functions (outside of Jinja2, where the env is constrained).

    Based on:
    http://stackoverflow.com/questions/12523516/using-ast-and-whitelists-to-make-pythons-eval-safe
    '''
    t_expr = '''
    foo(a,b)
    '''
    t_result_ok = 'True'
    t_result_fail = 'False'

    t_test_result_ok, t_test_exception_ok = safe_eval(t_result_ok)
    t_test_

# Generated at 2022-06-13 15:31:38.123759
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval("stuff") == "stuff"
    assert safe_eval("{{ stuff }}") == "{{ stuff }}"
    assert safe_eval("{{ stuff.split('a')[0] }}") == "{{ stuff.split('a')[0] }}"
    assert safe_eval("stuff.split") == "stuff.split"
    assert not safe_eval("stuff.split('a')")
    assert not safe_eval("os.system('/bin/echo hi')")
    assert safe_eval("ansible") == "ansible"
    assert safe_eval("ansible_facts") == "ansible_facts"
    assert not safe_eval("ansible_facts.anything")
    assert not safe_eval("ansible_facts['os_family']")
    assert safe_eval("False") == False

# Generated at 2022-06-13 15:31:45.670708
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval('1') == 1
    assert safe_eval('5*5') == 25
    assert safe_eval('1000 + 1000') == 2000
    assert safe_eval('3**3') == 27
    assert safe_eval('(3**3) + (3**3)') == 54
    assert safe_eval('(False or True) and (False or True)') is True
    assert safe_eval('true') is True
    assert safe_eval('false') is False
    assert safe_eval('null') is None
    assert safe_eval('true and false') is False
    assert safe_eval('true and true') is True
    assert safe_eval('not true') is False
    assert safe_eval('not false') is True
    assert safe_eval('false or false') is False

# Generated at 2022-06-13 15:31:55.722769
# Unit test for function safe_eval
def test_safe_eval():
    import unittest
    import contextlib

    class TestSafeEval(unittest.TestCase):
        def setUp(self):
            self.record_stdout = False

        def tearDown(self):
            if self.record_stdout:
                sys.stdout.flush()
                sys.stdout = sys.__stdout__

        def test_safe_eval(self):
            self.assertEqual(safe_eval("'foo'"), 'foo')
            self.assertEqual(safe_eval("'foo' + 'bar'"), 'foobar')
            self.assertEqual(safe_eval("'foo' + 'bar' + 'baz'"), 'foobarbaz')
            self.assertEqual(safe_eval("'bar' * 4"), 'barbarbarbar')
            self.assertEqual

# Generated at 2022-06-13 15:32:01.698734
# Unit test for function safe_eval
def test_safe_eval():
    # test empty strings
    assert safe_eval("") is None
    assert safe_eval("", include_exceptions=True) == ("", None)

    # test an expression containing only literal types
    assert safe_eval("42") == 42
    assert safe_eval("42", include_exceptions=True) == (42, None)
    assert safe_eval("42.5") == 42.5
    assert safe_eval("42.5", include_exceptions=True) == (42.5, None)
    assert safe_eval("1 + 2 * 3") == 7
    assert safe_eval("1 + 2 * 3", include_exceptions=True) == (7, None)
    assert safe_eval("'hello'") == 'hello'
    assert safe_eval("'hello'", include_exceptions=True) == ('hello', None)

# Generated at 2022-06-13 15:32:06.997282
# Unit test for function safe_eval

# Generated at 2022-06-13 15:32:18.430092
# Unit test for function safe_eval
def test_safe_eval():
    # confirm that a string value is returned unmodified when used in an expression
    assert 'test' == safe_eval('test')

    # confirm that a string value is returned unmodified when used in a list
    assert ['test'] == safe_eval('[test]')

    # confirm that a string value is returned unmodified when used in a dictionary
    assert {'test': 'value'} == safe_eval('{test: value}')

    # confirm that multiple levels of lists and dictionaries can be used
    assert [[{'a': 'b'}, 'c']] == safe_eval("[[a: 'b'], 'c']")

    # confirm that basic math works
    assert 10 == safe_eval('2 * 5')

    # confirm that the addition of a simple function causes the entire expression to fail
    assert '10 + len("string")' == safe_

# Generated at 2022-06-13 15:32:35.193299
# Unit test for function safe_eval
def test_safe_eval():
    # test expected pass
    expr = 'a_list_variable'
    assert safe_eval(expr) == expr

    # test pass with nested list
    expr = 'a_list_variable[1]'
    assert safe_eval(expr) == expr

    # test pass with nested list
    expr = 'a_list_variable[1][1]'
    assert safe_eval(expr) == expr

    # test pass with nested list + string
    expr = 'a_list_variable[1][1] + "123"'
    assert safe_eval(expr) == expr

    # test pass with nested list + string
    expr = 'a_list_variable[1][1] + "123"'
    assert safe_eval(expr) == expr

    # test pass with nested list + string
    expr = 'a_list_variable | length > 1'


# Generated at 2022-06-13 15:32:43.939255
# Unit test for function safe_eval
def test_safe_eval():
    print("*** test_safe_eval ***")

# Generated at 2022-06-13 15:32:53.888757
# Unit test for function safe_eval
def test_safe_eval():

    '''
        test_safe_eval
        This test module checks that only allowed
        expressions are evaluated.
    '''

    # We will test whitelisted expressions
    whitelist_eval = ['1+1', 'True', 'True or False',
                      '1+2 == 3', '1+2 > 0',
                      '1+2 > 0 and 3+4 > 4',
                      '1 > 0 or 2 < 1', '[]', '()', '{}',
                      '1 > 0 or False', 'None',
                      'not False']

    for expression in whitelist_eval:
        assert(safe_eval(expression) == eval(expression))

    # We will test non-whitelisted expressions

# Generated at 2022-06-13 15:33:04.101632
# Unit test for function safe_eval

# Generated at 2022-06-13 15:33:15.497481
# Unit test for function safe_eval
def test_safe_eval():
    # Most basic eval test
    assert safe_eval('1 + 1') == 2

    # Test invalid expression
    try:
        safe_eval('1 + <')
    except Exception:
        pass
    else:
        assert False, 'Invalid expression should have thrown exception'

    # Test invalid call
    try:
        safe_eval('__import__("os").getcwd()')
    except Exception:
        pass
    else:
        assert False, 'Invalid call should have thrown exception'

    # Test an invalid call that is reported as being a Name node
    try:
        safe_eval('abs(-1)')
    except Exception:
        pass
    else:
        assert False, 'Invalid call should have thrown exception'

    # Test valid call, and passing in a variable

# Generated at 2022-06-13 15:33:26.543914
# Unit test for function safe_eval
def test_safe_eval():

    def assert_safe_eval_fails(expr):
        result, err = safe_eval(expr, include_exceptions=True)
        if err is None:
            raise AssertionError("Expected %s to fail but it succeed: %s" % (expr, result))
        assert isinstance(err, Exception)

    def assert_safe_eval_succeeds(expr, expected_result):
        result, err = safe_eval(expr, include_exceptions=True)
        if err is not None:
            raise AssertionError("Expected %s to succeed but it failed with exception %s" % (expr, err))
        if result != expected_result:
            raise AssertionError("Expected result of %s to be '%s' but got '%s'" % (expr, expected_result, result))


# Generated at 2022-06-13 15:33:33.382532
# Unit test for function safe_eval
def test_safe_eval():
    import random
    from ansible.module_utils.six.moves import cPickle as pickle

    try:
        import simplejson as json
    except ImportError:
        import json

    def _test_pickle():
        # not safe for general use, but useful for testing safe_eval
        try:
            pickled = pickle.dumps({'test': 'val'})
        except Exception as e:
            return e.__class__.__name__

    def _test_json():
        try:
            json.dumps({'test': 'val'})
        except Exception as e:
            return e.__class__.__name__

    def _test_func(function):
        try:
            function({'test': 'val'})
        except Exception as e:
            return e.__class__.__name

# Generated at 2022-06-13 15:33:44.305160
# Unit test for function safe_eval
def test_safe_eval():
    if sys.version_info >= (3, 0):
        assert 'unicode' not in safe_eval("__builtins__.keys()")
    else:
        assert 'unicode' in safe_eval("__builtins__.keys()")
    assert safe_eval("'foo'") == 'foo'
    assert safe_eval("foo") == 'foo'
    assert safe_eval("2.5") == 2.5
    assert safe_eval("2 < 1") == False
    assert safe_eval("1 < 2") == True
    assert safe_eval("1 + 2") == 3
    assert safe_eval("1 - 2") == -1
    assert safe_eval("1 * 2") == 2
    assert safe_eval("1 / 2") == 0.5
    assert safe_eval("1.0 / 2") == 0.5

# Generated at 2022-06-13 15:33:55.517035
# Unit test for function safe_eval

# Generated at 2022-06-13 15:34:06.023250
# Unit test for function safe_eval
def test_safe_eval():
    # No calls to __import__
    assert(safe_eval("[]") == [])
    assert(safe_eval("{}") == {})
    assert(safe_eval("type(locals())") == dict)
    assert(safe_eval("type(globals())") == dict)
    assert(safe_eval("' '.join(['hello', 'world'])") == 'hello world')
    assert(safe_eval("{'a': 'b'}") == {'a': 'b'})
    assert(safe_eval("['a', 'b']") == ['a', 'b'])
    assert(safe_eval("{'a': 'b'}['a']") == 'b')
    assert(safe_eval("['a', 'b'][1]") == 'b')
    # Only safe math operations
   

# Generated at 2022-06-13 15:34:25.433198
# Unit test for function safe_eval
def test_safe_eval():
    from ansible.module_utils.common.text.converters import string_to_bytes
    from ansible.module_utils.common.text.converters import to_bytes
    from ansible.module_utils.common.text.converters import to_unicode
    from ansible.module_utils.common.text.converters import to_text
    from ansible.module_utils.common.text.converters import to_list
    from ansible.module_utils.common.text.converters import to_naive_datetime
    from ansible.module_utils.common.text.converters import to_datetime
    from ansible.module_utils.six import integer_types
    from ansible.module_utils.six import string_types
    import six
    import datetime
    import time
   

# Generated at 2022-06-13 15:34:32.631104
# Unit test for function safe_eval

# Generated at 2022-06-13 15:34:42.283962
# Unit test for function safe_eval
def test_safe_eval():
    try:
        from ansible.plugins.loader import module_loader
        my_vars = module_loader.module_vars_cache.get('debug', [{}, {}, {}])[0]
    except:
        my_vars = {}

# Generated at 2022-06-13 15:34:45.450902
# Unit test for function safe_eval
def test_safe_eval():
    expr = b"{{ '1' if 1 else '0' }}"
    ret = safe_eval(expr)
    assert ret == '1', "safe_eval did not produce exspected result"



# Generated at 2022-06-13 15:34:52.872910
# Unit test for function safe_eval
def test_safe_eval():
    from ansible.playbook.conditional import Conditional

    # assert conditional_eval works
    assert Conditional('1 == 1').evaluate_conditional()

    # assert jinja2 is not allowed
    assert safe_eval('{{ 1 + 1 }}') == '{{ 1 + 1 }}'

    # assert we can safely eval 1 + 1
    # assert isinstance(safe_eval('1 + 1'), int)
    # assert safe_eval('1 + 1') == 2

    # assert we can safely eval 1 + foo where foo equals 1
    # assert isinstance(safe_eval('1 + foo', locals={'foo': 1}), int)
    # assert safe_eval('1 + foo', locals={'foo': 1}) == 2

    # assert we can safely eval a list comprehension
    # should_be = [1, 2, 3, 4, 5

# Generated at 2022-06-13 15:35:02.634367
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval('1 + 2') == 3
    assert safe_eval('1 + 2', dict(a=1)) == 3
    assert safe_eval('1 + a', dict(a=2)) == 3
    assert safe_eval('1 + a', dict(a=2)) == 3
    assert safe_eval('dict') == dict
    assert safe_eval('[1,2,3]')[1] == 2
    assert safe_eval('[1,2,3]')[1] == 2
    assert safe_eval('{"a":"b"}')['a'] == 'b'
    assert safe_eval('{"a":"b"}')['a'] == 'b'
    assert safe_eval('"foo" + str(1)') == 'foo1'

# Generated at 2022-06-13 15:35:11.860944
# Unit test for function safe_eval
def test_safe_eval():
    from ansible.module_utils.six.moves.builtins import int, str
    from ansible.module_utils.common.text.converters import to_text

    def _test_eval(expr):
        if sys.version_info[0] >= 3:
            assert safe_eval(expr) == eval(expr), expr
        else:
            assert safe_eval(expr, include_exceptions=True) == (eval(expr), None), expr

    assert safe_eval("True") is True
    assert safe_eval("False") is False
    assert safe_eval("None") is None
    assert safe_eval("1") == 1
    assert safe_eval("1.1") == 1.1
    assert safe_eval("'1'") == '1'

# Generated at 2022-06-13 15:35:20.704600
# Unit test for function safe_eval
def test_safe_eval():
    from ansible.module_utils._text import to_text


# Generated at 2022-06-13 15:35:30.374340
# Unit test for function safe_eval

# Generated at 2022-06-13 15:35:38.790681
# Unit test for function safe_eval

# Generated at 2022-06-13 15:36:06.440361
# Unit test for function safe_eval
def test_safe_eval():
    (success_count, failure_count) = (0, 0)

    # Test values
    test_values = [
        ('6 * 7', 42),
        ('[22, 43]', [22, 43]),
        ('"hello"', 'hello'),
        ('true', True),
        ('null', None),
        ('{"foo": 12}', {"foo": 12}),
    ]

    # Test failures
    test_failures = [
        'abs(5)',
        '[5,6,7] + [5,6,7]',
        'str(5.2, 5.2)',
        '{} + {}',
        'foo',
    ]

    # Run the test

# Generated at 2022-06-13 15:36:14.482195
# Unit test for function safe_eval
def test_safe_eval():
    # Test valid expressions
    assert safe_eval('1') == 1
    assert safe_eval('1+1') == 2
    assert safe_eval('1+2*3') == 7
    assert safe_eval('1+2*3-4') == 3
    assert safe_eval('1 + 2*(3 - 4)') == -3
    assert safe_eval('8/4') == 2
    assert safe_eval('True') is True
    assert safe_eval('False') is False
    assert safe_eval('true') is True
    assert safe_eval('false') is False
    assert safe_eval('null') is None
    assert safe_eval('"abc"') == 'abc'
    assert safe_eval("'abc'") == 'abc'
    assert safe_eval("'a''b'") == "a'b"


# Generated at 2022-06-13 15:36:23.603038
# Unit test for function safe_eval
def test_safe_eval():
    """
    Tests for safe_eval
    """

    # Test basic usage
    assert safe_eval("[1, 2]") == [1, 2]
    assert safe_eval("'hello world'") == 'hello world'
    assert safe_eval("'hello world' + '!'") == 'hello world!'
    assert safe_eval("'hello' + ' ' + 'world!'") == 'hello world!'
    assert safe_eval("'hello world'[0]") == 'h'
    assert safe_eval("'hello world'[1:3]") == 'el'
    assert safe_eval("'hello world'[1:-1]") == 'ello worl'
    assert safe_eval("'hello world'[2:-2]") == 'llo wor'

# Generated at 2022-06-13 15:36:30.735905
# Unit test for function safe_eval
def test_safe_eval():
    # edge case, literal booleans are allowed
    assert safe_eval('True') == True
    assert safe_eval('False') == False

    # edge case, 'none' is a python None
    assert safe_eval('None') == None

    # edge case, 'none' is also JSON none
    assert safe_eval('null') == None

    # edge case, 'none' is also JSON false
    assert safe_eval('false') == False

    # this is a python dict literal
    result = safe_eval('{ "foo" : "bar" }')
    assert result == { "foo": "bar" }

    # this is a python dict of dicts
    result = safe_eval('{ "foo" : { "bar" : "baz" } }')

# Generated at 2022-06-13 15:36:41.765432
# Unit test for function safe_eval
def test_safe_eval():
    # Test safe eval with different expressions
    assert safe_eval('[]')      == []
    assert safe_eval('"hello"') == "hello"
    assert safe_eval('[1, 2, 3]') == [1, 2, 3]
    assert safe_eval('{"k1": "v1", "k2": "v2"}') == {"k1": "v1", "k2": "v2"}
    assert safe_eval('1 + 2') == 3
    assert safe_eval('1 - 2') == -1
    assert safe_eval('2 * 3') == 6
    assert safe_eval('4 / 2') == 2
    assert safe_eval('2 ** 8') == 256
    assert safe_eval('"ansible" * 3  + "rocks"') == "ansibleansibleansiblerocks"

# Generated at 2022-06-13 15:36:53.140112
# Unit test for function safe_eval

# Generated at 2022-06-13 15:37:02.096899
# Unit test for function safe_eval

# Generated at 2022-06-13 15:37:11.502739
# Unit test for function safe_eval
def test_safe_eval():
    module = AnsibleModule(argument_spec={})

    def check_safe_eval(s):
        r, e = safe_eval(s, include_exceptions=True)
        module.assertEqual(r, eval(s, {}, {}))
        return r, e

    # Basic types
    module.assertEqual(check_safe_eval(u"1"), (1, None))
    module.assertEqual(check_safe_eval(u"1.1"), (1.1, None))
    module.assertEqual(check_safe_eval(u"'string'"), (u'string', None))
    module.assertEqual(check_safe_eval(u"False"), (False, None))
    module.assertEqual(check_safe_eval(u"True"), (True, None))

# Generated at 2022-06-13 15:37:21.089533
# Unit test for function safe_eval
def test_safe_eval():
    # Some test examples
    evaldict = {
        'a': 1,
        'b': 2,
    }
    assert safe_eval('1 in [1,2,3]', evaldict) == True, 'Test 1 failed'
    assert safe_eval('a<b', evaldict) == True, 'Test 2 failed'
    assert safe_eval('a*(b+1)', evaldict) == 3, 'Test 3 failed'
    assert safe_eval('len(str(a*b))', evaldict) == 1, 'Test 4 failed'
    assert safe_eval('{}', evaldict) == {}, 'Test 5 failed'
    assert safe_eval('[]', evaldict) == [], 'Test 6 failed'

# Generated at 2022-06-13 15:37:32.797774
# Unit test for function safe_eval
def test_safe_eval():
    # Test that simple expressions are allowed.
    assert safe_eval("True")
    assert safe_eval("False")
    assert safe_eval("1 + 1 * 3 / 4")
    assert safe_eval("1 + 1 * (3 / 4)")
    assert safe_eval("True or False")
    assert safe_eval("True and False")

    # Test that constants and variable lookup are allowed.
    assert safe_eval("True == True")
    assert safe_eval("False == False")
    assert safe_eval("False != True")
    assert safe_eval("1 != 2")
    assert safe_eval("1 < 2")
    assert safe_eval("1 <= 2")
    assert safe_eval("1 <= 2")
    assert safe_eval("1 > 2")
    assert safe_eval("1 >= 2")