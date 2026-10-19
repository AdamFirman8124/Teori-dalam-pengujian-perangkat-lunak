

# Generated at 2022-06-14 17:49:04.957533
# Unit test for method extract_function of class JSInterpreter
def test_JSInterpreter_extract_function():
    code = (
            "function abc(a, b, c){var a = 123; var b = 456;}"
            "function def(d, e, f){var d = 123; var e = 456;}"
            "function ghi(g, h, i){var g = 123; var h = 456;}"
    )
    js_interpreter = JSInterpreter(code)
    f_abc = js_interpreter.extract_function("abc")
    f_def = js_interpreter.extract_function("def")
    f_ghi = js_interpreter.extract_function("ghi")
    assert f_abc(("a", "b", "c")) == 456
    assert f_def(("d", "e", "f")) == 456
    assert f_gh

# Generated at 2022-06-14 17:49:14.968937
# Unit test for method extract_object of class JSInterpreter

# Generated at 2022-06-14 17:49:26.713560
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    def test(expr,local_vars,expected):
        js = JSInterpreter('test')
        actual = js.interpret_expression(expr,local_vars)
        # if actual != expected:
        print('actual : {0}'.format(actual))
        print('expected : {0}'.format(expected))
    expr = '1+2'
    local_vars = {}
    expected = 3
    test(expr,local_vars,expected)
    expr = '(3+5)/6'
    local_vars = {}
    expected = 1.5
    test(expr,local_vars,expected)
    expr = 'cmd.split("")'
    local_vars = {'cmd':'abcde'}
    expected = ['a','b','c','d','e']

# Generated at 2022-06-14 17:49:38.224078
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    # Test case 1
    html = '''
        <script type="text/javascript">
            ABCDEFG.ABCDEFG = {
                "fa": function(b) {
                    return b
                },
                "fc": function(b) {
                    return b.reverse()
                }
            }
        </script>
    '''
    expected_obj = {
        'fa': lambda b: b,
        'fc': lambda b: b.reverse(),
    }
    obj = JSInterpreter(html).extract_object('ABCDEFG.ABCDEFG')
    assert obj == expected_obj
    assert JSInterpreter(html, {'ABCDEFG.ABCDEFG': obj}).call_function('ABCDEFG.ABCDEFG.fa', 'abc') == 'abc'

# Generated at 2022-06-14 17:49:43.990004
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    code = 'function test_function(arg1, arg2) {return arg1 + arg2;};'
    jsinterpreter = JSInterpreter(code)
    f = jsinterpreter.build_function(['arg1', 'arg2'], 'return arg1 + arg2;')

    assert f([1, 1]) == 2
    assert f([1, 2]) == 3
    assert f([5, 1]) == 6

# Generated at 2022-06-14 17:49:54.028199
# Unit test for method interpret_statement of class JSInterpreter
def test_JSInterpreter_interpret_statement():
    assert JSInterpreter(None).interpret_statement('var a = false') == (False, False)
    assert JSInterpreter(None).interpret_statement('var a = true') == (True, False)
    assert JSInterpreter(None).interpret_statement('var a = !false') == (True, False)
    assert JSInterpreter(None).interpret_statement('var a = !!true') == (True, False)
    assert JSInterpreter(None).interpret_statement('var a = ~0') == (-1, False)
    assert JSInterpreter(None).interpret_statement('var a = -1') == (-1, False)
    assert JSInterpreter(None).interpret_statement('var a = -1.2') == (-1.2, False)

# Generated at 2022-06-14 17:50:00.405282
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    JSInterpreter = JSInterpreter('''
        var A = {a:function(b){return b;},
        b:function(c){return c+1;}};''')

    A = JSInterpreter.extract_object('A')
    assert A['a'](1) == 1
    assert A['b'](3) == 4


# Generated at 2022-06-14 17:50:11.852399
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    code = '''\
    function function1(var1) {
        return var1;
    }
    function function2(var2) {
        return var2;
    }
    var obj1 = {
        member1: function(var3) {
            return var3;
        },
        member2: "value2",
        member3: 3
    };
    var obj2 = {
        member4: function(var4, var5){
            return var4 + var5;
        },
        member5: function1,
        member6: function2,
        member7: {
            member8: function(var7) {
                return var7;
            },
            member9: "value9"
        }
    };
    '''
    interpreter = JSInterpreter(code)
    obj2 = interpreter

# Generated at 2022-06-14 17:50:21.552714
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    def assertEqual(**kwargs):
        assert kwargs['a'] == kwargs['b']
    js_code1 = '''
        .
        .
        .
        var A = function (arg1, arg2) {
            if (arg1 > 0) {
                return 1;
            } else {
                return -1;
            }
        };
        .
        .
        .
    '''

