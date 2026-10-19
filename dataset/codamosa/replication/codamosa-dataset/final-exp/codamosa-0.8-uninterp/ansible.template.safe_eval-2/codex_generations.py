

# Generated at 2022-06-13 15:28:07.328959
# Unit test for function safe_eval
def test_safe_eval():
    FAILS_TO_PARSE = [
        '{{ [] }}',   # no list comprehension
        #'{{ print }}', # no statements
        #'{{ print("foo") }}', # no statements
        #'{{ "foo" if "bar" in x }}', # no control-flow
        '{{ [x for x in a if x in b] }}', # no list comprehension
        '{{ [x for x in a] }}', # no list comprehension
        '{{ [] }}', # no list comprehension
        '{{ {} }}', # no dict comprehension (or dict literal)
    ]

# Generated at 2022-06-13 15:28:16.623069
# Unit test for function safe_eval
def test_safe_eval():
    # ARRANGE
    # Make sure we have the expected Python version for the tests below.
    if sys.version_info[0] < 3:
        raise AssertionError("Python 3 required for the tests to work")

    # ACT & ASSERT
    assert safe_eval("a_list_of_stuff.1") == "a_list_of_stuff.1"

    assert safe_eval("a_list_of_stuff[1]") == "a_list_of_stuff[1]"

    assert safe_eval("a_list_of_stuff[1]", locals={"a_list_of_stuff": [1, 2, 3]}) == 2


# Generated at 2022-06-13 15:28:24.652781
# Unit test for function safe_eval
def test_safe_eval():

    # Verify the safe_eval function evaluates a string and returns back a value
    result = safe_eval("('abcd' is 'abcd')")
    assert result is True

    # Verify the safe_eval function returns back an error if the expression contains
    # a key word which is not in the SAFE_NODES list
    result = safe_eval("a ** b")
    assert "invalid expression" in result

    # Verify the safe_eval function throws an error if the expression contains a
    # key word which is not in the SAFE_NODES list
    result = safe_eval("False ** False")
    assert "invalid expression" in result

    # Verify the safe_eval function returns back an error if the expression contains
    # a key word which is not in the SAFE_NODES list
    result = safe_eval("a()")

# Generated at 2022-06-13 15:28:34.619668
# Unit test for function safe_eval
def test_safe_eval():
    # Evaluate expressions that are in a datastructure
    x = safe_eval("True and False")
    if x:
        raise Exception("should be False")
    x = safe_eval("True and 'a'")
    if not x:
        raise Exception("should be 'a'")
    x = safe_eval("('a' or 'b') and True")
    if x != 'a':
        raise Exception("should be 'a'")

    # Evaluate expressions that are in a string
    x = safe_eval("VARIABLE", locals=dict(VARIABLE="THIS"))
    assert x == "THIS", "Should be 'THIS', got '%s'" % x

# Generated at 2022-06-13 15:28:44.109212
# Unit test for function safe_eval
def test_safe_eval():
    '''Unit test for function safe_eval'''
    # From http://stackoverflow.com/questions/12523516/using-ast-and-whitelists-to-make-pythons-eval-safe

    # A clean expression
    expr = 'foo == 42'
    print('\nTesting expression: %s' % expr)
    print('safe_eval result: %s' % safe_eval(expr, dict(foo=42), include_exceptions=True))
    print('eval result:      %s' % eval(expr, dict(foo=42)))

    # An expression that does not parse
    expr = '42 == foo'
    print('\nTesting expression: %s' % expr)

# Generated at 2022-06-13 15:28:50.603502
# Unit test for function safe_eval
def test_safe_eval():
    # The purpose of this test is to check that safe_eval correctly
    # fails on unsafe expressions

    # Simple expression
    expr = "1 + 2"
    assert safe_eval(expr) == 3

    # Dict expression
    expr = "{'a': 1}"
    assert safe_eval(expr) == {'a': 1}

    # List expression
    expr = "[1, 2, 3]"
    assert safe_eval(expr) == [1, 2, 3]

    # Simple call expression
    expr = "str(2)"
    assert safe_eval(expr) == "2"

    # Tubple expression
    expr = "(1, 2)"
    assert safe_eval(expr) == (1, 2)

    # Subcall fail expression
    expr = "[len([1, 2])]"

