

# Generated at 2022-06-13 15:28:07.357680
# Unit test for function safe_eval
def test_safe_eval():
    '''
    test safe_eval function using the built in unittest module
    this is not a comprehensive test, only a smoke test to make
    sure nothing obvious is broken
    '''
    import unittest

    class TestSafeEval(unittest.TestCase):
        '''
        Test the safe_eval function using the built in unittest module
        '''

# Generated at 2022-06-13 15:28:16.656479
# Unit test for function safe_eval

# Generated at 2022-06-13 15:28:21.982664
# Unit test for function safe_eval
def test_safe_eval():
    globals = {"foo": "bar"}
    locals = {"baz": "quux"}

    result = safe_eval("foo", globals, locals)
    assert result == "bar"

    result = safe_eval("baz", globals, locals)
    assert result == "quux"

    result = safe_eval("foo and baz", globals, locals)
    assert result is True

    result = safe_eval("foo and baz and None", globals, locals)
    assert result is None

    result = safe_eval("[1,2,3,4]", globals, locals)
    assert result == [1,2,3,4]

    result = safe_eval("'foo' in bar", globals, locals)
    assert result is True

    result = safe_eval("None in bar", globals, locals)

# Generated at 2022-06-13 15:28:27.714899
# Unit test for function safe_eval
def test_safe_eval():
    # test cases taken from
    # http://stackoverflow.com/questions/12523516/using-ast-and-whitelists-to-make-pythons-eval-safe
    assert safe_eval('1 + 2') == 3
    assert safe_eval('1 + 2 + 3') == 6
    assert safe_eval('1 + 2 * 3') == 7
    assert safe_eval('1 - 2') == -1
    assert safe_eval('1 - 2 - 3') == -4
    assert safe_eval('1 - 2 * 3') == -5
    assert safe_eval('1 / 2') == 0.5
    assert safe_eval('1 / 2 * 3') == 1.5
    assert safe_eval('1 / (2 * 3)') == 1/6
    assert safe_eval('1 / 2 + 3')

# Generated at 2022-06-13 15:28:36.417984
# Unit test for function safe_eval
def test_safe_eval():
    expr = "{{ ansible_eth0['ipv4']['address'] }}"
    e = safe_eval(expr)
    assert e == expr
    expr = "ansible_eth0['ipv4']['address']"
    e = safe_eval(expr)
    assert e == expr
    expr = "ansible_eth0.ipv4.address"
    e = safe_eval(expr)
    assert e == expr
    expr = "ansible_eth0.ipv4['address']"
    e = safe_eval(expr)
    assert e == expr
    expr = "ansible_eth0['ipv4'].address"
    e = safe_eval(expr)
    assert e == expr
    expr = "ansible_eth0.ipv4['address']"
    e = safe_eval

# Generated at 2022-06-13 15:28:45.387922
# Unit test for function safe_eval

# Generated at 2022-06-13 15:28:53.349427
# Unit test for function safe_eval
def test_safe_eval():
    # Tests for function safe_eval
    assert safe_eval("a and b or c") == (True and False or True)
    assert safe_eval("a or b and c") == (True or False and True)
    assert safe_eval("a or b") == (True or False)
    assert safe_eval("a and b") == (True and False)
    assert safe_eval("a + b") == (1 + 2)
    assert safe_eval("a + b + c") == (1 + 2 + 3)
    assert safe_eval("a + b + c - d") == (1 + 2 + 3 - 4)
    assert safe_eval("(a - b) * c") == ((1 - 2) * 3)
    assert safe_eval("(a - b) * c - d") == ((1 - 2) * 3 - 4)

# Generated at 2022-06-13 15:29:00.239851
# Unit test for function safe_eval
def test_safe_eval():
    '''
    Test to confirm that safe_eval raises an error on invalid
    input and returns expected data on valid input.
    '''
    assert safe_eval("foo.bar()") == "foo.bar()"
    assert safe_eval(u"a == b or c == d or f == g") == u"a == b or c == d or f == g"
    assert safe_eval("a==b") == "a==b"
    assert safe_eval("a==b", dict(a=1, b=1)) == True
    assert safe_eval("a==b", dict(a=1, b=2)) == "a==b"
    assert safe_eval("[1,2,3]") == [1,2,3]
    assert safe_eval("foo") == "foo"

