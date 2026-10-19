

# Generated at 2022-06-13 15:28:10.347581
# Unit test for function safe_eval
def test_safe_eval():
    # No exception raised
    assert safe_eval("3*3") == 9

    # Make sure builtins are not allowed (should raise exception)
    assert safe_eval("__import__('os').getcwd()") == "__import__('os').getcwd()"

    # Make sure we allow safe functions to be called
    assert safe_eval("hash(3)") == hash(3)

    # Make sure invalid constants are not allowed (should raise exception)
    assert safe_eval("0x0fff") == "0x0fff"

    # Make sure invalid expression raises an exception
    assert safe_eval(":") == ":"
    assert safe_eval("for a in b: pass") == "for a in b: pass"
    assert safe_eval("with a as b: pass") == "with a as b: pass"

    # Make

# Generated at 2022-06-13 15:28:15.007100
# Unit test for function safe_eval

# Generated at 2022-06-13 15:28:23.390834
# Unit test for function safe_eval
def test_safe_eval():

    assert safe_eval('""') == ''
    assert safe_eval('42') == 42
    assert safe_eval('42.0') == 42.0
    assert safe_eval('true') == True
    assert safe_eval('false') == False
    assert safe_eval('null') == None
    assert safe_eval('[]') == []
    assert safe_eval('a_list_variable') == 'a_list_variable'
    assert safe_eval('[1,2,3]') == [1, 2, 3]
    assert safe_eval('[1,2,a_list_variable]') == [1, 2, 'a_list_variable']
    assert safe_eval('{"a": "b"}') == {'a': 'b'}

# Generated at 2022-06-13 15:28:33.428631
# Unit test for function safe_eval
def test_safe_eval():
    print('Testing safe_eval...')
    failed = 0

# Generated at 2022-06-13 15:28:43.232328
# Unit test for function safe_eval
def test_safe_eval():
    if not sys.version_info[:2] >= (2, 6):
        raise Exception("python 2.6+ required")
    assert safe_eval("a", {"a": 1}) == 1
    assert safe_eval("a.keys()", {"a": {"b": 1}}) == ['b']
    assert safe_eval("a", {"a": 1}) == 1
    assert safe_eval("a", {"a": 1, "b": 2}) == 1
    assert safe_eval("a + b", {"a": 1, "b": 2}) == 3
    assert safe_eval("dict(a=1, b=2)", {"a": 1, "b": 2}) == {'a': 1, 'b': 2}

# Generated at 2022-06-13 15:28:51.697069
# Unit test for function safe_eval
def test_safe_eval():
    # Evaluating a string is safe, since there are no eval calls.
    assert safe_eval("'abc'") == 'abc'

    # Evaluating a number is safe, since there are no eval calls.
    assert safe_eval("123") == 123

    # Evaluating a boolean is safe, since there are no eval calls.
    assert safe_eval("true") == True

    # Evaluating a dictionary is safe, since there are no eval calls.
    assert safe_eval("{'a': 'b'}") == {'a': 'b'}

    # Evaluating a list is safe, since there are no eval calls.
    assert safe_eval("['a', 'b']") == ['a', 'b']

    # Evaluating a set is safe, since there are no eval calls.

# Generated at 2022-06-13 15:28:57.884734
# Unit test for function safe_eval
def test_safe_eval():
    ret = safe_eval("[]")
    assert ret == [], "%s is not []" % ret

    # ret = safe_eval("[x for x in range(5) if x in range(10)]")
    # assert ret == [0, 1, 2, 3, 4], "%s is not [0, 1, 2, 3, 4]" % ret

    # ret = safe_eval("[x for x in range(5) if x in range(10)]")
    # assert ret == [0, 1, 2, 3, 4], "%s is not [0, 1, 2, 3, 4]" % ret

    ret = safe_eval("some_func(3)")
    assert ret == "some_func(3)", "%s is not 'some_func(3)'" % ret

    ret = safe_eval("x+2")
   

# Generated at 2022-06-13 15:29:07.623518
# Unit test for function safe_eval
def test_safe_eval():

    # Empty string
    assert safe_eval("") == ""

    # Constant literals
    assert safe_eval("2") == 2
    assert safe_eval("2.1") == 2.1
    assert safe_eval("'foo'") == "foo"
    assert safe_eval("True") == True
    assert safe_eval("[1,2,3]") == [1, 2, 3]
    assert safe_eval("{'a': 1, 'b': 2}") == {'a': 1, 'b': 2}
    assert safe_eval("(1,2,3,4)") == (1, 2, 3, 4)
    assert safe_eval("-1") == -1
    assert safe_eval("-2.1") == -2.1

    # Named literals

