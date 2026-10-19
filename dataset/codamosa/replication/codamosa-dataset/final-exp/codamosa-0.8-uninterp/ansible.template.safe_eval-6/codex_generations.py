

# Generated at 2022-06-13 15:28:06.541028
# Unit test for function safe_eval

# Generated at 2022-06-13 15:28:15.863843
# Unit test for function safe_eval
def test_safe_eval():
    print("Testing safe_eval()...")

    def compare_result(expr, expected, locals=None, include_exceptions=False):
        (res, err) = safe_eval(expr, locals, include_exceptions)
        if res == expected:
            print("Pass: safe_eval('%s') gave the expected result." % expr)
        else:
            print("Fail: safe_eval('%s') gave '%s' instead of the expected '%s'." % (expr, res, expected))
            if err is not None:
                print("Exception was: %s" % err)
            sys.exit(1)

    # Simple cases
    compare_result('[]', [])
    compare_result('{}', {})
    compare_result('2 + 2', 4)

# Generated at 2022-06-13 15:28:24.088622
# Unit test for function safe_eval

# Generated at 2022-06-13 15:28:31.848105
# Unit test for function safe_eval
def test_safe_eval():
    test_pass_input = "item"
    test_pass_return = "item"
    test_fail_input = "list('abc')"
    test_fail_return = "list('abc')"

    test_pass = safe_eval(test_pass_input)
    test_fail = safe_eval(test_fail_input)

    assert type(test_pass) == type(test_pass_return)
    assert test_pass == test_pass_return

    assert type(test_fail) == type(test_fail_return)
    assert test_fail == test_fail_return


# Generated at 2022-06-13 15:28:38.439948
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval("1") == 1
    assert safe_eval("foo") == "foo"
    assert safe_eval("foo.bar()") == "foo.bar()"
    assert safe_eval("foo.bar[1]") == "foo.bar[1]"
    assert safe_eval("foo.bar.baz()") == "foo.bar.baz()"
    assert safe_eval("foo.bar.baz[1]") == "foo.bar.baz[1]"
    assert safe_eval("foo.bar.baz[1].ding()") == "foo.bar.baz[1].ding()"
    assert safe_eval("foo.bar.baz[1].ding.dong()") == "foo.bar.baz[1].ding.dong()"

# Generated at 2022-06-13 15:28:46.687498
# Unit test for function safe_eval
def test_safe_eval():
    result, exception = safe_eval("['a','b','c']", include_exceptions=True)
    assert result == ['a', 'b', 'c']
    assert exception is None

    result, exception = safe_eval("['a', 'b', 'c']", include_exceptions=True)
    assert result == ['a', 'b', 'c']
    assert exception is None

    result, exception = safe_eval("['a', 'b', 'c']", include_exceptions=True)
    assert result == ['a', 'b', 'c']
    assert exception is None

    result, exception = safe_eval("[1, 2, 3]", include_exceptions=True)
    assert result == [1, 2, 3]
    assert exception is None


# Generated at 2022-06-13 15:28:54.409425
# Unit test for function safe_eval
def test_safe_eval():
    # Ensure the function behaves as expected
    assert safe_eval('[1, 2]') == [1, 2]

    # Ensure the function sanitizes potentially harmful calls
    assert safe_eval('__import__("os").remove("/etc/passwd")') == '__import__("os").remove("/etc/passwd")'
    assert safe_eval('open("/etc/passwd")') == 'open("/etc/passwd")'

    # Ensure the function fails if error is True
    assert safe_eval('[1, 2, 3', include_exceptions=True)[0] == '[1, 2, 3'
    assert isinstance(safe_eval('[1, 2, 3', include_exceptions=True)[1], SyntaxError)

    # Ensure we can specify a custom locals()/globals()
    assert safe_eval

# Generated at 2022-06-13 15:29:00.770958
# Unit test for function safe_eval
def test_safe_eval():
    ''' Unit tests for function ansible.module_utils.common.eval.safe_eval '''
    import ast

    result = safe_eval('["foo", "bar"]', dict(), include_exceptions=True)
    assert result[0] == ["foo", "bar"]
    assert result[1] is None

    result = safe_eval('["foo", "bar"]', dict(), include_exceptions=False)
    assert result == ["foo", "bar"]

    result = safe_eval('foo', dict(foo="bar"), include_exceptions=True)
    assert result[0] == "bar"
    assert result[1] is None

    result = safe_eval('foo', dict(foo="bar"), include_exceptions=False)
    assert result == "bar"