# Generated at 2022-06-13 15:28:59.391256
# Unit test for function safe_eval

# Generated at 2022-06-13 15:29:08.378176
# Unit test for function safe_eval
def test_safe_eval():

    expr = 'a'
    locals = {'a': 1}
    result, err = safe_eval(expr, locals, True)
    assert err is None
    assert result == 1

    expr = 'a + 1'
    locals = {'a': 1}
    result, err = safe_eval(expr, locals, True)
    assert err is None
    assert result == 2

    expr = 'a_list'
    locals = {'a_list': [1, 2, 3]}
    result, err = safe_eval(expr, locals, True)
    assert err is None
    assert result == [1, 2, 3]

    expr = 'a_tuple'
    locals = {'a_tuple': (1, 2, 3)}
    result, err = safe_eval(expr, locals, True)
    assert err

# Generated at 2022-06-13 15:29:18.102223
# Unit test for function safe_eval
def test_safe_eval():
    '''
    Test a few different expressions.  Enabling all the builtins
    can be done, but it's not necessary as long as we ensure function
    calls are only to builtins that we've verified as being safe.
    '''
    # TODO: add some call tests

# Generated at 2022-06-13 15:29:29.316557
# Unit test for function safe_eval
def test_safe_eval():
    """
    This is the basic test for the function safe_eval.
    It creates a list of expected results and executes the function with
    the same list of expressions to test.

    :return:
    """
    # list of tuples with each tuple containing expression to be evaluated
    # and result to be returned as output

# Generated at 2022-06-13 15:29:39.367184
# Unit test for function safe_eval

# Generated at 2022-06-13 15:29:50.360027
# Unit test for function safe_eval
def test_safe_eval():
    # Test each type of expression against both safe and unsafe values
    # to ensure that safe_eval returns None for each.
    bool_exprs = ['true', 'false']
    for expr in bool_exprs:
        for value in ['true', 'false', '1', '0', 1, 0]:
            assert safe_eval("%s == %s" % (expr, value)) == (value == expr)

    int_exprs = ['0', '1', '-1']
    for expr in int_exprs:
        for value in ['true', 'false', '1', '0', 1, 0]:
            assert safe_eval("%s == %s" % (expr, value)) == (value == int(expr))
            assert safe_eval("%s + %s" % (expr, value)) == (int(expr) + value)

# Generated at 2022-06-13 15:29:58.806073
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval('1 == 1') is True
    assert safe_eval('1 < 2') is True
    assert safe_eval('1 + 1') == 2
    assert safe_eval('False') is False
    assert safe_eval('[1, 2, 3]') == [1, 2, 3]
    assert safe_eval('{1: 2, 3: 4}') == {1: 2, 3: 4}
    assert safe_eval('"abcd"') == "abcd"
    assert safe_eval('None') is None

    # fails with syntax error
    assert safe_eval('{{a') == "{{a"

    # fails with certifiably unsafe call
    assert safe_eval('open("/etc/passwd")') == "open(\"/etc/passwd\")"


# Generated at 2022-06-13 15:30:07.736987
# Unit test for function safe_eval
def test_safe_eval():
    # When expr contains invalid syntax, safe_eval should return expr.
    test = "{{ foo"
    assert safe_eval(test) == test
    assert safe_eval(test, include_exceptions=True) == (test, None)

    # When expr contains a call to an invalid function, safe_eval should raise
    # an exception.
    test = "{{ foo() }}"
    assert safe_eval(test) == test
    assert safe_eval(test, include_exceptions=True) == (test, Exception("invalid function: foo"))

    # When expr contains a call to a builtin function, safe_eval should return
    # expr.
    CALL_ENABLED.append("sys_setresuid")
    test = "{{ sys_setresuid(65534,65534,65534) }}"

# Generated at 2022-06-13 15:30:18.283089
# Unit test for function safe_eval
def test_safe_eval():
    """
    Run tests against the safe_eval function.
    """
    import pytest