# Generated at 2022-06-13 15:29:09.268673
# Unit test for function safe_eval
def test_safe_eval():
    '''
    see the testcases in lib/ansible/module_utils/facts/system/__init__.py
    '''
    pass

# Generated at 2022-06-13 15:29:18.743620
# Unit test for function safe_eval
def test_safe_eval():
    '''
    Unit test for function safe_eval
    '''
    # Note, you will need to uncomment the following line in order to run this
    # self-test, as the function is only defined when the setting is enabled
    # in the config file.
    # from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    # Add some callables to the whitelist and re-load the module so that
    # the settings are reset.  This is necessary because this unit test
    # may be run more than once when run as part of the main test suite.
    C.DEFAULT_CALLABLE_WHITELIST.append('to_native')
    C.DEFAULT_CALLABLE_WHITELIST.append('container_to_text')
    if C.CALLABLE_WHITELIST is None:
        C

# Generated at 2022-06-13 15:29:25.738471
# Unit test for function safe_eval
def test_safe_eval():
    # Test valid expression
    assert safe_eval('2') == 2
    # Test invalid expression
    assert safe_eval('2+') == '2+'


# Generated at 2022-06-13 15:29:34.683613
# Unit test for function safe_eval

# Generated at 2022-06-13 15:29:40.367192
# Unit test for function safe_eval
def test_safe_eval():
    # Make sure simple evaluation works
    result, exception = safe_eval('[1, 2, 3, 4]', include_exceptions=True)
    assert result == [1, 2, 3, 4] and exception is None

    # Make sure simple evaluation returns exception
    result, exception = safe_eval('[1, 2, 3, 4, invalid_func(4)]', include_exceptions=True)
    assert result == '[1, 2, 3, 4, invalid_func(4)]' and exception is not None

    # Make sure simple evaluation returns exception, with no function
    # call enabled
    result, exception = safe_eval('foo', include_exceptions=True)
    assert result == 'foo' and exception is not None

    # Make sure simple evaluation works, with lowercase

# Generated at 2022-06-13 15:29:51.694511
# Unit test for function safe_eval
def test_safe_eval():
    C.DEFAULT_DEBUG = True

    # Tests for list, dict and string
    assert safe_eval('[1, 2, 3, 4]') == [1, 2, 3, 4]
    assert safe_eval('[1, 2, 3, 4,]') == [1, 2, 3, 4,]
    assert safe_eval('{"a": 1, "b": 2 }') == {"a": 1, "b": 2 }
    assert safe_eval('{ "a": 1, "b": 2,}') == {"a": 1, "b": 2,}
    assert safe_eval('{"a": 1, "b": 2,}') == {"a": 1, "b": 2,}
    assert safe_eval('{"a": 1, "b": 2 }') == {"a": 1, "b": 2 }

# Generated at 2022-06-13 15:29:59.905997
# Unit test for function safe_eval

# Generated at 2022-06-13 15:30:05.855772
# Unit test for function safe_eval
def test_safe_eval():
    """
    Test safe_eval function
    """
    # Constants
    expr = 'some string'
    locals = {'some_var': 'some value'}

    # Setup mock ansible context
    ansible_context = {'ANSIBLE_CONFIG': None}
    ansible_context['ANSIBLE_CONFIG'] = C.DEFAULT_CONFIG_FILE
    C.config = C.load_config_file()

    # Test safe_eval eval
    assert expr == safe_eval(expr, locals=locals)



# Generated at 2022-06-13 15:30:10.988685
# Unit test for function safe_eval

# Generated at 2022-06-13 15:30:21.296248
# Unit test for function safe_eval
def test_safe_eval():
    # Test that constants are eval'd correctly
    assert safe_eval('null') is None
    assert safe_eval('true') is True
    assert safe_eval('false') is False

    # Test that standard operators are eval'd correctly
    assert safe_eval('5+5') == 10
    assert safe_eval('5-5') == 0
    assert safe_eval('5*5') == 25
    assert safe_eval('5**5') == 3125
    assert safe_eval('5/5') == 1
    assert safe_eval('5//5') == 1
    assert safe_eval('5%5') == 0

    # Test that tuples, lists and dicts are eval'd correctly
    assert safe_eval('("foo", "bar")') == ('foo', 'bar')
    assert safe_eval('("foo")') == ('foo',)


