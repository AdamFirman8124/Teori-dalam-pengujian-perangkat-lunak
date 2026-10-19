

# Generated at 2022-06-13 15:28:07.329139
# Unit test for function safe_eval
def test_safe_eval():

    def mapped(i):
        return i * 2

    # some basic tests to make sure safe_eval is working
    assert safe_eval("1+1") == 2
    assert safe_eval("foo", dict(foo=42)) == 42
    assert safe_eval("foo.bar", dict(foo=dict(bar=42))) == 42
    assert safe_eval("1+1") == 2
    assert safe_eval("foo", dict(foo=42)) == 42
    assert safe_eval("foo.bar", dict(foo=dict(bar=42))) == 42
    assert safe_eval("[1,2,3]") == [1, 2, 3]
    assert safe_eval("{'a':1, 'b':2}") == {'a': 1, 'b': 2}

# Generated at 2022-06-13 15:28:16.611870
# Unit test for function safe_eval

# Generated at 2022-06-13 15:28:24.649940
# Unit test for function safe_eval
def test_safe_eval():
    '''
    Test that safe_eval allows only the intended expressions, and that
    it only allows those expressions to call the expected functions
    '''
    # these are all the functions we want to allow to be called
    # from expressions. Note that of course this does not "harden"
    # the code for calling these functions, we're just whitelisting
    # the ability to call them from the expression.

# Generated at 2022-06-13 15:28:34.618002
# Unit test for function safe_eval

# Generated at 2022-06-13 15:28:44.097841
# Unit test for function safe_eval
def test_safe_eval():

    # Make sure we can safely evaluate all the possible builtin types
    # That are specified in http://www.json.org/
    # We need to be able to evaluate those so that the json module can safely
    # decode the datastructure sent by the user via the command line

    assert safe_eval('42') == 42
    assert safe_eval('-42') == -42
    assert safe_eval('3.14') == 3.14
    assert safe_eval('-3.14') == -3.14
    assert safe_eval('true') is True
    assert safe_eval('false') is False
    assert safe_eval('null') is None
    assert safe_eval('["tea", "eggs", "milk", "toast"]') == ["tea", "eggs", "milk", "toast"]
    assert safe_eval

# Generated at 2022-06-13 15:28:50.602870
# Unit test for function safe_eval
def test_safe_eval():
    def assert_safe_eval(expr, expected_result, locals=None, include_exceptions=False):
        locals = locals or {}
        if include_exceptions:
            result, exception = safe_eval(to_native(expr), locals=locals, include_exceptions=True)
        else:
            result = safe_eval(to_native(expr), locals=locals)
        if include_exceptions:
            assert exception is None
        assert result == expected_result

    # Test some valid expressions
    assert_safe_eval("1 + 2", 3)
    assert_safe_eval("1 + 2", 3, locals={"foo": "bar"})
    assert_safe_eval("foo", "bar", locals={"foo": "bar"})
    assert_safe_eval("0", 0)

# Generated at 2022-06-13 15:28:59.363070
# Unit test for function safe_eval
def test_safe_eval():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.six import PY3

    platform_stdout = getattr(sys.stdout, "buffer", sys.stdout)
    platform_stdout.write(to_bytes(
        u"Testing safe_eval() w/o any restricted functions ... "))
    restricted_safe_eval = safe_eval

    # Simple tests. We don't need to test every possible case here because
    # any well-behaved Python AST evaluator should pass these tests.
    assert restricted_safe_eval("True") is True
    assert restricted_safe_eval("False") is False
    assert restricted_safe_eval("1") == 1
    assert restricted_safe_eval("1.0") == 1.0

# Generated at 2022-06-13 15:29:08.378100
# Unit test for function safe_eval
def test_safe_eval():
    """Run through a series of tests on the safe_eval() function.
    This includes invalid and potentially dangerous (even if valid)
    expressions and ensuring they have been properly escaped.
    """

    # Test proper handling of syntax errors
    assert safe_eval("{'a':1}") == "{'a':1}"
    assert safe_eval("{'a':1,}") == "{'a':1,}"
    assert safe_eval("{a':1}") == "{a':1}"
    assert safe_eval("a:1}") == "a:1}"
    assert safe_eval("{a'1") == "{a'1"
    assert safe_eval("a}") == "a}"
    assert safe_eval("{a") == "{a"

    # Test that 'str' type is allowed