# Generated at 2022-06-13 15:30:25.335882
# Unit test for function safe_eval
def test_safe_eval():
    # Test case:
    expr = "[{'a': 'b'}] if True else None"
    try:
        result = safe_eval(expr, locals={'True': True}, include_exceptions=False)
        assert result == [{'a': 'b'}]
    except AssertionError as e:
        print(e)
        sys.exit(1)

    # Test case:
    expr = "[{'a': 'b'}] if True else None"
    try:
        result = safe_eval(expr, locals={'True': False}, include_exceptions=False)
        assert result is None
    except AssertionError as e:
        print(e)
        sys.exit(1)

    # Test case:
    expr = "[{'a': 'b'}] if True else None"

# Generated at 2022-06-13 15:30:31.585841
# Unit test for function safe_eval

# Generated at 2022-06-13 15:30:40.840133
# Unit test for function safe_eval

# Generated at 2022-06-13 15:30:52.555915
# Unit test for function safe_eval
def test_safe_eval():
    ''' test safe_eval '''
    from ast import literal_eval

    # these are a collection of strings and their expected
    # return value when run through safe_eval

# Generated at 2022-06-13 15:30:58.968635
# Unit test for function safe_eval

# Generated at 2022-06-13 15:31:10.861470
# Unit test for function safe_eval
def test_safe_eval():
    '''
    This is a unit test for the safe_eval function.

    It is not a test per se, but can be run standalone to check that
    different expressions evaluate as expected.
    '''
    # We want to be able to pass both a string expression to evaluate
    # or a pre-parsed AST expression to evaluate.
    #
    # For instance, the string expression:
    #
    #   "a.keys()"
    #
    # is parsed by ast.parse as:
    #
    #   <_ast.Expression object at 0x7fb6bbe5dbd0>
    #
    # so to test both string expressions and AST expressions
    # we pass a tuple of (expression, parsed_expression) in the
    # test_expressions array below.

# Generated at 2022-06-13 15:31:17.843155
# Unit test for function safe_eval
def test_safe_eval():
    def test_error(expr, msg):
        v, e = safe_eval(expr, include_exceptions=True)
        if e is None:
            raise Exception("%s did not fail when it should have: %s" % (expr, v))
        if not msg in to_native(e):
            raise Exception("expected to %s but got: %s" % (msg, to_native(e)))

    def test_success(expr):
        v, e = safe_eval(expr, include_exceptions=True)
        if e is not None:
            raise Exception("%s failed when it should not have: %s" % (expr, e))

    test_error("__import__('os').system('echo hello')", "invalid expression")

# Generated at 2022-06-13 15:31:29.286427
# Unit test for function safe_eval
def test_safe_eval():
    '''
    Make sure the safe_eval is doing what we expect
    '''
    # These should all work
    assert safe_eval("1") == 1
    assert safe_eval("2 + 3") == 5
    assert safe_eval("2 + 3 * (4 - 2)") == 10
    x = "hello"
    assert safe_eval("x", locals=dict(x=x)) == x
    assert safe_eval("x + 'world'", locals=dict(x=x)) == (x + 'world')
    assert safe_eval("1 != 0") is True

    # None of these should work
    try:
        safe_eval("[i for i in range(10)]")
        assert False, "List Comprehensions not allowed"
    except Exception:
        pass


# Generated at 2022-06-13 15:31:36.917308
# Unit test for function safe_eval

# Generated at 2022-06-13 15:31:42.199457
# Unit test for function safe_eval

# Generated at 2022-06-13 15:31:53.112489
# Unit test for function safe_eval

# Generated at 2022-06-13 15:32:04.369559
# Unit test for function safe_eval
def test_safe_eval():
    expr = "{{ [ 1, 2, 3] }}"
    expected = [1, 2, 3]
    actual = safe_eval(expr)
    assert actual == expected, 'Failed to evaluate %s as a list and got output %s instead of %s' % (expr, actual, expected)

    expr = "{{ {'a': 1, 'b': 2} }}"
    expected = {'a': 1, 'b': 2}
    actual = safe_eval(expr)
    assert actual == expected, 'Failed to evaluate %s as a dict and got output %s instead of %s' % (expr, actual, expected)

    expr = "[item for item in [1, 2, 3] if item > 1]"
    expected = [2, 3]
    actual = safe_eval(expr)