# Generated at 2022-06-14 17:50:24.985612
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    interpreter = JSInterpreter(None)
    func = interpreter.build_function(['a', 'b'], 'return a+b;')
    assert func((1, 2)) == 3
    func = interpreter.build_function(['a'], '''
    var b = a;
    return b - a;
    ''')
    assert func((7,)) == 0



# Generated at 2022-06-14 17:50:46.674303
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    # Test 1: test None
    js_interpreter = JSInterpreter('''
        var x = 0;
        var y = 0;
        x = y + null;
        y = null + y;
        y = x + y;
        y = y + x;
    ''')
    assert js_interpreter.interpret_expression('') is None
    assert js_interpreter.interpret_expression('  ') is None
    assert js_interpreter.interpret_expression('''
    ''') is None
    # Test 2: test int

# Generated at 2022-06-14 17:50:51.908468
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    interpreter = JSInterpreter('')
    func = interpreter.build_function(['a', 'b', 'c'], ';'.join([
        'var d = a + b + c',
        'var e = d + 3',
        'var f = d + e',
        'return f',
    ]))

    assert func(['1', '1', '1']) == 9

# Generated at 2022-06-14 17:51:02.071393
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    test_code = '''var x = {
        "a":function(){return 1;},
        "b":function(x, y){return x*y;},
        "c":function(x, y){return x*y;},
    };'''
    js_i = JSInterpreter(test_code)
    f = js_i.extract_function("x['a']")
    assert f() == 1
    f = js_i.extract_function("x.b")
    assert f((5,5)) == 25
    f = js_i.extract_function("x.c")
    assert f((5,5)) == 25


# Generated at 2022-06-14 17:51:14.525953
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    jsinterpreter = JSInterpreter('')
    def f1(a, b, c):
        return a * b * c
    def f2(a, b, c):
        return a * (b + c)
    def f3(a, b, c, d, e):
        return a * b * (c + d) * e

    for f in (f1, f2, f3):
        resf = jsinterpreter.build_function(f.__code__.co_varnames[:f.__code__.co_argcount], f.__code__.co_code)
        assert resf(*range(1, f.__code__.co_argcount + 1)) == f(*range(1, f.__code__.co_argcount + 1))

# Generated at 2022-06-14 17:51:26.480378
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    # test1
    code = [
        'function test1(a, b) {',
        '    var c, d;',
        '    c = d = a + b;',
        '    return c;',
        '};'
    ]
    jsi = JSInterpreter(code)
    test_func = jsi.build_function(['a', 'b'], '\n'.join(code))
    assert test_func(1, 2) == 3

    code = [
        'function test1(a, b) {',
        '    var c, d;',
        '    c = d = a + b;',
        '    return c;',
        '};'
    ]
    jsi = JSInterpreter(code)

# Generated at 2022-06-14 17:51:34.809691
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    jsinterpreter = JSInterpreter('')
    # code example from https://en.wikipedia.org/wiki/JavaScript
    test_code = '''
        var add = function(x, y) {
           return x + y;
        };
    '''
    func = jsinterpreter.build_function(['x', 'y'], test_code)
    assert func([1, 2]) == 3


# Generated at 2022-06-14 17:51:47.687781
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    assert JSInterpreter('', {}).interpret_expression('(b + b)', {'b':2}) == 4
    assert JSInterpreter('', {}).interpret_expression('a + a', {'a':2}) == 4
    assert JSInterpreter('', {}).interpret_expression('a(0)', {'a': [1,2,3]}) == 1
    assert JSInterpreter('', {}).interpret_expression('a.join("-")', {'a': [1,2,3]}) == '1-2-3'
    assert JSInterpreter('', {'a':[1,2,3]}).interpret_expression('a.join("-")', {}) == '1-2-3'
    assert JSInterpreter('', {}).interpret_expression('{a:1}["a"]', {})

# Generated at 2022-06-14 17:51:55.404434
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    js_code = '''
    var v1 = 5;
    var v2 = {'f': function(a, b){return a + b;}};
    var v3 = {'a': 1, 'b': 2, 'c': 3};
    var v4 = [v3, [{'x': 1}, {'x': 2}], {'d': 4, 'e': 5}];
    var v5 = [3, 4, 2, 1];
    var v6 = {'func': function(a, b){return a + b - 5}};
    '''
    js_interpreter = JSInterpreter(js_code)
    assert js_interpreter.interpret_expression('v1', {}) == 5