# Generated at 2022-06-13 15:29:08.987164
# Unit test for function safe_eval
def test_safe_eval():
    # simple expression
    assert safe_eval("2 + 2") == 4
    assert safe_eval("2 + 2 * 3") == 8
    assert safe_eval("foo(1)") == "foo(1)"

    # simple expression with a variable
    assert safe_eval("{{ x + y }}", dict(x=3, y=4)) == 7
    assert safe_eval("{{ x + y * z }}", dict(x=3, y=4, z=2)) == 11

    # dict to be included
    assert safe_eval("{{ dict1.key1 }}", dict(dict1=dict(key1="val1"))) == "val1"

    # template to be included

# Generated at 2022-06-13 15:29:18.520889
# Unit test for function safe_eval

# Generated at 2022-06-13 15:29:25.951427
# Unit test for function safe_eval

# Generated at 2022-06-13 15:29:31.514175
# Unit test for function safe_eval
def test_safe_eval():

    # a simple test string, includes a call to 'in'
    test_string = "teststring"
    result = safe_eval(test_string)
    assert result == test_string, "%s != %s" % (result, test_string)

    # test a safe builtin call allowed by default
    test_string = 'len(teststring)'
    result = safe_eval(test_string)
    assert result == len(test_string), "%s != %s" % (result, len(test_string))

    ret = safe_eval({'a': 1, 'b': 2}, include_exceptions=True)
    assert ret[0] == ret[1] == None
    assert ret[0] == {'a': 1, 'b': 2}

    # test a builtin call not allowed by default

# Generated at 2022-06-13 15:29:38.035205
# Unit test for function safe_eval

# Generated at 2022-06-13 15:29:44.178480
# Unit test for function safe_eval
def test_safe_eval():
    safe_eval("a_list_variable", {'a_list_variable': [1, 2, 3]})
    safe_eval("a_list_variable[0]", {'a_list_variable': [1, 2, 3]})
    safe_eval("a_list_variable[0][0]", {'a_list_variable': [[1], 2, 3]})
    safe_eval("a_list_variable[1]", {'a_list_variable': [1, 2, 3]})

    # normal (unsafe) Python
    safe_eval("__import__('os').system('rm -rf')")

    # a real world example which was problematic
    safe_eval("a_list_variable[1]", {'a_list_variable': (1, 2, 3)})

# Generated at 2022-06-13 15:29:54.780591
# Unit test for function safe_eval
def test_safe_eval():
    def catch_exception(expr):
        # catch_exception() - return error (if any) generated by safe_eval()
        try:
            safe_eval(expr, include_exceptions=True)
        except Exception as e:
            return e

    def test_expr(expr, expected_result):
        # test_expr() - unit test safe_eval() with a single expression
        #
        # expr:             expression to evaluate
        # expected_result:  expected result from safe_eval()
        assert safe_eval(expr) == expected_result

    #
    # Test safe_eval() when CALL_ENABLED is disabled
    #
    CALL_ENABLED = []
    test_expr('1 - 2', -1)
    test_expr('1 == 1', True)
    test_expr('1 != 1', False)

# Generated at 2022-06-13 15:30:02.436528
# Unit test for function safe_eval

# Generated at 2022-06-13 15:30:09.147160
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval('5') == 5
    assert safe_eval('1 + 1') == 2
    assert safe_eval('foo.bar()', dict(foo=dict(bar=lambda: True))) is True
    assert safe_eval('[1,2,3]') == [1,2,3]
    assert safe_eval('{ "foo": "bar" }') == { "foo": "bar" }
    assert safe_eval('null') is None
    assert safe_eval('true') is True
    assert safe_eval("""foo(arg='arg')""", dict(foo=lambda arg: True)) is True
    assert safe_eval("""foo(arg='arg')""", dict(foo=lambda arg: True), include_exceptions=True) == (True, None)


# Generated at 2022-06-13 15:30:19.578967
# Unit test for function safe_eval
def test_safe_eval():
    """
    This unit test will test the safe_eval function to ensure
    it behaves as expected.
    """
    from ansible.module_utils.six import PY3

    # Empty string should return empty string
    empty_result, _excp = safe_eval('', include_exceptions=True)
    assert empty_result == ''

    # Strings should return themselves
    string_result, _excp = safe_eval('abc', include_exceptions=True)
    assert string_result == 'abc'

    # Boolean values should return booleans
    bool_result, _excp = safe_eval('true', include_exceptions=True)
    assert bool_result is True
    false_result, _excp = safe_eval('false', include_exceptions=True)
    assert false_result is False

    # Numbers should return

