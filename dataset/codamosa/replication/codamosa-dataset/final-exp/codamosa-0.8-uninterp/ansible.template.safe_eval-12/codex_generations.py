

# Generated at 2022-06-13 15:28:09.299998
# Unit test for function safe_eval
def test_safe_eval():
    expr = '{}'  # should evaluate to a python dict
    value = safe_eval(expr)
    # ensure result is a dict (as expected)
    assert isinstance(value, dict)

    # ensure that calling an unsafe function fails as expected
    expr = 'myfunc()'
    try:
        safe_eval(expr)
    except Exception as e:
        # ensure that the exception includes the invalid function name
        assert 'myfunc' in str(e)

    # ensure that calling a safe function works as expected
    expr = 'int(myvar)'
    value = safe_eval(expr)
    # ensure value is an integer (as expected)
    assert isinstance(value, int)

    # ensure that calling a safe function works as expected
    expr = 'str(myvar)'
    value = safe_eval(expr)
   

# Generated at 2022-06-13 15:28:18.361943
# Unit test for function safe_eval
def test_safe_eval():
    # Test valid expressions
    assert safe_eval('1 + 1') == 2
    assert safe_eval('1 + 1 == 2') == True
    assert safe_eval('1 + 1 != 2') == False
    assert safe_eval('a == "hello"', locals={'a': 'hello'}) == True
    assert safe_eval('a == "hello"', locals={'a': 'hello2'}) == False
    assert safe_eval('1 < int(a) < 5', locals={'a': '5'}) == False
    assert safe_eval('1 < int(a) < 5', locals={'a': '2'}) == True
    assert safe_eval('"a" + "b"', locals={'a': 'hello'}) == 'hellob'

# Generated at 2022-06-13 15:28:25.684381
# Unit test for function safe_eval

# Generated at 2022-06-13 15:28:35.028858
# Unit test for function safe_eval
def test_safe_eval():

    module = AnsibleModule(
        argument_spec=dict(
            test_expr=dict(required=True, type='str'),
        )
    )

    expr = module.params['test_expr']
    if expr is not None:
        (result, exception) = safe_eval(expr, include_exceptions=True)
        if exception is not None:
            module.exit_json(failed=True, msg=to_native(exception))
        else:
            module.exit_json(failed=False, result=result)


# Generated at 2022-06-13 15:28:41.391881
# Unit test for function safe_eval
def test_safe_eval():
    expr = "var1.split(',')[1:3]"
    var1 = 'a,b,c,d'
    locals = {'var1': var1, 'len': len}
    result = safe_eval(expr, locals=locals)
    if result is None:
        print('Failed to eval expression: %s' % expr)
        sys.exit(1)
    assert var1.split(',')[1:3] == result



# Generated at 2022-06-13 15:28:48.551590
# Unit test for function safe_eval

# Generated at 2022-06-13 15:28:54.141704
# Unit test for function safe_eval

# Generated at 2022-06-13 15:29:00.631231
# Unit test for function safe_eval

# Generated at 2022-06-13 15:29:09.178119
# Unit test for function safe_eval

# Generated at 2022-06-13 15:29:18.682854
# Unit test for function safe_eval
def test_safe_eval():
    token = '{{foo}}'
    res = safe_eval(token)
    assert res == token, res

    # safe_eval can take builtin names in string form
    res = safe_eval("False")
    assert not res, res

    res = safe_eval("None")
    assert res is None, res

    res = safe_eval("True")
    assert res, res

    # None assigned as a variable is valid as a statement
    res = safe_eval("None = False")
    assert res is None, res

    # containers should work
    res = safe_eval("[0, 1, 2]")
    assert res == [0, 1, 2], res

    res = safe_eval("{'foo': 'bar'}")
    assert res == {'foo': 'bar'}, res

    # nested containers

# Generated at 2022-06-13 15:29:31.938810
# Unit test for function safe_eval
def test_safe_eval():
    # Test exceptions
    try:
        safe_eval("__import__('os').system('touch /tmp/testing_safe_eval')")
        assert False
    except:
        assert True

    try:
        safe_eval("__import__('os').system('touch /tmp/testing_safe_eval').bytes")
        assert False
    except:
        assert True

    try:
        safe_eval("__import__('os').system")
        assert False
    except:
        assert True

    try:
        safe_eval("__import__('os').system('touch /tmp/testing_safe_eval').close")
        assert False
    except:
        assert True

    # Test basic functionality
    assert safe_eval('2 + 3') == 5
    assert safe_eval('ansible_distribution') == 'RedHat'

