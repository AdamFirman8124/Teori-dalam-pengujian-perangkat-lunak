

# Generated at 2022-06-13 15:28:10.251286
# Unit test for function safe_eval
def test_safe_eval():
    # special cases
    assert safe_eval(None) is None

    # simple cases
    assert safe_eval('1') == 1
    assert safe_eval('1 + 1') == 2
    assert safe_eval('foo') == 'foo'
    assert safe_eval('foo.bar') == 'foo.bar'

    # container types
    assert safe_eval('[]') == []
    assert safe_eval('[1]') == [1]
    assert safe_eval('["foo"]') == ['foo']
    assert safe_eval('{"foo": "bar"}') == {'foo': 'bar'}

    # fails due to invalid identifier
    try:
        safe_eval('foo-bar')
        assert False
    except:
        assert True

    # fails due to invalid operator

# Generated at 2022-06-13 15:28:14.932230
# Unit test for function safe_eval
def test_safe_eval():
    # define list of tests and expected results
    tests = {
        "0": 0,
        "True": True,
        "False": False,
        "true": True,
        "false": False,
        "None": None,
        "'hello'": "hello",
        "'hello' + ' world'": "hello world",
        "[1, 2, 3]": [1, 2, 3],
        "[1, 2, 3] + [4, 5, 6]": [1, 2, 3, 4, 5, 6],
        "[1, 2, 3] * 2": [1, 2, 3, 1, 2, 3],
        "1 * 2 + 3 * 4 / 2": 7,
        "1 * (2 + 3) * 4": 20,
    }

    # run tests and compare results to expected results

# Generated at 2022-06-13 15:28:23.354680
# Unit test for function safe_eval
def test_safe_eval():
    # single-statement expressions
    a = safe_eval("1 + 1")
    assert a == 2
    a = safe_eval("1 + 1", include_exceptions=True)
    assert a == (2, None)
    b = safe_eval("unsupported_function()")
    assert b == "unsupported_function()"
    b = safe_eval("unsupported_function()", include_exceptions=True)
    assert b == ("unsupported_function()", None)
    c = safe_eval("callable_function(1)")
    assert c == "callable_function(1)"
    c = safe_eval("callable_function(1)", include_exceptions=True)
    assert c == ("callable_function(1)", None)
    d = safe_eval("1 + {'a': 2}")
   

# Generated at 2022-06-13 15:28:33.347061
# Unit test for function safe_eval
def test_safe_eval():
    def test_eval_result(result, expected):
        assert result[0] == expected, "expected %s, got %s" % (expected, result[0])

    # test passing a non-string
    test_eval_result(safe_eval({}), {})
    # test simple expressions
    test_eval_result(safe_eval("5"), 5)
    test_eval_result(safe_eval("5 + 5"), 10)
    test_eval_result(safe_eval("5 - 5"), 0)
    test_eval_result(safe_eval("5 * 5"), 25)
    test_eval_result(safe_eval("5 / 5"), 1)
    test_eval_result(safe_eval("5 % 5"), 0)
    test_eval_result(safe_eval("-5"), -5)
    test_eval

# Generated at 2022-06-13 15:28:43.219576
# Unit test for function safe_eval
def test_safe_eval():
    # Simple tests
    assert safe_eval('1+1') == 2
    assert safe_eval('"a" + "b"') == "ab"
    assert safe_eval('True') is True
    assert safe_eval('[]') == []
    assert safe_eval('["foo", "bar"]') == ['foo', 'bar']
    assert safe_eval('{"1": 1, "2": 2}') == {'1': 1, '2': 2}
    assert safe_eval('{"a": "b", "c": "d"}') == {'a': 'b', 'c': 'd'}

    # Test tuples
    assert safe_eval('(1, 2)') == (1, 2)
    assert safe_eval('(1, [2, 3])') == (1, [2, 3])
    assert safe_

# Generated at 2022-06-13 15:28:51.698554
# Unit test for function safe_eval

