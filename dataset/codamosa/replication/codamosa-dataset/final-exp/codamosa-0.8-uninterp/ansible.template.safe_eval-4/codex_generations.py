

# Generated at 2022-06-13 15:28:10.094229
# Unit test for function safe_eval

# Generated at 2022-06-13 15:28:19.059792
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval("foo == 'bar'") == "foo == 'bar'"
    assert safe_eval('true')
    assert safe_eval('false') is False
    assert safe_eval('null') is None
    assert safe_eval('1 + 2') == 3
    assert safe_eval('foo') == 'foo'
    assert safe_eval('foo.bar') == 'foo.bar'
    assert safe_eval('foo[0]') == 'foo[0]'
    assert safe_eval('foo[bar]') == 'foo[bar]'
    assert safe_eval('foo[0].bar[1][another].baz()') == 'foo[0].bar[1][another].baz()'
    assert safe_eval('[1, 2, 3]') == [1, 2, 3]

# Generated at 2022-06-13 15:28:26.146732
# Unit test for function safe_eval
def test_safe_eval():
    class TestException(Exception):
        def __init__(self, value):
            self.value = value

        def __str__(self):
            return repr(self.value)

    def test(expr, locals, result, expect_err=False):
        try:
            actual_result = safe_eval(expr, locals)
            actual_result = container_to_text(actual_result)
            actual_result = to_native(actual_result)
        except Exception as e:
            actual_result = 'Exception: ' + str(e)
        if actual_result == result:
            print("PASS: %s ==> %s" % (expr, result))
        elif expect_err:
            print("FAIL: %s ==> %s (expected result) but got %s" % (expr, result, actual_result))


# Generated at 2022-06-13 15:28:35.443530
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval("foo") == "foo"
    assert safe_eval("foo", {"foo": None}) is None
    assert safe_eval("foo", {"foo": True})
    assert safe_eval("foo", {"foo": False}) == False
    assert safe_eval("foo", {"foo": 1}) == 1
    assert safe_eval("foo", {"foo": "bar"}) == "bar"
    assert safe_eval("foo", {"foo": ["bar"]}) == ["bar"]
    assert safe_eval("[]") == []
    assert safe_eval("{}") == {}
    assert safe_eval("{'foo': 'bar'}") == {'foo': 'bar'}
    assert safe_eval("()") == ()
    assert safe_eval("(True, False)") == (True, False)

# Generated at 2022-06-13 15:28:44.625836
# Unit test for function safe_eval
def test_safe_eval():

    class TestModule(object):
        def fail_json(self, *args, **kwargs):
            raise Exception(args, kwargs)

    fake_module = TestModule()

    def check_result(module, result, expected, expr):
        if expected != result:
            raise Exception(
                "safe_eval(%s) returned %s but expected %s" %
                (expr, result, expected))

    fake_module.fail_json.called = False
    check_result(
        module=fake_module,
        result=safe_eval(
            expr="[]",
            locals=dict(foo="bar")),
        expected=[],
        expr="[]")

# Generated at 2022-06-13 15:28:52.888115
# Unit test for function safe_eval
def test_safe_eval():
    import pytest
    from ansible.errors import AnsibleFilterError
    from ansible.module_utils.six.moves import builtins

    # setup: create a fake builtin function
    def fake_builtin():
        pass

    fake_builtin.__module__ = '__builtin__'

    # based on the '__builtins__' dict in
    # ansible.module_utils.common.eval_tools.safe_eval()
    OUR_GLOBALS = {
        '__builtins__': {},  # avoid global builtins as per eval docs
        'false': False,
        'null': None,
        'true': True,
        'True': True,
        'False': False,
        'None': None
    }

    # Exception raised when the options 'constants' is not a list

# Generated at 2022-06-13 15:29:00.063081
# Unit test for function safe_eval
def test_safe_eval():
    '''
    Test of safe_eval function

    :return: Boolean True if test is successful
    '''
    test_vars = {'var1': 'I am a string', 'var2': ['a', 'b', 'c', 'd'], 'var3': {'dict1': {'subdict1': 'subdict1value'}}}

# Generated at 2022-06-13 15:29:08.923624
# Unit test for function safe_eval
def test_safe_eval():
    safe_eval("foo")
    safe_eval("foo is bar")
    safe_eval("foo is not bar")
    safe_eval("1")
    safe_eval("1+2")
    safe_eval("1+2*3")
    safe_eval("(1+2)*3")
    safe_eval("[1,2,3]")
    safe_eval("{1:2,3:4}")
    safe_eval("True")
    safe_eval("False")
    safe_eval("None")
    safe_eval("null")
    safe_eval("true")
    safe_eval("false")
    safe_eval("'hello, world'")

    # list comprehensions
    #safe_eval("[x for x in stuff]")
    #safe_eval("[x for x in stuff if x]")

