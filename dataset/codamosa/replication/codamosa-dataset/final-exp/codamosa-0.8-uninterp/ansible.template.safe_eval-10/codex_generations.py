

# Generated at 2022-06-13 15:28:13.818965
# Unit test for function safe_eval

# Generated at 2022-06-13 15:28:22.294002
# Unit test for function safe_eval
def test_safe_eval():
    def test(eval_string, expected_output, expected_exception=None):
        '''
        Test that the given eval string returns the given output,
        and that the expected exception occurs, if any
        '''
        included_exceptions = False
        if expected_exception:
            included_exceptions = True

        result, exception = safe_eval(eval_string, include_exceptions=included_exceptions)

        assert result == expected_output, ('string: "%s" expected: %s, got: %s' % (eval_string, expected_output, result))

        if expected_exception:
            assert exception, 'string: "%s" expected exception: %s' % (eval_string, expected_exception)

# Generated at 2022-06-13 15:28:26.710659
# Unit test for function safe_eval
def test_safe_eval():
    # check if we can call lower()
    code = u"lower('foo')"
    result = safe_eval(code, include_exceptions=True)
    assert result == (u"foo", None)

    # check if we can call lower() on something
    code = u"lower(hello)"
    result = safe_eval(code, dict(hello=u"foo"), include_exceptions=True)
    assert result == (u"foo", None)

    # check if we can call lower() on a list element
    code = u"lower(a_list_variable[0])"
    result = safe_eval(code, dict(a_list_variable=[u"FOO"]), include_exceptions=True)
    assert result == (u"foo", None)

    # check if we can call lower() on a list element
    code

# Generated at 2022-06-13 15:28:35.859710
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval('[]') == []
    assert safe_eval('{"key": "value"}') == {'key': 'value'}
    assert safe_eval('-2') == -2
    assert safe_eval('-2 + 3') == 1
    assert safe_eval('-2 + (-3)') == -5
    assert safe_eval('2 * 3') == 6
    assert safe_eval('6 / 2') == 3
    assert safe_eval('2**3') == 8
    assert safe_eval('"string"') == 'string'
    assert safe_eval('["item1", "item2"]') == ['item1', 'item2']
    assert safe_eval('(1, 2)') == (1, 2)
    assert safe_eval('true') is True
    assert safe_eval('false') is False
   

# Generated at 2022-06-13 15:28:44.963283
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval('1 + 3') == 4
    assert safe_eval('a', locals={'a': 'b'}) == 'b'
    assert safe_eval('a') is None
    assert safe_eval('c', locals={'c': 2}) == 2
    assert safe_eval('c', locals={'c': [1, 2]}) == [1, 2]
    assert safe_eval('c', locals={'c': {1: 2}}) == {1: 2}
    assert safe_eval('c and d', locals=dict(c=True, d=False)) is False
    assert safe_eval('c or d', locals=dict(c=True, d=False)) is True
    assert safe_eval({'a': 'b'}) == {'a': 'b'}

# Generated at 2022-06-13 15:28:53.012457
# Unit test for function safe_eval
def test_safe_eval():
    # Test success cases
    assert safe_eval('a_list_variable') == 'a_list_variable'
    assert safe_eval('a_list_variable', dict(a_list_variable=[1, 2, 3])) == [1, 2, 3]
    assert safe_eval('a_list_variable', dict(a_list_variable=[1, 2, 3]), True)[0] == [1, 2, 3]
    assert safe_eval('a_list_variable[1]', dict(a_list_variable=[1, 2, 3])) == 2
    assert safe_eval('a_list_variable[1]', dict(a_list_variable=dict(test=2))) == 2
    assert safe_eval('a_list_variable.test', dict(a_list_variable=dict(test=2))) == 2
   

# Generated at 2022-06-13 15:29:00.087455
# Unit test for function safe_eval
def test_safe_eval():
    # test eval of numbers, strings and booleans
    assert safe_eval("1") == 1
    assert safe_eval("-1") == -1
    assert safe_eval("1.1") == 1.1
    assert safe_eval("-1.1") == -1.1
    assert safe_eval("'test'") == 'test'
    assert safe_eval("'TEST'") == 'TEST'
    assert safe_eval("'1'") == '1'
    assert safe_eval("true")
    assert not safe_eval("false")
    if not sys.version_info < (3,):
        assert safe_eval("True")
        assert not safe_eval("False")
    # test expressions
    assert safe_eval("1 + 2") == 1 + 2