# Generated at 2022-06-13 15:30:29.188203
# Unit test for function safe_eval
def test_safe_eval():
    def assertRaises(expr, exception):
        #expr = str(expr)
        _expr = safe_eval(expr, include_exceptions=True)
        if isinstance(_expr, tuple):
            if not isinstance(_expr[1], exception):
                print("%s, expr=%s" % (_expr[1], expr))
                sys.exit(1)
    def assertWritable(expr, value):
        #expr = str(expr)
        _expr = safe_eval(expr, include_exceptions=True)
        if isinstance(_expr, tuple):
            if not isinstance(_expr[1], Exception):
                print("%s, expr=%s" % (_expr[1], expr))
                sys.exit(1)

# Generated at 2022-06-13 15:30:37.985373
# Unit test for function safe_eval
def test_safe_eval():
    '''Test cases for the safe_eval function'''

    def _test(expr, expected):
        test_expr = expr.replace('{', '{{').replace('}', '}}')
        compiled = safe_eval(test_expr)
        print("Test: %s" % test_expr)
        if isinstance(expected, Exception):
            assert isinstance(compiled, (string_types, Exception))
        else:
            try:
                assert(compiled == expected)
            except AssertionError:
                print(compiled)
                print(type(compiled))
                print(expected)
                print(type(expected))
                raise

    def _test_ex(expr, expected):
        test_expr = expr.replace('{', '{{').replace('}', '}}')

# Generated at 2022-06-13 15:30:52.593389
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval("[ 1, 2, 3 ]") == [1, 2, 3]
    assert safe_eval("[ 1, 2, 3, 4]") == [1, 2, 3, 4]
    assert safe_eval("[ 1, 2, 3,   4]") == [1, 2, 3, 4]
    assert safe_eval("[1, 2, 3]") == [1, 2, 3]
    assert safe_eval("[1, 2, 3, 4]") == [1, 2, 3, 4]
    assert safe_eval("[1, 2, 3,   4]") == [1, 2, 3, 4]
    assert safe_eval("[1, 2, 3, %(a)s]" % {'a': '4'}) == [1, 2, 3, 4]
    assert safe_

# Generated at 2022-06-13 15:30:57.175840
# Unit test for function safe_eval
def test_safe_eval():
    my_dict = {'a':1, 'b':2}
    my_tuple = (1,2,3)
    my_list = [1,2,3,4,'a','b','c',{'d':1,'e':2}]
    my_set = {1,2,3}
    my_bool = True
    my_none = None
    safe_expr = 'True'
    unsafe_expr = 'import os'
    assert safe_eval(safe_expr) == True
    assert safe_eval(safe_expr, include_exceptions=True) == (True, None)
    assert safe_eval(unsafe_expr) == unsafe_expr
    assert safe_eval(unsafe_expr, include_exceptions=True) == (unsafe_expr, None)

# Generated at 2022-06-13 15:31:08.027887
# Unit test for function safe_eval
def test_safe_eval():

    def _assert_safe_eval(result, test_input):
        if not isinstance(test_input, tuple):
            test_input = (test_input,)
        for expr in test_input:
            assert result == safe_eval(expr)
    # Should work
    _assert_safe_eval(10, '10')
    _assert_safe_eval(0, ['0'])
    _assert_safe_eval(0.0, ['0.0'])
    _assert_safe_eval({'a': 'b'}, "{'a':'b'}")
    _assert_safe_eval({'a': 'b', 'c': 'd'}, "{'a':'b', 'c':'d'}")
    _assert_safe_eval(['a', 'b'], "['a', 'b']")


# Generated at 2022-06-13 15:31:12.822943
# Unit test for function safe_eval

# Generated at 2022-06-13 15:31:23.153149
# Unit test for function safe_eval
def test_safe_eval():
    global CALL_ENABLED
    CALL_ENABLED = ['set', 'map', 'list']