# Generated at 2022-06-13 15:29:38.239212
# Unit test for function safe_eval
def test_safe_eval():

    # assert that invalid expression fail
    try:
        safe_eval('1+1; import os')
        assert False
    except Exception:
        assert True

    # assert that valid expression are evaluated correctly
    assert safe_eval('True and False') is False
    assert safe_eval('True == True') is True
    assert safe_eval('True != False') is True
    assert safe_eval('True or False') is True
    assert safe_eval('1+1') == 2
    assert safe_eval('1+1 == 2') is True
    assert safe_eval('1+1 != 2') is False
    assert safe_eval('1+1; 1+1') == 2
    assert safe_eval('{}') == {}
    assert safe_eval('[]') == []
    assert safe_eval('{} or []') == {}

# Generated at 2022-06-13 15:29:42.640761
# Unit test for function safe_eval

# Generated at 2022-06-13 15:29:53.369274
# Unit test for function safe_eval
def test_safe_eval():
    def _test(expr, expected, expected_exception=None):
        if expected_exception:
            result, exception = safe_eval(expr, include_exceptions=True)
            assert exception
            assert expected == result
        else:
            result = safe_eval(expr)
            assert expected == result

    _test("True", True)
    _test("False", False)
    _test("None", None)
    _test('"foo"', "foo")
    _test("123", 123)
    _test("1.23", 1.23)
    _test("[1,2,3]", [1, 2, 3])
    _test("{'a':1}", {'a': 1})
    _test("'abc'.upper()", 'abc'.upper())

# Generated at 2022-06-13 15:30:01.250657
# Unit test for function safe_eval
def test_safe_eval():
    def failsafe(x):
        '''
        a simple failsafe function for testing
        '''
        pass

    # add to a list if the test passed or failed
    # tests that should not pass
    # (test_input, error_msg)

# Generated at 2022-06-13 15:30:08.660915
# Unit test for function safe_eval
def test_safe_eval():
    # simple cases
    assert safe_eval('1 + 1') == 2
    assert safe_eval('"foo"'), 'foo'
    assert safe_eval('[1, "foo", ["bar", "baz"], {"key": "value"}]') == [1, 'foo', ['bar', 'baz'], {'key': 'value'}]
    assert safe_eval('(1, "foo", ("bar", "baz"), {"key": "value"})') == (1, 'foo', ('bar', 'baz'), {'key': 'value'})

    # check that we are whitelisting known json types
    assert safe_eval('true')
    assert safe_eval('false')
    assert safe_eval('null')

    # check we can do basic comparisons
    assert safe_eval('1 == 1')
    assert not safe_

# Generated at 2022-06-13 15:30:19.079505
# Unit test for function safe_eval
def test_safe_eval():
    # nested structures
    assert 1 == safe_eval("1")

    # safe things
    assert None == safe_eval("None")
    assert True == safe_eval("True")
    assert 1 == safe_eval("1")
    assert [1,2,3] == safe_eval("[1,2,3]")
    assert dict(a=1, b=2) == safe_eval("{'a': 1, 'b': 2}")

    # list comprehension (very useful, but can be constructed to run arbitrary code)
    assert [1,2,3] == safe_eval("[x for x in [1,2,3]]")
    assert [1,2,3] == safe_eval("[x for x in (1,2,3)]")

# Generated at 2022-06-13 15:30:24.030070
# Unit test for function safe_eval
def test_safe_eval():
    # Passing None as the first arg will make the function return None
    assert safe_eval(None) is None

    # Passing a string will make it return the string
    assert safe_eval("hello world") == "hello world"

    # Passing an integer will make it return the integer
    assert safe_eval("5") == 5

    # Passing a variable will make it look it up in the locals variable
    my_variable = 5
    locals = {'my_variable': my_variable}
    assert safe_eval("my_variable", locals=locals) == 5

    # Passing a function that is defined in locals will make it call the function
    def a_function(a,b,c=5):
        return a*b*c
    locals = {'a_function': a_function}

# Generated at 2022-06-13 15:30:30.702090
# Unit test for function safe_eval
def test_safe_eval():
    # Test invalid syntax
    invalid_exprs = [
        "func()",
        "a = 5",
        "import os",
    ]
    for expr in invalid_exprs:
        assert safe_eval(expr) == expr

    # Test valid syntax
    valid_exprs = [
        "a_var",
        "a_var.strip()",
        "func_var('foo')",
        "func_var(a_var.strip())",
        "a_var.strip('f')",
        "a_var.split('o')",
    ]
    for expr in valid_exprs:
        safe_eval(expr)

    # Test with locals