# Generated at 2022-06-13 15:29:08.924442
# Unit test for function safe_eval
def test_safe_eval():

    # Test 1: simple literals
    expr = '123'
    expected_result = 123
    result = safe_eval(expr)
    assert result == expected_result

    # Test 2: simple arithmetic
    expr = '1+2*3'
    expected_result = 7
    result = safe_eval(expr)
    assert result == expected_result

    # Test 3: simple conditional
    expr = '0 if false else 1'
    expected_result = 1
    result = safe_eval(expr)
    assert result == expected_result

    # Test 4: simple list creation
    # The syntax of the test expression is equivalent to the following
    # Python literal: [0, 1, 2, 3, 4, 5, 6]
    expr = '[i for i in range(7)]'

# Generated at 2022-06-13 15:29:18.450810
# Unit test for function safe_eval
def test_safe_eval():
    # simple test cases
    print("safe_eval(\"{}\"):", safe_eval("{}"))
    print("safe_eval(\"{'a' if True else 'b'}\", include_exceptions=True):", safe_eval("{'a' if True else 'b'}", include_exceptions=True))
    print("safe_eval(\"[{'a': ['Foo', 'Bar']}]\"):", safe_eval("[{'a': ['Foo', 'Bar']}]"))
    print("safe_eval(\"{'a': ['Foo', 'Bar']}\"):", safe_eval("{'a': ['Foo', 'Bar']}"))

# Generated at 2022-06-13 15:29:29.909786
# Unit test for function safe_eval
def test_safe_eval():
    # check that unsafe expressions can't get through
    assert safe_eval("__import__('os').system('echo hello')") == "__import__('os').system('echo hello')"
    assert safe_eval("__import__('os').system('echo hello')", include_exceptions=True) == ("__import__('os').system('echo hello')", None)
    assert safe_eval("import os; os.system('echo hello')") == "import os; os.system('echo hello')"
    assert safe_eval("{k:v for k,v in [('x',1)]}") == "{k:v for k,v in [('x',1)]}"

# Generated at 2022-06-13 15:29:41.178909
# Unit test for function safe_eval
def test_safe_eval():
    """
    Unit test for function safe_eval
    """
    # general truthy values
    assert safe_eval('1') == 1
    assert safe_eval('true') is True
    assert safe_eval('false') is False
    assert safe_eval('null') is None

    # complex boolean expressions
    assert safe_eval('(true and false) or (1 == 1)') is True
    assert safe_eval('true and (false or (1 == 1))') is True
    assert safe_eval('(true and false) or (1 == 1)') is True
    assert safe_eval(
        'true and (false or (1 == 1)) and (2 * 3 == 6)') is True

    # complex numeric expressions
    assert safe_eval('(1 + 1) * 2') == 4

# Generated at 2022-06-13 15:29:52.239158
# Unit test for function safe_eval
def test_safe_eval():

    # test function to use as a valid callable
    def tester(arg):
        return '123'

    # test data sets

# Generated at 2022-06-13 15:30:00.236756
# Unit test for function safe_eval
def test_safe_eval():
    # Successful tests
    assert safe_eval('(x in my_list if y)', dict(my_list=[1,2,3], x=2, y=True)) == 2
    assert safe_eval('(1 if False else 2)', dict()) == 2
    assert safe_eval('(1 if False else testvar)', dict(testvar=2)) == 2
    assert safe_eval('(testvar if False else 2)', dict(testvar=1)) == 1
    assert safe_eval('(True if False else False)', dict()) == False
    assert safe_eval('(testvar2 if testvar1 else False)', dict(testvar1=True, testvar2=True)) == True
    assert safe_eval('(1 if False else 2 if False else 3)', dict()) == 3