# Generated at 2022-06-13 15:29:09.237836
# Unit test for function safe_eval
def test_safe_eval():
    expr = 'a | int * 3'
    result = safe_eval(expr)
    assert result == expr, "safe_eval should not allow pipes"

    expr = 'dict(a=1, b=2)'
    result = safe_eval(expr)
    assert isinstance(result, dict), "safe_eval should allow dicts"

    expr = 'list(v1, v2)'
    v1 = 'a'
    v2 = 'b'
    result = safe_eval(expr, locals={'v1': v1, 'v2': v2})
    assert isinstance(result, list) and v1 in result and v2 in result, "safe_eval should allow lists"

    expr = '{v1: v2}'
    v1 = 'a'
    v2 = 'b'
    result = safe_

# Generated at 2022-06-13 15:29:18.713442
# Unit test for function safe_eval
def test_safe_eval():
    expr = 'foo.bar'
    result = safe_eval(expr)
    assert result is None

    expr = 'foo.bar[0]'
    result = safe_eval(expr)
    assert result is None

    expr = 'foo.bar[0].baz'
    result = safe_eval(expr)
    assert result is None

    expr = 'foo["bar"][0].baz'
    result = safe_eval(expr)
    assert result is None

    expr = 'foo["bar"][0].baz[1]'
    result = safe_eval(expr)
    assert result is None

    expr = 'foo.bar[0].baz[1]["aaa"]'
    result = safe_eval(expr)
    assert result is None

    expr = 'foo + 1'

# Generated at 2022-06-13 15:29:25.951288
# Unit test for function safe_eval

# Generated at 2022-06-13 15:29:34.866986
# Unit test for function safe_eval
def test_safe_eval():
    # Test that valid expressions work
    assert safe_eval('1 + 1') == 2
    assert safe_eval('1 + 1', {'key': 'value'}) == 2
    assert safe_eval('1 + 1', {}, True) == (2, None)
    assert safe_eval('1 + 1', {'key': 'value'}, True) == (2, None)

    # Test basic but invalid expressions
    assert safe_eval('1 + ') == '1 + '
    assert safe_eval('1 + ', {}, True) == ('1 + ', None)
    assert safe_eval('1 + ', {}, True) == ('1 + ', None)
    assert safe_eval('1 + ', {'key': 'value'}, True) == ('1 + ', None)

    # Test the raise of an exception

# Generated at 2022-06-13 15:29:40.495979
# Unit test for function safe_eval
def test_safe_eval():
    # These tests are specific to Python3; we use the builtin
    # 'bool' callable, which is not present in Python 2.  This
    # is important because we are specifically trying to ensure
    # external callables cannot be called in safe_eval
    if sys.version_info[0] < 3:
        return True


# Generated at 2022-06-13 15:29:52.081008
# Unit test for function safe_eval
def test_safe_eval():
    # test_string_unacceptable_syntax
    expr = "['a', 'b']"
    try:
        result = safe_eval(expr)
        raise Exception("Should have failed for : %s " % expr)
    except Exception as e:
        pass

    # test_string_identifier_not_defined
    expr = "a"
    try:
        result = safe_eval(expr, locals={"b": 2, "c": 3})
        raise Exception("Should have failed for : %s " % expr)
    except Exception as e:
        pass

    # test_string_identifier_defined
    expr = "b + c"
    result = safe_eval(expr, locals={"b": 2, "c": 3})
    assert result == 5

    # test_numeric
    expr = 4

# Generated at 2022-06-13 15:30:00.144276
# Unit test for function safe_eval
def test_safe_eval():
    '''
    Test function safe_eval
    '''
    (ret, exc) = safe_eval('2+2', include_exceptions=True)
    assert exc is None, "expected no exception. Got %s" % exc
    assert ret == 4

    (ret, exc) = safe_eval('dict(a=1,b=2)', include_exceptions=True)
    assert exc is None, "expected no exception. Got %s" % exc
    assert ret == {'a': 1, 'b': 2}

    (ret, exc) = safe_eval('foo', include_exceptions=True)
    assert exc is None, "expected no exception. Got %s" % exc
    assert ret == 'foo'

    (ret, exc) = safe_eval('[1,2,3]', include_exceptions=True)