# Generated at 2022-06-13 15:29:14.108019
# Unit test for function safe_eval
def test_safe_eval():
    def test(expr, expected, **kwargs):
        result, exception = safe_eval(expr, **kwargs)
        # Syntax errors return the expression back unevaluated
        if isinstance(expected, SyntaxError):
            assert result == expr
            assert isinstance(exception, SyntaxError)
        # Non-Syntax errors raise an exception
        else:
            assert result == expected
            assert exception is None

    test('{{ foo }}', '{{ foo }}')
    test('{{ foo() }}', '{{ foo() }}')
    test('{{ foo.bar() }}', '{{ foo.bar() }}')
    test('{{ foo["bar"] }}', '{{ foo["bar"] }}')
    test('{{ foo()["bar"] }}', '{{ foo()["bar"] }}')

# Generated at 2022-06-13 15:29:19.184521
# Unit test for function safe_eval

# Generated at 2022-06-13 15:29:32.866582
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval("1 + 1") == 2
    assert safe_eval("True") is True
    assert safe_eval("true") is True
    assert safe_eval("false") is False
    assert safe_eval("[]") == []
    assert safe_eval("[1,2]") == [1,2]
    assert safe_eval("{}") == {}
    assert safe_eval("{'a': 'b'}") == {'a':'b'}
    assert safe_eval("()") == ()
    assert safe_eval("(1,2)") == (1,2)
    assert safe_eval("1 < 2") is True
    assert safe_eval("1 > 2") is False
    assert safe_eval("1 * 2") == 2
    assert safe_eval("1 + 2 * 3") == 7

# Generated at 2022-06-13 15:29:40.650824
# Unit test for function safe_eval
def test_safe_eval():
    # success cases
    assert safe_eval("{{ 5 + 5 }}") == 10
    assert safe_eval("{{ 'ansible' + '_' + ('string' * 2) }}") == 'ansible_stringstring'
    assert safe_eval("{{ 'ansible' ~ '_' ~ ('string' * 2) }}") == 'ansible_stringstring'
    assert safe_eval("{{ 'ansible' ~ '_' ~ ('string' * 2) ~ '_extra' }}") == 'ansible_stringstring_extra'
    assert safe_eval("{{ ['a','b','c'] | join('_') }}") == 'a_b_c'
    assert safe_eval("{{ ('a','b','c') | join('_') }}") == 'a_b_c'

# Generated at 2022-06-13 15:29:52.081467
# Unit test for function safe_eval
def test_safe_eval():

    def safe_eval_callable(expr, locals=None):
        if C.DEFAULT_KEEP_REMOTE_FILES:
            raise Exception('test_safe_eval should not access '
                            'C.DEFAULT_KEEP_REMOTE_FILES')
        return safe_eval(expr, locals=locals)


# Generated at 2022-06-13 15:30:00.133705
# Unit test for function safe_eval
def test_safe_eval():
    # Test correct expressions
    assert safe_eval("sum([1, 2, 3])") == 6
    assert safe_eval("'x' + 'y'") == 'xy'
    assert safe_eval("1.1 * 4") == 1.1 * 4
    assert safe_eval("[True, False]") == [True, False]
    assert safe_eval("dict(a=1, b=3)") == dict(a=1, b=3)
    assert safe_eval("{'a':1, 'b':3}") == dict(a=1, b=3)
    assert safe_eval("('a', 1)") == ('a', 1)
    assert safe_eval("(1,)") == (1,)
    assert safe_eval("'a'") == 'a'
    assert safe_eval("1") == 1

# Generated at 2022-06-13 15:30:06.393828
# Unit test for function safe_eval
def test_safe_eval():
    source = "{{ {}|to_json }}"
    (result, error) = safe_eval(source, dict(a_list_variable=[1,2,3]), include_exceptions=True)
    assert result == [1,2,3]
    assert error is None

    source = "{{ a_list_variable|to_json }}"
    (result, error) = safe_eval(source, dict(a_list_variable=[1,2,3]), include_exceptions=True)
    assert result is None
    assert error is not None
    assert isinstance(error, Exception)

    source = "a_list_variable|to_json"
    (result, error) = safe_eval(source, dict(a_list_variable=[1,2,3]), include_exceptions=True)
    assert result is None

# Generated at 2022-06-13 15:30:16.863123
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval('foo is bar', {'foo': 'bar'}) == True
    assert safe_eval('foo is bar', {'foo': 'baz'}) == False
    assert safe_eval('foo == bar', {'foo': 'bar'}) == True
    assert safe_eval('foo == bar', {'foo': 'baz'}) == False
    assert safe_eval('foo in bar', {'foo': 'a', 'bar': ['a', 'b', 'c']}) == True
    assert safe_eval('foo in bar', {'foo': 'd', 'bar': ['a', 'b', 'c']}) == False
    assert safe_eval('foo == true', {'foo': True}) == True
    assert safe_eval('foo == true', {'foo': False}) == False