# Generated at 2022-06-13 15:30:08.187373
# Unit test for function safe_eval
def test_safe_eval():
    '''
    Unit test for function safe_eval.

    Note: the function already has extensive test coverage in the above mentioned
    stackoverflow question and its answers.
    '''
    # Test for syntax error
    test_syntax_err = safe_eval('{"a": "b"', {})
    assert type(test_syntax_err) == str
    assert test_syntax_err == '{"a": "b"'

    # Test for non-whitelisted AST node
    with_items = '[{"a": "b"}, {"c": "d"}]'
    try:
        test_non_whitelisted = safe_eval(with_items, {})
    except Exception as e:
        assert type(e) == Exception
        assert 'invalid expression' in str(e)

# Generated at 2022-06-13 15:30:14.869118
# Unit test for function safe_eval

# Generated at 2022-06-13 15:30:23.902255
# Unit test for function safe_eval
def test_safe_eval():
    expression = 'wibble'
    assert safe_eval(expression) == 'wibble'

    expression = 'false'
    assert safe_eval(expression) is False

    expression = 'true'
    assert safe_eval(expression) is True

    expression = 'null'
    assert safe_eval(expression) is None

    expression = 'foo is bar'
    assert safe_eval(expression) == 'foo is bar'

    expression = '1 + 1'
    assert safe_eval(expression) == 2

    expression = '1 + "1"'
    assert safe_eval(expression) is None

    expression = 'foo.bar()'
    assert safe_eval(expression) == 'foo.bar()'

    expression = 'foo.(ansible=bar)'
    assert safe_eval(expression) == 'foo.(ansible=bar)'

    expression

# Generated at 2022-06-13 15:30:30.638002
# Unit test for function safe_eval
def test_safe_eval():
    def noop():
        pass

# Generated at 2022-06-13 15:30:39.628946
# Unit test for function safe_eval
def test_safe_eval():
    class A:
        pass

    a = A()
    a.b = 'hello world'
    assert safe_eval('') == ''
    assert safe_eval(4) == 4
    assert safe_eval('4') == 4
    assert safe_eval('4 + 3') == 7
    assert safe_eval('4 + 3 * 4') == 16
    assert safe_eval('4 == 3') is False
    assert safe_eval('4 != 3') is True
    assert safe_eval('4 <= 3') is False
    assert safe_eval('4 >= 3') is True
    assert safe_eval('4 < 3') is False
    assert safe_eval('4 > 3') is True
    assert safe_eval('a.b') == 'hello world'

# Generated at 2022-06-13 15:30:46.579502
# Unit test for function safe_eval
def test_safe_eval():
    # following safe_eval invocations should all succeed without error
    safe_eval("1")
    safe_eval(1)
    safe_eval("true")
    safe_eval(True)
    safe_eval("null")
    safe_eval(None)
    safe_eval("[1,2]")
    safe_eval([1,2])
    safe_eval("{'k':'v'}")
    safe_eval({'k':'v'})
    safe_eval("(1,)")
    safe_eval((1,))
    safe_eval("1 + 1")
    safe_eval("myvar")
    safe_eval("1 < 1")
    safe_eval("1 <= 1")
    safe_eval("1 == 1")
    safe_eval("1 >= 1")
    safe_eval("1 > 1")

# Generated at 2022-06-13 15:30:55.600702
# Unit test for function safe_eval
def test_safe_eval():
    #
    # Test that unsafe code raises the proper exception
    #
    # Unsafe code that tries to evaluate to a string
    unsafe_string_code = "__import__('subprocess').check_output('ls')"
    try:
        safe_eval(unsafe_string_code)
        assert False
    except Exception:
        # Correct exception was raised
        pass

    # Unsafe code that tries to evaluate to an integer
    unsafe_int_code = "__import__('subprocess').check_output('ls').__len__()"
    try:
        safe_eval(unsafe_int_code)
        assert False
    except Exception:
        # Correct exception was raised
        pass

    #
    # Test that safe code does not raise an exception
    #
    # Safe string code

