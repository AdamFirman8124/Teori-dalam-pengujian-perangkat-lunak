

# Generated at 2022-06-14 17:48:41.091934
# Unit test for method interpret_statement of class JSInterpreter
def test_JSInterpreter_interpret_statement():
    objects = {}

    # Create a JSInterpreter object with a defined object and function
    js_interpreter = JSInterpreter('''
        foo = {
            bar: function(a, b){
                return a + b;
            }
        };
        function foobar(a, b){
            return a * b;
        }
    ''', objects)

    # Test single statement that returns a int
    assert js_interpreter.interpret_statement('return 7;', {})[0] == 7

    # Test single statement that returns a string
    assert js_interpreter.interpret_statement('return "hi";', {})[0] == 'hi'

    # Test single statement that returns a list

# Generated at 2022-06-14 17:48:53.093448
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    js1 = JSInterpreter(code='''
    function wl(a){var b=a.split(""),c=b.length,d=z(y,"charCodeAt"),e=c;for(;e--;)if(55296==(b[e]|d.call(y,e))>>6){b.splice(e,1,b[e],b[++e]);c++;};return b}''',
                       objects={'y': 'Hello'})

# Generated at 2022-06-14 17:49:00.352261
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():

    code = """
        g = {
            a: function(v) {return v;},
            b: function(v, w) {return [v, w];}
        };
    """
    objects = JSInterpreter(code)._objects
    assert objects['g']['a'](5) == 5
    assert objects['g']['b'](5, 10) == [5, 10]


if __name__ == '__main__':
    test_JSInterpreter_extract_object()

# Generated at 2022-06-14 17:49:13.623672
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    test = JSInterpreter('', {})
    assert test.interpret_expression(
        '12', {}, 100) == 12
    assert test.interpret_expression(
        '12.34', {}, 100) == 12.34
    assert test.interpret_expression(
        '"foo"', {}, 100) == "foo"
    assert test.interpret_expression(
        '1 + 23', {}, 100) == 24
    assert test.interpret_expression(
        '2 - 1', {}, 100) == 1
    assert test.interpret_expression(
        '1 + 23 * 2', {}, 100) == 47
    assert test.interpret_expression(
        'a', {'a': 'A'}, 100) == 'A'

# Generated at 2022-06-14 17:49:25.981373
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    test_JSInterpreter = JSInterpreter('''
        var b = 2;
        var a = 1;
        a += b;
        var c = [4, 5, 6];
        c.reverse();
        var x = 'abcdefghijklmnopqrstuvwxyz';
        x = x.substr(a, b) + c.join('');
        var d = [1, 2, 3];
        var e = d.slice(0, 1);
        var f = d.splice(1, 1);
        ''')
    assert test_JSInterpreter.interpret_expression('a') == 3
    assert test_JSInterpreter.interpret_expression('x') == 'cdefghijklmnopqrstuvwxyz'

# Generated at 2022-06-14 17:49:32.590093
# Unit test for method extract_function of class JSInterpreter

# Generated at 2022-06-14 17:49:43.026549
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    js_interpreter = JSInterpreter("var func = function(arg1, arg2, arg3) {"\
        + "var var1 = arg1;"\
        + "var var2 = arg2;"\
        + "var var3 = arg3;"\
        + "return var1;"\
        + "};")
    func = js_interpreter.build_function(["arg1", "arg2", "arg3"], "var var1 = arg1;var var2 = arg2;var var3 = arg3;return var1;")
    assert func(["a", "b", "c"]) == "a"

# Generated at 2022-06-14 17:49:48.329350
# Unit test for method extract_object of class JSInterpreter

# Generated at 2022-06-14 17:49:56.743928
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    js = '''
var a = 1;
var b = "abc";
var c = {
    f: function(v) {
        var x = a + 2;
        var y = b;
        y = y.reverse();
        y = y.join(v);
        return y;
    }
};
'''
    jsi = JSInterpreter(js)
    f = jsi.build_function([], 'var x = 42; var y = "abc"; return x')
    assert f(tuple()) == 42
    f = jsi.build_function(['a', 'b'], 'return a + b')
    assert f((1, 2)) == 3
    f = jsi.build_function(['a'], 'return a(2, 3)')