# Generated at 2022-06-14 17:52:07.968124
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():

    # method call_function for class JSInterpreter returns the result of
    # extracting a function from a javascript string and calling it with
    # arguments
    js_code_1 = (
        'var A = function() {'
        'var arg = "foo";'
        'var B = function() {'
        'var out = "bar";'
        'return out;'
        '};'
        'return arg;'
        '};')
    interpreter = JSInterpreter(js_code_1)
    output = interpreter.call_function('A')
    assert output == 'foo'

    # method call_function for class JSInterpreter returns the result of
    # extracting a function from a javascript string and calling it with
    # arguments

# Generated at 2022-06-14 17:52:19.396186
# Unit test for method interpret_statement of class JSInterpreter
def test_JSInterpreter_interpret_statement():
    code_1 = 'var my_var3 = "value"; my_var3'
    code_2 = 'var my_var1 = "value1"; var my_var2 = "value2"; my_var1 + my_var2'
    code_3 = 'var my_var1 = "value1"; var my_var2 = "value2"; my_var1 + my_var2 + "value3"'
    code_4 = 'my_var1=my_var1+"value3";return my_var1'
    code_5 = 'my_var1="value3"'
    code_6 = 'my_var1=my_var3.substring(5, 7)'
    code_7 = 'return my_var1'

    js_interpreter = JSInterpreter(code_1)
    local_v

# Generated at 2022-06-14 17:52:40.143838
# Unit test for method build_function of class JSInterpreter

# Generated at 2022-06-14 17:52:52.399633
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    js = JSInterpreter(r'var a = 5;')
    assert js.interpret_expression('a', {}) == 5
    js = JSInterpreter(r'var a = 5;')
    assert js.interpret_expression('a + 3', {}) == 8
    js = JSInterpreter(r'var a = 5;')
    assert js.interpret_expression('5 + 3', {}) == 8
    js = JSInterpreter(r'var a = [1, 2, 3];')
    assert js.interpret_expression('a', {}) == [1, 2, 3]
    js = JSInterpreter(r'var a = [1, 2, 3];')
    assert js.interpret_expression('a[1]', {}) == 2

# Generated at 2022-06-14 17:53:03.085170
# Unit test for method interpret_expression of class JSInterpreter

# Generated at 2022-06-14 17:53:14.002190
# Unit test for method interpret_expression of class JSInterpreter

# Generated at 2022-06-14 17:53:25.677918
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    print("")
    print("Testing interpret_expression()...")
    js_code = r"""e = function(a, b) {
        if (b == 0) {
          return 1;
        }
        return a * e(a, b - 1);
      }
      """
    interpreter = JSInterpreter(js_code)
    print("e(2, 3) = ", interpreter.interpret_expression("e(2, 3)", dict()))

    js_code = r"""function b(a) {
        var c = a.split(""),
            d = c.length,
            e = Math.floor(d / 2);
        c[e] = '*';
        var f = c.join("");
        return f;
      }
      """
    interpreter = JSInterpreter(js_code)
    print

# Generated at 2022-06-14 17:53:37.445628
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    test_obj = JSInterpreter(
        "return a;",
        {"a": "a", "b": "b", "c": "c"}
    )
    assert test_obj.interpret_expression("a", {"a": "a", "b": "b", "c": "c"}) == "a"
    assert test_obj.interpret_expression("b", {"a": "a", "b": "b", "c": "c"}) == "b"
    assert test_obj.interpret_expression("c", {"a": "a", "b": "b", "c": "c"}) == "c"
    assert test_obj.interpret_expression("a == 'a'", {"a": "a", "b": "b", "c": "c"}) == True

# Generated at 2022-06-14 17:53:48.850896
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    def test_interpret(js_code, dict_in, dict_out):
        JSInterpreter(js_code).interpret_expression(js_code, dict_in)
        assert dict_in == dict_out, "interpret_expression(%r, %r) should return %r instead of %r" % (js_code, dict_in, dict_out, dict_in)

    test_interpret("a[b]=1", {"a":{}, "b":2}, {"a":{2:1}, "b":2})
    test_interpret("a[b]=c", {"a":{}, "b":2, "c":3}, {"a":{2:3}, "b":2, "c":3})