# Generated at 2022-06-13 15:32:08.989305
# Unit test for function safe_eval
def test_safe_eval():
    '''
    Test function for safe_eval. This test function can also be used
    for other unit testing of safe_eval.
    '''
    assert safe_eval('3 * [1,2]') == [1, 2, 1, 2, 1, 2]
    assert safe_eval('2 + 2') == 4
    assert safe_eval('"foo" in ["foo", "bar", "baz"]') is True
    assert safe_eval('"foo" not in ["foo", "bar", "baz"]') is False
    assert safe_eval('"foobar"') == "foobar"
    assert safe_eval('{ "test": "foo", "bar": "baz" }') == { "test": "foo", "bar": "baz" }

# Generated at 2022-06-13 15:32:19.331209
# Unit test for function safe_eval
def test_safe_eval():
    # Test simple expression
    assert safe_eval('x', dict(x='foo')) == 'foo'
    # Test complex expression
    assert safe_eval('x+y', dict(x='foo', y='bar')) == 'foobar'
    # Test invalid expression
    assert safe_eval('some_unknown_variable', {}) == 'some_unknown_variable'
    # Test valid expression with invalid function
    assert safe_eval('some_unknown_variable or "foo"', {}) == 'foo'
    # Test invalid function
    assert safe_eval('str(some_unknown_variable)', {}) == 'str(some_unknown_variable)'

    # Test unsafe expression
    assert safe_eval('__import__("os").system("id")') == '__import__("os").system("id")'

    # Test valid function

# Generated at 2022-06-13 15:32:31.868658
# Unit test for function safe_eval
def test_safe_eval():

    assert safe_eval('[1,2,3,4]') == [1, 2, 3, 4]
    assert safe_eval('[1,2,3,4]', include_exceptions=True)[0] == [1, 2, 3, 4]
    assert safe_eval('2+3') == 5
    assert safe_eval('2+3', include_exceptions=True)[0] == 5
    assert safe_eval('[1,2,3,4]') == [1, 2, 3, 4]
    assert safe_eval('[1,2,3,4]', include_exceptions=True)[0] == [1, 2, 3, 4]

# Generated at 2022-06-13 15:32:43.196029
# Unit test for function safe_eval
def test_safe_eval():
    # Define some test cases to apply to safe_eval()
    test_cases = [
        ('1', 1),
        ('1.1', 1.1),
        ('"foo"', 'foo'),
        ("''", ''),
        ('["foo","bar"]', ['foo', 'bar']),
        ('{"foo":"bar"}', {'foo': 'bar'}),
        ('{"foo":"bar","baz": [1, 2, 3]}', {'foo': 'bar', 'baz': [1, 2, 3]}),
        ('null', None),
        ('true', True),
        ('false', False),
        ('[1,2,3]', [1, 2, 3]),
    ]

    # Define some invalid test cases

# Generated at 2022-06-13 15:32:53.311183
# Unit test for function safe_eval
def test_safe_eval():

    # Simple expressions
    assert isinstance(safe_eval('true'), bool)
    assert isinstance(safe_eval('t', dict(t=True)), bool)
    assert isinstance(safe_eval('t', dict(t=1)), bool)
    assert isinstance(safe_eval('t', dict(t=0)), bool)
    assert isinstance(safe_eval('t', dict(t=0.1)), bool)
    assert isinstance(safe_eval('t', dict(t='')), bool)
    assert isinstance(safe_eval('t', dict(t='a')), bool)
    assert isinstance(safe_eval('t', dict(t=[])), bool)
    assert isinstance(safe_eval('t', dict(t={})), bool)

# Generated at 2022-06-13 15:32:59.158684
# Unit test for function safe_eval
def test_safe_eval():
    # simple expression that can be evaluated
    if sys.version_info[0] < 3:
        assert safe_eval('[True,False]') == [True, False]
    else:
        assert safe_eval('[True,False]') == [True, False]
    assert safe_eval('{"fizz":"buzz"}') == {"fizz": "buzz"}
    assert safe_eval('foo==bar') == 'foo==bar'
    # invalid expression; eval() would raise a SyntaxError
    assert safe_eval('foo bar') == 'foo bar'
    assert safe_eval('foo()') == 'foo()'
    # invalid expression that is a valid python string.  in this case,
    # safe_eval() should return the original string
    assert safe_eval('"foo()"') == 'foo()'
    # variables