# Generated at 2022-06-14 17:50:10.210233
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    code = '''
        var a = 2;
        var b = [1, 2, 3];
        function f(x, y) { z = x + y; return z; }'''
    jsi = JSInterpreter(code)

    # Test operands
    assert jsi.interpret_expression('100', {}) == 100
    assert jsi.interpret_expression('0xa', {}) == 10
    assert jsi.interpret_expression('{}', {}) == {}
    assert jsi.interpret_expression('[]', {}) == []
    assert jsi.interpret_expression('"abcd"', {}) == 'abcd'
    assert jsi.interpret_expression("'efgh'", {}) == 'efgh'
    assert jsi.interpret_expression("true", {}) == True
    assert jsi.interpret_expression

# Generated at 2022-06-14 17:50:39.132306
# Unit test for method extract_function of class JSInterpreter
def test_JSInterpreter_extract_function():
    JSInterpreter_instance = JSInterpreter(
        """
        function abc(a,b,c)
        {
            var d = a + b + c;
            return d;
        }
        """)

    assert JSInterpreter_instance.extract_function('abc')([1, 2, 3]) == 6

if __name__ == "__main__":
    test_JSInterpreter_extract_function()

# Generated at 2022-06-14 17:50:50.555727
# Unit test for method extract_function of class JSInterpreter

# Generated at 2022-06-14 17:50:57.853432
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    js_interpreter = JSInterpreter('function func1 (arg1, arg2) { var arg3 = arg1 + arg2; return arg3; return arg3; }')
    func1 = js_interpreter.build_function(['arg1', 'arg2'], 'var arg3 = arg1 + arg2; return arg3; return arg3;')
    assert func1(['1', '2']) == '12'



# Generated at 2022-06-14 17:51:03.148773
# Unit test for method interpret_statement of class JSInterpreter
def test_JSInterpreter_interpret_statement():
    code = 'var a = (5 + 6) * 3 - b;c[(d - 3)] = (g + 5) * 3 - 1;'
    js_interpreter = JSInterpreter(code)
    v = {'b': 1, 'c': [8, 9, 3, 4], 'd': 5, 'g': 6}
    js_interpreter.interpret_statement('var a = (5 + 6) * 3 - b;', v)
    assert v['a'] == 33
    js_interpreter.interpret_statement('c[(d - 3)] = (g + 5) * 3 - 1;', v)
    assert v['c'] == [8, 45, 3, 4]


# Generated at 2022-06-14 17:51:14.941796
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    interpreter = JSInterpreter(
        """var a = 1;
            var b = 2;
            var c = 3;
            var d = 4;""")
    assert interpreter.call_function('f1', 5, 6) == 11
    assert interpreter.call_function('f2', 7, 8) == 15

    interpreter = JSInterpreter(
        """var a = 1;
            var b = 2;
            var c = 3;
            var d = 4;""")
    assert interpreter.call_function('f3', 9, 10) == 19
    assert interpreter.call_function('f4', 11, 12) == 23

    interpreter = JSInterpreter(
        """var a = 1;
            var b = 2;
            var c = 3;
            var d = 4;""")
    assert interpreter.call_function

# Generated at 2022-06-14 17:51:24.444774
# Unit test for method extract_function of class JSInterpreter
def test_JSInterpreter_extract_function():
    assert JSInterpreter('').call_function("foo", 1, 2) == 3
    assert JSInterpreter('').call_function("reverse", [1, 2, 3]) == [3, 2, 1]
    assert JSInterpreter('').call_function("bar", 1) == False
    assert JSInterpreter('').call_function("bar", 2) == True
    assert JSInterpreter('').call_function("swap", 1, 2) == (2, 1)
    try:
        JSInterpreter('').call_function("unimplemented_func")
    except ExtractorError as e:
        assert "Could not find JS function 'unimplemented_func'" in str(e)


# Generated at 2022-06-14 17:51:27.285421
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    js = 'function test(a,b) {return (a+b)};'

    function_object = JSInterpreter(js).build_function(['a', 'b'], 'return (a+b);')
    assert function_object((1, 2)) == 3

# Generated at 2022-06-14 17:51:34.100343
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    # String
    code = 'var a = "This is a string";'
    interpreter = JSInterpreter(code)
    v = interpreter.interpret_expression('a', {})
    assert v == 'This is a string'

    # Number
    code = 'var b = 123456;'
    interpreter = JSInterpreter(code)
    v = interpreter.interpret_expression('b', {})
    assert v == 123456

    # Array
    code = 'var c = [100, 200, 300];'
    interpreter = JSInterpreter(code)
    v = interpreter.interpret_expression('c', {})
    assert v == [100, 200, 300]

    code = 'var d = [100, 200, 300];'
    interpreter = JSInterpreter(code)