# Generated at 2022-06-14 17:53:58.645399
# Unit test for method interpret_statement of class JSInterpreter
def test_JSInterpreter_interpret_statement():
    code = '''
        var a = 5;
        var b = "ab";
        var c = {
            "1": 1,
            bar: function(baz) {
                a = 7;
                return foo(baz);
            }
        };
        function foo(baz) {
            var r = a + baz;
            b = "cd";
            return r;
        }
    '''
    jsi = JSInterpreter(code)
    local_vars = {}
    v, _ = jsi.interpret_statement('a + 3', local_vars)
    assert v == 8

    local_vars = {'a': 1, 'b': 2}
    v, _ = jsi.interpret_statement('a + b', local_vars)
    assert v == 3

    local_

# Generated at 2022-06-14 17:54:04.910807
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    JSInterpreter_interpret_expression = JSInterpreter("", {}).interpret_expression
    assert JSInterpreter_interpret_expression("15+2", {}, 100) == 17
    assert JSInterpreter_interpret_expression("a", {"a": 3}, 100) == 3
    assert JSInterpreter_interpret_expression("a.b", {"a": {"b": "c"}}, 100) == "c"


# Generated at 2022-06-14 17:54:16.647408
# Unit test for method interpret_statement of class JSInterpreter
def test_JSInterpreter_interpret_statement():
    jsi = JSInterpreter('')
    assert jsi.interpret_statement('return 3;', {})[0] == 3
    assert jsi.interpret_statement('return var1;', {'var1': 4})[0] == 4
    assert jsi.interpret_statement('var1 = 3;', {})[0] == 3
    assert jsi.interpret_statement('var1 = 3;', {})[1] == False
    assert jsi.interpret_statement('return var1;', {})[1] == True

# Generated at 2022-06-14 17:54:50.905485
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    # Test variables
    code = '''
        var d=function(){};
        var c=function(){};
        var a=function(b){};
        var f={"a":function(){}};
        var e={"a":function(){}};
        a(b)//5;
        f.a()//2;
        e.a()//3;
        d()//1;
        c()//4;
    '''
    js_interpreter = JSInterpreter(code)

    # Test 1
    val = js_interpreter.interpret_expression('a', {'a': 1})
    assert val == 1

    # Test 2
    val = js_interpreter.interpret_expression('d', {'d': 1})
    assert val == 1

    # Test 3
    val = js_interpre

# Generated at 2022-06-14 17:55:01.932757
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    def assert_interpret_expression(jsi, expression, expected):
        actual = jsi.interpret_expression(expression, {})
        assert actual == expected
        print('JS expression {} correctly interpreted as {}'.format(
            expression, actual))

    print('Asking JSInterpreter to interpret expressions')
    jsi = JSInterpreter('')
    assert_interpret_expression(jsi, '', None)
    assert_interpret_expression(
        jsi, "a = '\\x3c'", '\\x3c')
    assert_interpret_expression(
        jsi, "a = '\\x3c'; (b = a + '\\x3e') + '\\x3e'", '<>')
    assert_interpret_expression(
        jsi, '(a + \',\') + b', '1,2')

# Generated at 2022-06-14 17:55:07.103743
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    interpreter = JSInterpreter(None)
    function = interpreter.build_function(['a', 'b'], 'a + b')
    assert function((1, 2)) == 3


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

# Generated at 2022-06-14 17:55:19.639887
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    interp = JSInterpreter('')
    assert interp.interpret_expression('5', {}) == 5
    assert interp.interpret_expression('5 + 5', {}) == 10
    assert interp.interpret_expression('5 * 5', {}) == 25
    assert interp.interpret_expression('5 + 5 * 5', {}) == 30
    assert interp.interpret_expression('(5 + 5) * 5', {}) == 50
    assert interp.interpret_expression('5 + 5 + 5', {}) == 15
    assert interp.interpret_expression('5 + 5 * 5 + 5', {}) == 35
    assert interp.interpret_expression('(5 + 5) * 5 + 5', {}) == 55
    assert interp.interpret_expression('(5 + 5) * (5 + 5)', {}) == 100
   

# Generated at 2022-06-14 17:55:31.486101
# Unit test for method interpret_statement of class JSInterpreter
def test_JSInterpreter_interpret_statement():
    js = JSInterpreter('')
    assert js.interpret_statement('11', {}) == (11, False)
    assert js.interpret_statement('11;22;', {}) == (22, False)
    assert js.interpret_statement('var a=10;', {}) == (None, False)
    assert js.interpret_statement('var b=(a+5)', {}) == (None, False)
    assert js.interpret_statement("""var b="a";if(a){b='c'}""", {}) == (None, False)
    assert js.interpret_statement("""var b=("a");if(a){b=("c")}""", {}) == (None, False)

# Generated at 2022-06-14 17:55:36.786600
# Unit test for method interpret_expression of class JSInterpreter