# Generated at 2022-06-13 15:33:08.055418
# Unit test for function safe_eval
def test_safe_eval():
    # simple tests for safe eval
    assert safe_eval("[]") == []
    assert safe_eval("(1,2,3)") == (1, 2, 3)
    assert safe_eval("{'a':1, 'b':2, 'c':3}") == {'a': 1, 'b': 2, 'c': 3}
    assert safe_eval("123") == 123
    assert safe_eval("-42") == -42
    assert safe_eval("123.45") == 123.45
    assert safe_eval("-42.01") == -42.01
    assert safe_eval("some_var") == 'some_var'
    assert safe_eval("some_var.split()") == 'some_var.split()'
    assert safe_eval("some_var|int") == 'some_var|int'

# Generated at 2022-06-13 15:33:17.362526
# Unit test for function safe_eval
def test_safe_eval():
    from ansible.module_utils.common.text.converters import to_text
    from ansible.module_utils.common.collections import is_sequence

    # List of tests to perform and their expected results
    # Note: safe_eval() can be called with or without locale variables
    #       If locale vars are provided, they will be prefixed to the expression
    #       If they are not provided, they are initialized to blank in safe_eval()

# Generated at 2022-06-13 15:33:27.660878
# Unit test for function safe_eval

# Generated at 2022-06-13 15:33:34.114765
# Unit test for function safe_eval

# Generated at 2022-06-13 15:33:44.973671
# Unit test for function safe_eval

# Generated at 2022-06-13 15:33:55.980856
# Unit test for function safe_eval
def test_safe_eval():
    # The 'expr' object should be a string.
    (result, exception) = safe_eval(123, include_exceptions=True)
    assert result == 123
    assert exception is None

    # The 'expr' object should be a string.
    (result, exception) = safe_eval(['a', 'b'], include_exceptions=True)
    assert result == ['a', 'b']
    assert exception is None

    # The 'expr' object should be a string.
    (result, exception) = safe_eval({'a': 1, 'b': 2}, include_exceptions=True)
    assert result == {'a': 1, 'b': 2}
    assert exception is None

    # Expected to fail since ast.Call and ast.Name are not allowed

# Generated at 2022-06-13 15:34:06.083908
# Unit test for function safe_eval
def test_safe_eval():
    import random
    import string
    # setup some test data to use
    letters = string.ascii_lowercase
    valid_json = dict((i, random.choice(letters)) for i in range(0, 10))
    valid_json["true"] = True
    valid_json["false"] = False
    valid_json["null"] = None
    valid_json["str_obj"] = "a_str"
    valid_json["int_obj"] = 1
    valid_json["float_obj"] = 1.0
    valid_json["list_obj"] = [1, 2, 3, 4]
    valid_json["dict_obj"] = {"key": "value"}
    valid_json["tuple_obj"] = (1, 2)

    assert safe_eval(expr=valid_json, include_exceptions=False)

# Generated at 2022-06-13 15:34:17.773044
# Unit test for function safe_eval
def test_safe_eval():
    # Basic test
    assert safe_eval("1 + 1") == 2

    # Test None as a value and key
    assert safe_eval("{None: 'None'}") == {None: 'None'}

    # Test booleans
    assert safe_eval("True") is True
    assert safe_eval("true") is True
    assert safe_eval("False") is False
    assert safe_eval("false") is False

    # Test newlines, tabs and quotes
    strings = ['["1", "2", "3"]', '["1", \n "2", \n "3"]', '["1", \t \n "2", \t \n "3"]']
    expected = ['1', '2', '3']
    for string in strings:
        assert safe_eval(string) == expected

    # Test various data types


# Generated at 2022-06-13 15:34:27.284861
# Unit test for function safe_eval

# Generated at 2022-06-13 15:34:35.592925
# Unit test for function safe_eval
def test_safe_eval():
    # test some valid expressions
    if safe_eval("10") != 10:
        raise Exception("Failed eval test")
    if safe_eval("'10'") != '10':
        raise Exception("Failed eval test")
    if safe_eval("'{}'".format('10')) != "{}".format('10'):
        raise Exception("Failed eval test")
    if safe_eval("['test', 20]") != ['test', 20]:
        raise Exception("Failed eval test")
    if safe_eval("{'test': 20}") != {'test': 20}:
        raise Exception("Failed eval test")
    if safe_eval("'test'") != 'test':
        raise Exception("Failed eval test")