# Generated at 2022-06-13 15:30:27.670141
# Unit test for function safe_eval
def test_safe_eval():

    # simple tests to see if safe_eval works for basic literals
    literals = ['simple', 'string', 3, 3.14, True, False, None]
    for l in literals:
        assert l == safe_eval(str(l))

    # test if safe_eval works for simple calculations
    assert 2 == safe_eval('1 + 1')
    assert 6 == safe_eval('2 * 3')
    assert 5 == safe_eval('10 - 5')
    assert 3 == safe_eval('15 / 5')
    assert 9 == safe_eval('3 ** 2')
    assert -4.4 == safe_eval('-4.4')
    assert 5 == safe_eval('(2 + 3)')
    assert 2 == safe_eval('(10 - 5 - 3)')

# Generated at 2022-06-13 15:30:33.594842
# Unit test for function safe_eval
def test_safe_eval():
    def do_test(test_case, expected):
        evaluated, err = safe_eval(test_case, include_exceptions=True)
        if err:
            print(to_native(err))
            print(test_case)
        assert expected in to_native(evaluated)

    # Make sure our basic operations work
    do_test("1", "1")
    do_test("1+1", "2")
    do_test("3-1", "2")
    do_test("2*2", "4")
    do_test("6/2", "3")
    do_test("-1", "-1")
    do_test("-1*-1", "1")
    # Make sure we can use the builtin names for True and False
    do_test("True", "True")
    do_test

# Generated at 2022-06-13 15:30:45.889761
# Unit test for function safe_eval
def test_safe_eval():
    '''
    Tests to ensure we can evaluate only expressions that will
    eventually return python data structures.

    This module is used to ensure that complex expressions cannot
    be used in Jinja2 templates.

    The following is copied from a comment in the related code in
    Jinja2:

        Calling functions may or may not be what you want.  If you
        don't want this you can re-enable the code from above.  Keep
        in mind that this makes it possible to e.g. read files from
        the filesystem under the account of the application server.
    '''

    def test(expr, expected, **kwargs):
        '''
        Test an expression.  The expression should evaluate to
        'expected' without any exceptions raised.
        '''
        # NOTE: This, from the original Jinja2 unit test,
        # causes safe_eval to

# Generated at 2022-06-13 15:30:55.026089
# Unit test for function safe_eval
def test_safe_eval():
    try:
        safe_eval('foobar')
        assert False, 'failed to raise exception'
    except:
        pass

    try:
        safe_eval('[x for x in [1,2,3,4] if x > 5]')
        assert False, 'failed to raise exception'
    except:
        pass

    try:
        safe_eval('repr(__builtins__)')
        assert False, 'failed to raise exception'
    except:
        pass

    assert safe_eval('[1,2,3,4]') == [1,2,3,4]
    assert safe_eval('{"foo": "bar"}') == {"foo": "bar"}
    assert safe_eval('[x for x in [1,2,3,4] if x < 3]') == [1,2]

# Generated at 2022-06-13 15:30:59.208132
# Unit test for function safe_eval
def test_safe_eval():
    # test the use of safe_eval() to allow for simple cases
    assert safe_eval("a") == 'a'
    assert safe_eval("'a'") == 'a'
    assert safe_eval("1") == 1
    assert safe_eval("1 + 1") == 2
    assert safe_eval("'a' in ['a']") is True
    assert safe_eval("'a' in ['a', 'b']") is True
    assert safe_eval("'a' in foo", dict(foo=['a','b'])) is True

    assert safe_eval("unresolved") == 'unresolved'
    assert safe_eval("unresolved in ['a','b']") == 'unresolved in [\'a\', \'b\']'

# Generated at 2022-06-13 15:31:09.764642
# Unit test for function safe_eval
def test_safe_eval():
    def test_safe_eval_returns_correct_value(test_text, expected):
        # Test that the safe_eval function returns the expected value,
        # and that there were no exceptions
        result, exception = safe_eval(test_text, include_exceptions=True)
        assert exception is None
        assert result == expected

    def test_safe_eval_raises_exception(test_text, expected_exc_type):
        # Test that the safe_eval function returns the correct
        # expression and that the correct exception was raised
        result, exception = safe_eval(test_text, include_exceptions=True)
        assert result == test_text
        assert isinstance(exception, expected_exc_type)

    # simple test cases:
    test_safe_eval_returns_correct_value('test', 'test')


# Generated at 2022-06-13 15:31:16.822826
# Unit test for function safe_eval
def test_safe_eval():
    # First, test things that should work
    # Note: ast.literal_eval already does some of these basic tests
    assert safe_eval('1') == 1
    assert safe_eval('True') == True
    assert safe_eval('False') == False
    assert safe_eval('None') == None
    assert safe_eval('false') == False
    assert safe_eval('true') == True
    assert safe_eval('null') == None
    assert safe_eval("'A test string'") == 'A test string'
    assert safe_eval('["A", "test", "list"]') == ['A', 'test', 'list']
    assert safe_eval('("A", "test", "tuple")') == ('A', 'test', 'tuple')