# Generated at 2022-06-13 15:30:05.926931
# Unit test for function safe_eval
def test_safe_eval():
    # Various cases where the input is good.
    assert safe_eval("True") is True
    assert safe_eval("1") == 1
    assert safe_eval("False") is False
    assert safe_eval("null") is None
    assert safe_eval("true") is True
    assert safe_eval("1") == 1
    assert safe_eval("false") is False
    assert safe_eval("null") is None
    assert safe_eval("'hello'") == 'hello'
    assert safe_eval("['a', true, 1, null]") == ['a', True, 1, None]
    assert safe_eval("{'a': true, 'b': 1, 'c': null}") == {'a': True, 'b': 1, 'c': None}
    assert safe_eval("-3") == -3
    assert safe_

# Generated at 2022-06-13 15:30:16.138461
# Unit test for function safe_eval

# Generated at 2022-06-13 15:30:24.767893
# Unit test for function safe_eval
def test_safe_eval():
    '''
    Basic unit test for the "safe_eval" function
    '''

    def _test_safe_eval(expr, expected, globals=None, locals=None):
        '''
        Helper function to test safe_eval
        '''
        if globals is None:
            globals = {}
        if locals is None:
            locals = {}
        res = safe_eval(expr, locals=locals, include_exceptions=True)
        if (expected, None) != res:
            print("For '{0}' result='{1}' expected='{2}'".format(expr, res, (expected, None)))
            sys.exit(1)

    # Test the error mode

# Generated at 2022-06-13 15:30:31.156811
# Unit test for function safe_eval

# Generated at 2022-06-13 15:30:40.365954
# Unit test for function safe_eval
def test_safe_eval():
    # test safe_eval
    # lists
    assert safe_eval('[1,2,3]') == [1,2,3]
    assert safe_eval('[1,2,a]', dict(a=3)) == [1,2,3]
    assert safe_eval('[1,2,a]', dict(a=3), include_exceptions=True) == ([1,2,3], None)
    # potentially unsafe, but using available builtins
    assert safe_eval('zip([1,2],[2,3])') == [(1, 2), (2, 3)]
    # disallowed builtin
    assert safe_eval('__import__("os").path.exists("/proc/cpuinfo")') == '__import__("os").path.exists("/proc/cpuinfo")'
    # forbidden builtin


# Generated at 2022-06-13 15:30:53.396980
# Unit test for function safe_eval
def test_safe_eval():

    # Simple test - should return the value of the expression
    assert safe_eval('foo == bar') is None

    # Try a comparison
    assert safe_eval('foo < bar or foo > bar or foo == bar') is None

    # Should return strings
    assert isinstance(safe_eval('foo'), string_types)

    # Should return True
    assert safe_eval('None == None') is True

    # Should return an empty list
    assert safe_eval('dict1 = {}') == {}

    # Should return a dict
    assert safe_eval('dict1 = {"test": 1}') == {"test": 1}

    # Should return an empty tuple
    assert safe_eval('()') == ()

    # Should return a tuple
    assert safe_eval('(1, 2, 3)') == (1, 2, 3)

    # Should return a

# Generated at 2022-06-13 15:30:57.246878
# Unit test for function safe_eval
def test_safe_eval():
    # Invalid expressions
    expr = "a_list_variable"
    res = safe_eval(expr)
    assert res == expr, 'Expression %s should not be valid (return original string)' % expr

    expr = "no_such_variable"
    res = safe_eval(expr)
    assert res == expr, 'Expression %s should not be valid (return original string)' % expr

    expr = "mylist['test'][0]"
    res = safe_eval(expr)
    assert res == expr, 'Expression %s should not be valid (return original string)' % expr

    expr = "'./mydir/myfile.conf'"
    res = safe_eval(expr)
    assert res == expr, 'Expression %s should not be valid (return original string)' % expr

    expr = "a_list_variable[0]"

# Generated at 2022-06-13 15:31:08.101671
# Unit test for function safe_eval
def test_safe_eval():
    # Note: the trailing newlines below are required when multiline strings are used.
    #       trailing whitespace is also allowed.

    # Successful expressions
    expr = "'b'"
    res = safe_eval(expr)
    assert res == 'b'

    expr = "'b' \n "
    res = safe_eval(expr)
    assert res == 'b'

    expr = "'b'    "
    res = safe_eval(expr)
    assert res == 'b'

    expr = "1 + 1"
    res = safe_eval(expr)
    assert res == 2

    expr = "1 + 1 \n "
    res = safe_eval(expr)
    assert res == 2

    expr = "1 + 1    "
    res = safe_eval(expr)
    assert res == 2