# Generated at 2022-06-13 15:29:18.451279
# Unit test for function safe_eval
def test_safe_eval():
    print('Testing safe_eval()')

    # Try a simple string
    result, err = safe_eval('a_list_variable', include_exceptions=True)
    assert result == 'a_list_variable'

    # Try a complex string
    result, err = safe_eval('a_list_variable + "test1"', include_exceptions=True)
    assert result == 'a_list_variable + "test1"'

    # Try an unquoted variable
    result, err = safe_eval('a_var', include_exceptions=True)
    assert result == 'a_var'

    # Try a non-string variable
    result, err = safe_eval('a_var', {'a_var': ['a_list_variable', 'test1']}, include_exceptions=True)

# Generated at 2022-06-13 15:29:29.898500
# Unit test for function safe_eval
def test_safe_eval():
    # Basic tests
    assert safe_eval("a+b", locals={'a':1,'b':2}) == 3
    assert safe_eval("a-b", locals={'a':1,'b':2}) == -1
    assert safe_eval("a*b", locals={'a':1,'b':2}) == 2
    assert safe_eval("a/b", locals={'a':4,'b':2}) == 2
    if sys.version_info[0] <= 2:
        # in python3, this raises a TypeError, as 1/2 gives a float
        assert safe_eval("a/b", locals={'a':1,'b':2}) == 0

    # Test that allowed list comprehension is intact

# Generated at 2022-06-13 15:29:41.740497
# Unit test for function safe_eval
def test_safe_eval():

    class module_args:
        name = 'test'

        def __init__(self, name):
            self.name = name


# Generated at 2022-06-13 15:29:52.741160
# Unit test for function safe_eval
def test_safe_eval():
    from ansible.vars.unsafe_proxy import UnsafeProxy, wrap_var
    assert safe_eval("foo") == 'foo'
    assert safe_eval(42) == 42
    assert safe_eval(42.0) == 42.0
    assert safe_eval(None) == None
    assert safe_eval(True) == True
    assert safe_eval(False) == False
    assert safe_eval("foo == 'foo'") == True
    assert safe_eval("foo is bar", dict(foo='foo', bar='foo')) == True
    assert safe_eval("foo is bar", dict(foo='foo', bar='bar')) == False
    assert safe_eval("'foo' in bar", dict(bar=['foo', 'baz'])) == True

# Generated at 2022-06-13 15:30:00.710078
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval("a_list_variable") == "a_list_variable"
    assert safe_eval("['foo', 'bar']") == ['foo', 'bar']
    assert safe_eval("{'a': 'b'}") == {'a': 'b'}
    assert safe_eval("{'a': 'b'}['a']") == 'b'
    assert safe_eval("{'a': 'b'}['c']") == None
    assert safe_eval("{'a': [1,2,3]}['a']") == [1,2,3]
    assert safe_eval("{'a': 'b'}['a']|int") == "b|int"
    assert safe_eval("['a', 'b']|int") == ['a', 'b']|int

# Generated at 2022-06-13 15:30:08.390045
# Unit test for function safe_eval
def test_safe_eval():
    safe_eval('[]')
    safe_eval('[1]')
    safe_eval('[1, 2]')
    safe_eval('[1, 2, 3]')
    safe_eval('dict()')
    safe_eval('dict(a=list())')
    safe_eval('dict(a=list(),b=list())')
    safe_eval('dict(a=list(),b=list(c=list()))')
    safe_eval('{}')
    safe_eval('1')
    safe_eval('1 and 1')
    safe_eval('1 or 1')
    safe_eval('1 and 1 or 1')
    safe_eval('1 and 1 and 1')
    safe_eval('1 and 1 and 1 and 1')
    safe_eval('1 or 1 and 1')

# Generated at 2022-06-13 15:30:18.789970
# Unit test for function safe_eval
def test_safe_eval():
    # Test 1: 'true' evaluated to True
    result, exception = safe_eval(u'true', None, True)
    assert exception is None
    assert result

    # Test 2: 'false' evaluated to False
    result, exception = safe_eval(u'false', None, True)
    assert exception is None
    assert not result

    # Test 3: 'null' evaluated to None
    result, exception = safe_eval(u'null', None, True)
    assert exception is None
    assert result is None

    # Test 4: 'null_var' evaluated to None
    null_var = None
    result, exception = safe_eval(u'null_var', dict(null_var=null_var), True)
    assert exception is None
    assert result is None

    # Test 5: '"hello world"' evaluated to 'hello world