# Generated at 2022-06-14 17:51:42.848188
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    js_interpreter = JSInterpreter("""
        function test() {
            var a = 1;
            var b = 2;
            var c = (a + b) * a;
            return c;
        }
    """)
    assert 9 == js_interpreter.build_function([], """
            var a = 1;
            var b = 2;
            var c = (a + b) * a;
            return c;
        """)()


# Generated at 2022-06-14 17:51:47.554320
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    js_interpreter = JSInterpreter("""
        var A = {
            "B": function(p) {
                return p;
            }
        };
    """)
    A = js_interpreter.extract_object("A")
    B = A["B"]
    assert (B("test") == "test")


# Generated at 2022-06-14 17:52:14.646747
# Unit test for method interpret_statement of class JSInterpreter
def test_JSInterpreter_interpret_statement():
    # Test case 1
    # Input
    local_vars = {'c':'abcdefg', 'a':1, 'b':2}
    stmt = "var a = 'abcdefg'[7], b=2; var d, e = 'abcdefg', f=((((3))))"
    interpreter = JSInterpreter(None)
    # Expected output
    expect_val = None
    expect_abort = False
    # Actual output
    actual_val, actual_abort = interpreter.interpret_statement(stmt, local_vars)
    # Assertion
    assert (expect_val == actual_val) and (expect_abort == actual_abort)
    # Test case 2
    # Input
    local_vars = {'a':1, 'b':2}
    stmt

# Generated at 2022-06-14 17:52:26.928551
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    code = '''\
        function f(a, b) {
            var c;
            c = a + b;
            return c;
        }
    '''

    interpreter = JSInterpreter(code)
    func = interpreter.extract_function('f')

    assert func((1, 2)) == 3
    assert func((3, 2)) == 5
    assert func((5, 2)) == 7
    assert func((0, 0)) == 0


# Generated at 2022-06-14 17:52:40.234571
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    js_interpreter = JSInterpreter('')

# Generated at 2022-06-14 17:52:52.480859
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    jsi = JSInterpreter("{'test': function(args){test2(args);return 'res';}, 'test2': function(args){return args;}}")
    assert jsi.call_function('test', 7) == 'res'
    assert jsi.call_function('test2', 'hej') == 'hej'

    jsi = JSInterpreter("{'test': function(a, b, c){return a + c;}, 'test2': function(a, b, c){return a + b + c;}}")
    assert jsi.call_function('test', 8, 9, 10) == 18
    assert jsi.call_function('test2', 8, 9, 10) == 27


# Generated at 2022-06-14 17:53:03.121349
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    js = JSInterpreter('foo = {}; foo.bar = function(baz, qux){return baz + qux;};')
    assert js.interpret_expression('foo.bar', {}, 100) == js.extract_object('foo')['bar']
    assert js.interpret_expression('foo.bar(2, 3)', {}, 100) == 5
    assert js.interpret_expression('foo["bar"](2, 3)', {}, 100) == 5
    assert js.interpret_expression('foo["bar"]()[0]', {}, 100) == u'5'
    js = JSInterpreter('foo = []; foo.push(2); foo.push(3); foo.push(4);')
    assert js.interpret_expression('foo.join(",")', {}, 100) == '2,3,4'


# Generated at 2022-06-14 17:53:08.560864
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    jsinterpreter = JSInterpreter("""
                                var name = {
                                foo: function() {
                                return abc;
                                }
                                };
                                """)
    object = jsinterpreter.extract_object('name')
    assert object['foo']() == 'abc'


# Generated at 2022-06-14 17:53:21.550274
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    # Example of JS function
    code = 'function test(a,b){var c = a*b;return c+2;}'
    # Example of JS object
    code += 'var obj = {f:function(a,b){var c= a+b;return c-3;}}'
    # Example of member access
    code += 'var length = obj.f(5,5);'
    # Example of member access and math operation
    code += 'var final_test = obj.f(21,21)+length;'

    interpreter = JSInterpreter(code)
    # Testing calling a JS function
    assert interpreter.call_function('test',2,3) == 8
    # Testing calling a JS object function
    assert interpreter.call_function('obj.f',3,7) == 5
    # Testing member access

