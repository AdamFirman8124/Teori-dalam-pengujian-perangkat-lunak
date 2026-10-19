

# Generated at 2022-06-14 17:48:49.268087
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    objects = {
        'function': {
            'some_function': lambda *args: args[0] + args[1]
        },
        'a': {
            'indexOf': lambda *args: 0
        }
    }

    js_interpreter = JSInterpreter(
        'var b = "abcd".split("");',
        objects=objects
    )
    assert js_interpreter.interpret_expression(
        'b.reverse()',
        {},
        1
    ) == ['d', 'c', 'b', 'a']

    js_interpreter = JSInterpreter(
        'var c = "abcd".split("").reverse().join("");',
        objects=objects
    )

# Generated at 2022-06-14 17:49:00.800640
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():

    jsinterpreter = JSInterpreter(code, objects=None)
    print("Interpreting expression, test #1")
    stmt = "a[1]=b>>8"
    local_vars = {'a':'a', 'b':'b'}
    jsinterpreter.interpret_expression(stmt, local_vars, 1)
    print("Interpreting expression, test #2")
    stmt = 'a[1]='
    local_vars = {'a':'a', 'b':'b'}
    jsinterpreter.interpret_expression(stmt, local_vars, 1)


if __name__ == '__main__':
    test_JSInterpreter_interpret_expression()
    pass

# Generated at 2022-06-14 17:49:09.588715
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    js_code = '''
    var WJIS=function(){};
    WJIS.prototype={
        zP:function(num){..},
        KP:function(num){..}
    }
    '''
    interpreter = JSInterpreter(js_code)
    extracted_obj = interpreter.extract_object('WJIS')
    assert extracted_obj == {
        'zP': None,
        'KP': None
    }


# Generated at 2022-06-14 17:49:12.651579
# Unit test for method call_function of class JSInterpreter
def test_JSInterpreter_call_function():
    my_js_interpreter = JSInterpreter(open('my_file').read())
    assert my_js_interpreter.call_function('my_func', 0, 1, 2) == 3



# Generated at 2022-06-14 17:49:18.558856
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    code = """
    function a() {
        var g = function() {
            this.b = function() {
                return 'b';
            };
            this.c = 'c';
        };
        return new g();
    }
    """
    interpreter = JSInterpreter(code)
    obj = interpreter.extract_object("g")
    assert obj["c"] == 'c'
    assert obj["b"]() == 'b'


if __name__ == '__main__':
    test_JSInterpreter_extract_object()

# Generated at 2022-06-14 17:49:28.590878
# Unit test for method interpret_expression of class JSInterpreter

# Generated at 2022-06-14 17:49:35.492181
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    js = JSInterpreter('', {})
    func = js.build_function(['a', 'b'], 'a + b;')
    result = func((3, 5))
    assert 8 == result
    func = js.build_function(['a'], 'return a * 2;')
    result = func((4,))
    assert 8 == result


# Generated at 2022-06-14 17:49:45.914261
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    code1 = '''
        var obj = {
            a: function() { return 1; },
            b: function(c, d) { return c + d },
            e: 4
        };
    '''
    js = JSInterpreter(code1)
    obj = js.extract_object('obj')
    assert obj == {'a': lambda: 1, 'b': lambda c, d: c + d, 'e': 4}
    assert obj['a']() == 1
    assert obj['b'](2, 3) == 5
    assert obj['e'] == 4


# Generated at 2022-06-14 17:49:55.404305
# Unit test for method call_function of class JSInterpreter
def test_JSInterpreter_call_function():
    # A simple function
    code = '''
        function f(a, b) {
            return a + b;
        }
    '''
    jsinter = JSInterpreter(code, {})
    assert jsinter.call_function('f', 1, 2) == 3

    # A simple function with an array
    code = '''
        function f(a, b) {
            return a[0] + b;
        }
    '''
    jsinter = JSInterpreter(code, {})
    assert jsinter.call_function('f', [1,2,3], 2) == 3

    # A function with an object variable
    code = '''
        var obj = {a: 1};
        function f(b) {
            return obj.a + b;
        }
    '''
    jsinter

# Generated at 2022-06-14 17:50:08.650993
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    with open('tests/test.js') as file:
        data = file.read()
    regex = '''\s*(?P<name>[a-zA-Z$][a-zA-Z0-9$]*)\s*\(\s*(?P<args>[a-zA-Z0-9,$]*)\)\s*{(?P<code>[^{}]*)}\s*'''
    for func_m in re.finditer(regex, data):
        name = func_m.group('name')
        args = func_m.group('args').split(',')
        code = func_m.group('code')
        print(name)
        print(args)
        print(code)
        js_interpreter = JSInterpreter(data)
        f = js_inter