# Generated at 2022-06-13 15:28:59.528775
# Unit test for function safe_eval
def test_safe_eval():
    for expression, expected in ((1, 1),
                                 ('1', 1),
                                 ('1+2', 3),
                                 ('1+2*3', 7),
                                 ('1+2*3', 7),
                                 ('1+2**3', 9),
                                 ('-1', -1),
                                 ('1 and 1', True),
                                 ('1 or 0', True),
                                 ('1 and 0 or 1', True)):
        result, exc = safe_eval(expression, include_exceptions=True)
        print("Expression: %s -> %s" % (expression, result))
        assert result == expected and exc is None, \
            "Failed to evaluate expression %s\nExpected %s\nActual: %s" % (expression, expected, result)


# Generated at 2022-06-13 15:29:08.520991
# Unit test for function safe_eval
def test_safe_eval():
    import textwrap

    def test_fail_parse(expr):
        # Test if this expression raises an exception in the safe_eval
        # parsing stage
        failed = False
        try:
            safe_eval(expr)
        except Exception:
            failed = True
        return failed

    def test_pass(expr):
        # Test if this expression passes the safe_eval
        passed = True
        try:
            safe_eval(expr)
        except Exception:
            passed = False
        return passed

    def test_pass_check_value(expr, out):
        # Test if this expression passes the safe_eval and returns the
        # expected output
        passed = True
        try:
            val = safe_eval(expr)
        except Exception:
            passed = False
        return passed and val == out


# Generated at 2022-06-13 15:29:18.180572
# Unit test for function safe_eval
def test_safe_eval():
    # Basic correct function
    result, err = safe_eval("42")
    assert result == 42 and err is None

    # String support
    result, err = safe_eval('"foo"')
    assert result == "foo" and err is None

    # Quotes must be escaped in strings
    result, err = safe_eval('"don\\\'t"')
    assert result == "don't" and err is None

    # Lists support
    result, err = safe_eval("[1, 2, 3]")
    assert result == [1, 2, 3] and err is None

    # Dicts support
    result, err = safe_eval("{'foo': 1, 'bar': 2}")
    assert result == {'foo': 1, 'bar': 2} and err is None

    # Tuple support
    result, err = safe_

# Generated at 2022-06-13 15:29:21.535604
# Unit test for function safe_eval
def test_safe_eval():
    import doctest
    doctest.testmod()

# if __name__ == '__main__':
#     import doctest
#     doctest.testmod()

# Generated at 2022-06-13 15:29:34.428932
# Unit test for function safe_eval
def test_safe_eval():
    import nose

    # setup

# Generated at 2022-06-13 15:29:40.163600
# Unit test for function safe_eval

# Generated at 2022-06-13 15:29:51.474118
# Unit test for function safe_eval
def test_safe_eval():
    # verify handling of syntax errors
    result, err = safe_eval('{{ "foo" )', include_exceptions=True)
    assert result == '{{ "foo" )' and err is None

    # verify proper handling of an expression not in the whitelist
    result, err = safe_eval('{}', include_exceptions=True)
    assert result == '{}' and isinstance(err, Exception)

    # verify proper handling of a dictionary that uses a non-string key
    result, err = safe_eval('{1:2}', include_exceptions=True)
    assert result == "{1: 2}" and isinstance(err, Exception)

    result, err = safe_eval('{1:2}', include_exceptions=True, locals={'foo': 3})

# Generated at 2022-06-13 15:29:59.626610
# Unit test for function safe_eval
def test_safe_eval():
    # Test various valid expressions
    expr = '1 + 1'
    assert safe_eval(expr) == 1 + 1

    expr = '-1 + 1'
    assert safe_eval(expr) == -1 + 1

    expr = 'True'
    assert safe_eval(expr) is True

    expr = '[1, 2, 3]'
    assert safe_eval(expr) == [1, 2, 3]

    # Test various invalid expressions
    expr = '__import__("os").system("echo hello")'
    try:
        safe_eval(expr)
        assert False
    except Exception:
        pass

    expr = '__import__("os").system("echo hello")'
    try:
        safe_eval(expr)
        assert False
    except Exception:
        pass


# Generated at 2022-06-13 15:30:06.205446
# Unit test for function safe_eval
def test_safe_eval():
    print("testing safe eval...")
    if len(sys.argv) < 2:
        print("missing args")
        print("usage: safe_eval.py expression")
        print("")
        print("expression may contain Python literals and variables from the following list:")
        print("  a_list    [9, 8, 7, 6, 5]")
        print("  a_dict    {'a': 9, 'b': 8, 'c': 7, 'd': 6, 'e': 5}")
        print("")
        sys.exit(1)

    expr = sys.argv[1]
    expr_result = eval(expr)

    a_list = [9, 8, 7, 6, 5]