# Generated at 2022-06-13 15:30:25.357098
# Unit test for function safe_eval
def test_safe_eval():

    # Define our own globals (similarly to how safe_eval is called)
    MY_GLOBALS = {
        '__builtins__': {},  # avoid global builtins as per eval docs
        'false': False,
        'null': None,
        'true': True,
        # also add back some builtins we do need
        'True': True,
        'False': False,
        'None': None
    }

    # list of expressions to evaluate and the expected result of each

# Generated at 2022-06-13 15:30:31.607713
# Unit test for function safe_eval

# Generated at 2022-06-13 15:30:40.841213
# Unit test for function safe_eval

# Generated at 2022-06-13 15:30:52.598313
# Unit test for function safe_eval
def test_safe_eval():
    # basic expressions
    assert safe_eval('1 + 1') == 2
    # dicts
    assert safe_eval('{"foo": "bar"}') == {'foo': 'bar'}
    # lists
    assert safe_eval('["foo", "bar"]') == ['foo', 'bar']
    # tuples
    assert safe_eval('("foo", "bar")') == ('foo', 'bar')
    # sets
    assert safe_eval('set([1, 2, 3])') == set([1, 2, 3])
    # None
    assert safe_eval('None') is None

    # booleans
    assert safe_eval('true') is True
    assert safe_eval('false') is False
    assert safe_eval('True') is True
    assert safe_eval('False') is False

    # invalid expressions

# Generated at 2022-06-13 15:31:07.059588
# Unit test for function safe_eval
def test_safe_eval():

    if C.DEFAULT_BECOME:
        # This test is only relevant when not using privilege escalation

        # Good expression
        assert safe_eval("1 + 1") == 2
        assert safe_eval("var1 + var2", dict(var1=1, var2=1)) == 2
        assert safe_eval("var1 == 1", dict(var1=1))
        assert safe_eval("var1 in [ 1, 2, 3 ]", dict(var1=1))
        assert safe_eval("var1 + ' ' + var2", dict(var1='hello', var2='world')) == 'hello world'
        assert safe_eval("var1 + var2", dict(var1='hello', var2=1)) == 'hello1'
        assert safe_eval("1 + 1") == 2

# Generated at 2022-06-13 15:31:11.751199
# Unit test for function safe_eval
def test_safe_eval():
    def run_test(test_name, expr, expected_output, expected_error=None):
        output, error = safe_eval(expr, include_exceptions=True)

        assert output == expected_output, \
            'test "%s" failed: expected %s, got %s' \
            % (test_name, expected_output, output)

        assert error is None or error.__class__.__name__ == expected_error, \
            'test "%s" failed: expected exception %s, got %s' \
            % (test_name, expected_error, error)

    # basic tests
    run_test('1+2', '1+2', 3)
    run_test('[1,2,3]', '[1,2,3]', [1, 2, 3])

# Generated at 2022-06-13 15:31:20.007079
# Unit test for function safe_eval
def test_safe_eval():
    unevaluated_expr = "[1,2,3]"
    evaluated_res = safe_eval(unevaluated_expr)
    assert evaluated_res == [1, 2, 3]

    unevaluated_expr = "1"
    evaluated_res = safe_eval(unevaluated_expr)
    assert evaluated_res == 1

    expr = "sum([n for n in a_list_variable if n%2==0], 0)"
    # use eval for comparison
    try:
        result = eval(expr)
        assert isinstance(result, int)
    except Exception as e:
        if C.DEFAULT_DEBUG:
            print("Exception: %s" % str(e), file=sys.stderr)

    glob = {'a_list_variable': [2, 3, 4, 6]}

# Generated at 2022-06-13 15:31:30.578037
# Unit test for function safe_eval
def test_safe_eval():
    enabled_safe_builtins = C.DEFAULT_ALLOWED_BUILTINS

# Generated at 2022-06-13 15:31:37.435508
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval("[1,2]") == [1,2]
    assert safe_eval("{1:2}") == {1:2}
    assert safe_eval("foo['bar']") == "foo['bar']"
    assert safe_eval("foobar") == "foobar"
    assert safe_eval("foobar", {'foobar': 'barfoo'}) == "barfoo"
    assert safe_eval("1 + 1") == 2
    assert safe_eval("1 + 1", include_exceptions=True) == (2, None)
    assert safe_eval("1 + 1", {'true': True}, include_exceptions=True) == (2, None)
    assert safe_eval("1 in [1,2]") == True