# Generated at 2022-06-13 15:31:12.883198
# Unit test for function safe_eval

# Generated at 2022-06-13 15:31:23.334389
# Unit test for function safe_eval

# Generated at 2022-06-13 15:31:32.655994
# Unit test for function safe_eval
def test_safe_eval():
    # basic tests for literal types that we support
    try:
        assert safe_eval("5") == 5
    except AssertionError:
        print("ERROR: 5 evalled to %s rather than 5" % safe_eval("5"))
        raise
    try:
        assert safe_eval("[1,2,3]") == [1, 2, 3]
    except AssertionError:
        print("ERROR [1,2,3] evalled to %s rather than [1,2,3]" % safe_eval("[1,2,3]"))
        raise
    try:
        assert safe_eval("5 + 5") == 10
    except AssertionError:
        print("ERROR: 5 + 5 evalled to %s rather than 10" % safe_eval("5 + 5"))
        raise

# Generated at 2022-06-13 15:31:39.017366
# Unit test for function safe_eval
def test_safe_eval():
    results = {}
    results["1+1"] = safe_eval("1+1")
    results["1+1==2"] = safe_eval("1+1==2")
    results["false"] = safe_eval("false")
    results["true"] = safe_eval("true")
    results["null"] = safe_eval("null")
    results["[1,2,3]"] = safe_eval("[1,2,3]")
    results["{'a':1,'b':2,'c':3}"] = safe_eval("{'a':1,'b':2,'c':3}")
    results["a==1"] = safe_eval("a==1", dict(a=1))
    results["a==2"] = safe_eval("a==2", dict(a=1))
    # We are going to fail

# Generated at 2022-06-13 15:31:41.439517
# Unit test for function safe_eval

# Generated at 2022-06-13 15:31:47.789853
# Unit test for function safe_eval

# Generated at 2022-06-13 15:31:57.056610
# Unit test for function safe_eval
def test_safe_eval():
    '''
    This function tests that safe_eval is doing what we expect.
    '''
    # pylint: disable=too-many-branches,too-many-statements
    # Generic tests

    # Whitespace test
    assert safe_eval('[ 1, 2 ]') == [1, 2]
    assert safe_eval('[ 1,2]') == [1, 2]
    assert safe_eval('[1, 2 ]') == [1, 2]
    assert safe_eval(' [ 1, 2 ]') == [1, 2]
    assert safe_eval('[ 1, 2 ] ') == [1, 2]
    assert safe_eval('[1, 2]') == [1, 2]

    # Empty list test
    assert safe_eval('[]') == []

    # Empty list test
    assert safe_eval

# Generated at 2022-06-13 15:32:06.954862
# Unit test for function safe_eval

# Generated at 2022-06-13 15:32:18.428239
# Unit test for function safe_eval

# Generated at 2022-06-13 15:32:30.174817
# Unit test for function safe_eval

# Generated at 2022-06-13 15:32:40.350018
# Unit test for function safe_eval
def test_safe_eval():
    from ansible.module_utils.six.moves import cStringIO as StringIO
    import sys

    out = StringIO()

    def test_expression(expr, result, locals=None, exception=None, enable_call=False):

        if enable_call:
            CALL_ENABLED.append(enable_call)

# Generated at 2022-06-13 15:32:47.602744
# Unit test for function safe_eval
def test_safe_eval():
    '''
    Demonstrate the basic usage of our safe_eval function.  We use
    the Python 2.7 eval() method here to show the differences in
    functionality between the two.  Look for cases where the two
    methods would behave differently to get an idea of the cases
    where this function is useful.
    '''

    # This is a valid dictionary, so both methods should be happy
    value = { 'x' : 1, 'y' : 2 }
    print("%s => %s" % (repr(value), repr(ast.literal_eval(value))))
    print("%s => %s" % (repr(value), repr(safe_eval(value))))

    # this is valid JSON and will succeed even if we don't know
    # that it's a dictionary