# Generated at 2022-06-14 17:53:30.107324
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    code = '''var func = function(a, b) {
              var a = 5;
              var c = {
                d: function(e) {
                  return true;
                }
              }
            }'''
    interpreter = JSInterpreter(code)
    f = interpreter.build_function(['a', 'b'], 'var a = 5; var c = {d: function(e) { return true;}}')
    assert f((1, 2)) == True
        

# Generated at 2022-06-14 17:53:34.486814
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    def _make_js_interpreter(objects):
        return JSInterpreter('', objects)

    js_interpreter = _make_js_interpreter({})
    js_interpreter.interpret_statement('foo&&bar', {})

# Generated at 2022-06-14 17:53:46.705957
# Unit test for method interpret_expression of class JSInterpreter

# Generated at 2022-06-14 17:54:10.551011
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    js = JSInterpreter('var a = function(b,c){return c;}')
    f = js.build_function(['b', 'c'], 'return c')
    assert f('1') == '1'
    assert f(1, 'a') == 'a'


if __name__ == '__main__':
    test_JSInterpreter_build_function()

# Generated at 2022-06-14 17:54:15.567692
# Unit test for method call_function of class JSInterpreter
def test_JSInterpreter_call_function():
    assert JSInterpreter('function test(a,b) { return a+b; }').call_function('test', 1, 2) == 3

if __name__ == '__main__':
    test_JSInterpreter_call_function()

# Generated at 2022-06-14 17:54:19.510422
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    js_interpreter = JSInterpreter('')
    fn = js_interpreter.build_function(['a', 'b'], '{c=b+" - "+a;return(c)}')

    assert fn(('1', '2')) == '2 - 1'

# Generated at 2022-06-14 17:54:29.438307
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    js_interpreter = JSInterpreter('', {})
    def func_for_testing(args):
        local_vars = dict(zip(['a', 'b'], args))
        for stmt in code.split(';'):
            res, abort = js_interpreter.interpret_statement(stmt, local_vars)
            if abort:
                break
        return res
    argnames = ['a', 'b']
    code = "return a+b"
    result = js_interpreter.build_function(argnames, code)
    assert result(1,2) == 3


# Generated at 2022-06-14 17:54:36.784452
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    resf = JSInterpreter.build_function(
        [],
        '''
        var a = '';
        a = "%s";
        return a;
        '''
        )
    assert resf(()) == ''
    assert resf(('foo',)) == 'foo'
    assert resf(('foo', 'bar')) == 'foo'


if __name__ == '__main__':
    test_JSInterpreter_build_function()

# Generated at 2022-06-14 17:54:43.948812
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    code = '''
    z = {
        sup: function (a) {
        }
    }
    f()
    '''
    interpreter = JSInterpreter(code)
    obj = interpreter.extract_object('z')
    assert len(obj) == 1
    assert obj['sup'] != None


# Generated at 2022-06-14 17:54:49.732266
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    # Test case 1
    code1 = '''
        b = {
            c : function(a){
                return a*a;
            }
        }
    '''

    obj1 = JSInterpreter(code=code1).extract_object('b')

    assert obj1['c'](3) == 9


# Generated at 2022-06-14 17:55:00.594643
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    # Clear
    JSInterpreter.extract_function = lambda self, a: globals()[a]
    JSInterpreter.extract_object = lambda self, a: globals()[a]

    # preload functions
    global f1, f2, a
    a = '1'
    f1 = lambda a: a
    f2 = lambda a, b=1: a + b

    def test_equals(expr, res):
        assert JSInterpreter('').interpret_expression(expr, {}) == res

    test_equals(';', None)  # Empty statement
    test_equals('5', 5)
    test_equals('5;6', 6)  # Expression with ending semicolon
    test_equals('f1(5)', 5)  # Function call
    test_equ

# Generated at 2022-06-14 17:55:09.937864
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    js_code = """
    var a = 'al';
    var b = 'php';
    var d = 'is';
    var e = 'awesome';
    var f = function (a,b,c) {
        if (a == 'al') {
            return b[1];
        }
        return c;
    };
    """
    jsi = JSInterpreter(js_code)
    jsi.build_function(['a', 'b', 'c'], """if (a == 'al') {
                                            return b[1];
                                         }""") == 'p'