# Generated at 2022-06-13 15:30:27.026280
# Unit test for function safe_eval

# Generated at 2022-06-13 15:30:33.348366
# Unit test for function safe_eval
def test_safe_eval():
    if len(sys.argv) > 1 and sys.argv[1] == 'safe_eval':
        # running unit test
        from collections import Mapping


# Generated at 2022-06-13 15:30:42.448985
# Unit test for function safe_eval
def test_safe_eval():
    error_msg = ("safe_eval: [%s] expected [%s], but got [%s]")
    func = safe_eval
    # Test dummy invocation of safe_eval()
    result = func()
    assert result is None, error_msg % ("no args", None, result)
    # Test safe operations

# Generated at 2022-06-13 15:30:53.062241
# Unit test for function safe_eval
def test_safe_eval():
    def assert_success(expr, expected_result):
        result, exception = safe_eval(expr, include_exceptions=True)
        assert result == expected_result
        assert exception is None

    def assert_failure(expr, expected_result=None):
        result, exception = safe_eval(expr, include_exceptions=True)
        assert result == expected_result
        assert exception is not None

        result = safe_eval(expr)
        assert result == expected_result

    # Test simple expressions
    assert_success("1 + 1", 2)
    assert_success("1 * 1", 1)
    assert_success("1 - 1", 0)
    assert_success("1 / 1", 1)
    # Test more complex expressions
    assert_success("1 + 2 * 2", 5)

# Generated at 2022-06-13 15:30:59.317185
# Unit test for function safe_eval
def test_safe_eval():
    expr = "['foo', 'bar', 'baz']"
    result = safe_eval(expr)
    assert result == ['foo', 'bar', 'baz']

    expr = "['%s', 'bar', 'baz']" % C.DEFAULT_VAULT_PASSWORD_FILE
    result = safe_eval(expr)
    assert result == [C.DEFAULT_VAULT_PASSWORD_FILE, 'bar', 'baz']

    # Expect to raise an exception because of the call to dict
    expr = "'foo' in dict()"
    try:
        result = safe_eval(expr)
        raise ValueError("Expected an exception")
    except:
        pass

    # Expect to raise an exception because of the call to hasattr
    expr = "'foo' in hasattr()"

# Generated at 2022-06-13 15:31:12.829603
# Unit test for function safe_eval
def test_safe_eval():
    # Test syntax errors
    assert safe_eval('{{', include_exceptions=True)[0] == '{{'
    assert safe_eval(' }}', include_exceptions=True)[0] == ' }}'
    # Test simple valid python expressions
    assert safe_eval('1', include_exceptions=True)[0] == 1
    assert safe_eval('1 and 2', include_exceptions=True)[0] == 2
    assert safe_eval('1 or 2', include_exceptions=True)[0] == 1
    assert safe_eval('a and b', include_exceptions=True)[0] == 'b'
    assert safe_eval('1 + 2*3', include_exceptions=True)[0] == 7
    assert safe_eval('[1, 2]', include_exceptions=True)[0] == [1, 2]
   

# Generated at 2022-06-13 15:31:23.151667
# Unit test for function safe_eval
def test_safe_eval():
    # Test that syntax errors are caught.
    try:
        safe_eval('function_foo(', {})
    except Exception as e:
        pass
    else:
        raise Exception("Should have raised an exception")

    # Test that function calls are not allowed by default.
    try:
        safe_eval('function_foo()', {})
    except Exception as e:
        pass
    else:
        raise Exception("Should have raised an exception")

    # Test that function calls to certain functions are allowed.
    try:
        safe_eval('function_foo(1,2,3)', {'function_foo': lambda x,y,z: x+y+z})
    except Exception as e:
        raise Exception("Should not have raised an exception")

    # Test we can call builtins

# Generated at 2022-06-13 15:31:32.564117
# Unit test for function safe_eval
def test_safe_eval():
    variables = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': ['a', 'b', 'c', 'd'],
        'f': 'Hello',
        'g': True
    }

    print(safe_eval('a + b', locals=variables))
    print(safe_eval('a + b + c + d', locals=variables))
    print(safe_eval('a + b + c + d + e', locals=variables))
    print(safe_eval('a + b + c + d + e + f', locals=variables))
    print(safe_eval('a + b + c + d + e + f + g', locals=variables))