# Generated at 2022-06-13 15:32:55.916895
# Unit test for function safe_eval
def test_safe_eval():
    import os, sys
    parent_dir = os.path.join(os.path.dirname(__file__), "../")
    sys.path.insert(0, parent_dir)

    # Verify we are running with python3, otherwise assume python2
    if sys.version_info[0] != 3:
        print("Expected to run with python 3, actual %d" % sys.version_info[0])
        sys.exit(1)

    # should match the list of SAFE_NODES in safe_eval
    test_cases = ["'True'", "True", "False", """{'a': 'b', 'c': 'd'}"""]
    for test in test_cases:
        # Test that it works normally
        result = safe_eval(test)

# Generated at 2022-06-13 15:33:05.145261
# Unit test for function safe_eval
def test_safe_eval():
    '''
    This tests the safe_eval function
    '''

    # test invalid expressions
    invalid_exprs = [
        'with_items: {{ a_var }}',
        'with_items: "{{ a_var }}"',
        'with_items: {{ a_var.append(1) }}',
        'with_items: "{{ a_var.append(1) }}"',
        'with_items: {{ [1, 2, 3].append(1) }}',
        'with_items: "{{ [1, 2, 3] }}"',
        'with_items: "{{ {a : b} }}"',
    ]
    for unsafe_expr in invalid_exprs:
        try:
            safe_eval(unsafe_expr)
            sys.exit(1)
        except Exception:
            pass

# Generated at 2022-06-13 15:33:16.062459
# Unit test for function safe_eval

# Generated at 2022-06-13 15:33:26.992397
# Unit test for function safe_eval
def test_safe_eval():
    def _test_for_exception(s, exception_type=Exception):
        try:
            safe_eval(s)
        except exception_type:
            pass
        else:
            raise Exception("expected exception from: %s" % s)

    def _test_for_no_exception(s):
        safe_eval(s)

    # Simple expressions involving only literal values
    _test_for_no_exception(u'1 + 1')
    _test_for_no_exception(u'6 / 2')
    _test_for_no_exception(u'(1 + 1) * (6 / 2)')
    _test_for_no_exception(u'1 and 2')
    _test_for_no_exception(u'1 or 2')
    _test_for_no_ex

# Generated at 2022-06-13 15:33:33.649029
# Unit test for function safe_eval
def test_safe_eval():
    import random
    import string

    # test a random sample of possible expressions
    for x in range(0, 100):
        # generate a random expression
        expr = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(random.randint(1, 100)))

        # also generate some random parameters and include then in the evaluation
        params = {}
        for y in range(0, random.randint(0, 10)):
            key = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(random.randint(1, 100)))
            value = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(random.randint(1, 100)))
            params[key] = value



# Generated at 2022-06-13 15:33:52.991722
# Unit test for function safe_eval

# Generated at 2022-06-13 15:33:58.398982
# Unit test for function safe_eval
def test_safe_eval():
    """
    This runs the safe_eval unit test.
    :return: True if tests pass else False.
    """
    from ansible.module_utils.basic import AnsibleModule

    args = dict(
        expr='3 * 5 * 2 * 4',
    )
    module = AnsibleModule(
        argument_spec=dict(
            expr=dict(),
        )
    )
    result = safe_eval(module.params.get('expr'))
    module.exit_json(changed=False, result=result)



# Generated at 2022-06-13 15:34:06.896250
# Unit test for function safe_eval
def test_safe_eval():
    unit_test_locals = {
        'foo': 'foo',
        'bar': ('bar',),
        'boo': {'boo': 'boo'},
    }
    def safeEval(expr, locals=None, include_exceptions=False):
        return safe_eval(expr, locals=locals, include_exceptions=include_exceptions)

    ###########################################################################
    # Positive tests
    ###########################################################################
    # Literals
    assert safeEval('1') == 1
    assert safeEval('"string"') == 'string'
    assert safeEval('"unicode"') == 'unicode'
    assert safeEval('()') == ()
    assert safeEval('[]') == []
    assert safeEval('{}') == {}
    assert safeEval('True')

# Generated at 2022-06-13 15:34:15.181153
# Unit test for function safe_eval
def test_safe_eval():
    def _test_eval(expr, result):
        # This is needed for Python 2.6, for which the test_safe_eval
        # test is ignored.
        if sys.version_info < (2, 7):
            import nose
            raise nose.SkipTest()
        v = safe_eval(expr)
        assert v == result

    _test_eval('[1,2,3]', [1, 2, 3])
    _test_eval('{"foo": "bar"}', {'foo': 'bar'})
    _test_eval('{"foo": ["bar", "baz"]}', {'foo': ['bar', 'baz']})
    _test_eval('{"foo": {"bar": true}}', {'foo': {'bar': True}})

    # Test exception propagation
    class testException(Exception):
        pass