# Generated at 2022-06-13 15:34:44.016375
# Unit test for function safe_eval
def test_safe_eval():
    '''
    Make sure that safe_eval handles all valid python expressions.
    '''
    # Line below tests list comprehension
    assert safe_eval("[i for i in j]") == [i for i in j]
    # Line below tests set comprehension
    assert safe_eval("{i for i in j}") == {i for i in j}
    # Line below tests dict comprehension
    assert safe_eval("{i: i for i in j}") == {i: i for i in j}
    # Line below tests set
    assert safe_eval("{i, j}") == {i, j}
    # Line below tests dict
    assert safe_eval("{'i' : i, 'j': j}") == {'i' : i, 'j': j}
    assert safe_eval("1") == 1
    assert safe

# Generated at 2022-06-13 15:34:51.975425
# Unit test for function safe_eval
def test_safe_eval():
    print("Testing safe_eval")
    # ast-safe expressions

# Generated at 2022-06-13 15:35:01.949982
# Unit test for function safe_eval
def test_safe_eval():
    # run through some simple test cases
    def _test(test_input, output_type, output_value):
        assert safe_eval(test_input) == output_value
        assert type(safe_eval(test_input)) == output_type

    _test('1+1', int, 2)
    # _test('str(1+1)', str, '2')
    _test('1+1', int, 2)
    _test('"foo" + "bar"', str, 'foobar')
    _test('"foo" * 3', str, 'foofoofoo')
    _test('"foo" in "foobar"', bool, True)
    _test('"foo" not in "foobar"', bool, False)
    _test('1 == 1', bool, True)

# Generated at 2022-06-13 15:35:09.781386
# Unit test for function safe_eval

# Generated at 2022-06-13 15:35:19.168959
# Unit test for function safe_eval

# Generated at 2022-06-13 15:35:28.801401
# Unit test for function safe_eval

# Generated at 2022-06-13 15:35:35.129714
# Unit test for function safe_eval
def test_safe_eval():
    import nose

    # Should not raise exceptions
    safe_eval('3 + 2')                   # Addition
    safe_eval('3 - 2')                   # Subtraction
    safe_eval('3 * 2')                   # Multiplication
    safe_eval('3 / 2')                   # Division
    safe_eval('3 ^ 2')                   # Exponentiation
    safe_eval('3 and 2')                 # and
    safe_eval('3 or 2')                  # or
    safe_eval('3, 2')                    # tuple
    safe_eval('[1, 2, 3]')               # list
    safe_eval('(1, 2, 3)')               # set
    safe_eval('{"a": 1, "b": 2}')        # dict
    safe_eval('5 > 4')                   # greater than
    safe_eval('4 > 4')

# Generated at 2022-06-13 15:35:43.593626
# Unit test for function safe_eval
def test_safe_eval():
    def _t(s, val=None, e=None):
        res = safe_eval(s, include_exceptions=True)
        if e is None:
            assert res[0] == val, res
        else:
            assert isinstance(res[1], e), res
            assert res[0] == s, res

    _t('foo')
    _t('foo.bar')
    _t('foo.bar()')
    _t('foo["bar"]')
    _t('[1,2,3]')
    _t('{"foo": "bar"}')
    _t('True')
    _t('False')
    _t('true', True)
    _t('false', False)
    _t('null', None)

    # booleans
    _t('true and not true', False)



# Generated at 2022-06-13 15:35:53.618625
# Unit test for function safe_eval
def test_safe_eval():
    # Test for bug #27775
    if not safe_eval('4 in [1,2,3]'):
        raise AssertionError('safe_eval() returned incorrect response')

    if safe_eval('[x for x in range(5) if x in 4]'):
        raise AssertionError('safe_eval() did not detect correct syntax error')

    if not safe_eval('{}; None'):
        raise AssertionError('safe_eval() should return correct response')

    if not safe_eval('{}'):
        raise AssertionError('safe_eval() should return correct response')

    if not safe_eval('[]'):
        raise AssertionError('safe_eval() should return correct response')