# Generated at 2022-06-13 15:30:16.580786
# Unit test for function safe_eval
def test_safe_eval():

    # Test simple expression
    # Note: simple expression like '2+2' is not allowed
    expr = "2*2"
    result = safe_eval(expr)
    assert result == 4

    # Test expression with variable
    expr = "a * 2"
    locals = {'a': 4}
    result = safe_eval(expr, locals)
    assert result == 8

    # Test string concatenation
    expr = "'Hello ' + 'World!'"
    result = safe_eval(expr)
    assert isinstance(result, str)
    assert result == 'Hello World!'

    # Test list element access
    expr = "a[1]"
    locals = {'a': ['a', 'b', 'c']}
    result = safe_eval(expr, locals)
    assert isinstance(result, str)

# Generated at 2022-06-13 15:30:25.139206
# Unit test for function safe_eval
def test_safe_eval():
    # This function is used to test the function safe_eval
    #
    # The function safe_eval checks for dangerous expressions in a string and
    # replaces them with a empty string.
    #
    # This is the test of a safe expression
    # Some arguments are:
    #   expr : The expression to test
    #   locals : Any variables in scope
    #   include_exceptions:
    #       If true, when an exception occurs it will be returned in the
    #       second value of the tuple.
    #       If false, when an exception occurs the expression will be returned
    #       as is.
    #
    # The expected result is a string "foo".
    result, exceptions = safe_eval("'foo'", include_exceptions=True)
    assert(result == 'foo' and exceptions == None)
    result = safe_eval

# Generated at 2022-06-13 15:30:31.444407
# Unit test for function safe_eval
def test_safe_eval():
    globals = dict(a=dict(foo=42))
    locals = dict(b=dict(bar='foo'))

    #
    # Basic test
    #

    # Test expected success
    # We should be able to do basic expressions
    assert safe_eval('3 + 2') == 5
    assert safe_eval('3 + 2 > 5') is False
    assert safe_eval('3 + 2 > 4') is True

    # We should be able to access our locals and globals
    assert safe_eval('foo', locals) == locals['foo']
    assert safe_eval('foo', globals) == globals['foo']
    assert safe_eval('foo', dict(locals, **globals)) == locals['foo']
    assert safe_eval('foo', dict(globals, **locals)) == globals['foo']

   

# Generated at 2022-06-13 15:30:40.684477
# Unit test for function safe_eval
def test_safe_eval():

    def _assert_safe_eval(expr, expected_result):
        actual_result = safe_eval(expr)
        assert actual_result == expected_result

    # Ensure eval handles container types correctly (lists, dicts, tuples)
    _assert_safe_eval('[1, 2, 3]', [1, 2, 3])
    _assert_safe_eval('(1, 2, 3)', (1, 2, 3))
    _assert_safe_eval('{1, 2, 3}', {1, 2, 3})
    _assert_safe_eval('{"a": "b"}', {"a": "b"})

    # Ensure eval allows keywords (True, False, None)
    _assert_safe_eval('True', True)
    _assert_safe_eval('False', False)

# Generated at 2022-06-13 15:30:47.205013
# Unit test for function safe_eval
def test_safe_eval():
    # function names to enable in call()
    CALL_ENABLED.extend([
        'int',
        'and',
        'or',
        'len',
    ])

    # Globals needed by function safe_eval()
    OUR_GLOBALS = {
        '__builtins__': {},  # avoid global builtins as per eval docs
        'false': False,
        'null': None,
        'true': True,
        # also add back some builtins we do need
        'True': True,
        'False': False,
        'None': None
    }

    # Lists of expected safe/unsafe expressions

# Generated at 2022-06-13 15:30:57.344625
# Unit test for function safe_eval
def test_safe_eval():
    """
    Test function safe_eval, including tests for presence of
    required builtins.
    """
    # test for presence of required builtins
    for b in ['True', 'False', 'None']:
        assert safe_eval(b) == eval(b)

    # test for absence of dangerous builtins