# Generated at 2022-06-13 15:34:25.484854
# Unit test for function safe_eval
def test_safe_eval():
    # Setup constants to test safe_eval with
    initial_result = None
    final_result = None
    rule_name = 'safe_eval'
    error_msg = '{0} rule failed: {1}'.format(rule_name, to_native(e))
    success_msg = '{0} rule passed'.format(rule_name)


# Generated at 2022-06-13 15:34:32.654212
# Unit test for function safe_eval
def test_safe_eval():
    # Test valid expressions
    # Pass in locals as an included argument
    assert safe_eval('1 + 1', locals={}) == 2

    # Use syck to create a dict with a 'type' value in it that would
    # not otherwise be valid YAML. It will be interpreted as a string
    # within the Jinja2 template, but then safe_eval will correctly
    # convert it to the object.
    assert safe_eval('{{ "{\"type\": null}" | from_json }}', locals={}) == {u'type': None}

    # Test invalid expressions
    try:
        safe_eval('[a]')
        assert False
    except Exception:
        assert True

    # Test exceptions
    try:
        safe_eval('[a]', include_exceptions=True)[1]
    except Exception:
        assert True


EX

# Generated at 2022-06-13 15:34:42.324277
# Unit test for function safe_eval

# Generated at 2022-06-13 15:34:51.132279
# Unit test for function safe_eval
def test_safe_eval():

    def _test(expr, expected):
        result, exception = safe_eval(expr, include_exceptions=True)
        if exception:
            print("%s => %s" % (expr, exception))
            assert False
        elif result != expected:
            print("%s => %s (expected %s)" % (expr, result, expected))
            assert False


# Generated at 2022-06-13 15:35:01.006763
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval('[1,2,3,4]') == [1,2,3,4]
    assert safe_eval('["a","b"]') == ['a', 'b']
    assert safe_eval('{"a":10}') == {'a': 10}
    assert safe_eval('{"a": {"b": 10}}') == {'a': {'b': 10}}
    assert safe_eval('4') == 4
    assert safe_eval('4 + 4') == 8
    assert safe_eval('4 - 4') == 0
    assert safe_eval('4 * 4') == 16
    assert safe_eval('4 / 4') == 1
    assert safe_eval('None') is None
    assert safe_eval('false') == False
    assert safe_eval('true') == True

# Generated at 2022-06-13 15:35:05.918546
# Unit test for function safe_eval

# Generated at 2022-06-13 15:35:18.833564
# Unit test for function safe_eval
def test_safe_eval():
    """
    We try to call a function (i.e. os.listdir()) and see if this is possible.
    This test passes if safe_eval() raises an Exception.
    """

    code = """os.listdir('.')"""
    test = safe_eval(code)
    if test:
        sys.exit(1)

if __name__ == '__main__':
    test_safe_eval()

# Generated at 2022-06-13 15:35:28.454762
# Unit test for function safe_eval
def test_safe_eval():
    test_function_list = [
        "abs",
        "all",
        "any",
        "ascii",
        "bin",
        "bool",
        "bytearray",
        "bytes",
        "chr",
        "complex",
        "divmod",
        "float",
        "format",
        "hex",
        "int",
        "len",
        "list",
        "max",
        "min",
        "next",
        "oct",
        "ord",
        "pow",
        "range",
        "reversed",
        "round",
        "set",
        "sorted",
        "str",
        "sum",
        "tuple",
        "type",
    ]

    builtin_test = []
    failed_list = []



# Generated at 2022-06-13 15:35:33.143273
# Unit test for function safe_eval
def test_safe_eval():
    GOOD_ONE = "{{ foo }}"
    GOOD_TWO = "[1,2,3,4]"
    BAD_ONE  = "{{ some_variable.func() }}"
    BAD_TWO  = "{{ some_other_variable.func() }}"
    GOOD_THREE = "[item for item in seq]"
    GOOD_FOUR = "{'key1': 1, 'key2': 2}"
    BAD_THREE = "open('/etc/passwd').read()"
    data = [GOOD_ONE, GOOD_TWO, BAD_ONE, BAD_TWO, GOOD_THREE, BAD_THREE, GOOD_FOUR]

    for item in data:
        (ans, err) = safe_eval(item, include_exceptions=True)
        print("%s => %s" % (item, ans))