# Generated at 2022-06-13 15:31:28.608716
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval("foo") == "foo"

    # simple, safe Python expressions
    assert safe_eval("[ 1, 2, 3 ]") == [1,2,3]
    assert safe_eval("{ 'foo': 'bar' }") == {'foo': 'bar'}
    assert safe_eval("foo.bar") == "foo.bar"
    assert safe_eval("[ 1, 2, 3 ].index(2)") == 1
    assert safe_eval("[ 'foo', 'bar' ]") == ['foo', 'bar']
    assert safe_eval("{ foo: 'bar', baz: 'foobar' }") == {'foo': 'bar', 'baz': 'foobar'}

# Generated at 2022-06-13 15:31:36.659249
# Unit test for function safe_eval

# Generated at 2022-06-13 15:31:44.629759
# Unit test for function safe_eval
def test_safe_eval():
    try:
        # Test safe eval of a valid expression with built-in call
        assert safe_eval("(1+2, 4, 5)") == (3, 4, 5)
    except Exception as e:
        print("Error: failed to safely evaluate expression: (%s)" % to_native(e))

    try:
        # Test safe eval of a valid expression with custom call
        CALL_ENABLED.append('container_to_text')
        test_input = {'a': [1, 2], 'b': 'test'}
        assert safe_eval("container_to_text(test_input)") == container_to_text(test_input)
    except Exception as e:
        print("Error: failed to safely evaluate expression: (%s)" % to_native(e))


# Generated at 2022-06-13 15:31:55.145630
# Unit test for function safe_eval
def test_safe_eval():

    # setup test environment
    ansible_vars = dict()
    ansible_vars['safe_str'] = "safe_str"
    ansible_vars['safe_num'] = 123
    ansible_vars['safe_bool'] = True
    ansible_vars['safe_none'] = None
    ansible_vars['safe_empty_str'] = ''
    ansible_vars['safe_empty_list'] = []
    ansible_vars['safe_empty_dict'] = dict()

    # should be safe to run safe_eval with an empty var
    expr = ''
    result = safe_eval(expr, include_exceptions=True)
    assert result[0] == expr and result[1] is None

    # safestr, safenum, safebool, safenone should be safe to evaluate


# Generated at 2022-06-13 15:32:05.808337
# Unit test for function safe_eval
def test_safe_eval():

    def run_expr_test(expr, err_msg='safe_eval, expression=%s'):
        try:
            result = safe_eval(expr)
            # if it didn't raise an exception, check that everything is ok
            if result is None and expr not in ('None', 'null'):
                raise Exception('unexpected result(%s) with expression=%s' % (result, expr))
        except Exception as e:
            # if it raised an exception, check that everything is ok
            if err_msg is None:
                raise Exception('unexpected exception, expression=%s, error=%s' % (expr, e))

# Generated at 2022-06-13 15:32:20.132549
# Unit test for function safe_eval
def test_safe_eval():
    if sys.version_info < (2, 6):
        print("Test skipped, known failure with Python 2.4")
        return

    assert safe_eval("1 + 1") == 2
    assert safe_eval("(1, 2)") == (1, 2)
    assert safe_eval("['a', 'b']") == ['a', 'b']
    assert safe_eval("{'a': 'b', 'c': 'd'}") == {'a': 'b', 'c': 'd'}

    assert safe_eval('"%s"' % C.DEFAULT_HASH_BEHAVIOUR) == C.DEFAULT_HASH_BEHAVIOUR
    assert safe_eval('"%s"' % C.DEFAULT_SYSLOG_FACILITY) == C.DEFAULT_SYSLOG_FACILITY

# Generated at 2022-06-13 15:32:32.595600
# Unit test for function safe_eval
def test_safe_eval():
    if sys.version_info[0] >= 3:
        filter_name = 'filter'
    else:
        filter_name = '_ans'
    error_msg = ("Invalid expression (default(%s %s %s, foo)), "
                 "got invalid expression (default(%s %s %s, foo))") % \
                (filter_name, 'a', 'b', filter_name, 'a', 'b')
    var = dict(a=1, b=2)