# Generated at 2022-06-13 15:31:45.161834
# Unit test for function safe_eval

# Generated at 2022-06-13 15:31:55.324739
# Unit test for function safe_eval
def test_safe_eval():
    # No exception, simple string
    value = safe_eval('"simple string"')
    assert value == 'simple string'

    # No exception, simple list
    value = safe_eval('[1, 2, 3]')
    assert value == [1, 2, 3]

    # No exception, simple map
    value = safe_eval('{"foo": "bar"}')
    assert value == {"foo": "bar"}

    # No exception, unicode string
    value = safe_eval(u'"foob\xe4r"')
    assert value == u'foob\xe4r'

    # No exception, simple json boolean
    value = safe_eval('true')
    assert value is True

    # No exception, simple json null
    value = safe_eval('null')
    assert value is None

    # No exception, simple json boolean

# Generated at 2022-06-13 15:32:05.889066
# Unit test for function safe_eval
def test_safe_eval():
    # type: () -> None
    '''
    If error occurs in safe_eval, it will print the error message to sys.stderr.
    This is not a desired behavior in unit test.
    The mock module can be used to help patch this behavior.
    To use the mock module, the patch function is called to replace a function
    with a mock object. In our case, sys.stderr is replaced.
    Then the mock object is used to verify that we get the right stderr message.
    '''
    try:
        from unittest.mock import patch, Mock
    except ImportError:
        from mock import patch, Mock

    #####################
    # Invalid expressions
    #####################
    # Expressions involving builtins
    # Note: the expression will be returned as a string
    expr = 'True or False'
    result

# Generated at 2022-06-13 15:32:17.928657
# Unit test for function safe_eval
def test_safe_eval():
    # Basic constant value tests
    # Test integers
    assert safe_eval("1") == 1
    assert safe_eval("-1") == -1
    # Test strings
    assert safe_eval("'test'") == 'test'
    assert safe_eval("'true'") == 'true'
    assert safe_eval('"test"') == 'test'
    # Test floats
    assert safe_eval("0.5") == 0.5
    assert safe_eval("-0.5") == -0.5
    # Test JSON booleans
    assert safe_eval("true") is True
    assert safe_eval("false") is False
    # Test null
    assert safe_eval("null") is None

    # Basic expression group tests
    # Test integer addition
    assert safe_eval("1 + 1") == 2
    assert safe_

# Generated at 2022-06-13 15:32:29.916477
# Unit test for function safe_eval
def test_safe_eval():
    # Test simple things with safe_eval
    assert safe_eval("[1,2,3,4]") == [1, 2, 3, 4]
    assert safe_eval("'a string'") == 'a string'
    assert safe_eval("1234") == 1234
    assert safe_eval("(1,2,3)") == (1, 2, 3)
    assert safe_eval("{'one':'two', 'three':'four'}") == {'one': 'two', 'three': 'four'}

    # Test simple math
    assert safe_eval("1 + 2") == 3
    assert safe_eval("1 + 2 - 3") == 0
    assert safe_eval("1 + 2 * 3 - 4") == 3
    assert safe_eval("4 - 4 / 1") == 4

    # Test for list literal

# Generated at 2022-06-13 15:32:42.384730
# Unit test for function safe_eval
def test_safe_eval():
    successful = 0
    failed = []


# Generated at 2022-06-13 15:32:52.685019
# Unit test for function safe_eval

# Generated at 2022-06-13 15:33:02.822398
# Unit test for function safe_eval
def test_safe_eval():
    '''
    This function includes a unit test for the safe_eval() function. It is not
    currently being used for anything else.
    '''

    def _test_string(expr, expected_value):
        result, exception = safe_eval(expr, include_exceptions=True)
        if exception:
            print("ERROR: Expression '%s' failed with exception '%s'" % (expr, exception))
        elif isinstance(expected_value, Exception):
            print("ERROR: Expected exception for expression '%s'. Got '%s'" % (expr, result))
        elif result != expected_value:
            print("ERROR: Expression '%s' did not return expected result. Expected '%s'. Got '%s'." % (expr, expected_value, result))

    print('Testing safe_eval...')
    _test_