# Generated at 2022-06-13 15:31:38.941321
# Unit test for function safe_eval

# Generated at 2022-06-13 15:31:46.248291
# Unit test for function safe_eval
def test_safe_eval():
    # Null tests
    assert safe_eval(None) == None
    assert safe_eval("None") == None
    assert safe_eval(1) == 1
    assert safe_eval("1") == 1

    # Dict tests
    assert safe_eval("{}") == {}
    assert safe_eval("{'test_key': 'test_value'}") == {'test_key': 'test_value'}
    assert safe_eval("{'test_key': 'test_value', 'foo': 'bar'}") == {'test_key': 'test_value', 'foo': 'bar'}
    assert safe_eval("{'test_key': {'test_key2': 'test_value2'}}") == {'test_key': {'test_key2': 'test_value2'}}
    assert safe_eval

# Generated at 2022-06-13 15:31:56.176659
# Unit test for function safe_eval
def test_safe_eval():

    # basic literals
    literals = [
        '1',
        '1+1',
        '1-1',
        '1*1',
        '1/1',
        'true',
        'null',
        'false',
        '["foo", "bar"]',
        '("foo", "bar")',
        '{"foo": "bar"}',
        '1 in [1,2]',
    ]
    for literal_str in literals:
        result = safe_eval(literal_str)
        assert result == ast.literal_eval(literal_str)
        assert type(result) == type(ast.literal_eval(literal_str))
        assert result != literal_str

    # ensure specific items are not evaluated as None

# Generated at 2022-06-13 15:32:06.254545
# Unit test for function safe_eval
def test_safe_eval():
    print("=== SAFE_EVAL ===")
    assert safe_eval('a_list_variable') == 'a_list_variable'
    assert safe_eval('a_list_variable', locals={'a_list_variable': ['foo']}) == ['foo']
    assert safe_eval('a_list_variable', locals={'a_list_variable': 'foo'}) == 'foo'
    assert container_to_text(safe_eval('a_list_variable', locals={'a_list_variable': ['foo']})) == 'foo'
    assert safe_eval("5 * 5") == 25
    assert safe_eval("2 + 2") == 4
    assert safe_eval("5 * (2 + 1)") == 15

    # Test invalid cases

# Generated at 2022-06-13 15:32:18.215712
# Unit test for function safe_eval
def test_safe_eval():
    '''
    test safe_eval function
    '''
    safe_expr_list = [
        "1 + 1",
        "1 * 3",
        "[1, 2, 3]",
        "'blah'",
        "true",
        'None',
        'False',
        {'a': 'b'},
    ]

    unsafe_expr_list = [
        'None.foo',
        '1/0',
        'import os; os.path',
        'open("/etc/passwd")',
        '__import__("os").path',
        '__builtins__.open("/etc/passwd").read()',
    ]

    for expr in safe_expr_list:
        assert safe_eval(expr) == expr  # should be a no-op

# Generated at 2022-06-13 15:32:29.980220
# Unit test for function safe_eval

# Generated at 2022-06-13 15:32:40.147891
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval('1+1', include_exceptions=False) == 2
    assert safe_eval('1+1', include_exceptions=True) == (2, None)
    assert safe_eval('abcdefghijklmnopqrstuvwxyz', include_exceptions=False) == 'abcdefghijklmnopqrstuvwxyz'
    assert safe_eval('abcdefghijklmnopqrstuvwxyz', include_exceptions=True) == ('abcdefghijklmnopqrstuvwxyz', None)
    assert safe_eval('"abcdefghijklmnopqrstuvwxyz"', include_exceptions=False) == 'abcdefghijklmnopqrstuvwxyz'

# Generated at 2022-06-13 15:32:54.507629
# Unit test for function safe_eval
def test_safe_eval():
    # safe_eval should fail for things like executable code
    assert not safe_eval("__import__('os').system('cat /etc/passwd')")

    # safe_eval should fail for references to builtins that are not allowed
    assert not safe_eval("abs(3)")
    assert not safe_eval("abs(-3)")

    # safe_eval should fail for invalid variable references
    assert not safe_eval("1 + thing")

    # safe_eval should fail for calls to things that are not callable
    assert not safe_eval("1 + thing()")

    # safe_eval should work for basic expressions
    assert safe_eval("1 + 1") == 2
    assert safe_eval("[1 + 1]") == [2]
    assert safe_eval("{'a': 'b'}") == {'a': 'b'}