# Generated at 2022-06-13 15:31:32.564491
# Unit test for function safe_eval
def test_safe_eval():  # pylint: disable=unused-argument
    '''
    Function ``safe_eval`` unit tests. Note that this is a named function
    (rather than a lambda) so that pylint can properly find its docstring.

    Also, because of the way the 'eval' function works, there is no way to
    convince pylint that this function is safe, so we disable the pylint
    'dangerous-default-value' check as well as the 'missing-docstring' check.
    '''
    if sys.version_info[0] >= 3:
        raise AssertionError("Python3 is not supported by this script")


# Generated at 2022-06-13 15:31:38.969206
# Unit test for function safe_eval

# Generated at 2022-06-13 15:31:43.912691
# Unit test for function safe_eval
def test_safe_eval():
    # Test a simple expression
    assert safe_eval("1 + 1") == 2
    # Test that the boolean false is not treated as the string "false"
    assert safe_eval("false") == False
    assert safe_eval("false", include_exceptions=True) == (False, None)
    # Test that the boolean true is not treated as the string "true"
    assert safe_eval("true") == True
    assert safe_eval("true", include_exceptions=True) == (True, None)
    # Test that the JSON null is not treated as the string "null"
    assert safe_eval("null") == None
    assert safe_eval("null", include_exceptions=True) == (None, None)
    # Test complex expression
    assert safe_eval("(a + 1) * 2") == 4
    # Test dictionary syntax


# Generated at 2022-06-13 15:31:54.652994
# Unit test for function safe_eval
def test_safe_eval():
    '''
    This is used by the test harness to perform some basic sanity checks
    on the functions provided.
    '''
    # Just some simple eval tests for now.  Will add more as needed.
    assert safe_eval("'foo'") == 'foo'
    assert safe_eval("'foo' + 'bar'") == 'foobar'
    assert safe_eval("1+1") == 2
    assert safe_eval("5-7") == -2
    assert safe_eval("'foo' * 3") == 'foofoofoo'
    assert safe_eval("[1,2,3]") == [1, 2, 3]
    assert safe_eval("{'foo': 'bar'}") == {'foo': 'bar'}

# Generated at 2022-06-13 15:32:01.037551
# Unit test for function safe_eval
def test_safe_eval():
    # this would fail if called directly
    # because many of the below are not valid code
    # but they are valid JSON/YAML so this is useful
    # to test in the context of our JSON/YAML parsing.
    try:
        from unittest.mock import patch
    except ImportError:
        from mock import patch

# Generated at 2022-06-13 15:32:19.213637
# Unit test for function safe_eval
def test_safe_eval():
    if sys.version_info >= (3, 0):
        print("Unable to test on python 3, which does not support 'exec' statement")
        return True

    def test_ex(expr, expected, locals_dict=None):
        result, err = safe_eval(expr, include_exceptions=True, locals=locals_dict)
        if err is not None:
            print("failed to evaluate expression: %s : %s" % (expr, err))

        if type(result) != type(expected):
            result = container_to_text(result)

        if result != expected:
            print("ERROR: failed to evaluate %s, expected %s, got %s" % (expr, expected, result))

    if C.DEFAULT_DEBUG:
        test_ex('{{success}}', 'OK')

# Generated at 2022-06-13 15:32:31.408579
# Unit test for function safe_eval

# Generated at 2022-06-13 15:32:41.230435
# Unit test for function safe_eval
def test_safe_eval():
    def _test_expr(expr, expected_result):
        result, exception = safe_eval(expr, {}, include_exceptions=True)
        if exception is not None:
            sys.exit("Unable to test %s due to %s" % (expr, exception))
        assert result == expected_result

    _test_expr('foo', 'foo')
    _test_expr('foo.bar', 'foo.bar')
    _test_expr('foo().bar', 'foo().bar')
    _test_expr('foo{}.bar', 'foo{}.bar')
    _test_expr('(foo).bar', '(foo).bar')
    _test_expr('foo(bar)', 'foo(bar)')
    _test_expr('foo(bar=1)', 'foo(bar=1)')

# Generated at 2022-06-13 15:32:51.753047
# Unit test for function safe_eval