# Generated at 2022-06-13 15:33:14.476355
# Unit test for function safe_eval
def test_safe_eval():
    # Test safe_eval() on the examples which failed in ansible 2.1.1.1

    # We include match tests for both 2.6 and 2.7 because 2.6 and 2.7 have
    # different exceptions which we don't want to have to handle on each test.

    expr = "{{ 'a' + 'b' }}"
    result = safe_eval(expr)
    assert result == "ab"

    expr = "{{ 'a' + 'b' }}"
    result = safe_eval(expr, include_exceptions=True)
    assert result[0] == "ab" and result[1] is None

    expr = "{{ 'a' + 'b' }}"
    result = safe_eval(expr, include_exceptions=False)
    assert result == "ab"


# Generated at 2022-06-13 15:33:25.215852
# Unit test for function safe_eval

# Generated at 2022-06-13 15:33:31.528474
# Unit test for function safe_eval
def test_safe_eval():
    # Code from the module utils.safe_eval documentation
    expr = '''
[item for item in sequence if item.attribute == 'value']
'''
    expr = '''
{ key: value for (key, value) in mapping }
'''
    # Expected result

# Generated at 2022-06-13 15:33:42.428825
# Unit test for function safe_eval
def test_safe_eval():
    # Test simple (but valid) expression
    assert 2 == safe_eval('1 + 1')

    # Test string input
    assert 'hello world' == safe_eval("'hello world'")

    # Test escaping
    assert b'hello world' == safe_eval("b'hello world'")

    # Test a dict expression
    assert dict(abc='def') == safe_eval("{'abc': 'def'}")

    # Test a list expression
    assert [1, 2, 3] == safe_eval("[1, 2, 3]")

    # Test a list expression with a dict
    assert [1, dict(abc='def')] == safe_eval("[1, dict(abc='def')]")

    # Test a dict containing a list

# Generated at 2022-06-13 15:33:54.032178
# Unit test for function safe_eval
def test_safe_eval():

    def _assert_safe_eval(expr, desired_result):
        result = safe_eval(expr)
        assert(expr)
        assert(desired_result == result)

    # valid expressions
    _assert_safe_eval("3", 3)
    _assert_safe_eval("3 + 3", 6)
    _assert_safe_eval("'test'", "test")
    _assert_safe_eval("'test' + 'test'", "testtest")
    _assert_safe_eval("'test' * 3", "testtesttest")
    _assert_safe_eval("['test', 'test2', 'test3']", ['test', 'test2', 'test3'])

# Generated at 2022-06-13 15:34:02.893771
# Unit test for function safe_eval
def test_safe_eval():
    def _test_safe_eval(expr, expected_result, fail_msg=None):
        result, exception = safe_eval(expr, include_exceptions=True)
        assert result == expected_result, fail_msg
        assert exception is None, fail_msg

        # make sure it works without include_exceptions too
        result = safe_eval(expr)
        assert result == expected_result, fail_msg

    _test_safe_eval("True", True, "Failed to evaluate a normal value")
    _test_safe_eval("[1,2,3]", [1, 2, 3], "Failed to evaluate a list literal")
    _test_safe_eval("{'foo':'bar'}", {'foo': 'bar'}, "Failed to evaluate a dict literal")

# Generated at 2022-06-13 15:34:10.727048
# Unit test for function safe_eval
def test_safe_eval():
    # Basic sanity tests
    assert safe_eval('true') is True
    assert safe_eval('null') is None
    assert safe_eval('1 + 2') == 3
    assert safe_eval('(1,2)') == (1, 2)
    assert safe_eval('[1, 2]') == [1, 2]
    assert safe_eval('dict(a=1, b=2)') == dict(a=1, b=2)
    assert safe_eval('"foo"') == "foo"

    # Literal value objects are valid
    lit_true = ast.Constant(True, kind=None)
    assert safe_eval(lit_true, include_exceptions=True) == (True, None)

    # Test basic invalid expressions

    # Test invalid expression node types
    lit_delete = ast.Delete()
   

# Generated at 2022-06-13 15:34:22.710481
# Unit test for function safe_eval
def test_safe_eval():
    pass_list = ['[7]', '[7, 8, 9]', '[1, 2, 3, 4, 5, 6]', '[]']
    fail_list = ['[1, 2, 3', '[1, 2, 3, [, ]', '', '[7, 8, 9, foo]']
    for item in pass_list:
        assert safe_eval(item) == ast.literal_eval(item)
    for item in fail_list:
        assert safe_eval(item) == item



# Generated at 2022-06-13 15:34:28.362137
# Unit test for function safe_eval