# Generated at 2022-06-13 15:31:10.717062
# Unit test for function safe_eval
def test_safe_eval():
    # Tests for proper handling of builtin functions.
    #
    # DISABLED: starting in python 3.5, int() can take a float argument, and
    #           we probably want to allow that
    # assert safe_eval("int(3.4)") == 3
    #
    # DISABLED: we probably don't want to allow function calls
    # assert safe_eval("len('three')") == 5
    # assert safe_eval("len([1,2,3])") == 3
    # assert safe_eval("dict(one=1)") == {'one': 1}

    # Tests for proper handling of operators.
    assert safe_eval("2 + 3 * 4 - 6") == 8
    assert safe_eval("2 + 3 * 4 - 6 / 2") == 11

# Generated at 2022-06-13 15:31:17.432702
# Unit test for function safe_eval

# Generated at 2022-06-13 15:31:29.104577
# Unit test for function safe_eval
def test_safe_eval():
    expr = "[{'a': 'A', 'b': 'B'}, 1, 2, 'hello', 'world', true, false, null, [1, 2], ['a', 'b']]"
    # list of (expected-result, eval-expression)

# Generated at 2022-06-13 15:31:36.796443
# Unit test for function safe_eval
def test_safe_eval():
    # check literal and nested
    complex = ast.parse("{'a': [1,2,3]}", mode='eval')
    x = safe_eval(complex)
    assert x == {'a': [1, 2, 3]}

    # check numeric ops
    numeric = ast.parse("1+2", mode='eval')
    x = safe_eval(numeric)
    assert x == 3

    # check string ops
    string = ast.parse("'foo' + 'bar'", mode='eval')
    x = safe_eval(string)
    assert x == 'foobar'

    # check bad syntax, should return original
    bad_syntax = ast.parse("foo bar", mode='eval')
    x = safe_eval(bad_syntax)
    assert x == bad_syntax

    # check calls to built-in

# Generated at 2022-06-13 15:31:44.725358
# Unit test for function safe_eval
def test_safe_eval():
    result = safe_eval("5+3")
    assert result == 8

    result = safe_eval("['a', 'b', 'c']")
    assert result == ['a', 'b', 'c']

    result = safe_eval("{'a': 1, 'b': 2}")
    assert result == {'a': 1, 'b': 2}

    result = safe_eval("['a', 'b', 'c'] | join(',')", dict(join=lambda x: ','.join(x)))
    assert result == "a,b,c"

    # Check that invalid expressions are evaluated to None
    result = safe_eval("1/0")
    assert result is None

    # Check that exceptions are not raised
    result = safe_eval("['a', 'b', 'c']", include_exceptions=True)
   

# Generated at 2022-06-13 15:31:55.185187
# Unit test for function safe_eval

# Generated at 2022-06-13 15:32:05.808579
# Unit test for function safe_eval
def test_safe_eval():
    # disabled function tests
    assert safe_eval('hashlib.md5') == 'hashlib.md5'
    assert safe_eval('hashlib') == 'hashlib'

    # simple evaluation tests
    assert safe_eval('1+1') == 2
    assert safe_eval('1+1 == 2') is True
    assert safe_eval('1+1 != 2') is False
    assert safe_eval('100*100') == 10000
    assert safe_eval('"hello"') == 'hello'

    # simple substitution tests
    assert safe_eval('one_plus_one') == 'one_plus_one'
    assert safe_eval('one_plus_one', dict(one_plus_one=2)) == 2

    # simple python datastructure tests
    # dict

# Generated at 2022-06-13 15:32:17.853574
# Unit test for function safe_eval
def test_safe_eval():
    expr = "{{ 1 | random }}"
    assert(isinstance(safe_eval(expr), string_types))

    expr = "[item for item in range(4)]"
    result = safe_eval(expr)
    assert(result == [0, 1, 2, 3])

    expr = "foo.bar"
    result = safe_eval(expr, dict(foo=dict(bar=42)))
    assert(result == 42)

    expr = "foo.bar"
    result = safe_eval(expr, dict(foo=dict(bar=dict(baz=42))))
    assert(result == dict(baz=42))

    expr = "{{ True }}"
    result = safe_eval(expr)
    assert(result is True)

    expr = "{{ False }}"
    result = safe_eval(expr)