# Generated at 2022-06-13 15:33:04.317103
# Unit test for function safe_eval

# Generated at 2022-06-13 15:33:15.498287
# Unit test for function safe_eval
def test_safe_eval():
    test1 = safe_eval("1+1")
    assert test1 == 2
    test2 = safe_eval("1+1", include_exceptions=True)
    assert test2[0] == 2
    assert not test2[1]
    # Test for exceptions
    test3 = safe_eval("1+", include_exceptions=True)
    assert test3 == ('1+', None)
    assert test3[1]
    # Test for locals
    test4 = safe_eval("x+1", locals={'x':1})
    assert test4 == 2
    # Test for dict
    test5 = safe_eval("dict(x=1, y=2)")
    assert test5 == dict(x=1, y=2)
    # Test for string
    test6 = safe_eval("'A string'")


# Generated at 2022-06-13 15:33:26.544445
# Unit test for function safe_eval
def test_safe_eval():
    # Test that syntax generated by a dict is accepted
    results = safe_eval('{\"a\": 1, \"b\": [1, 2, 3]}')
    assert results == {"a": 1, "b": [1, 2, 3]}, results

    # Test that syntax generated by a list is accepted
    results = safe_eval('[1, 2, 3]')
    assert results == [1, 2, 3], results

    # Test that syntax generated by a dict/list combo is accepted
    results = safe_eval('{\"a\": [1, 2, 3]}')
    assert results == {"a": [1, 2, 3]}, results

    # Test that a simple dictionary returns a dict
    results = safe_eval('a=dict(foo=1,bar=2)', dict(a="1"))
    assert results == "1", results



# Generated at 2022-06-13 15:33:37.165425
# Unit test for function safe_eval
def test_safe_eval():
    # An exception should be raised if the expression is invalid
    try:
        safe_eval('{{ ansible_test_variable }}')
        assert False, 'safe_eval allowed an expression that should fail.'
    except Exception:
        pass

    # If a syntax error is raised, the expression is returned unchanged
    assert safe_eval('{{ ansible_test_variable }}', include_exceptions=True) == ('{{ ansible_test_variable }}', None)

    # Test that valid expressions are evaluated properly
    assert safe_eval('foo', {'foo': 'bar'}) == 'bar'
    assert safe_eval('foo.bar', {'foo': {'bar': 'test'}}) == 'test'
    assert safe_eval('foo', {'foo': None}) is None
    assert safe_eval('foo', {'foo': False}) is False

# Generated at 2022-06-13 15:33:48.044424
# Unit test for function safe_eval
def test_safe_eval():
    # Successful evaluations
    assert safe_eval("1+1") == 2
    assert safe_eval("1+1", include_exceptions=True) == (2, None)
    assert safe_eval("1+1", include_exceptions=True)[0] == 2
    assert safe_eval("1+1", include_exceptions=True)[1] is None
    assert safe_eval("foo", {'foo': 'bar'}) == 'bar'
    assert safe_eval("foo", include_exceptions=True, locals={'foo': 'bar'})[0] == 'bar'
    assert safe_eval("1", include_exceptions=True, locals={'foo': 'bar'})[0] == 1
    assert safe_eval("foo.strip('f')", {'foo': 'foo'}) == 'oo'
    assert safe

# Generated at 2022-06-13 15:33:57.932836
# Unit test for function safe_eval
def test_safe_eval():
    class TestClassThing:
        pass

    test_class_thing = TestClassThing()

    test_list1 = "{{ [1,2,3] }}"
    test_list2 = "{{ 1+2 }}"
    test_list3 = "{{ [1,2,{}] }}".format(test_class_thing)
    test_list4 = "{{ [x,y,z] }}"
    test_list5 = "{{ these are not items }}"

    test_dict1 = "{{ {'key':'value'} }}"
    test_dict2 = "{{ 1+2 }}"
    test_dict3 = "{{ {'key':{}} }}".format(test_class_thing)
    test_dict4 = "{{ {'key': {'nested': 'dict'} }}}"


# Generated at 2022-06-13 15:34:06.637661
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval('1 + 3') == 4
    assert safe_eval('(1, 2, 3)') == (1, 2, 3)
    assert safe_eval('[1, 2, 3]') == [1, 2, 3]
    assert safe_eval('{"a": 1, "b": 2}') == dict(a=1, b=2)
    assert safe_eval('false') is False
    assert safe_eval('!false') is True
    assert safe_eval('false or false') is False
    assert safe_eval('(1 in [1, 2, 3])') is True
    assert safe_eval('(4 in [1, 2, 3])') is False
    assert safe_eval('"foo"') == 'foo'

    # these should all fail to parse