# Generated at 2022-06-13 15:31:08.173887
# Unit test for function safe_eval
def test_safe_eval():

    assert safe_eval('a + b') == 'a + b'
    assert safe_eval('a + b + c', dict(a=1, b=2, c=3)) == 1 + 2 + 3
    if sys.version_info >= (3, 8):
        assert safe_eval('f"a + b + c"', dict(a=1, b=2, c=3)) == "a + b + c"
        assert safe_eval('f"a = {a} b = {b} c = {c}"', dict(a=1, b=2, c=3)) == "a = 1 b = 2 c = 3"
    assert safe_eval('a + b', dict(a=1)) == "1 + b"

# Generated at 2022-06-13 15:31:15.680438
# Unit test for function safe_eval
def test_safe_eval():

    # Test to make sure function safe_eval
    # works in a module environment where
    # global psuedo-builtins might be available.
    # tests:
    # safe_eval('lookup("file", "foo")')
    # safe_eval('lookup("template", "foo.j2")')
    # safe_eval('lookup("pipe", "foo")')
    # safe_eval('lookup("env", "foo")')
    # safe_eval('lookup("passwd", "foo")')
    # safe_eval('lookup("command", "foo")')
    # safe_eval('lookup("inventory_hostname", "foo")')

    # Used for generate the lookup values
    from ansible.utils.vars import combine_vars
    from ansible.parsing.dataloader import DataLoader


# Generated at 2022-06-13 15:31:27.550384
# Unit test for function safe_eval
def test_safe_eval():
    # ensure that safe_eval works for these expressions
    for expr in [
            '1 + 1', '1 + 1 == 2', 'true', 'false',
            'null', '"string"', '"string" + "string"', 'len("string") == 6',
            'foo == "bar"', 'foo == "baz"',
            'foo is not defined', '"string" + "string"',
            '{"a": "b", "c": "d"}',
            '[1, 2, 3]',
            ('1 if not (2 if 3 else 4) else 5'),
            ('(lambda x: x)')
    ]:
        assert safe_eval(expr)

    # ensure that safe_eval fails for these expressions

# Generated at 2022-06-13 15:31:35.913222
# Unit test for function safe_eval
def test_safe_eval():

    # This is a set of tests designed to exercise the safe_eval function
    # as part of validating the changes implemented in this pull request:
    # https://github.com/ansible/ansible/pull/13944

    def test_json_types():
        ''' JSON types should be accepted by safe_eval '''
        assert safe_eval("true")
        assert not safe_eval("false")
        assert safe_eval("null") is None
        assert not safe_eval("false or true")

    def test_literals():
        ''' Literals should be accepted by safe_eval '''
        assert safe_eval("[]") == []
        assert safe_eval("['a', 1, true]") == ['a', 1, True]
        assert safe_eval("{}") == {}

# Generated at 2022-06-13 15:31:44.316170
# Unit test for function safe_eval
def test_safe_eval():
    '''
    Evaluate expressions in a sandbox
    '''

# Generated at 2022-06-13 15:31:55.145603
# Unit test for function safe_eval
def test_safe_eval():
    """Return unit test status for safe_eval function"""

    OK = '\033[92mOK\033[0m'
    FAIL = "\033[91mFAIL\033[0m"

    expression = "{{ lookup('template', 'foo.j2') }}"
    assert safe_eval(expression) == expression, FAIL
    assert safe_eval(expression, include_exceptions=True) == (expression, None), FAIL

    expression = "6 * 7"
    assert safe_eval(expression) == 42, FAIL
    assert safe_eval(expression, include_exceptions=True) == (42, None), FAIL

    expression = "{'a': 'b'}"
    assert safe_eval(expression) == {'a': 'b'}, FAIL

# Generated at 2022-06-13 15:32:05.824319
# Unit test for function safe_eval
def test_safe_eval():

    valid = ["true", "false", "null", "True", "False", "None", "1+2", "2*3",
        "{'a':1, 'b': [1,2,3] }", "[1,2,3]", "1-2", "1/2"]

    invalid = ["__import__('os').system('echo got root?')",
        "__import__('os').system('echo got root?') if False else False",
        "__import__('os').system('echo got root?')",
        "__import__('os').system('echo got root?') if False else False"]

    for expr in valid:
        safe_eval(expr)