# Generated at 2022-06-13 15:32:29.871608
# Unit test for function safe_eval
def test_safe_eval():
    '''
    Unit test for function safe_eval
    '''
    from ansible.module_utils.common.text.converters import to_text
    def test_expr(expr, result, locals=None, fn=safe_eval):
        if locals is None:
            locals = {}
        try:
            evald = fn(expr, locals)
            if result != evald:
                print("%s: %s != %s" % (expr, result, evald))
                sys.exit(1)
        except Exception as e:
            if result != to_text(e):
                print("%s: %s != %s" % (expr, result, to_text(e)))
                sys.exit(1)

    # basic tests
    test_expr('1', 1)

# Generated at 2022-06-13 15:32:40.103880
# Unit test for function safe_eval
def test_safe_eval():

    # Load test_safe_eval.yaml so that we can use its test cases
    # to validate this function.
    import os
    test_file_path = os.path.join(os.path.dirname(__file__), "test_safe_eval.yaml")
    if not os.path.exists(test_file_path):
        raise Exception("File %s not found!" % test_file_path)

    test_cases = {}
    with open(test_file_path, 'rb') as f:
        from ansible.module_utils.six import PY3
        if PY3:
            from yaml import SafeLoader
            test_cases = yaml.load(f, Loader=SafeLoader)
        else:
            from ansible.parsing.yaml.loader import AnsibleLoader
            test

# Generated at 2022-06-13 15:32:52.992977
# Unit test for function safe_eval
def test_safe_eval():
    eval_env = {'x': 32, 'y': [1, 2, 3]}
    # Python3: callable() moved to builtins, so provide C.CALLABLE_WHITELIST_NAME
    if sys.version_info[0] == 3:
        eval_env[C.CALLABLE_WHITELIST_NAME] = ['pow']
    else:
        # Python2: we might as well support callables
        # TODO: test this scenario
        import __builtin__
        eval_env['__builtin__'] = __builtin__
    # Simplest case: bool
    assert safe_eval('true', eval_env) == True
    # Simple int
    assert safe_eval('1', eval_env) == 1
    # Simple variable
    assert safe_eval('x', eval_env) == 32

# Generated at 2022-06-13 15:33:03.259754
# Unit test for function safe_eval
def test_safe_eval():
    import unittest

    class TestSafeEval(unittest.TestCase):
        def test_json_types(self):
            self.assertEqual(safe_eval("true"), True)
            self.assertEqual(safe_eval("false"), False)
            self.assertEqual(safe_eval("null"), None)

        def test_eval_safe_nodes(self):
            self.assertEqual(safe_eval("'string'"), 'string')
            self.assertEqual(safe_eval("'a string' + 'another string'"), 'a stringanother string')
            self.assertEqual(safe_eval("'a string' + 'another string' + ' a third string'"), 'a stringanother string a third string')

# Generated at 2022-06-13 15:33:14.770839
# Unit test for function safe_eval
def test_safe_eval():
    # assert successful tests
    assert safe_eval('{"foo": "bar"}') == {"foo": "bar"}
    assert safe_eval('[1,2,3]') == [1,2,3]
    assert safe_eval('True') is True
    assert safe_eval('1 + 1') == 2
    assert safe_eval('1 * (1 + 1)') == 2
    assert safe_eval('1 - 1 / 1') == 0

    # assert failure
    assert safe_eval('1 + 1') == 2

    assert safe_eval('__import__("os")') == '__import__("os")'
    assert safe_eval('__import__("os").getuid()') == '__import__("os").getuid()'

    # This works even if the __builtins__ is a dict and not a module
    OUR_GL

# Generated at 2022-06-13 15:33:25.601507
# Unit test for function safe_eval
def test_safe_eval():
    assert(safe_eval('1+1') == 2)
    assert(safe_eval('True') is True)
    assert(safe_eval('False') is False)
    assert(safe_eval('None') is None)
    assert(safe_eval('{"foo": "bar"}'))
    assert(safe_eval('["foo", "bar"]'))
    assert(safe_eval('("foo", "bar")'))
    assert(safe_eval("True or False") == True)
    assert(safe_eval("True and False") == False)
    assert(safe_eval("a_list_variable", dict(a_list_variable=["foo", "bar"])) == ["foo", "bar"])