# Generated at 2022-06-13 15:30:39.724712
# Unit test for function safe_eval
def test_safe_eval():
    import six
    import datetime

    # Note: some of these tests also test for the jinja2 filter of the same name

    assert safe_eval("{{ 5 }}") == '{{ 5 }}'
    assert safe_eval("TEST") == 'TEST'
    assert safe_eval("'TEST'") == 'TEST'
    assert safe_eval("5") == 5
    assert safe_eval("6 * 7") == 42
    assert safe_eval("True and False") is False
    assert safe_eval("True or False") is True
    assert safe_eval("5 | int") == 5
    assert safe_eval("5.1 | float") == 5.1
    assert safe_eval("5.1 | round(0, 'floor')") == 5
    assert safe_eval("[]") == []

# Generated at 2022-06-13 15:30:48.411810
# Unit test for function safe_eval

# Generated at 2022-06-13 15:30:54.163223
# Unit test for function safe_eval
def test_safe_eval():
    # symbolics
    assert safe_eval('True') is True
    assert safe_eval('False') is False
    assert safe_eval('None') is None
    assert safe_eval('true') is True
    assert safe_eval('false') is False
    assert safe_eval('null') is None
    assert safe_eval('TRUE') is True
    assert safe_eval('FALSE') is False
    assert safe_eval('NULL') is None
    assert safe_eval('None') is None
    assert safe_eval('none') is None
    assert safe_eval('NONE') is None

    # Simple expressions
    assert safe_eval('1') == 1
    assert safe_eval('1 + 1') == 2
    assert safe_eval('1 + 1 == 2') is True
    assert safe_eval('1 + 1 != 2') is False



# Generated at 2022-06-13 15:31:00.204842
# Unit test for function safe_eval
def test_safe_eval():
    test_facts = {
        "test_facts1": '{ "foo": "bar", "nested": { "aaa": "bbb" } }',
        "test_facts2": '{ "bar": "foo", "nested": { "aaa": "bbb" } }',
        "test_facts3": '{ "bar": "foo", "nested": { "aaa": "bbb" } }',
        "test_facts4": 'test_facts4',
        "test_facts5": 'test_facts5',
        "test_facts6": 'test_facts6',
        "test_facts7": 'test_facts7',
        "test_facts8": 'test_facts8',
    }


# Generated at 2022-06-13 15:31:10.473216
# Unit test for function safe_eval
def test_safe_eval():
    # verify basics
    assert safe_eval('1 + 2') == 3
    assert safe_eval('True') is True
    assert safe_eval('None') is None

    # some items that should fail
    failed = False
    try:
        safe_eval('abs()')
    except Exception:
        failed = True
    assert failed

    failed = False
    try:
        safe_eval('__import__("os").unlink("/bin/rm")')
    except Exception:
        failed = True
    assert failed

    # make sure we can safely handle tuples
    assert safe_eval('(1,2)') == (1, 2)
    assert safe_eval('(1 + 2, 2 + 3)') == (3, 5)

    # make sure we can safely handle list
    assert safe_eval('[1,2]')

# Generated at 2022-06-13 15:31:17.345071
# Unit test for function safe_eval
def test_safe_eval():
    try:
        import astor
        ASTOR_AVAILABLE = True
    except ImportError:
        ASTOR_AVAILABLE = False

    # basic test, check that an invalid expression raises exception
    invalid_expr = "some_var + &&*"
    try:
        safe_eval(invalid_expr)
    except Exception as e:
        if ASTOR_AVAILABLE:
            # check that the invalid part of the expression is in the message
            # we get out of safe_eval()
            parsed = ast.parse(invalid_expr, mode='eval')
            invalid_part = astor.to_source(parsed).strip()
            assert invalid_part in str(e)
        # test passed
        pass
    else:
        assert False, "expected expression to raise exception"

    # check that a

# Generated at 2022-06-13 15:31:29.067257
# Unit test for function safe_eval

# Generated at 2022-06-13 15:31:36.762386
# Unit test for function safe_eval

# Generated at 2022-06-13 15:31:44.695689
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval('1+1', {}, True) == (2, None)
    assert safe_eval('foo', {}, True) == ('foo', None)
    assert safe_eval('foo.bar', {}, True) == ('foo.bar', None)
    assert safe_eval('1+1', {}, False) == 2

    assert safe_eval('"hello world"', {}, True) == ('hello world', None)
    assert safe_eval('"hello world"', {}, False) == 'hello world'

    assert safe_eval('a_list_variable', {'a_list_variable': [1, 2, 3]}, True) == ([1, 2, 3], None)