# Generated at 2022-06-13 15:32:42.082231
# Unit test for function safe_eval
def test_safe_eval():
    # Test some good expressions
    assert safe_eval('3 * 5') == 15
    assert safe_eval('(8 * 4) + (3 * 2)') == 32
    assert safe_eval('3 * 5.0 + 4') == 19.0
    assert safe_eval('["ham", "eggs", "spam"] + ["bacon"]') == ["ham", "eggs", "spam", "bacon"]
    assert safe_eval('{"a": "b"}') == {"a": "b"}
    assert safe_eval('{"a": "b"}.keys()') == ['a']
    assert safe_eval('["ham", "eggs", "spam"][0]') == "ham"
    assert safe_eval('["ham", "eggs", "spam"][1]') == "eggs"
    assert safe_

# Generated at 2022-06-13 15:32:52.605026
# Unit test for function safe_eval
def test_safe_eval():
    from ansible.module_utils.common.text.converters import to_text
    from ansible.module_utils._text import to_bytes

    for expr in [
        'foo',
        'foo()',
        'foo().bar',
        'foo().bar()',
        'foo().bar().baz',
        'foo().bar().baz()',
        'foo().bar().baz().qux',
        'foo().bar().baz().qux()',
    ]:
        print("Trying '{0}'".format(expr))
        print("{0} -> {1}".format(to_bytes(expr, nonstring='passthru'), to_text(safe_eval(expr), nonstring='passthru')))

# Generated at 2022-06-13 15:33:02.746507
# Unit test for function safe_eval
def test_safe_eval():

    # negative tests
    assert safe_eval("python.version") == "python.version"
    # this tests whether the whitelist is being enforced
    assert safe_eval("__import__('os').system('rm -rf /')") == "__import__('os').system('rm -rf /')"
    assert safe_eval("x(1)") == "x(1)"
    assert safe_eval("[x for x in range(10) if x % 2 == 0]") == "[x for x in range(10) if x % 2 == 0]"

    # tests with statements
    # this is not valid syntax, even if we were to enable 'with'
    assert safe_eval("with foo: pass") == "with foo: pass"

    # tests which should evaluate correctly

# Generated at 2022-06-13 15:33:14.176786
# Unit test for function safe_eval

# Generated at 2022-06-13 15:33:24.976257
# Unit test for function safe_eval

# Generated at 2022-06-13 15:33:32.520492
# Unit test for function safe_eval
def test_safe_eval():
    # Some tests against known-safe expressions
    ok_expr1 = """
    [ item.strip() for item in foo.split(',') ]
    """
    ok_expr2 = """
    foo.rsplit(' ')[0].strip()
    """
    ok_expr3 = """
    ' '.join(items)
    """
    ok_expr4 = """
    bar
    """
    ok_expr5 = """
    foo
    """
    ok_expr6 = """
    'foo'.replace('f', 'b')
    """
    ok_expr7 = """
    'bar' if foo == 'foo' else 'foo'
    """
    ok_expr8 = """
    foo[1]
    """
    ok_expr9 = """
    {"a": "b"}
    """
    ok_expr

# Generated at 2022-06-13 15:33:43.538225
# Unit test for function safe_eval

# Generated at 2022-06-13 15:33:54.679866
# Unit test for function safe_eval

# Generated at 2022-06-13 15:34:09.470790
# Unit test for function safe_eval
def test_safe_eval():
    '''
    Unit test for safe_eval function.
    '''
    # The type of the result of safe_eval should be checked through
    # the type() function. The isinstance function is not reliable
    # in this test case, because of the nature of the safe_eval function.

    assert type(safe_eval('1')) == int
    assert type(safe_eval('1.1')) == float
    assert type(safe_eval('1+1')) == int
    assert type(safe_eval('1.0+1')) == float
    assert type(safe_eval('1+1.0')) == float
    assert type(safe_eval('1.0+1.0')) == float
    assert type(safe_eval('-1')) == int
    assert type(safe_eval('-1.1'))

# Generated at 2022-06-13 15:34:19.210788
# Unit test for function safe_eval
def test_safe_eval():
    # test None
    assert safe_eval(None) is None

    # test simple types
    for value in [1, 1.2, "a", True, False, [1,2], {'a':'b'}]:
        assert safe_eval(value) == value
        assert safe_eval(value, include_exceptions=True) == (value, None)
        assert safe_eval(value) == value

    # test that expressions which return simple types work
    for expr, result in [
        ('1', 1),
        ('1.2', 1.2),
        ('"a"', "a"),
        ('True', True),
        ('False', False),
        ('[1,2]', [1,2]),
        ('dict(a="b")', {'a':'b'})
    ]:
        assert safe