# Generated at 2022-06-14 17:50:56.513205
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    # Test 1
    print("Test 1: ")
    code = """
    var key_func={
        a: function(p){return p},
        b: function(p){},
        c: function(){}
    };
    var key_func_empty={};
    var key_func_not_exists={
        d: function(){}
    };
    """
    interpreter = JSInterpreter(code)
    print("Key Func1: " + str(interpreter.extract_object("key_func")))
    print("Key Func Empty: " + str(interpreter.extract_object("key_func_empty")))
    print("Key Func Not Exists: " + str(interpreter.extract_object("key_func_not_exists")))
    # Test 2
    print

# Generated at 2022-06-14 17:51:07.187444
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    expr = '27*a+b'
    expr_eval = {'a': 3, 'b':5}

    js_interpreter = JSInterpreter(None)
    result = js_interpreter.interpret_expression(expr, expr_eval)

    assert result == 42

    expr = '27 * a + b'
    result = js_interpreter.interpret_expression(expr, expr_eval)

    assert result == 42

    expr = '27*a+b'
    result = js_interpreter.interpret_expression(expr, expr_eval)

    assert result == 42

    expr = '27*a + b'
    result = js_interpreter.interpret_expression(expr, expr_eval)

    assert result == 42

    expr = '"test" + "test"'
    result = js_interpre

# Generated at 2022-06-14 17:51:17.346367
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    js_interp_test = JSInterpreter('''
        var obj = {
            obj2: {
                func1: function(x, y) {
                    var z = x + y;
                    return z;
                },
                func2: function(x, y) {
                    var z = x * y;
                    return z;
                }
            },

            func1: function(x, y) {
                var z = x + y;
                return z;
            },

            func2: function(x, y) {
                var z = x * y;
                return z;
            }
        };
        ''')

    # Adding two numbers
    assert js_interp_test.call_function('obj.func1', 2, 3) == 5
    # Multiplying two numbers
    assert js_inter

# Generated at 2022-06-14 17:51:28.437197
# Unit test for method extract_function of class JSInterpreter

# Generated at 2022-06-14 17:51:33.920475
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    jsinterpreter = JSInterpreter(None, None)
    jsinterpreter.build_function(['a'], 'a=a+1;return a')([2]) == 3
    jsinterpreter.build_function(['a', 'b', 'c'], 'var d=a+b+c;var e=d*2;return e')([1, 2, 3]) == 12
    jsinterpreter.build_function(['a', 'b'], r"""function x(a,b) { if (a==b) return 1; else return 0; }""")([2, 2]) == 1
    jsinterpreter.build_function(['a', 'b'], r"""function x(a,b) { return (a+b)*2; }""")([1, 2]) == 6
    jsinterpre

# Generated at 2022-06-14 17:51:46.842548
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    code = """
        var o={"doIt" : function(a,b){return b + (a.length === 0 ? "" : a[0]);}};
        var f=function(a,b){return b + (a.length === 0 ? "" : a[0]);};
        var g=function(a,b){return b + (a.length === 0 ? "" : a[0]);};
        var h=function(){return [1,2,3].splice(1,1);};"""
    i = JSInterpreter(code)

# Generated at 2022-06-14 17:51:54.778749
# Unit test for method extract_object of class JSInterpreter

# Generated at 2022-06-14 17:52:07.874500
# Unit test for method extract_function of class JSInterpreter
def test_JSInterpreter_extract_function():
    import unittest
    import unittest.mock

# Generated at 2022-06-14 17:52:19.297722
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    print('testing interpret_expression')
    # TODO: only tested for youtube.com, needs to be updated for additional sites
    try:
        code = open('test/testcode.js').read()
    except FileNotFoundError:
        code = open('youtube_dl/test/testcode.js').read()
    objects = {
        'null': None,
        'true': True,
        'false': False,
    }
    interpreter = JSInterpreter(code, objects)

    # Test equality of expressions
    f = open('test/expressions.txt')
    expressions = f.read().splitlines()
    f.close()
    for e in expressions:
        e = e.strip().split('=')
        if len(e) < 2:
            continue
        expected = e[1].strip()