# Generated at 2022-06-13 15:33:32.918007
# Unit test for function safe_eval
def test_safe_eval():
    '''
    Ensure that the safe eval function works as expected
    '''
    def assert_safe_eval(expr, expected, locals=None, include_exceptions=False):
        '''
        Helper to perform an assert in which we validate the
        results of safe_eval and include the expression we
        called on in the output if the assert fails
        '''
        result, exception = safe_eval(expr, locals=locals, include_exceptions=True)
        assert result == expected, "Expected: %s, Got: %s, input: %s" % (expected, result, expr)


    # simple tests, should evaluate to the same as input
    assert_safe_eval('abc', 'abc')
    assert_safe_eval('[1, 2, 3]', [1, 2, 3])
    assert_safe_eval

# Generated at 2022-06-13 15:33:43.894365
# Unit test for function safe_eval
def test_safe_eval():
    assert None == safe_eval(None)
    assert 'foo' == safe_eval('foo')
    assert 1.5 == safe_eval('1.5')
    assert 1.5 == safe_eval('1+0.5')
    assert 'foo' == safe_eval('1+"foo"')
    assert [1, 'foo'] == safe_eval('[1, "foo"]')
    assert {'a': 1, 'b': 'foo'} == safe_eval('{"a": 1, "b": "foo"}')
    assert {'a': 1, 'b': 'foo'} == safe_eval('dict(a=1,b="foo")')
    assert {'a': 1, 'b': 'foo'} == safe_eval('{u"a": 1, u"b": "foo"}')

# Generated at 2022-06-13 15:33:55.047525
# Unit test for function safe_eval

# Generated at 2022-06-13 15:34:05.701581
# Unit test for function safe_eval

# Generated at 2022-06-13 15:34:14.082204
# Unit test for function safe_eval
def test_safe_eval():

    assert safe_eval("1 + 2") == 3

    # this should fail, as ast.Call is a disallowed type
    try:
        safe_eval("1 + 2 * func(5)")
        assert False, "safe_eval call test failed"
    except:
        pass

    # this should fail, as str() is not in our CALL_ENABLED list
    try:
        safe_eval("1 + 2 * str(5)")
        assert False, "safe_eval call test failed"
    except:
        pass

    CALL_ENABLED.append('str')
    assert safe_eval("1 + 2 * str(5)") == "155"
    CALL_ENABLED.pop()

    # this should fail, as int() is not in our CALL_ENABLED list

# Generated at 2022-06-13 15:34:24.293974
# Unit test for function safe_eval
def test_safe_eval():
    # Test strings
    expr = '123'
    assert safe_eval(expr) == 123

    expr = '"hello"'
    assert safe_eval(expr) == 'hello'

    expr = "({'a': 1, 'b': 'c'})"
    assert safe_eval(expr) == {'a': 1, 'b': 'c'}

    expr = 'print'
    assert safe_eval(expr) == 'print'

    # Test inbuilt functions
    expr = 'True'
    assert safe_eval(expr) is True

    expr = 'False'
    assert safe_eval(expr) is False

    expr = 'None'
    assert safe_eval(expr) is None

    # Test invalid strings
    expr = 'abs'
    assert safe_eval(expr) == 'abs'


# Generated at 2022-06-13 15:34:42.053199
# Unit test for function safe_eval
def test_safe_eval():
    print("Testing with safe_eval")

# Generated at 2022-06-13 15:34:48.605652
# Unit test for function safe_eval
def test_safe_eval():
    # The type of JSON value
    # boolean
    assert safe_eval("true") is True
    assert safe_eval("false") is False
    # number
    assert safe_eval("1") == 1
    assert safe_eval("3.14") == 3.14
    # string
    assert safe_eval("'123'") == "123"
    # null
    assert safe_eval("null") is None
    # list
    assert safe_eval("[1,2,3]") == [1, 2, 3]
    # dict
    assert safe_eval("{'a': 1, 'b': 2}") == {'a': 1, 'b': 2}

    # Some variable assignments
    assert safe_eval("a = 1") == 1

# Generated at 2022-06-13 15:34:59.621711
# Unit test for function safe_eval