# Generated at 2022-06-13 15:34:37.258075
# Unit test for function safe_eval
def test_safe_eval():
    # No errors raised
    assert safe_eval("['a', 'b']") == ['a', 'b']
    assert safe_eval("['a', 'b', 1]") == ['a', 'b', 1]
    assert safe_eval("['a', 'b', 1, 2]") == ['a', 'b', 1, 2]
    assert safe_eval("['a', 'b', 1, 2, 3]") == ['a', 'b', 1, 2, 3]
    assert safe_eval("['a', 'b', 1, 2, 3, 4]") == ['a', 'b', 1, 2, 3, 4]
    assert safe_eval("['a', 'b', 1, 2, 3, 4, 5]") == ['a', 'b', 1, 2, 3, 4, 5]

# Generated at 2022-06-13 15:34:41.461178
# Unit test for function safe_eval
def test_safe_eval():
    examples = '/path/to/file'
    try:
        assert safe_eval('/bin/ls') == '/bin/ls'
        assert safe_eval('/bin/ls', include_exceptions=True) == ('/bin/ls', None)
        assert safe_eval('/bin/ls', include_exceptions=True)[0] == '/bin/ls'
        assert safe_eval('/bin/ls', include_exceptions=True)[1] is None
    except Exception as e:
        print('exception caught! (%s)' % to_native(examples))
        sys.exit(1)

    for i in string_types:
        assert isinstance(safe_eval(i, include_exceptions=True), string_types)


# Generated at 2022-06-13 15:34:48.283757
# Unit test for function safe_eval
def test_safe_eval():
    '''
    tests safe_eval to make sure we return the value that Jinja2 would return
    '''


# Generated at 2022-06-13 15:34:52.890087
# Unit test for function safe_eval
def test_safe_eval():
    good_cases = [
        ('[1, 2, 3]', [1, 2, 3]),
        ('{1: 2, 3: 4}', {1: 2, 3: 4}),
        ('"hello"', "hello"),
    ]
    for test, answer in good_cases:
        result = safe_eval(test)
        if result != answer:
            print("ERROR: %s eval'd to %s instead of %s" % (test, result, answer))
    bad_cases = [
        '__import__("os").listdir("/")',
        '1 + __import__("os").listdir("/")',
        '__builtins__.__import__("os").listdir("/")',
        '1 + __builtins__.__import__("os").listdir("/")',
    ]


# Generated at 2022-06-13 15:35:02.672935
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval('[1, "a", {"foo": "bar"}]', []) == [1, "a", {"foo": "bar"}]
    assert safe_eval('"a"') == "a"
    assert safe_eval('a_string', {'a_string': '123'}) == "123"
    assert safe_eval('[1, 2, a_string]', {'a_string': '123'}) == [1, 2, "123"]
    assert safe_eval('{"a": 1} + {"b": 2}') == {"a": 1, "b": 2}

    result, exception = safe_eval('1 + __import__("os")', {}, True)

# Generated at 2022-06-13 15:35:11.860788
# Unit test for function safe_eval
def test_safe_eval():
    import unittest

    # If a string type is passed to the function then it is checked
    # if it is safe for evaluation
    list_expression = "[4,5,6]"
    dict_expression = "{'test1':'test2','test3':'test4'}"
    booleans = "false or true and not false"

    assert safe_eval(list_expression) == [4, 5, 6]
    assert safe_eval(dict_expression) == {'test3': 'test4', 'test1': 'test2'}
    assert safe_eval(booleans) == True

    # Only certain AST nodes are allowed
    class Foo(object):
        pass

    class Bar(object):
        pass


# Generated at 2022-06-13 15:35:20.705011
# Unit test for function safe_eval
def test_safe_eval():
    # These tests fail on Python 3.4 due to our usage of the ast module.
    # For now, we should test them on Python 2.7 only
    if sys.version_info[0] == 2:

        # This expression should evaluate to True
        expr = "x == 2 or x == 3 or x == 5"

        # None of these variables should pass the whitelist

# Generated at 2022-06-13 15:35:30.373321
# Unit test for function safe_eval
def test_safe_eval():
    # try a simple expression
    assert safe_eval("1+2") == 3
    assert safe_eval("foo=='bar'") == False

    # try a more complex containing dicts and lists
    assert safe_eval("[1,2,3]+[4,5,6]") == [1, 2, 3, 4, 5, 6]
    assert safe_eval("foo.bar|d({'la':'te'})|list") == [{'la': 'te'}]

    # try an invalid expression
    #    assert safe_eval("__import__('os').system('ls')") == "__import__('os').system('ls')"
    assert safe_eval("__import__('os').system('ls')") == "__import__('os').system('ls')"

    # try a valid expression with an invalid function