# Generated at 2022-06-13 15:31:55.185656
# Unit test for function safe_eval
def test_safe_eval():
    # Test for customized builtins
    expr = 'false'
    val, err = safe_eval(expr, include_exceptions=True)
    if val is False and err is None:
        print("[PASSED] Expr: %s" % expr)
    else:
        print("[FAILED] Expr: %s, Val: %s, Error: %s" % (expr, val, err))

    expr = 'null'
    val, err = safe_eval(expr, include_exceptions=True)
    if val is None and err is None:
        print("[PASSED] Expr: %s" % expr)
    else:
        print("[FAILED] Expr: %s, Val: %s, Error: %s" % (expr, val, err))

    expr = 'true'
    val

# Generated at 2022-06-13 15:32:05.810417
# Unit test for function safe_eval
def test_safe_eval():
    # basic tests
    assert safe_eval('1+2') == 3
    assert safe_eval('4*4') == 16
    assert safe_eval('"foo"') == "foo"
    assert safe_eval('["foo", "bar"]') == ["foo", "bar"]
    assert safe_eval('{"foo": "bar"}') == {"foo": "bar"}
    assert safe_eval('{"foo": "bar", "baz": "quux"}') == {"foo": "bar", "baz": "quux"}

    # tests with non-constant expressions
    # safe_eval uses a whitelist of allowable AST nodes.
    # it should not allow things not in its whitelist.
    # In safe_eval, the following will raise an exception.
    # This test checks to make sure that it raises an exception.
    # Note that the

# Generated at 2022-06-13 15:32:18.879461
# Unit test for function safe_eval
def test_safe_eval():
    # no exception raised, safe objects
    eval_safe_objects(["false", "null", "true", "True", "False", "None"])
    # basic operations
    eval_safe_objects(["300", "300.10", "300+10", "300.1+10"])
    eval_safe_objects(["300", "300.10", "300-10", "300.1-10"])
    eval_safe_objects(["300", "300.10", "300*10", "300.1*10"])
    eval_safe_objects(["300", "300.10", "300/10", "300.1/10"])
    eval_safe_objects(["300**10", "300.1**10"])
    # list
    eval_safe_objects(["[1, 2, 3]"])

# Generated at 2022-06-13 15:32:30.988796
# Unit test for function safe_eval

# Generated at 2022-06-13 15:32:40.875440
# Unit test for function safe_eval
def test_safe_eval():
    # we have to specify some sane limits on the range function
    # because python3 is more strict than python2
    if sys.version_info >= (3, 0):
        range_str = 'range(0, sys.maxsize)'
    else:
        range_str = 'range(0, 2**63-1)'
    print(safe_eval(range_str))
    print(safe_eval('[1,2,3,4,5]'))
    print(safe_eval('{"a": "foo", "b": "bar"}'))
    # no builtin functions
    try:
        safe_eval('len(range())')
    except Exception as e:
        print(e)
    # no lambdas
    try:
        safe_eval('lambda x: x+1')
    except Exception as e:
        print

# Generated at 2022-06-13 15:32:47.898422
# Unit test for function safe_eval
def test_safe_eval():
    # Valid expressions - no exceptions
    assert safe_eval('1') == 1
    assert safe_eval('2 + 3') == 5
    assert safe_eval('true') is True
    assert safe_eval('1 == 1') is True
    assert safe_eval('a', locals={'a': 2}) == 2
    assert safe_eval('a', locals={'a': None}) is None
    assert safe_eval('a', locals={'a': None}) is None
    assert safe_eval('[1,2,3]') == [1,2,3]
    assert safe_eval('[1,2,3]', locals={'a': 2}) == [1,2,3]
    assert safe_eval('{"a":1}') == {"a":1}
    assert safe_eval('1 + 1', include_exceptions=True)

# Generated at 2022-06-13 15:32:55.946020
# Unit test for function safe_eval
def test_safe_eval():
    print("test_safe_eval")

    # enable functions that are ok to use
    CALL_ENABLED.append('abs')

    # Some good expressions
    assert safe_eval("3.1415926") == 3.1415926
    assert safe_eval("0xface") == 0xface
    assert safe_eval("0o755") == 0o755
    assert safe_eval("0b10101") == 0b10101
    assert safe_eval("abs(-1)") == 1
    assert safe_eval("true")
    assert not safe_eval("false")
    assert safe_eval("null") is None
    assert safe_eval("[]") == []
    assert safe_eval("{}") == {}
    assert safe_eval("[1, 2, 3]") == [1, 2, 3]
    assert safe_eval