# Generated at 2022-06-13 15:35:08.082876
# Unit test for function safe_eval
def test_safe_eval():
    # This function is just to test the safe_eval function
    # so it is not important if the output is not really what we want
    #

    # Any other value is a valid input for this test
    for value_to_test in (1, True, False, 0, 100.1, {'test': 'test'}, 'test', [1, 2], (3, 4)):
        # We evaluate the value to test itself
        result = safe_eval(str(value_to_test))

        # And check that we have the same output
        msg = u"Value '%s' converted to '%s' instead of '%s'" % (value_to_test, result, value_to_test)
        assert result == value_to_test, msg

    # The only value that we want to fail is a function (except eval can be used on

# Generated at 2022-06-13 15:35:16.847455
# Unit test for function safe_eval
def test_safe_eval():

    # simple expressions
    assert safe_eval("1 + 1") == 2
    assert safe_eval("'foo'") == "foo"
    assert safe_eval("'foo' + 'bar'") == "foobar"

    # complex expressions
    assert safe_eval("[1, 2]") == [1, 2]
    assert safe_eval("{ 'a': 1, 'b': 2 }") == { "a": 1, "b": 2 }
    assert safe_eval("(1, 'a')") == (1, "a")

    # expressions involving missing variables
    assert safe_eval("missing_var") == "missing_var"

    # syntax errors
    assert safe_eval("1 +") == "1 +"

    # invalid expressions

# Generated at 2022-06-13 15:35:24.620413
# Unit test for function safe_eval
def test_safe_eval():
    # Basic tests
    if not safe_eval('{"foo": "abc"}') == {'foo': 'abc'}:
        sys.stderr.write("test_safe_eval: failed test_basic_dict\n")
        sys.exit(1)

    if not safe_eval('["foo","bar"]') == ['foo', 'bar']:
        sys.stderr.write("test_safe_eval: failed test_basic_list\n")
        sys.exit(1)

    if not safe_eval('["foo",{"bar": "abc"}]') == ['foo', {'bar': 'abc'}]:
        sys.stderr.write("test_safe_eval: failed test_list_dict\n")
        sys.exit(1)


# Generated at 2022-06-13 15:35:33.881620
# Unit test for function safe_eval
def test_safe_eval():
    # Test safe_eval with a complex dictionary
    complex_dict = '''{'first': 'key',
                    'second':
                    {'nested': 'dict',
                    'another': {'key': 'value'}}}'''

    new_dict = safe_eval(complex_dict)
    assert new_dict == {'first': 'key',
                        'second':
                        {'nested': 'dict',
                        'another': {'key': 'value'}}}

    # Test safe_eval with a complex list
    complex_list = '''[1, 'two', ['three three', {'key': 'value'}], 'four', ['five']]'''

    new_list = safe_eval(complex_list)

# Generated at 2022-06-13 15:35:41.076692
# Unit test for function safe_eval

# Generated at 2022-06-13 15:35:51.326117
# Unit test for function safe_eval
def test_safe_eval():
    # Trying to access attributes of None
    expr = "var.hostvars[inventory_hostname].foo"
    result = safe_eval(expr)
    assert result == expr, "test_safe_eval() failed with: %s" % result

    # Trying to access attributes of a string
    expr = "var.hostvars[inventory_hostname].foo"
    result = safe_eval(expr, locals={'var': {'hostvars': {'localhost': 'localhost'}}})
    assert result == expr, "test_safe_eval() failed with: %s" % result

    # Trying to access attributes of an array
    expr = "var.hostvars[inventory_hostname].foo"
    result = safe_eval(expr, locals={'var': {'hostvars': {'localhost': ['bar']}}})

# Generated at 2022-06-13 15:36:02.590439
# Unit test for function safe_eval
def test_safe_eval():
    try:
        import ast
    except ImportError:
        # Skip if ast is not present
        return

    # List of tuples (input, expected_output)

# Generated at 2022-06-13 15:36:23.427685
# Unit test for function safe_eval
def test_safe_eval():
    print("testing safe_eval")

# Generated at 2022-06-13 15:36:30.629397
# Unit test for function safe_eval
def test_safe_eval():
    safe_dict = dict(a=1, b=2, c='cow')