# Generated at 2022-06-13 15:35:59.752383
# Unit test for function safe_eval

# Generated at 2022-06-13 15:36:08.330190
# Unit test for function safe_eval
def test_safe_eval():

    # The following assert is expected to fail as Jinja2
    # evaluates strings with quotes as sequences.
    assert safe_eval('"foo"') == '"foo"'

    # The following assert is expected to fail as Jinja2
    # evaluates strings with quotes as sequences.
    assert safe_eval("'foo'") == "'foo'"

    assert safe_eval(42) == 42
    assert safe_eval(42.42) == 42.42

    assert safe_eval("42") == 42
    assert safe_eval("42.42") == 42.42

    assert safe_eval("True") == True
    assert safe_eval("False") == False

    assert safe_eval("None") == None

    assert safe_eval("42+42") == 84

    assert safe_eval("42+42") == 84

# Generated at 2022-06-13 15:36:16.638999
# Unit test for function safe_eval

# Generated at 2022-06-13 15:36:25.623944
# Unit test for function safe_eval
def test_safe_eval():
    # Verify handling of invalid string
    expr = "{{ my_variable }}"
    try:
        safe_eval(expr)
    except Exception as e:
        pass
    else:
        assert False, 'invalid string "%s" did not raise exception: %s' % (expr)

    # Verify handling of valid string
    expr = "my_list | length"
    result = safe_eval(expr)
    assert expr == result, 'valid string "%s" was changed after evaluation: %s' % (expr, result)

    # Verify handling of invalid expression
    expr = "{{ my_list | reject('search','foo') | list }}"
    try:
        safe_eval(expr)
    except Exception as e:
        assert e, 'invalid expression "%s" did not raise exception: %s' % (expr, e)
   

# Generated at 2022-06-13 15:36:32.660525
# Unit test for function safe_eval

# Generated at 2022-06-13 15:36:37.730035
# Unit test for function safe_eval
def test_safe_eval():
    # Examples of successful safe_eval
    assert isinstance(safe_eval('[1, 2, 3]'), list)
    assert isinstance(safe_eval('{\'a\': 1}'), dict)
    assert isinstance(safe_eval('[1, 2, 3] + [4, 5]'), list)
    assert isinstance(safe_eval('[1, 2, 3] * 2'), list)
    assert safe_eval('"foo" + " bar"') == "foo bar"
    assert safe_eval('"foo" * 3') == "foofoofoo"
    assert safe_eval('1 | 2') == 2
    assert safe_eval('1 ^ 2') == 3
    assert safe_eval('1 & 2') == 0

# Generated at 2022-06-13 15:36:45.279867
# Unit test for function safe_eval
def test_safe_eval():
    '''
    Test function that runs a full suite of safe_eval tests
    '''
    # Note: This try/except block is needed because of the __file__ reference below
    try:
        from ansible.utils.display import Display
    except ImportError:
        # This is the case where someone tries to run the module directly
        # as a script, so we will just print the exception and exit.
        display = Display()
        display.warning('Unable to import ansible.utils.display')
        sys.exit()

    display = Display()
    display.display('#' * 25 + ' Testing safe_eval ' + '#' * 25)


# Generated at 2022-06-13 15:36:56.870252
# Unit test for function safe_eval
def test_safe_eval():
    expr = '2 + 3'
    assert safe_eval(expr) == 2 + 3
    expr = '{"a": [1,2,3]}'
    assert safe_eval(expr) == {"a": [1,2,3]}
    expr = '2 ** 3'
    assert safe_eval(expr) == 8
    expr = '1 < 2'
    assert safe_eval(expr) is True
    expr = '"foo" == "foo"'
    assert safe_eval(expr) is True
    expr = '("foo" == "foo")'
    assert safe_eval(expr) is True
    expr = '("foo" == "foo") and (1 == 1)'
    assert safe_eval(expr) is True
    expr = '(("foo" == "foo") and (1 == 1))'