# Generated at 2022-06-13 15:33:02.588904
# Unit test for function safe_eval
def test_safe_eval():
    # Test empty string, should return an empty string
    assert safe_eval('') == ''
    # Test a single variable
    assert safe_eval('a') == 'a'
    # Test a dict with values, should return an empty dict
    assert safe_eval({}) == {}
    # Test a dict with string as keys, should return an empty dict
    assert safe_eval({'a': 'b'}) == {}
    # Test a dict with None as keys
    assert safe_eval({None: None}) == {None: None}
    # Test a dict with string and None as keys, should return an empty dict
    assert safe_eval({'a': None}) == {}
    # Test a dict with string and None as keys, should return an empty dict
    assert safe_eval({None: 'a'}) == {}
    # Test a dict with string and

# Generated at 2022-06-13 15:33:13.176663
# Unit test for function safe_eval
def test_safe_eval():
    # Test if the type and the value of the expression is returned
    assert safe_eval('test_expression') == 'test_expression'
    assert safe_eval('True') == True
    assert safe_eval('1+1') == 2
    assert safe_eval('[1,2,3]') == [1, 2, 3]
    assert safe_eval('{"a":1}') == {'a': 1}
    assert safe_eval('(1,2)') == (1, 2)
    # Test for the exception
    assert safe_eval('__import__("os").getcwd()') == '__import__("os").getcwd()'
    assert safe_eval('(1,2)') == (1, 2)



# Generated at 2022-06-13 15:33:17.456926
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval("[1,2,3]") == [1,2,3]
    assert safe_eval("{'a':1,'b':'foo', 'c':false, 'd':null, 'e':True}") == {'a':1,'b':'foo', 'c':False, 'd':None, 'e':True}
    assert safe_eval("{'a':true}") == {'a':True}
    assert safe_eval("({'key1':'a', 'key2':'b'})") == {'key1': 'a', 'key2': 'b'}

    # basic arithmetic operations
    assert safe_eval("2 + 3") == 5
    assert safe_eval("8 * 9") == 72
    assert safe_eval("6 - 2") == 4

# Generated at 2022-06-13 15:33:27.734599
# Unit test for function safe_eval
def test_safe_eval():
    # test basic eval
    assert safe_eval('1 + 2') == 3
    assert safe_eval('foo') == 'foo'

    # test basic eval with multiple statements (which should be invalid)
    assert safe_eval('1; 2') == '1; 2'
    assert safe_eval('foo; bar') == 'foo; bar'

    # test simple calls
    assert safe_eval('True') == True
    assert safe_eval('False') == False
    assert safe_eval('None') == None
    assert safe_eval('null') == None

    assert safe_eval('foo is not None') == 'foo is not None'
    assert safe_eval('foo is not None and bar') == 'foo is not None and bar'
    assert safe_eval('foo is not None and bar') == 'foo is not None and bar'
    assert safe

# Generated at 2022-06-13 15:33:38.911155
# Unit test for function safe_eval
def test_safe_eval():
    '''
    Test function safe_eval
    '''


# Generated at 2022-06-13 15:33:44.955180
# Unit test for function safe_eval
def test_safe_eval():

    # Test successful evals
    assert safe_eval('1 + 2') == 3
    assert safe_eval('1 + 2 + foo', dict(foo=3)) == 6
    assert safe_eval('"1 " + "2"') == "1 2"
    assert safe_eval('[1, 2, 3]') == [1, 2, 3]
    assert safe_eval('{"a":1, "b":2}') == {"a":1, "b":2}
    assert safe_eval('{"a":1, "b":[1, 2]}') == {"a":1, "b":[1, 2]}

    # Test unsuccessful evals
    assert safe_eval('1 + 2', include_exceptions=True) == (3, None)

# Generated at 2022-06-13 15:34:01.858145
# Unit test for function safe_eval

# Generated at 2022-06-13 15:34:08.206077
# Unit test for function safe_eval

# Generated at 2022-06-13 15:34:17.666536
# Unit test for function safe_eval
def test_safe_eval():
    # Test strings
    assert safe_eval("True") is True
    assert safe_eval("False") is False
    assert safe_eval("42") == 42

    # Test dicts
    assert safe_eval("{}") == {}
    assert safe_eval("{'a': 1, 'b': 'b'}") == {'a': 1, 'b': 'b'}
    assert safe_eval("{'a': [{'c': '1'}]}") == {'a': [{'c': '1'}]}

    # Test lists
    assert safe_eval("[]") == []
    assert safe_eval("[1, 2, 'a']") == [1, 2, 'a']