# Generated at 2022-06-14 17:52:30.944791
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    interpreter = JSInterpreter('')
    assert interpreter.interpret_expression('1+1') == 2
    assert interpreter.interpret_expression('1+1+1') == 3
    assert interpreter.interpret_expression('1+2*2') == 5
    assert interpreter.interpret_expression('1+(2*2)') == 5
    assert interpreter.interpret_expression('(1+2)*2') == 6
    assert interpreter.interpret_expression('(1+2)*3') == 9
    assert interpreter.interpret_expression('abs(-5)') == 5
    assert interpreter.interpret_expression('(1+2)*(4-2)') == 6
    assert interpreter.interpret_expression('(((1+2)))*(((4-2)))') == 6
    assert interpreter.interpret_expression('1+1*3+1') == 5
    assert interpreter

# Generated at 2022-06-14 17:52:58.256664
# Unit test for method extract_function of class JSInterpreter

# Generated at 2022-06-14 17:53:04.292829
# Unit test for method extract_object of class JSInterpreter

# Generated at 2022-06-14 17:53:08.982693
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    assert JSInterpreter.interpret_expression(
        '((function(){return "abc";})())', {}, 100) == 'abc'
    assert JSInterpreter.interpret_expression(
        '((function(){return "abc";})())', {}, 100) == 'abc'
    assert JSInterpreter.interpret_expression(
        '((function(){return "abc";})())', {}, 100) == 'abc'


if __name__ == '__main__':
    import sys
    test_JSInterpreter_interpret_expression()
    sys.exit(0)

# Generated at 2022-06-14 17:53:11.344460
# Unit test for method call_function of class JSInterpreter
def test_JSInterpreter_call_function():
    # TODO: implement test
    return True


# Generated at 2022-06-14 17:53:14.624308
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    interpreter = JSInterpreter('')
    run = interpreter.build_function(["argname"], "return argname;")
    assert 'test' == run(['test'])


# Generated at 2022-06-14 17:53:26.162403
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    js_interpreter = JSInterpreter('')

    def test_interpret_expression(js_interpreter, expr, expected_value):
        if isinstance(expected_value, list):
            varnames = expected_value.pop(0)
            expected_value = expected_value[0]
            local_vars = {k: v for k, v in zip(varnames[0::2], varnames[1::2])}
        else:
            local_vars = {}
        res = js_interpreter.interpret_expression(expr, local_vars)
        assert res == expected_value

    # test integer
    test_interpret_expression(
        js_interpreter,
        '1234',
        1234)

    # test float

# Generated at 2022-06-14 17:53:31.727965
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    objname = 'Foo'
    js = '%s = {baz: function(a, b) {return a + b;}, bar: function(){return 1;}};' % objname
    interpreter = JSInterpreter(js)
    obj = interpreter.extract_object(objname)
    assert obj['baz'](2, 3) == 5


# Generated at 2022-06-14 17:53:43.506307
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    js_interpreter = JSInterpreter(None)
    # Basic function call
    assert js_interpreter.interpret_expression('f') is None
    # Basic variable assignment
    assert js_interpreter.interpret_expression('x=100') == 100
    assert js_interpreter.interpret_expression('x') == 100
    # Test string
    assert js_interpreter.interpret_expression("'abc'") == 'abc'
    # Test string concatenation
    assert js_interpreter.interpret_expression("'ab' + 'c'") == 'abc'
    # Test string concatenation with number
    assert js_interpreter.interpret_expression("'ab' + 1") == 'ab1'
    # String member access

# Generated at 2022-06-14 17:53:49.207878
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    jsinter = JSInterpreter('function f(a, b) {return a + b;}')
    f = jsinter.build_function(['a', 'b'], 'return a + b')
    assert f([3, 4]) == 7
    # TODO: Add more test cases for the method build_function()


# Generated at 2022-06-14 17:53:56.538294
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    code = '''
    function get_url(a,b,c) {
        var d = {
            e:"f",
            g:"h",
            i:"/j/k"
        };

        return d.e + a + b + c + d.g + d.i;
    }
    '''
    js_interpreter = JSInterpreter(code)
    get_url = js_interpreter.extract_function('get_url')
    assert get_url(('1','2','3')) == 'f12/j/kh'

# Generated at 2022-06-14 17:54:22.973876
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    objects = {'location': dict(href='http://www.example.com')}

# Generated at 2022-06-14 17:54:27.170071
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    code = """
        var a1 = 5;
        var b1 = 10;
        var result = a1 + b1;
    """
    js_interpreter = JSInterpreter(code)
    assert js_interpreter.interpret_expression('result;') == 15