# Generated at 2022-06-13 15:32:17.858723
# Unit test for function safe_eval

# Generated at 2022-06-13 15:32:29.871268
# Unit test for function safe_eval
def test_safe_eval():
    assert 1 == safe_eval("1")

    assert 1 == safe_eval("1+0")
    assert 1 == safe_eval("1+0", include_exceptions=True)[0]

    assert 2 == safe_eval("1 + 1")
    assert 2 == safe_eval("1 + 1", include_exceptions=True)[0]

    assert 1 == safe_eval("2 - 1")
    assert 1 == safe_eval("2 - 1", include_exceptions=True)[0]

    assert 10 == safe_eval("2 * 5")
    assert 10 == safe_eval("2 * 5", include_exceptions=True)[0]

    assert 2 == safe_eval("10 / 5")
    assert 2 == safe_eval("10 / 5", include_exceptions=True)[0]


# Generated at 2022-06-13 15:32:34.419723
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval("'blah'") == 'blah'

# Generated at 2022-06-13 15:32:43.531621
# Unit test for function safe_eval

# Generated at 2022-06-13 15:32:53.642247
# Unit test for function safe_eval
def test_safe_eval():
    # disabled until we can write code to enable ast.Call
    # for specific functions like "len", etc.
    return

    ###
    # Test ast.Call is allowed after adding/removing from CALL_ENABLED
    ###

    # negative test - ast.Call should be disabled by default
    if safe_eval('len([1, 2])') == 2:
        sys.exit(1)

    # positive test - ast.Call after adding to CALL_ENABLED
    CALL_ENABLED.append('len')
    if safe_eval('len([1, 2])') != 2:
        sys.exit(1)
    CALL_ENABLED.remove('len')

    ###
    # Test ast.Call with invalid function name
    ###

# Generated at 2022-06-13 15:33:03.903633
# Unit test for function safe_eval

# Generated at 2022-06-13 15:33:15.311719
# Unit test for function safe_eval
def test_safe_eval():
    rc, exception = safe_eval('1 + 1', include_exceptions=True)
    assert rc == 2
    assert exception is None
    rc, exception = safe_eval('{"a": 1, "b": 2}', include_exceptions=True)
    assert rc == {'a': 1, 'b': 2}
    assert exception is None
    rc, exception = safe_eval('[1, 2, 3]', include_exceptions=True)
    assert rc == [1, 2, 3]
    assert exception is None
    rc, exception = safe_eval('false', include_exceptions=True)
    assert rc is False
    assert exception is None
    rc, exception = safe_eval('null', include_exceptions=True)
    assert rc is None
    assert exception is None

# Generated at 2022-06-13 15:33:26.460790
# Unit test for function safe_eval
def test_safe_eval():
    '''Unit test for function ansible.utils.safe_eval.'''

    from ansible.module_utils.six import PY3

    # Set up locals
    locals = {'foo': 'bar', 'boo': ['zoo'], 'faz': {'biz': 'baz'}}
    # Set up expected
    expected = {'foo': 'bar', 'boo': ['zoo'], 'faz': {'biz': 'baz'}}

    # Test no exceptions

# Generated at 2022-06-13 15:33:36.659584
# Unit test for function safe_eval
def test_safe_eval():
    # Setup
    import ast
    import sys
    import textwrap
    tests = [('True', True),
             (sys.version_info, sys.version_info),
             ('None', None),
             ('True + True', True),
             ('None is not None', True),
             ('True if False else False', False),
             ('True and False', False)]
    for i, (expr, expected) in enumerate(tests):
        try:
            val = safe_eval(expr)
        except Exception:
            print('test #{0} failed: {1}'.format(i, expr))
        else:
            if val != expected:
                print('test #{0} failed: {1} != {2}'.format(i, val, expected))



# Generated at 2022-06-13 15:33:47.614567
# Unit test for function safe_eval
def test_safe_eval():
    '''
    unit tests for function safe_eval
    '''

    expected_keys = {
        u"expr_str": "a_list_variable",
        u"unexpected_exception_type": "",
        u"eval_exception_type": "",
        u"eval_exception_msg": "",
        u"eval_result": "",
        u"safe_eval_result": "",
        u"safe_eval_exception_type": "",
        u"safe_eval_exception_msg": "",
    }

    # List of dicts, each dict has:
    #   u'expr_str'        = string to be evaluated by safe_eval
    #   u'eval_result'     = expected result of eval(expr_str)
    #   u'safe_eval_result = expected