# Generated at 2022-06-14 17:55:22.221965
# Unit test for method call_function of class JSInterpreter
def test_JSInterpreter_call_function():
    def test(func, expected_result, expected_args):
        actual_result = JSInterpreter('').call_function(func, *expected_args)
        if type(expected_result) is list:
            assert len(actual_result) == len(expected_result)
            for prop, val in zip(actual_result, expected_result):
                assert prop == val
        else:
            assert actual_result == expected_result


# Generated at 2022-06-14 17:55:48.476939
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    js_interpreter = JSInterpreter('')
    func_name_list = [
        "a",
        "a1",
        "a1a",
        "a1a2",
        "a1a2a",
        "b",
        "b1",
        "b1a",
        "b1a2",
        "b1a2a",
        "c",
        "c1",
        "c1a",
        "c1a2",
        "c1a2a",
    ]

# Generated at 2022-06-14 17:55:55.181221
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    code = r'''var a = 10;
var b = {
    "c": function (d, e) {
        return a + d + e;
    },
    "f": {
        "g": "h"
    }
};
var i = function (j, k) {
    return j + k;
};
'''
    jsi = JSInterpreter(code)
    assert jsi.interpret_expression('a', {}) == 10
    assert jsi.interpret_expression('b.c', {})(1, 2) == 13
    assert jsi.interpret_expression('b["c"]', {})(1, 2) == 13
    assert jsi.interpret_expression('b.f.g', {}) == 'h'
    assert jsi.interpret_expression('i(1, 2)', {}) == 3



# Generated at 2022-06-14 17:56:01.397225
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():

    def assert_raises(exception, func, *args):
        try:
            func(*args)
        except exception:
            pass
        else:
            assert False, "Exception " + str(exception) + " not raised"

    def assert_equal(v1, v2):
        assert v1 == v2, "%s != %s" % (str(v1), str(v2))

    # assert_equal(JSInterpreter("").interpret_expression("", {}, 100), None)
    assert_equal(JSInterpreter("").interpret_expression("1", {}, 100), 1)
    assert_equal(JSInterpreter("").interpret_expression("1 + 2", {}, 100), 3)
    assert_equal(JSInterpreter("").interpret_expression("1 - 2", {}, 100), -1)
   

# Generated at 2022-06-14 17:56:13.031146
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    j = JSInterpreter('a x = function(p) { var r = p+1; return r; }')
    a = j.build_function(['p'], 'var r = p+1; return r;')

    assert a(1) == 2

    j = JSInterpreter('var a = function(p) { var r = p+1; return r; }')
    a = j.build_function(['p'], 'var r = p+1; return r;')

    assert a(1) == 2

    j = JSInterpreter('var a = function(b, c) { var r = b+c; return r; }')
    a = j.build_function(['b', 'c'], 'var r = b+c; return r;')

    assert a(1, 2) == 3


# Generated at 2022-06-14 17:56:25.486191
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    interpreter = JSInterpreter('')
    assert interpreter.interpret_expression('a', {'a': '10'}) == '10'
    assert interpreter.interpret_expression('var', {'var': 1}) == 1
    assert interpreter.interpret_expression('10', {}) == 10
    assert interpreter.interpret_expression('10%2', {}) == 0
    assert interpreter.interpret_expression('10+2', {}) == 12
    assert interpreter.interpret_expression('10-2', {}) == 8
    assert interpreter.interpret_expression('10*2', {}) == 20
    assert interpreter.interpret_expression('10/2', {}) == 5
    assert interpreter.interpret_expression('10<<2', {}) == 40
    assert interpreter.interpret_expression('10>>2', {}) == 2

# Generated at 2022-06-14 17:56:38.301399
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    js_interpreter = JSInterpreter(code='', objects=None)
    local_vars = {}
    assert js_interpreter.interpret_expression('x', local_vars, 10) is None

    local_vars = {'x': 'y'}
    assert js_interpreter.interpret_expression('x', local_vars, 10) == 'y'

    local_vars = {'x': ['a', 'b', 'c']}
    assert js_interpreter.interpret_expression('x[0]', local_vars, 10) == 'a'

    local_vars = {'x': ['a', 'b', 'c']}
    assert js_interpreter.interpret_expression('x[1]', local_vars, 10) == 'b'


# Generated at 2022-06-14 17:56:43.212540
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    expr = 'function test(a) {return a*2;}'
    ji = JSInterpreter(expr)
    f = ji.build_function(['a'], 'return a*2;')
    assert f(3) == 6
    assert f(5) == 10