# Generated at 2022-06-13 15:35:40.392306
# Unit test for function safe_eval
def test_safe_eval():
    '''
    Test function to ensure that safe_eval works as expected.
    '''

    def raise_syntax_error(expr):
        '''
        Helper function that raises a syntax error.
        '''

        try:
            safe_eval(expr)
        except SyntaxError:
            return

        raise AssertionError('safe_eval did not raise a syntax error for %s' % expr)

    raise_syntax_error('for i in range(5): print i')
    raise_syntax_error('import os')
    raise_syntax_error('os.remove("/etc/passwd")')

    assert safe_eval('5 + 5') == 10
    assert safe_eval('a + b', dict(a=10, b=15)) == 25

# Generated at 2022-06-13 15:35:50.519196
# Unit test for function safe_eval
def test_safe_eval():

    # trying to call a builtin function should not be allowed
    test_expr = "max([1,2,3])"
    test_eval = safe_eval(test_expr)
    assert test_eval == test_expr, "Failed to restrict builtin function call"

    # trying to use a builtin method should not be allowed
    test_expr = "'x'.upper()"
    test_eval = safe_eval(test_expr)
    assert test_eval == test_expr, "Failed to restrict builtin method call"

    # trying to submit a python list should not be allowed
    test_expr = "[max, map]"
    test_eval = safe_eval(test_expr)
    assert test_eval == test_expr, "Failed to restrict builtin type"

    # however a dict *should* be allowed
    test_expr

# Generated at 2022-06-13 15:35:57.936786
# Unit test for function safe_eval
def test_safe_eval():

    if not sys.version_info >= (2, 6):
        raise SkipTest("SKIP: safe_eval is only used on python 2.6+")

    # empty callable
    assert safe_eval('foo') == 'foo'
    assert safe_eval('some_name') == 'some_name'
    assert safe_eval(0) == 0
    assert safe_eval('0') == 0
    assert safe_eval('0.0') == 0.0
    assert safe_eval('1') == 1
    assert safe_eval('1.0') == 1.0
    assert safe_eval('1 + 1.0') == 2.0
    assert safe_eval('1 + 1.2') == 2.2
    assert safe_eval('1 - 1.0') == 0.0
    assert safe_eval('1 - 1.2')

# Generated at 2022-06-13 15:36:07.233688
# Unit test for function safe_eval

# Generated at 2022-06-13 15:36:15.409245
# Unit test for function safe_eval
def test_safe_eval():
    """
    This function tests the safe_eval function in ansible/utils/unsafe_proxy.py.
    This ensures that the following functions raise an exception as Ansible
    does not allow them to be called:
        - subprocess.Popen
        - os.system
    """

    from ansible.errors import AnsibleError

    # Testing a case where safe_eval returns the original expression
    # and does not raise an exception
    test_expr = "{{ 2 | int + 2 }}"
    (result, err) = safe_eval(test_expr, include_exceptions=True)
    if err:
        raise AnsibleError("safe_eval should not have raised an exception "
                           "for expression '%s', but got '%s' instead"
                            % (test_expr, container_to_text(err)))

# Generated at 2022-06-13 15:36:24.546426
# Unit test for function safe_eval
def test_safe_eval():
    # Test valid expressions
    expr = '1 + 2'
    res = safe_eval(expr)
    assert isinstance(res, int)
    assert res == 3

    expr = 'True or False'
    res = safe_eval(expr)
    assert isinstance(res, bool)
    assert res

    expr = 'False or True'
    res = safe_eval(expr)
    assert isinstance(res, bool)
    assert res

    expr = 'True and False'
    res = safe_eval(expr)
    assert isinstance(res, bool)
    assert not res

    expr = 'False and True'
    res = safe_eval(expr)
    assert isinstance(res, bool)
    assert not res

    expr = 'not 1'
    res = safe_eval(expr)

# Generated at 2022-06-13 15:36:31.290578
# Unit test for function safe_eval