# Generated at 2022-06-13 15:34:28.352941
# Unit test for function safe_eval
def test_safe_eval():
    '''
    This function is used to test the safe_eval function
    '''

    # Use cases:
    # 1. Safe evaluation of a string variable
    # 2. Safe evaluation of a string variable with a math operation
    # 3. Safe evaluation of a string variable that is an array
    # 4. Safe evaluation of a string variable that is an array with a math operation
    # 5. Safe evaluation of a string variable that is a dictionary with a math operation
    # 6. Safe evaluation of a string variable that is a dictionary
    # 7. Safe evaluation of a string variable that calls a builtin function
    # 8. Unsafe evaluation of a string variable that calls a builtin function
    # 9. Safe evaluation of a literal
    # 10. Safe evaluation of a literal with a math operation
    # 11. Safe evaluation of a literal that is an array
    # 12. Safe

# Generated at 2022-06-13 15:34:37.255311
# Unit test for function safe_eval
def test_safe_eval():
    # general expression types
    assert safe_eval("1") == 1
    assert safe_eval("1+1") == 2
    assert safe_eval("1+1==2") is True

    # We want safe_eval to return a string when it fails
    assert isinstance(safe_eval("1+1=="), string_types)

    # sequence types
    assert safe_eval("[1, 2, 3]") == [1, 2, 3]
    assert safe_eval("(1, 'a', 3)") == (1, 'a', 3)
    assert safe_eval("{1:'a', 2:'b'}") == {1: 'a', 2: 'b'}

    # builtins
    assert safe_eval("True") is True
    assert safe_eval("False") is False

# Generated at 2022-06-13 15:34:45.319085
# Unit test for function safe_eval
def test_safe_eval():
    m = "safe_eval failed"

    assert safe_eval("[1]") == [1], m
    assert safe_eval("[]") == [], m
    assert safe_eval("[[1,1]]") == [[1, 1]], m
    assert safe_eval("{'a':1}") == {'a': 1}, m
    assert safe_eval("{}") == {}, m
    assert safe_eval("1 in [1]") is True, m
    assert safe_eval("2 in [1]") is False, m
    assert safe_eval("1 not in [1]") is False, m
    assert safe_eval("1==1") is True, m
    assert safe_eval("1==2") is False, m
    assert safe_eval("1!=2") is True, m
    assert safe_eval

# Generated at 2022-06-13 15:34:52.794927
# Unit test for function safe_eval
def test_safe_eval():
    ''' safe_eval() should not execute custom python functions
        or raise any exceptions. It should just return its input.
    '''

    def test_function():
        return "test"

    # Testing builtins
    assert(safe_eval("abs(5)") == abs(5))

    # Testing passing a parameter to a builtin
    assert(safe_eval("any([True, False, False])") == any([True, False, False]))

    # Testing passing multiple parameters to a builtin
    assert(safe_eval("bin(10)") == bin(10))

    # Testing a builtin that tries to eval
    assert(safe_eval("compile('1', '<string>', 'eval')") == "compile('1', '<string>', 'eval')")

    # Testing a custom function

# Generated at 2022-06-13 15:35:02.593329
# Unit test for function safe_eval
def test_safe_eval():

    def assert_safe_eval(expr, expected_result=None, locals=None, include_exceptions=True):
        # Use the locals dict to make sure that safe_eval is not trying to access
        # the variable 'anotherlocal' by itself.
        if locals is None:
            locals = dict(anotherlocal=1)
        result, exception = safe_eval(expr, locals, include_exceptions=True)
        if include_exceptions:
            if expected_result is None:
                assert result == expr, 'expected: %s, got: %s' % (expr, result)
                assert exception is not None, "expected exception for: %s" % expr
            else:
                assert result == expected_result, 'expected: %s, got: %s' % (expected_result, result)

# Generated at 2022-06-13 15:35:07.340198
# Unit test for function safe_eval
def test_safe_eval():
    # Ensure that the various builtins are disallowed while the function
    # len() is still allowed.
    assert safe_eval('len(foo)', dict(foo=[1, 2, 3])) == 3
    assert safe_eval('abs(foo)', dict(foo=9)) == 9
    assert safe_eval('[1, 2, 3]', dict(foo=9)) == [1, 2, 3]
    assert safe_eval('[1, 2, 3]') == [1, 2, 3]
    assert safe_eval('{"a": 1, "b": 2}') == {"a": 1, "b": 2}
    assert safe_eval('foo[1]', dict(foo=[1, 2, 3])) == 2
    assert safe_eval('foo.bar', dict(foo=dict(bar=9))) == 9
   