# Generated at 2022-06-13 15:37:10.782959
# Unit test for function safe_eval
def test_safe_eval():
    def _test(input, expected_results):
        # We expect both a success and fail since the syntax is valid
        # and we should not be calling functions
        result = safe_eval(input)
        assert result == expected_results

    _test('1', 1)
    _test('1.0', 1.0)
    _test('true', True)
    _test('false', False)
    _test('none', None)
    _test('1 + 1', 2)
    _test('1 * 1', 1)
    _test('1 + 2 * 3', 7)
    _test('[1,2]', [1, 2])
    _test('{1:2}', {1: 2})
    _test('["a", "b"]', ["a", "b"])

# Generated at 2022-06-13 15:37:20.594628
# Unit test for function safe_eval

# Generated at 2022-06-13 15:37:26.962425
# Unit test for function safe_eval
def test_safe_eval():

    assert safe_eval("1+1") == 2
    assert safe_eval("'foo'") == 'foo'
    assert safe_eval("['foo', 'bar']") == ['foo', 'bar']
    assert safe_eval("{foo: 'bar'}") == {'foo': 'bar'}
    assert safe_eval("false") == False
    assert safe_eval("null") is None
    assert safe_eval("true") == True

    # unsafe variable access
    assert safe_eval("foo", {"foo": "bar"}, include_exceptions=True)[0] == 'foo'
    # unsafe function call
    assert safe_eval("foo", {"foo": "open"}, include_exceptions=True)[0] == 'foo'
    # unsafe attribute access

# Generated at 2022-06-13 15:37:35.382463
# Unit test for function safe_eval
def test_safe_eval():
    # Scenario 1: dict object with string, int and float values
    test_string = '{"a":"Ansible", "b":10, "c":1.23}'
    result, exception = safe_eval(test_string, None, True)
    if exception:
        # Incorrect behavior
        print("Test 1 failed: exception %s for '%s'" % (exception, test_string))
        sys.exit(1)
    else:
        if isinstance(result, dict) and result["a"] == "Ansible" and result["b"] == 10 and result["c"] == 1.23:
            # Correct behavior
            print("Test 1 passed: '%s' evaluated to '%s'" % (test_string, result))

# Generated at 2022-06-13 15:37:44.659491
# Unit test for function safe_eval
def test_safe_eval():
    # Make sure safe_eval works with a function that calls other functions
    class DummyClass:
        def __init__(self, name):
            self.name = name
        def __str__(self):
            return self.name

    test_dc = DummyClass('dummy')
    assert safe_eval(
        'test + ": " + str(test_dc)',
        dict(test=1, test_dc=test_dc),
        include_exceptions=True
    ) == (
        '1: dummy',
        None
    )

    # Make sure safe_eval prevents calling unsafe functions
    assert safe_eval(
        'open',
        dict()
    ) == 'open'

    # Make sure safe_eval does not prevent calling safe functions

# Generated at 2022-06-13 15:37:48.676723
# Unit test for function safe_eval
def test_safe_eval():
    # eval allows oracle attack via __import__
    # this one forces eval() to import os
    assert safe_eval('__import__("os")') is None
    # None, False, True are okay
    assert safe_eval('None') is None
    assert safe_eval('False') is False
    assert safe_eval('True') is True
    # test number parsing
    assert safe_eval('1') == 1
    assert safe_eval('1.0') == 1.0
    # ensure that strings are not allowed
    assert safe_eval('"1.0"') == '"1.0"'
    assert safe_eval("'1.0'") == "'1.0'"
    # ensure that binary operations are allowed
    assert safe_eval('1 + 1') == 2
    assert safe_eval('True and False') is False

# Generated at 2022-06-13 15:37:54.179870
# Unit test for function safe_eval
def test_safe_eval():
    # to start with, ensure that safe_eval works
    # in a way that is compatible with normal eval
    for (expr, expected) in (
            ('2', 2),
            ('2 + 5', 7),
            ('True', True),
            ('True and False', False),
            ('True or False', True),
            ('1 in [1,2]', True),
            ('[1,2] + [3,4]', [1,2,3,4]),
            ('[1,2] * 2', [1,2,1,2]),
            ('"foo" in "foobar"', True),
            ('"foo" not in "foobar"', False),
            ('"alice" > "bob"', False),
            ('"alice" < "bob"', True),
    ):
        assert safe_