# Generated at 2022-06-13 15:34:27.167833
# Unit test for function safe_eval
def test_safe_eval():
    import pytest

    # Test that we can evaluate any valid python expression.
    # That is not a statement.
    def test_eval_expr(expr):
        safe_expr = safe_eval(expr)
        assert expr == safe_expr
        with pytest.raises(Exception):
            safe_eval(expr + '\nfoo()')

    test_eval_expr('(True and False) or (True and True)')
    test_eval_expr('1 + 2 * 3 - 4')
    test_eval_expr('[x for x in (1,2,3)]')
    test_eval_expr('[0] + [1,2]')
    test_eval_expr('(1,2) + (3,4)')
    test_eval_expr('[0,1] + (2,3)')
   

# Generated at 2022-06-13 15:34:35.597205
# Unit test for function safe_eval
def test_safe_eval():
    if __name__ == '__main__':
        test_string = "{{ 1 + true }}"
        result = safe_eval(test_string)
        assert result == 2, "'%s' evaluated to %s" % (test_string, result)

        test_string = "{{ 1 + false }}"
        result = safe_eval(test_string)
        assert result == 1, "'%s' evaluated to %s" % (test_string, result)

        test_string = "{{ 1 +     null     }}"
        result = safe_eval(test_string)
        assert result == 1, "'%s' evaluated to %s" % (test_string, result)

        test_string = "{{ 1 +       }}"
        result = safe_eval(test_string)
        print(result)

# Generated at 2022-06-13 15:34:43.947803
# Unit test for function safe_eval
def test_safe_eval():
    # basic math
    assert safe_eval('1 + 2 + 3') == 6

    # dicts
    assert safe_eval('{"a": 1}') == {u'a': 1}

    # lists
    assert safe_eval('[1,2,3]') == [1, 2, 3]

    # variable replacement
    assert safe_eval('foo', dict(foo=42)) == 42

    # disallowed functions
    assert safe_eval('dir()') == 'dir()'

    # unallowed AST node type
    assert safe_eval('__import__("os").system("rm -rf")') == '__import__("os").system("rm -rf")'

    # json types
    assert safe_eval("true") is True
    assert safe_eval("false") is False


# Generated at 2022-06-13 15:34:51.947230
# Unit test for function safe_eval
def test_safe_eval():
    def fake_builtin(param):
        return param.upper()

    import __builtin__
    b_name = 'fake_builtin'
    if not hasattr(__builtin__, b_name):
        setattr(builtins, b_name, fake_builtin)

    if not hasattr(__builtin__, b_name):
        sys.stderr.write('%s: internal error, unable to override builtins' % __name__)
        sys.exit(1)

    CALL_ENABLED.append(b_name)


# Generated at 2022-06-13 15:35:01.910696
# Unit test for function safe_eval
def test_safe_eval():

    # Simple arithmetic expressions
    assert safe_eval('1') == 1
    assert safe_eval('1 + 2') == 3
    assert safe_eval('3 - 1') == 2
    assert safe_eval('4 * 2') == 8
    assert safe_eval('10 / 5') == 2

    # Boolean values
    assert safe_eval('true') is True
    assert safe_eval('false') is False

    # Boolean logic
    assert safe_eval('false and false') is False
    assert safe_eval('true and false') is False
    assert safe_eval('false and true') is False
    assert safe_eval('true and true') is True
    assert safe_eval('false or false') is False
    assert safe_eval('true or false') is True
    assert safe_eval('false or true') is True

# Generated at 2022-06-13 15:35:09.749271
# Unit test for function safe_eval
def test_safe_eval():
    def check_eval(expr, **kwargs):
        ret = safe_eval(expr, **kwargs)
        if C.DEFAULT_DEBUG:
            print('Eval<%s>=%s' % (expr, ret))
        assert ret
        return ret

    # constants
    assert check_eval('true') is True
    assert check_eval('false') is False
    assert check_eval('null') is None

    # numeric arithmetic
    assert check_eval('3') == 3
    assert check_eval('3+3') == 6
    assert check_eval('3+3+3') == 9
    assert check_eval('3*3') == 9
    assert check_eval('6/3') == 2
    assert check_eval('1.5+2.5') == 4.0

    # string concat

# Generated at 2022-06-13 15:35:19.131223
# Unit test for function safe_eval