# Generated at 2022-06-13 15:33:05.145237
# Unit test for function safe_eval
def test_safe_eval():
    def test_safe_eval_assert(msg, expr, expected_result, locals=None):
        if locals is not None:
            result, exception = safe_eval(expr, locals, include_exceptions=True)
        else:
            result, exception = safe_eval(expr, include_exceptions=True)
        test_safe_eval_assert_result(msg, result, expected_result, exception)

    def test_safe_eval_assert_result(msg, result, expected_result, exception=None):
        assert result == expected_result, "%s: Result(%s), Expected(%s), Exception(%s)" % (msg, result, expected_result, exception)

    # testing for EXCEPTION
    # - invalid syntax

# Generated at 2022-06-13 15:33:16.094170
# Unit test for function safe_eval
def test_safe_eval():
    # it should work on simple arithmetic expressions
    assert safe_eval('2 + 2') == 4
    assert safe_eval('2 * 2') == 4
    assert safe_eval('2 - 2') == 0
    assert safe_eval('2 / 2') == 1
    # it should work on string expressions too
    assert safe_eval('"foo"') == "foo"
    assert safe_eval('"foo" * 2') == "foofoo"
    assert safe_eval('"foo" + "bar"') == "foobar"
    assert safe_eval('"foo" - "bar"') == "foo-bar"
    # it should work on string expressions too
    assert safe_eval('[1, 2]') == [1, 2]

# Generated at 2022-06-13 15:33:27.031339
# Unit test for function safe_eval
def test_safe_eval():
    # This is not an exhaustive test.  However, it does cover several
    # simple use cases.  It should be easy to add more use cases.
    # If you are working on safe_eval and you add to this test suite
    # please add a comment describing why you added the test case.
    if sys.version_info < (2, 7):
        # safe_eval uses ast.parse on python 2.7 and higher.
        return None
    # container_to_text used to return None for failed conversions.
    # container_to_text now throws an exception.
    def safe_text(obj):
        try:
            text = container_to_text(obj)
        except Exception:
            text = None
        return text

    # test safe_eval with several simple valid expressions
    assert safe_eval('1 + 1') == 2

# Generated at 2022-06-13 15:33:33.142083
# Unit test for function safe_eval

# Generated at 2022-06-13 15:33:44.100335
# Unit test for function safe_eval
def test_safe_eval():
    true_tests = [
        'true',
        'true and not false',
        'true and not false and true == true',
        'true and not false and true == false',
        'true and not false and false == false',
        'not false and true'
    ]
    false_tests = [
        'false',
        'false and not true',
        'false and true == false',
        'false and true',
        'false and (1 == 1)',
        'false and false',
        'true and false',
        'not true',
    ]
    all_tests = true_tests + false_tests
    for t in all_tests:
        native_test = to_native(t)
        result = safe_eval(t)

# Generated at 2022-06-13 15:33:58.028359
# Unit test for function safe_eval

# Generated at 2022-06-13 15:34:04.920988
# Unit test for function safe_eval
def test_safe_eval():
    # Testing that safe_eval works properly
    val = safe_eval('[1, 2, 3]')
    assert type(val) is list

    val = safe_eval('("foo", "bar")')
    assert type(val) is tuple

    val = safe_eval('{"foo": "bar"}')
    assert type(val) is dict

    val = safe_eval('foo == bar')
    assert type(val) is ast.expr

    # Testing that invalid expressions cause failure
    rval = safe_eval('import os')
    assert rval == 'import os'

# Generated at 2022-06-13 15:34:09.852454
# Unit test for function safe_eval
def test_safe_eval():
    """Test the safe_eval function"""

    # Test some safe values
    assert 'hello' == safe_eval(u"hello")
    assert 'hello' == safe_eval(u"'hello'")
    assert 'hello' == safe_eval(u"u'hello'")
    assert 'hello' == safe_eval(u"b'hello'")
    assert 42 == safe_eval(u"42")
    assert 42 == safe_eval(u"42+0")
    assert 42 == safe_eval(u"6*7")
    assert 42.0 == safe_eval(u"6.0*7")
    assert 42.0 == safe_eval(u"6*7.0")
    assert 42.0 == safe_eval(u"6.0*7.0")

# Generated at 2022-06-13 15:34:19.661387
# Unit test for function safe_eval
def test_safe_eval():

    # test that safe eval correctly returns objects on success
    assert safe_eval("1") == 1
    assert safe_eval("'abc'") == 'abc'

    # test that safe eval correctly raises errors
    # with undefined variables
    try:
        safe_eval("foo")
        assert False
    except Exception:
        pass

    # test that safe eval correctly raises errors
    # with undefined functions
    try:
        safe_eval("my_func()")
        assert False
    except Exception:
        pass

    # test that safe eval correctly raises errors
    # with forbidden operations, such as multiply
    try:
        safe_eval("1 * 2")
        assert False
    except Exception:
        pass

    # test that safe_eval correctly returns container on success
    assert safe_eval("{1: 2}") == {1: 2}