# Generated at 2022-06-13 15:34:14.905536
# Unit test for function safe_eval

# Generated at 2022-06-13 15:34:25.209745
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval('True') is True
    assert safe_eval('true') is True
    assert safe_eval('False') is False
    assert safe_eval('false') is False
    assert safe_eval('None') is None
    assert safe_eval('null') is None
    assert safe_eval('42') == 42
    assert safe_eval('42.5') == 42.5
    assert safe_eval('"foo"') == "foo"
    assert safe_eval("'foo'") == "foo"
    assert safe_eval('["foo", "bar"]') == ["foo", "bar"]
    assert safe_eval('("foo", "bar")') == ("foo", "bar")
    assert safe_eval('{"foo": "bar"}') == {"foo": "bar"}
    assert safe_eval('1 == 1') is True
   

# Generated at 2022-06-13 15:34:42.557612
# Unit test for function safe_eval
def test_safe_eval():
    '''
    Test for function safe_eval
    '''

    test_table = []

    if sys.version_info < (3, 0):
        test_table.append(([], '[]'))
    else:
        test_table.append(([], 'list()'))

    test_table.append((
        {}, '{}'
    ))
    test_table.append((
        set(['foo']), 'set(["foo"])'
    ))
    test_table.append((
        {'foo': 'bar'}, '{\'foo\': \'bar\'}'
    ))
    test_table.append((
        {'foo': 'bar', 'foo1': 'bar1'}, '{\'foo\': \'bar\', \'foo1\': \'bar1\'}'
    ))
    test

# Generated at 2022-06-13 15:34:51.268608
# Unit test for function safe_eval
def test_safe_eval():
    '''
    Test cases for safe_eval()
    '''

# Generated at 2022-06-13 15:35:01.131866
# Unit test for function safe_eval
def test_safe_eval():
    # A basic test of the safe_eval function
    x = dict(e='f')
    y = dict(a=[1,2,3])
    z = dict(g=3)


# Generated at 2022-06-13 15:35:09.157137
# Unit test for function safe_eval
def test_safe_eval():
    '''
    Test the safe_eval function.
    '''
    def _test_safe_eval(args, expected_result, expected_type=None, expected_exception=None):
        '''
        Test the safe_eval function.
        '''
        if isinstance(args, str):
            args = (args,)
        if len(args) < 2:
            args = args + (None,)
        if len(args) < 3:
            args = args + (False,)
        result = safe_eval(*args)
        if args[2]:
            result, exception = result
        else:
            exception = None
        if exception is not None:
            assert expected_exception is not None
            assert exception.__class__.__module__ == 'ansible.module_utils.common.text.converters'
           

# Generated at 2022-06-13 15:35:18.358440
# Unit test for function safe_eval
def test_safe_eval():
    import json
    import copy

    # initialize the safe eval locals
    safe_eval_locals = {
        'a': 32,
        'b': 'b_value',
        'c': ['a', 'list', 'of', 'things'],
        'nested_list': [['a', 'nested'], ['list']],
        'd': {'a': 'nested', 'dictionary': ['with', 'some', 'values']},
        'true_val': True,
        'false_val': False,
        'null_val': None,
        'empty_list': [],
    }
    val_to_test = copy.deepcopy(safe_eval_locals)

    # use the safe eval locals to build a set of test values

# Generated at 2022-06-13 15:35:27.781549
# Unit test for function safe_eval
def test_safe_eval():
    # Ensure bare strings are returned as-is
    assert safe_eval('foo') == 'foo'
    assert safe_eval('foo', include_exceptions=True)[0] == 'foo'
    assert safe_eval('foo', include_exceptions=True)[1] is None

    # Ensure syntax errors are returned as-is
    assert safe_eval('foo{% if foo %}') == 'foo{% if foo %}'
    assert safe_eval('foo{% if foo %}', include_exceptions=True)[0] == 'foo{% if foo %}'
    assert isinstance(safe_eval('foo{% if foo %}', include_exceptions=True)[1], SyntaxError)

    # Ensure syntax errors due to templating are not swallowed