# Generated at 2022-06-13 15:35:45.622602
# Unit test for function safe_eval
def test_safe_eval():
    def test_eval(expr, expected_result):
        if isinstance(expr, (dict, list)):
            # These expressions are already templated and should not be
            # passed through safe_eval
            result, exc = safe_eval(expr, include_exceptions=True)
            assert result == expr, "safe_eval: bad result for '%s'" % expr
            assert not exc, "safe_eval: unexpected exception for '%s'" % expr
        else:
            # These expressions should be strings and should be passed
            # through safe_eval to be evaluated
            result, exc = safe_eval(expr, include_exceptions=True)
            assert exc == expected_result, "safe_eval: bad result for '%s'" % expr

    # First test some strings that should NOT be evaluated

# Generated at 2022-06-13 15:35:54.197517
# Unit test for function safe_eval
def test_safe_eval():

    # check for exceptions during safe_eval
    test_expr = "{{ lookup('name') }}"
    result, exception = safe_eval(test_expr, include_exceptions=True)
    assert(exception is not None)

    # check positive testing case
    test_expr = "{{ [1, 1, 2] }}"
    result = safe_eval(test_expr)
    assert(result == [1, 1, 2])

    # check exception is thrown and caught on invalid expression.
    # Not all syntax errors are caught. Fallback to old behavior
    # by returning the expression when an exception is caught.
    test_expr = "{{ {{ {} }} }}"
    result = safe_eval(test_expr)
    assert(result == test_expr)


# Generated at 2022-06-13 15:36:04.198291
# Unit test for function safe_eval
def test_safe_eval():
    """
    This is a unit test for function safe_eval. It will test basic use-cases of the function.
    """
    import os
    import random

    list_of_expression = [
        "{{ mylist }}",
        "mylist",
        "",
        "{{ 'Hello' if mylist|length == 3 }}",
        "{{ 'Hello' if mylist|length == 3 }}",
        "a_list_variable",
        "",
        "[1, 2, 3]",
        "{}",
        "None",
        "True",
        "False",
        "''",
        "A == 'B'",
        "C == D",
        "[]",
        "()"
    ]


# Generated at 2022-06-13 15:36:12.099318
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval("a and b") == "a and b"
    assert safe_eval("'a' and 'b'") == "'a' and 'b'"
    assert safe_eval("a and b", {"a": "x", "b": "y"}) == "xy"
    assert safe_eval("a and b", {"a": "x", "b": False}) == "x"
    assert safe_eval("a and b", {"a": None, "b": False}) is None
    assert safe_eval("a and b", {"a": None, "b": None}) is None
    assert safe_eval("a and b", {"a": "", "b": ""}) == ""
    assert safe_eval("a and b", {"a": 0, "b": 0}) == 0

# Generated at 2022-06-13 15:36:21.833702
# Unit test for function safe_eval
def test_safe_eval():
    import ast
    import sys
    from ansible.module_utils.common.text.converters import container_to_text

    # test one exception at a time
    # following jinja2 syntax we changed from '.' to '_'

    # syntax error
    expr = '{{{{{ var1}}}}}}'
    try:
        result = safe_eval(expr)
    except Exception as e:
        # SyntaxError exceptions are not caught
        if type(e) is not SyntaxError:
            print("***Wrong exception***")
            sys.exit(1)
    else:
        print("***SyntaxError not caught***")
        sys.exit(1)

    # unsupported node type
    expr = '1+1'
    ast.Add.__class__ = ast.LShift

# Generated at 2022-06-13 15:36:29.609688
# Unit test for function safe_eval
def test_safe_eval():
    # Success tests
    safe_eval('8')
    safe_eval(8)
    safe_eval('8.0')
    safe_eval(8.0)
    safe_eval('-8')
    safe_eval(-8)
    safe_eval('True')
    safe_eval(True)
    safe_eval('False')
    safe_eval(False)
    safe_eval('"a string"')
    safe_eval('null')
    safe_eval('True or False')
    safe_eval('True and False')
    safe_eval('1 < 8')
    safe_eval('-8 + 8')
    safe_eval('8 - 6')
    safe_eval('10 / 2')
    safe_eval('5 * -2')
    safe_eval('-8')