# Generated at 2022-06-14 17:54:35.726846
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    code = "var test = 'test'; var gC=''; var test2=10; function f(arg1,arg2){ gC='gC'; return test + ' ' + arg1 + ' ' + arg2; }"
    interpreter = JSInterpreter(code)
    assert(interpreter.build_function(["arg1","arg2"], "gC='gC'; return test + ' ' + arg1 + ' ' + arg2")(["1", "2"]) == "test 1 2")


# Generated at 2022-06-14 17:54:41.276599
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    js_interpreter = JSInterpreter("f = function(name, flv_url){return flv_url;}")
    assert js_interpreter.build_function(["name", "flv_url"], "return flv_url;")(['a', 'b']) == 'b'
    assert js_interpreter.call_function("f", "a", "b") == 'b'



# Generated at 2022-06-14 17:54:50.493088
# Unit test for method interpret_statement of class JSInterpreter
def test_JSInterpreter_interpret_statement():
    assert JSInterpreter(code='').interpret_statement('var x = "hello";', {}) == ("hello", False)
    assert JSInterpreter(code='').interpret_statement('return "hello";', {}) == ('hello', True)
    assert JSInterpreter(code='').interpret_statement('"hello";', {}) == ('hello', False)
    assert JSInterpreter(code='').interpret_statement('"hello"; return "world";', {}) == ('hello', False)


# Generated at 2022-06-14 17:54:52.633131
# Unit test for method call_function of class JSInterpreter
def test_JSInterpreter_call_function():
    js_interpreter = JSInterpreter('function get_a(b) { return b; }')

    assert js_interpreter.call_function('get_a', 10) == 10

# Generated at 2022-06-14 17:55:01.492003
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    js = '''
    var a = 12;
    var b = 34;
    var c = 56;
    function test(arg1, arg2, arg3){
        c = a + b + arg1 + arg2 + arg3;
        return c;
    }
    '''
    interpreter = JSInterpreter(js)
    funcname = 'test'
    code = '''
        c = a + b + arg1 + arg2 + arg3;
        return c;
    '''
    argnames = ['arg1', 'arg2', 'arg3']
    f = interpreter.build_function(argnames, code)
    assert f([9, 3, 8]) == 12 + 34 + 9 + 3 + 8



# Generated at 2022-06-14 17:55:07.924843
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    code = '''
        n = {
            split: function(a) {},
            reverse: function() {},
            charCodeAt: function(x) {return 97},
            slice: function(x) {},
            join: function(x) {}
        }
    '''
    jsi = JSInterpreter(code=code, objects={'n': [1, 2, 3]})
    assert jsi.interpret_expression('n.length', {}) == 3
    assert jsi.interpret_expression('n.reverse()', {}) == [3, 2, 1]
    assert jsi.interpret_expression('n.slice(1)', {}) == [2, 3]
    assert jsi.interpret_expression('n[1]', {}) == 2

# Generated at 2022-06-14 17:55:18.205162
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    code = r'''
        var tvehb = {
            rV: function (a) {
                return a;
            },
            KfvR: function (a) {
                return a;
            }
        };
    '''
    i = JSInterpreter(code)
    obj = i.extract_object('tvehb')

    assert len(obj) == 2
    assert obj['rV']('x') == 'x'
    assert obj['KfvR']('x') == 'x'

test_JSInterpreter_extract_object()



# Generated at 2022-06-14 17:55:25.963680
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    js_code = r"""
        var a = 'hello';
        var b = 'world';
        var c = '=';
        var d = '"';
        var e = '"';
        var f = a+' '+b+' '+c+' '+d+a+' '+b+e;
        var g = function () {return f;};
        return g();
    """
    assert (JSInterpreter(js_code).interpret_expression('g()')
            == 'hello world = "hello world"')
    assert (JSInterpreter(js_code).interpret_expression('a') == 'hello')

# Generated at 2022-06-14 17:55:55.660721
# Unit test for method call_function of class JSInterpreter
def test_JSInterpreter_call_function():
    # input
    code = '''
    d.set("timestamp", 1415723475);
    d.set("formats", [{"url": "asdf"}]);
    '''
    interpreter = JSInterpreter(code)
    formats_response = interpreter.call_function("d.set", "timestamp", 1415723475)
    print(formats_response)
    assert formats_response == None
    formats_response = interpreter.call_function("d.set", "formats", [{"url": "asdf"}])
    print(formats_response)
    assert formats_response == None

if __name__ == '__main__':
    test_JSInterpreter_call_function()