# Generated at 2022-06-13 15:35:15.827340
# Unit test for function safe_eval

# Generated at 2022-06-13 15:35:25.772332
# Unit test for function safe_eval
def test_safe_eval():
    '''
    basic sanity tests for the safe_eval function
    '''
    # Make sure we can evaluate stuff that is OK
    safe_eval('1+1')
    safe_eval('counter + 1')
    safe_eval('1.1 + 1.1')
    safe_eval('2.0 / 2.0')
    safe_eval('1.1 + 1.1')
    safe_eval('[1,2] + [2,3]')
    safe_eval('{"a":1}')
    safe_eval('{"a":[1,2]}')
    safe_eval('{"a":[1,(1,2)]}')
    safe_eval('(1,2)')
    safe_eval('[1,2]')
    safe_eval('-2')
    safe_eval('-2.0')


# Generated at 2022-06-13 15:35:54.354554
# Unit test for function safe_eval
def test_safe_eval():
    # Tests for safe_eval
    assert safe_eval("foo", locals={'foo': 'bar'}) == 'bar'
    assert safe_eval("foo is bar", locals={'foo': 'bar'}) is True
    assert safe_eval("foo is not bar", locals={'foo': 'bar'}) is False
    assert safe_eval("foo == 'bar'", locals={'foo': 'bar'}) is True
    assert safe_eval("foo != 'bar'", locals={'foo': 'bar'}) is False
    assert safe_eval("foo != bar", locals={'foo': 'bar'}) is False
    assert safe_eval("3 > 1") is True
    assert safe_eval("3 < 1") is False
    assert safe_eval("3 >= 3") is True
    assert safe_eval("3 <= 3") is True

# Generated at 2022-06-13 15:36:00.295987
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval("foo") == "foo"
    assert safe_eval("foo.bar()") == "foo.bar()"

    # list, dict
    assert safe_eval("[1, 2]") == [1, 2]
    assert safe_eval("[1, 2, 3, {'a': 2, 'b': [4, 5]}]") == [1, 2, 3, {'a': 2, 'b': [4, 5]}]

    # basic operations
    assert safe_eval("1 + 2") == 3
    assert safe_eval("4 - 3") == 1
    assert safe_eval("[1, 2] * 2") == [1, 2, 1, 2]
    assert safe_eval("4 / 2") == 2
    assert safe_eval("3 ** 2") == 9

    # complex
    assert safe

# Generated at 2022-06-13 15:36:06.525309
# Unit test for function safe_eval
def test_safe_eval():
    # basic cases
    assert safe_eval('0') == 0
    assert safe_eval('1') == 1
    assert safe_eval('1 + 1') == 2
    assert safe_eval('1 + 1') == 2
    assert safe_eval('"ab"') == 'ab'
    assert safe_eval('True')
    assert safe_eval('True and False') == False
    # negative number
    assert safe_eval('-1') == -1
    # negative expressions
    assert safe_eval('-1 + -1') == -2
    assert safe_eval('-1 - 1') == -2
    assert safe_eval('1 - 2') == -1
    assert safe_eval('-1 * -1') == 1
    assert safe_eval('-1 / 1') == -1

# Generated at 2022-06-13 15:36:14.592445
# Unit test for function safe_eval
def test_safe_eval():
    """ Test safe_eval() """
    # Test errors
    assert safe_eval("foo()") == "foo()"
    assert safe_eval("foo.bar()") == "foo.bar()"
    assert safe_eval("foo['bar']") == "foo['bar']"
    assert safe_eval("foo.bar['baz']") == "foo.bar['baz']"
    assert safe_eval("foo(bar)") == "foo(bar)"
    assert safe_eval("foo.bar(baz)") == "foo.bar(baz)"
    assert safe_eval("foo['bar'](baz)") == "foo['bar'](baz)"
    assert safe_eval("foo.bar['baz'](qux)") == "foo.bar['baz'](qux)"
    # Test passes

# Generated at 2022-06-13 15:36:23.713724
# Unit test for function safe_eval
def test_safe_eval():
    # Basic syntax error
    (result, error) = safe_eval('{{', include_exceptions=True)
    assert result == error == '{{'

    # Invalid operator
    (result, error) = safe_eval('1 ** 2', include_exceptions=True)
    assert result == error == '1 ** 2'

    # Non-existing variable
    (result, error) = safe_eval('{{ test }}', include_exceptions=True)
    assert result == error == '{{ test }}'

    # Invalid function
    (result, error) = safe_eval('{{ os.getuid() }}', include_exceptions=True)
    assert result == error == '{{ os.getuid() }}'

    # Invalid expression where we are trying to call function