# Generated at 2022-06-13 15:36:35.586410
# Unit test for function safe_eval
def test_safe_eval():
    # These tests should pass
    assert(safe_eval("1 + 3") == 4)
    assert(safe_eval("[1, 2, 3] + [4, 5, 6]") == [1, 2, 3, 4, 5, 6])
    assert(safe_eval("1 + 2 > 4"))
    assert(safe_eval("1 == 1") == True)
    assert(safe_eval("1 == 2") == False)
    assert(safe_eval("1 != 1") == False)
    assert(safe_eval("1 != 2") == True)
    assert(safe_eval("1 < 2") == True)
    assert(safe_eval("4 > 2") == True)
    assert(safe_eval("1 <= 2") == True)
    assert(safe_eval("2 <= 2") == True)

# Generated at 2022-06-13 15:36:44.062849
# Unit test for function safe_eval
def test_safe_eval():
    # This example picks out the "unified_job" portion of the job
    # template path to identify the job type for a project update.
    example1 = "${playbook.job_template.unified_job_template.unified_job_type}"

    # This example picks out the "name" attribute of a VLAN object
    # to initialize a variable in the playbook.
    example2 = "${vlan.name}"

    # This example creates an array of VLAN names.
    example3 = "[% for vlan in vlans %]${vlan.name}[% endfor %]"

    # A 'clever' user (or attacker) could try to sneak something into a
    # playbook that should not run, such as a password generator or
    # system command.
    evil1 = "${password()}"

# Generated at 2022-06-13 15:36:55.562683
# Unit test for function safe_eval
def test_safe_eval():
    assert False == safe_eval('false')
    assert True == safe_eval('true')
    assert None == safe_eval('null')
    assert 42 == safe_eval('42')
    assert 42 == safe_eval('true + 42')
    assert [1, 2, 3] == safe_eval('[1,2,3]')
    assert (1, 2, 3) == safe_eval('(1,2,3)')
    assert 'abc' == safe_eval('"abc"')
    assert 'abc' == safe_eval('u"abc"')
    assert u'abc' == safe_eval(u'"abc"')
    assert 'abc' == safe_eval('"ab" + "c"')
    assert 'ab' + 'c' == safe_eval('"ab" + "c"')

# Generated at 2022-06-13 15:37:03.927346
# Unit test for function safe_eval

# Generated at 2022-06-13 15:37:34.778584
# Unit test for function safe_eval
def test_safe_eval():
    # simple tests should pass
    safe_eval("{ 'a': 1 }")
    # some not-so-simple examples which should pass (or fail)
    safe_eval("['a', 'b']")
    safe_eval("('a', 'b')")
    safe_eval("0xFFFF")
    safe_eval("2+2")
    safe_eval("2+-2")
    safe_eval("{'a': 'a', 'b': 'b'}")
    safe_eval("{'a': 'a', 'b': ['b', 'b']}")
    safe_eval("{'a': ['a', 'a'], 'b': 'b'}")
    safe_eval("{'a': ['a', 'a'], 'b': ['b', 'b']}")
    # test that calls to built

# Generated at 2022-06-13 15:37:44.379298
# Unit test for function safe_eval
def test_safe_eval():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    # Tests for unsafe_proxy
    expr = "[1]"
    safe_test = safe_eval(expr)
    assert isinstance(safe_test, list)
    expr = AnsibleUnsafeText("[1]")
    safe_test = safe_eval(expr)
    assert isinstance(safe_test, list)

    # Test for dict
    expr = 'dict(a=1, b=2)'
    safe_test = safe_eval(expr)
    assert isinstance(safe_test, dict)
    assert safe_test == {'a': 1, 'b': 2}

    # Test for list
    expr = '[1, 2]'
    safe_test = safe_eval(expr)
    assert isinstance(safe_test, list)

# Generated at 2022-06-13 15:37:54.523469
# Unit test for function safe_eval
def test_safe_eval():
    # Test to see if numeric value is extracted from string
    string_value = '1'
    assert safe_eval(string_value) == 1

    # Test to see if numeric value is extracted from string containing number and word
    string_value = '1 dogs'
    assert safe_eval(string_value) == 1

    # Test to see if string value is returned when string contains no numeric values
    string_value = 'dogs only'
    assert safe_eval(string_value) == string_value

    # Test to see if string value is returned when string contains list of numbers
    string_value = '[1, 2, 3]'
    assert safe_eval(string_value) == string_value

    # Test to see if string value is returned when string contains list of numbers and words
    string_value = '[1, 2, 3] dogs'
    assert safe