# Generated at 2022-06-13 15:35:40.633412
# Unit test for function safe_eval
def test_safe_eval():
    safe_eval_result = safe_eval("1 + 2")
    assert safe_eval_result == 3
    try:
        assert safe_eval("__import__('sys').exit()")
        assert False
    except Exception as e:
        assert str(e) == "invalid expression (__import__('sys').exit())"
    assert safe_eval("obj_local", dict(obj_local=dict(a=1, b=2))) == dict(a=1, b=2)
    assert safe_eval("obj_local.foo", dict(obj_local=dict(a=1, b=2))) == "obj_local.foo"
    assert safe_eval("obj_local.a", dict(obj_local=dict(a=1, b=2))) == 1

# Generated at 2022-06-13 15:35:50.863265
# Unit test for function safe_eval
def test_safe_eval():
    '''
    Unit test of function safe_eval
    '''
    # Simple test to see if it works at all
    x = None
    y = safe_eval('1')
    if y != 1:
        sys.stderr.write("Construct '1' did not evaluate to 1.")
        return False

    # Now test the evaluation of something a bit more complex
    z = safe_eval('[1,2,3]')
    if z != [1, 2, 3]:
        sys.stderr.write("Construct '[1,2,3]' did not evaluate to [1,2,3].")
        return False

    # Test for exceptions which should occur

    # Division by 0
    x = None
    try:
        x = safe_eval('1/0')
    except:
        pass

# Generated at 2022-06-13 15:35:58.089829
# Unit test for function safe_eval
def test_safe_eval():
    def test_expression(expression, expected_result, expected_to_fail=False):
        if expected_to_fail:
            try:
                result = safe_eval(expression)
                return False, 'Unexpectedly run "%s", got result "%s"' % (expression, result)
            except:
                return True, ''
        else:
            result = safe_eval(expression)
            if result != expected_result:
                return False, 'Got result "%s" instead of "%s"' % (result, expected_result)
            else:
                return True, ''

    if C.DEFAULT_KEEP_REMOTE_FILES:
        print('\nDisabling remote file caching to run unit test\n')
        C.DEFAULT_KEEP_REMOTE_FILES = False


# Generated at 2022-06-13 15:36:07.387686
# Unit test for function safe_eval
def test_safe_eval():
    import pytest

    # simple tests for math ops
    assert safe_eval('3 + 4 + 5') == 12
    assert safe_eval('3 + 4 + 5', include_exceptions=True)[0] == 12
    assert safe_eval('6 * 7') == 42
    assert safe_eval('6 * 7', include_exceptions=True)[0] == 42
    assert safe_eval('2 ** 8') == 256
    assert safe_eval('2 ** 8', include_exceptions=True)[0] == 256

    # basic list support
    assert safe_eval('[1, 2, 3]') == [1, 2, 3]
    assert safe_eval('[1, 2, 3]', include_exceptions=True)[0] == [1, 2, 3]

# Generated at 2022-06-13 15:36:15.614020
# Unit test for function safe_eval
def test_safe_eval():
    # test ast.List
    string_list = "['a','b','c']"
    list_result = safe_eval(string_list)
    assert(isinstance(list_result, list))
    # test ast.Call (disabled by default)
    string_call = "str(42)"
    call_result = safe_eval(string_call)
    assert(isinstance(call_result, string_types))
    # test ast.Call re-enabled
    string_call = "str(42)"
    call_result = safe_eval(string_call, include_exceptions=True)[0]
    assert(isinstance(call_result, string_types))
    # test ast.Dict
    string_dict = "{'a':'b', 'c':'d'}"

# Generated at 2022-06-13 15:36:24.753789
# Unit test for function safe_eval

# Generated at 2022-06-13 15:36:31.419003
# Unit test for function safe_eval
def test_safe_eval():
    conn_port = '2222'

    a = False
    b = True
    c = "name"
    d = dict(a=a, b=b, c=c)
    e = ['a', 'b', 'c']
    f = 1
    g = 1.1
    h = {'a':1, 'b':2, 'c':3}
    i = None
    j = dict(a=[1,2,3], b=[4,5,6])
    k = dict(a=dict(b=dict(c='1 2 3')))
    l = dict(a='1 2 3')
    m = dict(a='1 {{conn.port}}')

    # This is a mapping of test_val (given as a param to safe_eval) to
    # the expected results (what safe_eval should return