# Generated at 2022-06-13 15:34:28.720049
# Unit test for function safe_eval
def test_safe_eval():
    '''
    Unit test for function safe_eval
    '''
    # Check that simple safe_eval works
    assert safe_eval("2 + 2") == 4
    # Make sure that exception is thrown for invalid expressions
    try:
        safe_eval("==")
        assert False
    except Exception:
        pass
    # Make sure that exception is thrown for invalid expression logic
    try:
        safe_eval("2 + 2 == 5")
        assert False
    except Exception:
        pass
    # Make sure that calling a non-whitelisted function throws an exception
    try:
        safe_eval("open()")
        assert False
    except:
        pass
    # Make sure that calling a whitelisted function doesn't throw an exception
    assert safe_eval("len([2, 3])") == 2



# Generated at 2022-06-13 15:34:37.928485
# Unit test for function safe_eval
def test_safe_eval():
    expr = "{{ foo }}"
    expr2 = "{{ foo }}/{{ bar }}"
    expr3 = "{{foo}}/{{bar}}"
    expr4 = '{{foo}}/{{bar}}'
    expr5 = "{{ '%s' | format(foo) }}"
    expr6 = '{{ foo.bar }}'
    expr7 = "{% if foo %}T{% endif %}"
    expr8 = "{{ '%s' | format('foo') }}"
    expr9 = '{{ (1, 2, 3) }}'
    expr10 = '{{ [1, 2, 3] }}'
    expr11 = '{{ {a:1, b:2} }}'
    expr12 = '{{ foo.bar | mando(a=1, b=2) }}'

# Generated at 2022-06-13 15:34:45.830865
# Unit test for function safe_eval
def test_safe_eval():
    '''
    Check a few simple and obvious cases.
    '''
    # Simple literal evaluation
    assert 42 == safe_eval('42')
    assert 42.0 == safe_eval('42.0')
    assert 'hello' == safe_eval("'hello'")
    assert [1, 2, 3, 4] == safe_eval("[1, 2, 3, 4]")
    assert {'a': 'b', 'c': 'd'} == safe_eval("{'a': 'b', 'c': 'd'}")

    # Simple ops
    assert 10 == safe_eval('2 + 8')
    assert 7 == safe_eval('2 + 3 * 2')
    assert 13 == safe_eval('2 * 3 + 5')
    assert 4 == safe_eval('(2 + 8) / 2')
    assert 6.5

# Generated at 2022-06-13 15:34:53.085417
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval("foo") == "foo"
    assert safe_eval("foo", dict(foo=False)) == False
    assert safe_eval("foo", dict(foo=True)) == True

    # test with_subelements
    assert safe_eval("'bar'", dict(foo=[dict(bar="baz")])) == "bar"
    assert safe_eval("42", dict(foo=[dict(bar=42)])) == 42

    # test arrays
    assert safe_eval("foo[1]", dict(foo=[1, 2, 3])) == 2
    assert safe_eval("foo[1]", dict(foo='bar')) == 'a'
    assert safe_eval("foo[1]", dict(foo=[1])) == 1
    assert safe_eval("foo[1]") == 1

    # test dictionaries

# Generated at 2022-06-13 15:35:02.839122
# Unit test for function safe_eval
def test_safe_eval():
    expr = "dummy"
    assert safe_eval(expr) == expr
    expr = "dummy(7)"
    assert safe_eval(expr) == expr
    expr = "{'a': 7}"
    assert safe_eval(expr) == {'a': 7}
    expr = "['b', 7]"
    assert safe_eval(expr) == ['b', 7]
    expr = "7 + 3"
    assert safe_eval(expr) == 10
    expr = "7 + not_allowed"
    assert safe_eval(expr) == expr
    expr = "7 * 3"
    assert safe_eval(expr) == 21
    expr = "7 - 3"
    assert safe_eval(expr) == 4
    expr = "-7"
    assert safe_eval(expr) == -7

# Generated at 2022-06-13 15:35:11.901516
# Unit test for function safe_eval
def test_safe_eval():
    test_expr = [
        "2 + 2",
        "2 + 2 == 4",
        "foo == 'bar'",
        "foo == 'baz' and bar == 'foo'",
        "True",
        "False",
        "None",
        "['red', 'blue', 'green']",
        "'blue' in colors",
        "('red' in colors) or ('blue' in colors)",
        "'yellow' in colors",
        "var2 == var1",
    ]
    test_locals = {
        'var1': 'bar',
        'var2': 'bar',
        'colors': ['red', 'blue', 'green'],
    }
    for expr in test_expr:
        result, error = safe_eval(expr, test_locals, include_exceptions=True)
       