# Generated at 2022-06-13 15:33:57.580600
# Unit test for function safe_eval
def test_safe_eval():
    import pytest

    safe_str = "({'key': 'value'})"
    result = safe_eval(safe_str)
    assert result == {'key': 'value'}, "Failed to eval %s" % safe_str

    # test function call to a safe function, like `len()`
    safe_str = 'len("test")'
    result, e = safe_eval(safe_str, include_exceptions=True)
    assert result == 4 and not e, "Failed to eval %s" % safe_str

    # test function call to an unsafe function, like `eval()`
    safe_str = 'eval("1+1")'
    result, e = safe_eval(safe_str, include_exceptions=True)
    assert not result and e

# Generated at 2022-06-13 15:34:06.441181
# Unit test for function safe_eval
def test_safe_eval():
    results = []

# Generated at 2022-06-13 15:34:12.884135
# Unit test for function safe_eval

# Generated at 2022-06-13 15:34:23.172034
# Unit test for function safe_eval
def test_safe_eval():
    def check(i, o):
        ival, err = safe_eval(i, include_exceptions=True)
        assert ival == o
        if o is not None:
            assert err is None

    check('6', 6)
    check('6 + 4', 10)
    check('a_list_variable', 'a_list_variable')
    check('6 + a_list_variable', '6 + a_list_variable')
    check('a_list_variable.append(10)', 'a_list_variable.append(10)')
    check('a_list_variable[1:]', 'a_list_variable[1:]')
    check('a_list_variable[:-1]', 'a_list_variable[:-1]')
    check('range(4)', range(4))

# Generated at 2022-06-13 15:34:31.263546
# Unit test for function safe_eval
def test_safe_eval():
    def NoneTest():
        txt = 'None'
        print('Executing', txt)
        result = safe_eval(txt)
        print(result, type(result))
        assert result is None

    def TrueTest():
        txt = 'True'
        print('Executing', txt)
        result = safe_eval(txt)
        print(result, type(result))
        assert result is True

    def FalseTest():
        txt = 'False'
        print('Executing', txt)
        result = safe_eval(txt)
        print(result, type(result))
        assert result is False

    def NonStrTest():
        not_a_str = 42
        print('Executing', not_a_str)
        result = safe_eval(not_a_str)

# Generated at 2022-06-13 15:34:41.029729
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval("{{ 1 + 1 }}") == "{{ 1 + 1 }}"
    assert safe_eval("'{{ 1 + 1 }}'") == "{{ 1 + 1 }}"
    assert safe_eval("[1,2,{{ 1 + 1 }},4]") == [1, 2, "{{ 1 + 1 }}", 4]
    assert safe_eval("{'a': '1' }").get('a') == '1'
    assert safe_eval("foo.lower()") == "foo.lower()"
    assert safe_eval("open()") == "open()"
    assert safe_eval("1 + 2") == 3
    assert safe_eval("foo", dict(foo='bar')) == 'bar'
    assert safe_eval("foo.upper()", dict(foo='bar')) == 'BAR'
    assert safe_

# Generated at 2022-06-13 15:34:48.021353
# Unit test for function safe_eval

# Generated at 2022-06-13 15:34:59.481942
# Unit test for function safe_eval
def test_safe_eval():
    # define a whitelist of AST node types we will allow
    SAFE_NODES = set(
        (
            ast.Add,
            ast.Compare,
            ast.Constant,
            ast.Div,
            ast.Expression,
            ast.Mult,
            ast.Num,
            ast.Sub,
            ast.Tuple,
            ast.UnaryOp,
        )
    )

    # define a list of expressions we will allow

# Generated at 2022-06-13 15:35:07.971967
# Unit test for function safe_eval

# Generated at 2022-06-13 15:35:16.533191
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval('True') is True
    assert safe_eval('False') is False
    assert safe_eval('x', {'x': 1}) == 1
    assert safe_eval('x', {'x': True}) is True
    assert safe_eval('!x', {'x': True}) is False
    assert safe_eval('x == "foo"', {'x': "foo"}) is True
    assert safe_eval('x == "foo"', {'x': "bar"}) is False
    assert safe_eval('not x', {'x': False}) is True
    assert safe_eval('x and y', {'x': False, 'y': True}) is False
    assert safe_eval('x and y', {'x': True, 'y': True}) is True