# Generated at 2022-06-13 15:36:42.514501
# Unit test for function safe_eval
def test_safe_eval():
    # Test expression parsing
    if not hasattr(sys, '_called_from_test'):
        # If this is running as a top-level script then we can't use
        # a module-level global to communicate with the subprocess version
        # of this module, so use command-line arguments to pass test results
        # back to the subprocess.
        import sys
        print('SKIP: module_utils.common.text.eval_input not testing itself in isolation')
        sys.stdout.flush()
        sys.exit(0)

    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.module_utils.six import PY3
    from ansible.module_utils.six import iteritems
    from ansible.module_utils.six import string_types

    # This test mostly tests the

# Generated at 2022-06-13 15:36:54.208091
# Unit test for function safe_eval
def test_safe_eval():
    # test unquoted strings
    if sys.version_info >= (3,0):
        assert safe_eval("foo") == 'foo'
    else:
        assert safe_eval("foo") == unicode('foo', 'unicode_escape')

    # test the use of strings containing quotes
    assert safe_eval('"abc"') == 'abc'
    assert safe_eval('"abc\'def"') == "abc'def"
    assert safe_eval('"abc" "def"') == 'abc def'
    assert safe_eval('"abc" + "def"') == 'abcdef'
    assert safe_eval('"abc" "def"', dict(a='a')) == 'abc def'
    assert safe_eval('"abc" "def"', dict(a='a'), True)[0] == 'abc def'
   

# Generated at 2022-06-13 15:37:03.186701
# Unit test for function safe_eval
def test_safe_eval():
    # Test JSON objects (they are not allowed by default)
    if PY3:
        json_string = "'{\"foo\": true}'"
    else:
        json_string = "u'{\"foo\": true}'"

    assert safe_eval(json_string) == json_string

    # Test JSON objects with allow_unsafe_lookups
    C.DEFAULT_ALLOW_UNSAFE_LOOKUPS = True
    assert safe_eval(json_string) == {u'foo': True}

    # Disable unsafe lookups
    C.DEFAULT_ALLOW_UNSAFE_LOOKUPS = False

    # Test builtin python functions are not allowed, unless explicitly allowed
    with pytest.raises(Exception) as e:
        safe_eval("vars()")
    assert 'invalid function' in to_

# Generated at 2022-06-13 15:37:44.203951
# Unit test for function safe_eval
def test_safe_eval():

    # make sure literal int/str work
    assert safe_eval('5') == 5
    assert safe_eval('"a" + "b"') == "ab"

    # make sure that None, True, False work
    assert safe_eval('null') == None
    assert safe_eval('false') == False
    assert safe_eval('true') == True

    # make sure standard python syntax works
    assert safe_eval('[[1,2],[3,4]]') == [[1, 2], [3, 4]]
    assert safe_eval('{"a":1,"b":2}') == {'a': 1, 'b': 2}
    assert safe_eval('(True, False, None)') == (True, False, None)
    assert safe_eval('f.__doc__') == eval('f.__doc__')

    # make

# Generated at 2022-06-13 15:37:54.524360
# Unit test for function safe_eval
def test_safe_eval():
    expr = safe_eval('1+1')
    assert expr == 2

    expr = safe_eval('dict(foo="bar")')
    assert expr == {"foo": "bar"}

    expr = safe_eval('[1,2,3][0]')
    assert expr == 1

    expr = safe_eval('[1,2,3][0:2]')
    assert expr == [1, 2]

    expr = safe_eval('[1,2,3][::-1]')
    assert expr == [3, 2, 1]

    expr = safe_eval('{"foo": "bar"}["foo"]')
    assert expr == "bar"

    expr = safe_eval('(1,2,3)[0]')
    assert expr == 1

    expr = safe_eval('1>=0')
    assert expr == True



# Generated at 2022-06-13 15:38:02.919029
# Unit test for function safe_eval
def test_safe_eval():
    # Make sure we raise an exception if the expression contains
    # only a string
    result = safe_eval("foo")
    assert result == "foo"
    result = safe_eval("foo", include_exceptions=True)
    assert result[0] == "foo" and result[1] is None
    # Make sure we raise an exception if the expression is not a string
    result = safe_eval(["foo", "bar"])
    assert result == ["foo", "bar"]
    result = safe_eval(["foo", "bar"], include_exceptions=True)
    assert result[0] == ["foo", "bar"] and result[1] is None
    # Test a simple string expression
    result = safe_eval("foo.bar")
    assert result == "foo.bar"