# Generated at 2022-06-13 15:36:30.828121
# Unit test for function safe_eval
def test_safe_eval():
    # constant strings
    assert safe_eval("'foo'") == 'foo'
    # integer literals
    assert safe_eval("1") == 1
    # float literals
    assert safe_eval("1.2") == 1.2
    # addition
    assert safe_eval("1 + 1") == 2
    # subtraction
    assert safe_eval("1 - 1") == 0
    # multiplication
    assert safe_eval("1 * 1") == 1
    # division
    assert safe_eval("1 / 1") == 1
    # modulo
    assert safe_eval("2 % 3") == 2
    # unary operator
    assert safe_eval("-1") == -1
    # boolean 'or'
    assert safe_eval("1 or 1") == 1
    # boolean 'and'

# Generated at 2022-06-13 15:36:41.969466
# Unit test for function safe_eval
def test_safe_eval():
    # Test successful evals
    assert safe_eval("1 + 1", include_exceptions=True) == (2, None)
    assert safe_eval("(1, 2, 3)", include_exceptions=True) == ((1, 2, 3), None)
    assert safe_eval("{'a': 1, 'b': 2}", include_exceptions=True) == ({'a': 1, 'b': 2}, None)
    assert safe_eval("['a', 'b', 'c']", include_exceptions=True) == (['a', 'b', 'c'], None)
    assert safe_eval("True and False", include_exceptions=True) == (False, None)
    assert safe_eval("True or False", include_exceptions=True) == (True, None)

# Generated at 2022-06-13 15:36:53.447261
# Unit test for function safe_eval
def test_safe_eval():
    array = ['item1', 'item2', 'item3']
    array_str = '["item1", "item2", "item3"]'
    dict = {"key1": "value1", "key2": "value2", "key3": "value3"}
    dict_str = '{"key1": "value1", "key2": "value2", "key3": "value3"}'
    array_dict = [{"key1": "value1"}, {"key2": "value2"}, {"key3": "value3"}]
    array_dict_str = '[{"key1": "value1"}, {"key2": "value2"}, {"key3": "value3"}]'
    dict_array = {"key1": ["value1"], "key2": ["value2"], "key3": ["value3"]}
    dict_array_str

# Generated at 2022-06-13 15:37:02.655300
# Unit test for function safe_eval
def test_safe_eval():
    '''
    Ensures that safe_eval works as expected
    '''

    # successful evaluations
    assert safe_eval("{{ 1 + 2 }}") == 3
    assert safe_eval("{{ 'foo' + 'bar' }}") == 'foobar'
    assert safe_eval("{{ 42 == 6*7 }}") is True
    assert safe_eval("{{ 42 == 7*7 }}") is False
    assert safe_eval("{{ 'foo' in ['foo', 'bar'] }}") is True
    assert safe_eval("{{ 'baz' in ['foo', 'bar'] }}") is False
    assert safe_eval("{{ 42 }}") == 42
    assert safe_eval("{{ 'foo' }}") == 'foo'
    assert safe_eval("{{ 'foo' * 3 }}") == 'foofoofoo'

# Generated at 2022-06-13 15:37:11.612953
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval('foo') == 'foo'
    assert safe_eval(123) == 123
    assert safe_eval([]) == []
    assert safe_eval({}) == {}
    assert safe_eval({'k1': 'v1'}) == {'k1': 'v1'}
    assert safe_eval(None) == None

    assert isinstance(safe_eval('True'), bool)
    assert not safe_eval('False')
    assert not safe_eval('')
    assert not safe_eval('null')
    assert safe_eval('true')
    assert isinstance(safe_eval('[1,2,3]'), list)
    assert isinstance(safe_eval('{1,2,3}'), set)
    assert isinstance(safe_eval('foo'), string_types)

# Generated at 2022-06-13 15:37:59.107095
# Unit test for function safe_eval
def test_safe_eval():
    test_result = {
        'description': 'Testing safe_eval',
        'passed': False,
        'msg': [],
    }
    # Allowed syntax
    test_result['msg'].append("Running eval on allowed syntax.")
    safe_eval("[i for i in range(0, 256)]")

    # Unsafe syntax
    try:
        test_result['msg'].append("Running eval on unsafe syntax.")
        safe_eval("__import__('os').system('echo Hello!')")
    except Exception as e:
        test_result['msg'].append("Unsafe syntax not allowed: %s" % e)

    # Function calls (unsafe)