# Generated at 2022-06-13 15:35:36.901829
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval('{}') == {}
    assert safe_eval('[]') == []
    assert safe_eval('[1, 2, 3]') == [1, 2, 3]
    assert safe_eval('{"a": "b"}') == {"a": "b"}
    assert safe_eval('{"a": "b", "c": "d"}') == {"a": "b", "c": "d"}
    assert safe_eval('{"a": "b", "c": "d", "e": "f"}') == {"a": "b", "c": "d", "e": "f"}
    assert safe_eval('set([])') == set([])
    assert safe_eval('["a", "b", "c"]') == ["a", "b", "c"]

# Generated at 2022-06-13 15:35:42.253224
# Unit test for function safe_eval
def test_safe_eval():
    # Test calls to safe_eval
    # Note: We test that safe_eval does not allow certain functions by trying
    # to call them and catching the exception.  This is a somewhat indirect
    # test, but it is anyway the best we can do.  Note that some builtins
    # are allowed, but that isn't tested here yet.  (It's ok to allow some
    # builtins)

    # Test safe_eval (kwargs, "true", "false" and "null" are allowed)
    value = safe_eval('{"a": ["foo","bar"]}')
    assert value['a'][0] == 'foo'
    value = safe_eval('{"a": "foo"}')
    assert value['a'] == 'foo'
    value = safe_eval('{"a": 1}')
    assert value['a'] == 1
   

# Generated at 2022-06-13 15:35:52.773604
# Unit test for function safe_eval
def test_safe_eval():
    # Simple expressions
    assert safe_eval('1') == 1
    assert safe_eval('1 + 3') == 4
    assert safe_eval('1 + 3 * 4') == 13
    assert safe_eval('(1 + 3) * 4') == 16
    assert safe_eval('-1') == -1
    assert safe_eval('1 - 3') == -2
    assert safe_eval('1 - 3 / 4') == 0.25
    assert safe_eval('(1 - 3) / 4') == -0.25
    assert safe_eval('True') == True
    assert safe_eval('False') == False
    assert safe_eval('None') == None

    # Nested lists and dicts
    assert safe_eval('[1, 2, 3]') == [1, 2, 3]

# Generated at 2022-06-13 15:36:03.656907
# Unit test for function safe_eval
def test_safe_eval():
    from ansible.module_utils.common.text.converters import to_unicode

    mock_module = {'_': lambda x: to_unicode(x)}

    group_vars = {
        'foo': '{{ user_mapping["michael"] }}',
        'bar': '{{ gilead.world_capital }}',
        'gilead': {'world_capital': 'Novi Zagreb'},
        'user_mapping': {'michael': 'zadar'},
    }
    user_vars = {
        'user_mapping': {
            'dennis': 'zagreb',
            'michael': 'splite',
        },
    }


# Generated at 2022-06-13 15:36:27.453427
# Unit test for function safe_eval
def test_safe_eval():
    # Define some test data.
    inputs = [
        # valid expressions
        'a + b',
        'a[0]',
        'a.b',
        'a["b"]',
        "a.replace('b')",
        '"abc"',
        '["a", "b"]',
        '{"a":"b"}',
    ]
    outputs = []

    # This is our test eval function.  It must be as restrictive as
    # safe_eval() in order for the tests below to be meaningful.
    class test_class():
        def replace(self, a):
            return a

    def test_eval(expr):
        locals = {
            'a': 1,
            'b': 2,
        }

# Generated at 2022-06-13 15:36:34.083594
# Unit test for function safe_eval

# Generated at 2022-06-13 15:36:43.593839
# Unit test for function safe_eval
def test_safe_eval():
    # test basic values
    assert safe_eval('42') == 42
    assert safe_eval('-42') == -42
    assert safe_eval('3.14') == 3.14

    # test strings
    assert safe_eval('"foo"') == 'foo'
    assert safe_eval("'foo'") == 'foo'

    # test lists
    assert safe_eval('[1, 2, 3]') == [1, 2, 3]

    # test dicts
    assert safe_eval('{"foo": "bar"}') == {"foo": "bar"}

    # test true and false
    assert safe_eval('true') == True
    assert safe_eval('false') == False

    # test None
    assert safe_eval('null') is None
    assert safe_eval('none') is None

    # test some basic math
   