# Generated at 2022-06-13 15:36:41.603267
# Unit test for function safe_eval
def test_safe_eval():
    # Begin tests
    # Test use in with_items
    assert safe_eval("a_list_variable") == "a_list_variable"
    # Test empty string
    assert safe_eval("") == ""
    # Test numeric string
    assert safe_eval("5") == 5
    # Test float
    assert safe_eval("5.5") == 5.5
    # Test float string
    assert safe_eval("5.5") == 5.5
    # Test negative string
    assert safe_eval("-5.5") == -5.5
    # Test unicode string
    assert safe_eval("u'unicode string'") == u'unicode string'
    # Test byte string
    assert safe_eval("b'byte string'") == b'byte string'
    # Test dict string

# Generated at 2022-06-13 15:36:47.281856
# Unit test for function safe_eval
def test_safe_eval():
    def _safe_eval(expr, expected, locals=None, include_exceptions=False):
        result, error = safe_eval(expr, locals=locals, include_exceptions=True)
        assert error is None, "%s -> %s" % (expr, error)
        assert result == expected, "'%s'.safe_eval() returned %s" % (expr, result)

    # assert no exception is thrown
    safe_eval("{'foo': 'bar'}")

    # assert valid expressions are evaluated
    assert safe_eval("{'foo': 'bar'}") == {'foo': 'bar'}
    assert safe_eval("['foo', 'bar']") == ['foo', 'bar']
    assert safe_eval("['foo', ('bar',)]") == ['foo', ('bar',)]

# Generated at 2022-06-13 15:36:58.706784
# Unit test for function safe_eval
def test_safe_eval():
    fake_dict = dict(foo='bar', baz='qux')

    # check if safe_eval works with good inputs
    assert safe_eval('foo') == 'foo'
    assert safe_eval('123') == 123
    assert safe_eval('foo.bar') == 'foo.bar'
    assert safe_eval('[1, 2, 3]') == [1, 2, 3]
    assert safe_eval('{"a": 1, "b": 2, "c": 3}') == {"a": 1, "b": 2, "c": 3}
    assert safe_eval('[ 1 + 2, 3 * 4, 5 - 6 ]') == [3, 12, -1]

# Generated at 2022-06-13 15:37:08.968085
# Unit test for function safe_eval
def test_safe_eval():
    '''
    Test safe_eval()
    '''
    # expressions that should evaluate with no exception

# Generated at 2022-06-13 15:37:19.595006
# Unit test for function safe_eval

# Generated at 2022-06-13 15:37:24.257712
# Unit test for function safe_eval
def test_safe_eval():
    '''
    test the safe_eval function, invoking with various inputs and expecting various output
    '''
    import os
    import stat
    import time
    import unittest


# Generated at 2022-06-13 15:37:34.265706
# Unit test for function safe_eval
def test_safe_eval():
    # empty module, just requiring to test the function
    # this is needed to handle relative imports
    module = sys.modules[__name__]

    module.assertEqual(
        safe_eval('[1, 2, 3, 4]', dict()),
        [1, 2, 3, 4]
    )

    module.assertEqual(
        safe_eval('[1, 2, (3, 4)]', dict()),
        [1, 2, (3, 4)]
    )

    module.assertEqual(
        safe_eval('{1: 2, 3: 4, 5: 6}', dict()),
        {1: 2, 3: 4, 5: 6}
    )


# Generated at 2022-06-13 15:37:44.203675
# Unit test for function safe_eval
def test_safe_eval():
    # simple tests
    assert safe_eval("a + 1") == "a + 1"
    assert safe_eval("1 + 1") == 2

    # test a literal
    assert safe_eval("a_list_variable", {"a_list_variable": [1, 2, 3]}) == [1, 2, 3]

    # test a literal with a Jinja2 filter
    assert safe_eval("a_list_variable|length", {"a_list_variable": [1, 2, 3]}) == 3

    # can't really test this one, Jinja2 isn't embedded
    assert safe_eval("a_list_variable|random", {"a_list_variable": [1, 2, 3]}) == "a_list_variable|random"

    # test a variable lookup