# Generated at 2022-06-13 15:35:24.365680
# Unit test for function safe_eval
def test_safe_eval():
    # basic sanity check
    assert(safe_eval("['a', 'b']") == ['a', 'b'])
    assert(safe_eval("{'a': 1, 'b': 2}") == {'a': 1, 'b': 2})
    assert(safe_eval("a") == "a")
    assert(safe_eval("True") == True)
    assert(safe_eval("False") == False)

    # single item list of variable name
    assert(safe_eval("a_list_variable", dict(a_list_variable=['a', 'b'])) == ['a', 'b'])

    # single item dict of variable name

# Generated at 2022-06-13 15:35:33.652051
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval('{{ foo }}') == '{{ foo }}'
    assert safe_eval('{{ foo }}', {'foo': 'bar'}) == 'bar'
    assert safe_eval('{{ foo }}', {'foo': 'bar'}, include_exceptions=True)[0] == 'bar'
    assert safe_eval('{{ foo }}', include_exceptions=True)[1] is not None
    assert safe_eval('{{ foo.bar }}', {'foo': {'bar': 'baz'}}) == 'baz'
    assert safe_eval('{{ foo["bar"] }}', {'foo': {'bar': 'baz'}}) == 'baz'
    assert safe_eval('{{ [1,2,3,4][1] }}') == 2

# Generated at 2022-06-13 15:35:43.059211
# Unit test for function safe_eval

# Generated at 2022-06-13 15:35:53.330584
# Unit test for function safe_eval
def test_safe_eval():
    # nosetests -v test_utils.py:test_safe_eval
    from ansible.module_utils import basic

    def test(str, expected):
        system_stdout = sys.stdout
        sys.stdout = basic.AnsibleModuleStub(dict())
        result = safe_eval(str)
        sys.stdout = system_stdout
        if result != expected:
            raise AssertionError("%s != %s" % (result, expected))

    test("[1] + [2]", [1,2])
    test("{'a': 'b'}", {'a':'b'})
    test("[1] + 'string'", [1, 's', 't', 'r', 'i', 'n', 'g'])

# Generated at 2022-06-13 15:36:04.008208
# Unit test for function safe_eval
def test_safe_eval():
    '''
    Tests included with the function to test the functionality.
    '''

# Generated at 2022-06-13 15:36:11.971319
# Unit test for function safe_eval
def test_safe_eval():
    """
    Tests for safe_eval.

    In some cases it is not necessary to include the first exception of a
    failed assertion in the message, as it reveals implementation details
    (for example, by mentioning the name of the function being tested).

    The following function raises an AssertionError, but only with the
    message 'Expected...', not the details of the exception that
    would've been raised if the expression is invalid, since the
    exception message is not always descriptive enough to avoid confusion.

    """
    def assert_valid_expr(expr):
        """Assert that an expression is valid, else raise an error with
        generic message.
        """
        try:
            safe_eval(expr, include_exceptions=True)
        except AssertionError as e:
            raise AssertionError('Unexpected invalid expression: %s' % expr)

# Generated at 2022-06-13 15:36:19.488948
# Unit test for function safe_eval

# Generated at 2022-06-13 15:36:27.558095
# Unit test for function safe_eval
def test_safe_eval():
    from ansible.module_utils.common.text.converters import to_text


# Generated at 2022-06-13 15:36:33.096890
# Unit test for function safe_eval
def test_safe_eval():
    import unittest

    class TestSafeEval(unittest.TestCase):
        def test_safe_eval(self):
            def check_safe_eval(in_str, out_str, exception=None):
                (ret_str, ret_exception) = safe_eval(in_str, include_exceptions=True)
                self.assertEqual(ret_str, out_str)
                if exception:
                    self.assertIsInstance(ret_exception, exception)
                else:
                    self.assertIsNone(ret_exception)

            check_safe_eval("'foo'", 'foo')
            check_safe_eval("['foo', 'bar']", ['foo', 'bar'])
            check_safe_eval("{'foo': 'bar'}", {'foo': 'bar'})
            check_