# Generated at 2022-06-14 17:55:47.682081
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    code = '''
        function foo(a, b) {
            var c = a + b;
            return c;
        }
    '''
    js_interpreter = JSInterpreter(code)
    assert js_interpreter.call_function('foo', 1, 2) == 3

    code = '''
        function foo(a, b) {
            var c = a + b;
            c += 100;
            return c;
        }
    '''
    js_interpreter = JSInterpreter(code)
    assert js_interpreter.call_function('foo', 1, 2) == 103

    code = '''
        function foo(a, b) {
            var c = a + b;
            c %= 3;
            return c;
        }
    '''
    js_

# Generated at 2022-06-14 17:55:59.000995
# Unit test for method interpret_expression of class JSInterpreter

# Generated at 2022-06-14 17:56:08.784348
# Unit test for method interpret_statement of class JSInterpreter
def test_JSInterpreter_interpret_statement():
    code = ''.join('''
        a = 12;
        var b = function() {
            return 3 + c;
        };
        b();
        var c = a + b();
        function func(one, two) {
            var tmp = "abcd";
            return tmp.split("").reverse().join("");
        }
        func(a, c);
    ''').strip()
    i = JSInterpreter(code)
    assert i.call_function('func', 12, 15) == 'dcba'

if __name__ == '__main__':
    from .jsinterpreter_test import test_JSInterpreter_interpret_expression
    test_JSInterpreter_interpret_expression()
    test_JSInterpreter_interpret_statement()

# Generated at 2022-06-14 17:56:17.855881
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    code = '''
        var a = "fldkv";
        var b = [1, 2 , [3, 4], "5"];
        var c = {
            "foo": "bar",
            "baz": function(){}
        };
        var d = function(x){
            return (x + 5);
        };
        function e(x, y) {
            return (x + y);
        }
        var f = [1, 2, 3];
        var g = 0;
        g = f.length;
    '''
    interpreter = JSInterpreter(code)


# Generated at 2022-06-14 17:57:25.757039
# Unit test for method interpret_statement of class JSInterpreter
def test_JSInterpreter_interpret_statement():
    import os
    import sys

    if sys.version_info.major == 3:
        unicode = str

    def unescape_b(s):
        # PY3 = sys.version_info.major == 3
        return s.encode('latin-1').decode('unicode-escape')

    def unescape_u(s):
        # PY3 = sys.version_info.major == 3
        return s.encode('ascii').decode('unicode-escape')

    data_dir = os.path.join(os.path.dirname(__file__), 'js_data')

    # test interpret_statement
    jsinterpreter = JSInterpreter(code='''
        var x = {}
        x['a'] = 0
        x['b'] = 1
    ''')
   

# Generated at 2022-06-14 17:57:32.553854
# Unit test for method interpret_statement of class JSInterpreter

# Generated at 2022-06-14 17:57:36.917166
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():

    for test, correct_output in dict(
            ['var a', None],
            ['var a; a', None],
            ['var a = 1 + 2 / 5 | Math.floor', 1],
            ['var a = 9, b = 3; a %= b', 0],
            ['var a = [1, 2]; a[0]', 1],
            ['var a = [1, 2, 3]; a.slice(1)', [2, 3]],
            ['var a = [1, 2, 3]; a.splice(1, 2)', [2, 3]]
    ).items():
        assert JSInterpreter(test).interpret_expression(test, {}) == correct_output


# Generated at 2022-06-14 17:57:47.985852
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    # Test array
    code = 'var p1=["abc",null,[123,456,7],0,"",{}];'

    # Test array.length
    assert JSInterpreter(code).interpret_expression('p1.length', {}) == 6
    # Test array[0]
    assert JSInterpreter(code).interpret_expression('p1[0]', {}) == 'abc'
    # Test array[1]
    assert JSInterpreter(code).interpret_expression('p1[1]', {}) == None
    # Test array[2]
    assert JSInterpreter(code).interpret_expression('p1[2]', {}) == [123, 456, 7]
    # Test array[3]
    assert JSInterpreter(code).interpret_expression('p1[3]', {}) == 0


# Generated at 2022-06-14 17:57:57.087932
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    code = '''
        g = "getElementById";
        d = document;
        a = xmlHttp = new ActiveXObject("Msxml2.XMLHTTP");

        s = f = "";
        q = "t=" + (new Date()).getTime() + "&";
        e = "/empty.html/" + Math.floor(Math.random() * 1000);
        a.open("GET", e, false);
        a.setRequestHeader("Content-Type", "application/x-www-form-urlencoded; charset=UTF-8");
        a.send(null);
        z = d[g]("ce");
    '''

    # extract function from code