# Generated at 2022-06-14 17:56:01.715727
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    js = JSInterpreter('', {})
    assert js.build_function([], '1')() == 1

    # Test for normal functions
    js = JSInterpreter('', {})
    code = '''var n = 2;
    var m = 1;
    var k = 'some';
    n + m + k;
    '''
    assert js.build_function([], code)() == '3some'

    # Test for function objects
    js = JSInterpreter('', {})
    code = '''
    var k = 'some';
    var o = {'test': function () {this.k + 1;}};
    o.test();
    '''
    assert js.build_function([], code)() == 'some1'

    # Test for normal functions with arguments
    js = JSInterpre

# Generated at 2022-06-14 17:56:13.434308
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    # Test case 1
    # Javascript code: a = 2
    js = JSInterpreter('''a = 2''')
    local_vars = {}
    res = js.interpret_expression('a', local_vars, 100)
    assert res == 2

    # Test case 2
    # Javascript code: a = a + 1
    js = JSInterpreter('''a = a + 1''')
    local_vars = {}
    js.interpret_expression('a', local_vars, 100)
    assert local_vars['a'] == 1

    # Test case 3
    # Javascript code: a = 2; b = 2; b = b + 1; c = { 'a': a, 'b': b }

# Generated at 2022-06-14 17:56:25.759117
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    js = '''
        function foo(a, b) {
            return a + b;
        }
    '''
    js_interpreter = JSInterpreter(js)
    assert js_interpreter.call_function('foo', 1, 2) == 3

    js = '''
        function foo(a, b, c) {
            return (a + b) * c;
        }
    '''
    js_interpreter = JSInterpreter(js)
    assert js_interpreter.call_function('foo', 1, 2, 3) == 9

    js = '''
        function foo(a, b) {
            var c = a + b;
            var d = b - a;
            return c * d;
        }
    '''
    js_interpreter = JSInterpreter

# Generated at 2022-06-14 17:56:38.482757
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    jsi = JSInterpreter('')
    assert jsi.interpret_expression('1', {}) == 1
    assert jsi.interpret_expression('x', {'x': 2}) == 2
    assert jsi.interpret_expression('x[0]', {'x': [2]}) == 2
    assert jsi.interpret_expression('x.length', {'x': [2, 3]}) == 2
    assert jsi.interpret_expression('x[1]', {'x': ['a', 2]}) == 2
    assert jsi.interpret_expression('x.join(",")', {'x': ['a', 'b', 'c']}) == 'a,b,c'

# Generated at 2022-06-14 17:56:50.168457
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    def test_dict_methods(interpreter, obj_name, obj, methods):
        for method, argspec, result in methods:
            if argspec is None:
                assert interpreter.interpret_expression(
                    '%s.%s' % (obj_name, method), {}) == result
            else:
                args = ', '.join(['%s' % arg for arg in argspec])
                assert interpreter.interpret_expression(
                    '%s.%s(%s)' % (obj_name, method, args), {}) == result


# Generated at 2022-06-14 17:56:57.153543
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    code_chrumkrummenie = '''
    function chrumkrummenie() {
        chrum = {};
        chrum.reverse = function(){};
        chrum.splice = function(){};
        chrum.length = 0;
    }
    '''
    code_func_f = '''
        var f = function(){};
        f.reverse = function(){};
        f.splice = function(){};
        f.length = 0;
    '''
    code_func_g = '''
        var g = function(a,b,c){return "abra" + a + b + c;};
    '''
    code_functio_h = '''
        function h(a,b,c){return "abra" + a + b + c;};
    '''
    code

# Generated at 2022-06-14 17:57:06.102219
# Unit test for method interpret_expression of class JSInterpreter

# Generated at 2022-06-14 17:57:14.512119
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    jsinterp = JSInterpreter(None)
    assert jsinterp.interpret_expression('1 + 1') == 2
    assert jsinterp.interpret_expression('1 + 1 + 2') == 4
    assert jsinterp.interpret_expression('3 * 3') == 9
    assert jsinterp.interpret_expression('3 * 3 * 2') == 18
    assert jsinterp.interpret_expression('3 * 0') == 0
    assert jsinterp.interpret_expression('9 / 3') == 3
    assert jsinterp.interpret_expression('2 + 3 * 3') == 11
    assert jsinterp.interpret_expression('2 + 3 * 3 * 2') == 22
    assert jsinterp.interpret_expression('(2 + 3) * 3') == 15

# Generated at 2022-06-14 17:57:19.724674
# Unit test for method call_function of class JSInterpreter
def test_JSInterpreter_call_function():
    js_interpreter = JSInterpreter("""(function() {
  var a = 'foo', b = 'bar';
  return '' + a + b;
})();""")
    assert js_interpreter.call_function('anonymous') == 'foobar'