# Generated at 2022-06-14 17:56:49.208894
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    code = r'''
        function test(num, name){
            var res = num + ' ' + name;
            return res;
        }'''
    jsinterpreter = JSInterpreter(code)
    func = jsinterpreter.build_function(['name', 'num'], 'var res = num + " " + name; return res;')
    assert func(['Zoom', 123]) == '123 Zoom'


# Generated at 2022-06-14 17:56:57.039844
# Unit test for method call_function of class JSInterpreter
def test_JSInterpreter_call_function():
    js='''
    function d(a, b) {
        return a + b;
    }
    var e = function(a, b) {
        return a - b;
    }
    f = function(a, b) {
        return a * b;
    }
    g = { h: function(a, b) {
        return a / b;
    } }
    '''
    interpreter = JSInterpreter(js)
    def run_test(fname, x, y, expect):
        assert interpreter.call_function(fname, x, y) == expect
    run_test('d', 10, 15, 25)
    run_test('e', 10, 15, -5)
    run_test('f', 3, 5, 15)

# Generated at 2022-06-14 17:57:06.038865
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    code = '''
    var a = function(eh,seh) { for(;eh--;) { var a = seh.length, b = 0, seq = 0; for(; b < a; b++) if(seh[b] > seq) seq = seh[b]; return seq || -1; } };
    function c(eh, seh) { return eh.map(function(eh, seh) { return a(eh, seh) }); };
    '''
    interpreter = JSInterpreter(code)
    seq = interpreter.call_function('a', 1, [0, 0, 0, 1, 0, 0, 1])
    assert seq == 3
    seq = interpreter.call_function('a', 2, [0, 1, 0, 0, 1, 0, 1])
    assert seq == 4

# Generated at 2022-06-14 17:57:24.932330
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    js_interpreter = JSInterpreter("""
    		return (a, b, c) => {
    		  return (((a + b) >> c) ^ d) + e;
    		};""")
    assert js_interpreter.interpret_expression('(((a + b) >> c) ^ d) + e', {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}) == 6
    assert js_interpreter.interpret_expression('d+e', {'d': 2, 'e': 3}) == 5


# Generated at 2022-06-14 17:57:32.522759
# Unit test for method call_function of class JSInterpreter
def test_JSInterpreter_call_function():
    js_code = '''
    function test_method(num, x)
    {
        var res = num*x;
        return res;
    }
    '''
    jsi = JSInterpreter(js_code)
    assert jsi.call_function('test_method', 3, 5) == 15

if __name__ == '__main__':
    test_JSInterpreter_call_function()

# Generated at 2022-06-14 17:57:40.343831
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    from collections import defaultdict

    # Test data as dict of dicts, where the first dict key is the name of the js expression, the second
    # dict key is the name of the js variable, and its value is the variable value.
    # Each test js expression should evaluate to the same result as the value of the "res" key of the
    # second dict
    # The test data include test_dict and test_list data, so this test can also validate the js object extraction

# Generated at 2022-06-14 17:57:50.610716
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    code = '''
        function f(arg1, arg2, arg3, arg4) {
            var arg5 = arg1 + arg2 + arg3;
            var arg6 = arg2 * arg3;
            var arg7 = arg5 * arg6;
            var arg8 = arg1(arg7, arg4);
            var arg9 = arg8 + arg7;
            return arg9;
        }
    '''
    interpreter = JSInterpreter(code)
    f = interpreter.build_function(
        ['arg1', 'arg2', 'arg3', 'arg4'],
        code)
    assert f(
        [1, 2, 3, 4]) == (1 + 2 + 3) * (2 * 3) + (1 + 2 + 3) * (2 * 3)



# Generated at 2022-06-14 17:57:59.313891
# Unit test for method call_function of class JSInterpreter
def test_JSInterpreter_call_function():
    js_interpreter = JSInterpreter('''
        function test(arg) {
            var a = arg + 1;
            return a;
        }

        function test2(arg) {
            var a = arg + 2;
            return a;
        }

        function test3(arg) {
            var a = arg + test(1);
            return a;
        }

        function test4(arg) {
            return arg.split('').reverse().join('');
        }
    ''')
    assert js_interpreter.call_function('test', [4]) == 5
    assert js_interpreter.call_function('test2', [4]) == 6
    assert js_interpreter.call_function('test3', [4]) == 7
    assert js_interpreter.call_function