# Generated at 2022-06-13 15:36:58.665778
# Unit test for function safe_eval
def test_safe_eval():
    if sys.version_info[0] < 3:
        safe_eval_test_input = u'["foo", "bar", "baz"]'
    else:
        safe_eval_test_input = ['foo', 'bar', 'baz']
    assert safe_eval(safe_eval_test_input) == ['foo', 'bar', 'baz'], 'safe_eval should return an unchanged list'
    safe_eval_test_input = container_to_text(safe_eval_test_input)
    assert safe_eval(safe_eval_test_input) == ['foo', 'bar', 'baz'], 'safe_eval should return a list when passed a string representation of a list'
    safe_eval_test_input = ast.literal_eval(safe_eval_test_input)

# Generated at 2022-06-13 15:37:08.968740
# Unit test for function safe_eval
def test_safe_eval():
    if C.DEFAULT_DEBUG:
        print("Running the safe_eval unit test, to disable set 'debug: False'")
        print("in ansible.cfg\n")

    # base case, just a string
    (foo, exc) = safe_eval("'a string'", {}, True)
    assert(foo == 'a string')
    assert(exc is None)
    assert(safe_eval("'a string'", {}) == 'a string')

    # string with a quote embedded in it
    (foo, exc) = safe_eval("'a quote \" inside of string'", {}, True)
    assert(foo == 'a quote \" inside of string')
    assert(exc is None)
    assert(safe_eval("'a quote \" inside of string'", {}) == 'a quote \" inside of string')

    # keys

# Generated at 2022-06-13 15:37:19.586300
# Unit test for function safe_eval
def test_safe_eval():
    # check that these evals succeed

    if sys.version_info >= (3,):
        safe_eval("True")
        safe_eval("False")
        safe_eval("None")

    safe_eval("a_list_variable")
    safe_eval("a_list_variable[0]")
    safe_eval("'test'")
    safe_eval("'test' + 'test'")
    safe_eval("1+1")
    safe_eval("'%s %s' % ('a', 'b')")
    safe_eval("'%s %s' % a_list_variable")
    safe_eval("'abc'.replace('b', 'B')")
    safe_eval("a_list_variable.replace('b', 'B')", dict(a_list_variable='abc'))

# Generated at 2022-06-13 15:37:26.433557
# Unit test for function safe_eval
def test_safe_eval():
    print("Testing safe_eval\n")

    # Test case 1
    print("\tTest case 1")
    print("\tExpression: 1 + 2")
    result = safe_eval("1 + 2", include_exceptions=True)
    print("\tResult: %s" % container_to_text(result))

    # Test case 2
    print("\tTest case 2")
    print("\tExpression: 1 + 2 + 'a'")
    result = safe_eval("1 + 2 + 'a'", include_exceptions=True)
    print("\tResult: %s" % container_to_text(result))

    # Test case 3
    print("\tTest case 3")
    print("\tExpression: os.system('ls')")

# Generated at 2022-06-13 15:37:35.074573
# Unit test for function safe_eval
def test_safe_eval():
    '''
    test the safe_eval function
    '''
    # simple literals
    assert safe_eval("None") is None
    assert safe_eval("False") is False
    assert safe_eval("True") is True
    assert safe_eval("1") == 1
    assert safe_eval("1.0") == 1.0
    assert safe_eval("1.1") == 1.1
    assert safe_eval("-1") == -1
    assert safe_eval("-1.1") == -1.1
    assert safe_eval("'yay'") == 'yay'
    assert safe_eval('"yay"') == 'yay'
    assert safe_eval('u"yay"') == u'yay'
    assert safe_eval("['a', 'b']") == ['a', 'b']

# Generated at 2022-06-13 15:37:44.532836
# Unit test for function safe_eval
def test_safe_eval():
    '''Test the safe_eval function'''

# Generated at 2022-06-13 15:37:54.566166
# Unit test for function safe_eval
def test_safe_eval():
    # testing safe_eval
    assert safe_eval(None) is None
    assert safe_eval('None') is None

    # test calls to functions that we allow, list()
    assert safe_eval('list([])') == []

    # test calls to functions that are not allowed
    if C.STRICT_VARIABLES:
        assert safe_eval('bool(1)')
    else:
        # if we don't have STRICT_VARIABLES, then we just return the string
        assert safe_eval('bool(1)') == 'bool(1)'

    # test code that has been templated to a data structure
    # that is not a string, we'll just return the data structure
    assert safe_eval(dict(a=1)) == dict(a=1)

    # test valid JSON data structures
    assert safe