# Generated at 2022-06-13 15:36:55.179544
# Unit test for function safe_eval
def test_safe_eval():
    # Test that we can safely eval strings that are equal to Python
    # equivalents, and also JSON-safe strings
    assert safe_eval('[1,2,3,4]') == [1, 2, 3, 4]
    assert safe_eval('{"a":"b","c":null}') == {"a": "b", "c": None}
    assert safe_eval('None') is None

    # Disallow bare strings, as they are equivalent to calls to the str()
    # builtin, which are unsafe
    assert safe_eval('"invalid"') == '"invalid"'

    # Disallow calls to functions in Python's builtin namespace that we have
    # not enabled, eg. eval()
    assert safe_eval('__import__("os").system("dir")') == '__import__("os").system("dir")'

    # Dis

# Generated at 2022-06-13 15:37:03.709180
# Unit test for function safe_eval
def test_safe_eval():
    globals = {
        "test_globals": {
            "one": 1,
            "two": 2,
            "three": 3,
            "four": 4,
            "five": 5,
            "six": 6,
            "seven": 7,
            "eight": 8,
            "nine": 9,
            "ten": 10,
        }
    }
    locals = {}

# Generated at 2022-06-13 15:37:12.358160
# Unit test for function safe_eval
def test_safe_eval():
    # Test to make sure that we raise an exception on invalid expressions
    assert safe_eval("{{ foo }}") == "{{ foo }}"
    assert isinstance(safe_eval("{{ foo }}", include_exceptions=True)[1], ast.AST)

    # Test to make sure that we do not accept function calls that are not in our whitelist,
    # specifically we do not want to allow subprocess.Popen
    assert safe_eval("subprocess.Popen(['ls'])") == "subprocess.Popen(['ls'])"
    assert isinstance(safe_eval("subprocess.Popen(['ls'])", include_exceptions=True)[1], ast.Name)

    # Test to make sure that we can safely evaluate an expression

# Generated at 2022-06-13 15:37:17.309304
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval("1") == 1
    assert safe_eval("a_list_variable") == "a_list_variable"
    assert safe_eval('"1"') == "1"
    assert safe_eval('(1+2)*3') == 9
    assert safe_eval('1 + [1, 2, 3]') == [1, 1, 2, 3]
    assert safe_eval('{"a": 1}') == {"a": 1}
    assert safe_eval('1 + {"a": 1}') == {"a": 1}

    # not-allowed operations
    assert safe_eval("__import__('sys').modules") == "__import__('sys').modules"
    assert safe_eval("__import__('os').system('id')") == "__import__('os').system('id')"

# Generated at 2022-06-13 15:37:24.756109
# Unit test for function safe_eval
def test_safe_eval():

    # Test for correct evaluation of valid expressions
    # Single digit integer
    e = '1'
    assert safe_eval(e) == 1

    # Negative single digit integer
    e = '-1'
    assert safe_eval(e) == -1

    # Multiple digit integer
    e = '112233'
    assert safe_eval(e) == 112233

    # Integer with zero
    e = '101010'
    assert safe_eval(e) == 101010

    # Like a C macro, no space between - and digit
    e = '-123'
    assert safe_eval(e) == -123

    # Floating point number
    e = '3.14159'
    assert safe_eval(e) == 3.14159

    # Floating point number with exponential notation
    e = '31415E-4'

# Generated at 2022-06-13 15:37:34.295477
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval('1+1') == 2
    assert safe_eval('1+1') != 3
    assert safe_eval('false') is False
    assert safe_eval('true') is True
    assert safe_eval('null') is None
    assert safe_eval('foo bar') == 'foo bar'
    assert safe_eval('foo_bar') == 'foo_bar'
    assert safe_eval('foo_bar', {'foo_bar': 'test'}) == 'test'
    assert safe_eval('foo_bar', {'foo_bar': 'test'}) != 'test2'
    d = {'foo_bar': 'test'}
    assert safe_eval('foo_bar', d) == 'test'
    assert safe_eval('foo_bar', d) != 'test2'

# Generated at 2022-06-13 15:37:44.204193
# Unit test for function safe_eval
def test_safe_eval():
    # Set up some test vars
    test_var = 'world'
    test_var_int = 42
    test_var_list = ['foo','bar','baz']
    test_var_dict = {'foo': 1, 'bar': 2, 'baz': 3}
    test_var_mult = 3 * 3

    # Check that good expressions work
    assert safe_eval('hello_' + test_var) == 'hello_world'
    assert safe_eval(test_var_mult) == 9
    assert safe_eval('hello_' + test_var + '_' + str(test_var_int)) == 'hello_world_42'
    assert safe_eval(['foo','bar']) == ['foo','bar']
    assert safe_eval('True') == True
    assert safe_eval('False') == False