# Generated at 2022-06-13 15:35:29.250685
# Unit test for function safe_eval

# Generated at 2022-06-13 15:35:38.146256
# Unit test for function safe_eval
def test_safe_eval():
    # import sys, traceback
    # print '='*80
    # print traceback.format_exc()
    # print '='*80
    # sys.exit(1)
    # C.ANSIBLE_STRICT_TASK_NAMES = None
    # C.ANSIBLE_STRICT_VARS = None
    # C.ANSIBLE_NO_LOG = True

    def _get_result(expr):
        return safe_eval(expr, {}, True)


# Generated at 2022-06-13 15:35:43.322546
# Unit test for function safe_eval
def test_safe_eval():
    '''
    This is not a real unit test, just a way to exercise and debug the safe_eval
    function. To run this test, call it with 'test' as the first parameter.
    '''
    if 'test' in sys.argv[1:]:
        global CALL_ENABLED
        CALL_ENABLED = ['foo']
        print("eval %s: %s" % ('foo', safe_eval('foo')))
        print("eval %s: %s" % ('foo()', safe_eval('foo()')))
        print("eval %s: %s" % ('foo', safe_eval('foo', include_exceptions=True)))
        print("eval %s: %s" % ('foo()', safe_eval('foo()', include_exceptions=True)))
        CALL_ENABLED = ['int']
       

# Generated at 2022-06-13 15:35:53.341979
# Unit test for function safe_eval
def test_safe_eval():
    def test(expr, expected, cb=None):
        actual, exception = safe_eval(expr, include_exceptions=True)
        if exception:
            print("'%s' failed: %s" % (expr, exception))

            if cb:
                cb(expr, expected, actual, exception)

            raise AssertionError()
        if isinstance(expected, string_types):
            if actual != expected:
                print("'%s' failed. Expected '%s', got '%s'" % (expr, expected, actual))

                if cb:
                    cb(expr, expected, actual, exception)

                raise AssertionError()

# Generated at 2022-06-13 15:36:04.007176
# Unit test for function safe_eval
def test_safe_eval():
    class JsonTypeTestObj(object):
        def __init__(self, val):
            self.val = val
        def __repr__(self):
            return '%s(%r)' % (self.__class__.__name__, self.val)

    # to_text is used here because the same tests are run in both Python 2 and Python 3.
    # This ensures that the string literals used here are the same as the ones that would
    # be created in Python 3 via repr() on Python 2.  This prevents a bunch of unicode
    # errors that have nothing to do with our test.
    assert container_to_text(safe_eval("{'a': 'foo', 'b': 'bar'}")) == "{'a': 'foo', 'b': 'bar'}"

# Generated at 2022-06-13 15:36:11.997815
# Unit test for function safe_eval

# Generated at 2022-06-13 15:36:19.457141
# Unit test for function safe_eval
def test_safe_eval():
    from ansible.module_utils.six.moves import cStringIO as StringIO
    from ansible.vars.clean import module_args_value

    # Test for Bools (type, value)
    old_stdout = sys.stdout
    sys.stdout = mystdout = StringIO()


# Generated at 2022-06-13 15:36:27.520507
# Unit test for function safe_eval

# Generated at 2022-06-13 15:36:34.137086
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval("3+4") == 7
    assert safe_eval("a_variable", dict(a_variable=7)) == 7
    assert safe_eval("{{ an_unquoted_variable }}", dict(an_unquoted_variable=8)) == 8
    assert safe_eval("{{ a_list_variable }}", dict(a_list_variable=[1, 2, 3])) == [1, 2, 3]
    assert safe_eval("{{ a_dict_variable }}", dict(a_dict_variable={'a': 1, 'b': 2})) == {'a': 1, 'b': 2}
    assert safe_eval("{{ a_dict_variable }}", dict(a_dict_variable={'a': 1, 'b': 2})) == {'a': 1, 'b': 2}
    assert safe_

# Generated at 2022-06-13 15:36:43.588229
# Unit test for function safe_eval
def test_safe_eval():
    try:
        import astor
    except ImportError:
        print("SKIP: safe_eval unit test (cannot import astor)")
        return

    # These tests were generated with the following script.
    # Since the 'eval' builtin is itself a security risk, and since
    # 'ast.literal_eval' is too restrictive for our needs, we instead
    # parse the AST and allow only a subset of nodes to be present in it.
    #
    # This is a rather complex process, especially for those who are not familiar
    # with Python's AST module, so we will test it exhaustively here to aid
    # maintainability and help prevent regressions.
    #
    # This generates tests for safe_eval().
    #
    # import ast
    # import itertools
    # import string
    #
    # test_input