# Generated at 2022-06-13 15:36:42.865672
# Unit test for function safe_eval
def test_safe_eval():
    import json


# Generated at 2022-06-13 15:36:54.631480
# Unit test for function safe_eval
def test_safe_eval():

    try:
        safe_eval('{{ [1,2,3]|map("str")|join("")[2:3] }}')
        assert False, "Should have raised an exception"
    except:
        assert True

    try:
        safe_eval('{{ [1,2,3]|map("str")|join("")[2:3] }')
        assert False, "Should have raised an exception"
    except:
        assert True

    try:
        safe_eval('{{ [1,2,3]|map("str")|join("")[2:3]')
        assert False, "Should have raised an exception"
    except:
        assert True

    assert safe_eval('{{ [1,2,3]|max }}') == 3

# Generated at 2022-06-13 15:37:03.471777
# Unit test for function safe_eval

# Generated at 2022-06-13 15:37:20.927322
# Unit test for function safe_eval
def test_safe_eval():
    ''' test our safe eval function '''
    # the test scripts rely on output to stderr to detect failures
    # and this unit test uses the "assert" statement which outputs
    # to stderr.  So, we have to jump through some hoops to capture
    # that output and redirect it to stdout so it won't interfere.
    oldstderr = sys.stderr
    sys.stderr = sys.stdout

    # simple tests
    assert safe_eval("4+4") == 8
    assert safe_eval("4+4", include_exceptions=True)[0] == 8
    assert safe_eval("0xff") == 255
    assert safe_eval("0xff", include_exceptions=True)[0] == 255
    assert safe_eval("true") is True

# Generated at 2022-06-13 15:37:32.455414
# Unit test for function safe_eval
def test_safe_eval():
    # safe_eval can handle simple expressions
    assert safe_eval("foo") == "foo"
    assert safe_eval("foo.bar") == "foo.bar"
    assert safe_eval("foo.bar.bam") == "foo.bar.bam"
    assert safe_eval("foo_bar") == "foo_bar"
    assert safe_eval("foo_bar.bam_baz") == "foo_bar.bam_baz"

    # safe_eval can handle numerical expressions
    assert safe_eval("1 + 1") == 2
    assert safe_eval("1 + 1") != 3
    assert safe_eval("1 + (5 * 5)") == 26

    # safe_eval can handle more complex expressions
    assert safe_eval("foo and bar") == "foo and bar"

# Generated at 2022-06-13 15:37:44.043000
# Unit test for function safe_eval
def test_safe_eval():
    examples = [
        ('true', True),
        ('"hello"', 'hello'),
        ('[1,2,3]', [1, 2, 3]),
        ('{"a": 1}', {'a': 1}),
        ('1 + 2', 3),
        ('1 + [2, 3]', '1 + [2, 3]'),
        ('1 + null', '1 + null'),
        ('1 + false', '1 + false'),
        ('1 + true', '1 + true'),
    ]

    # For Python3 a string is an instance of str and bytes, so we need to
    # type check on str instead of basestring in Python3

# Generated at 2022-06-13 15:37:48.820657
# Unit test for function safe_eval
def test_safe_eval():
    # Test safe_eval fails with unnamed args
    # These tests are only to ensure we do not regress, as
    # safe_eval is no longer used.
    assert safe_eval('2+2') != 4
    assert safe_eval('2+2', include_exceptions=True) != 4
    assert safe_eval('func', include_exceptions=True) != 4



# Generated at 2022-06-13 15:37:58.903107
# Unit test for function safe_eval
def test_safe_eval():
    simple_test = [
        (1, 1),
        (dict(a=1), dict(a=1)),
        (dict(a=1, b=2), dict(a=1, b=2)),
        # invalid expressions
        ("{{ foo }}", "{{ foo }}"),
        ("{{ foo + bar }}", "{{ foo + bar }}"),
        ("{{ foo.bar.baz }}", "{{ foo.bar.baz }}"),
        # valid expressions
        ("foo", "foo"),
        ("foo.bar", "foo.bar"),
        ('"{0}"'.format("{{ foo }}"), u"{{ foo }}"),
        ('"{0}"'.format("{{ foo.bar }}"), u"{{ foo.bar }}"),
    ]