# Generated at 2022-06-13 15:37:09.607536
# Unit test for function safe_eval
def test_safe_eval():
    safe_test = '''
    with_sequence: count=2
    with_items:
      - "{{ range(1, 5) }}"
      - "{{ [6,7,8,9,10] }}" '''

    unsafe_test = '''
    with_sequence: count=2
    with_items:
      - "{{ range(1, 5) }}"
      - "{{ [6,7,8,9,10] }}"
    vars:
      localhost: "{{ foo('bar') }}"
      foo: "{{ bar('localhost') }}"'''

    safe_result = safe_eval(safe_test, include_exceptions=True)

    if safe_result[1]:
        print("Test Unsafe Eval Failed")
        print(safe_result[1])
        sys.exit(1)

# Generated at 2022-06-13 15:37:19.699754
# Unit test for function safe_eval
def test_safe_eval():

    # Test syntactically correct but unsafe evals
    try:
        safe_eval('__import__("os").system("touch /tmp/ANSIBLE_TESTING_SAFE_EVAL")')
    except Exception:
        pass
    else:
        raise AssertionError('safe_eval() failed to raise any exceptions for evaling __import__("os").system("touch /tmp/ANSIBLE_TESTING_SAFE_EVAL")')

    # Test syntactically incorrect evals
    try:
        safe_eval(1)
    except Exception:
        pass
    else:
        raise AssertionError('safe_eval() failed to raise any exceptions for evaling 1')

    # Test non-existant callables
    try:
        safe_eval('notexistent()')
    except Exception:
        pass

# Generated at 2022-06-13 15:37:26.552398
# Unit test for function safe_eval
def test_safe_eval():
    assert safe_eval("[]") == []
    assert safe_eval("{}") == {}
    assert safe_eval("0") == 0
    assert safe_eval("1") == 1
    assert safe_eval("-1") == -1
    assert safe_eval("True") == True
    assert safe_eval("False") == False
    assert safe_eval("None") == None
    assert safe_eval("true") == True
    assert safe_eval("false") == False
    assert safe_eval("none") == None
    assert safe_eval("1.1") == 1.1
    assert safe_eval("-1.1") == -1.1
    assert safe_eval("'h'") == 'h'
    assert safe_eval("'1.1'") == '1.1'

# Generated at 2022-06-13 15:37:35.160384
# Unit test for function safe_eval
def test_safe_eval():
    # Check basic functionality
    assert safe_eval('True') is True
    assert safe_eval('False') is False
    assert safe_eval('None') is None
    assert safe_eval('1 + 1') == 2
    assert safe_eval('1.9 - 0.8') == 1.1
    assert safe_eval('1.8 * 3.2') == 5.76
    assert safe_eval('8 / 2') == 4
    assert safe_eval('1 + 1') == 2
    assert safe_eval('3 - 1') == 2
    assert safe_eval('3 * 4') == 12
    assert safe_eval('(3 * 4) - 1 + (2 * 1)') == 13
    assert safe_eval('["a", "b", "c"]') == ["a", "b", "c"]

# Generated at 2022-06-13 15:37:44.589903
# Unit test for function safe_eval
def test_safe_eval():
    # load some data types for comparison
    null = None
    true = True
    false = False
    empty = ''
    test_string = 'value'
    test_list = [1, 2, 3]
    test_dict = {'a': 1, 'b': 2}
    # define a safe subset of builtins that we allow in safe_eval()
    CALL_ENABLED.extend(('list', 'dict', 'str', 'int', 'len', 'bool', 'any', 'all'))
    # test defined set of values that should always evaluate to same value
    for expr, expected in C.SAFE_EVAL_LOCALS.items():
        # convert returned value to builtin python data types for comparison
        result = safe_eval(expr)
        assert result == expected
    # test that a safe list comprehension can be evaluated


# Generated at 2022-06-13 15:37:54.567429
# Unit test for function safe_eval
def test_safe_eval():
    # test the safe_eval function and make sure it only allows the constructs
    # we want and disallows everything else
    examples = []

    # test literal evaluation
    examples.append((['1', '1'], 1))
    examples.append((['1', '-1'], -1))
    examples.append((['1', '1+2'], 3))
    examples.append((['1', '1+2*3'], 7))
    examples.append((['1', '1+2*3-8/4'], 5))
    examples.append((['1', '"a"'], 'a'))
    examples.append((['1', '"a"+"b"'], 'ab'))
    examples.append((['1', '"a"+"b"+"c"'], 'abc'))
    examples.append