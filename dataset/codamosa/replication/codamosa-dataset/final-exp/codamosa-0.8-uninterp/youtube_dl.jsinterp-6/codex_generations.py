

# Generated at 2022-06-14 17:49:01.422494
# Unit test for method interpret_expression of class JSInterpreter

# Generated at 2022-06-14 17:49:10.415372
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    code = '''
        var b = true;
        var c = false;
        var d = true;
        var k = false;
        var t = "true";
        var f = "false";
        var r = "true";
        var v = "false";
        var a = b^c;
        var e = d^k;
        var i = t^f;
        var j = r^v;
        var h = a^e;
        var g = i^j;
        var l = h^g;
    '''
    js = JSInterpreter(code)
    assert js.interpret_expression('a', {}) is True
    assert js.interpret_expression('e', {}) is True
    assert js.interpret_expression('i', {}) == 'true^false'
    assert js.interpret_

# Generated at 2022-06-14 17:49:17.212672
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    interpreter = JSInterpreter('code')
    func = interpreter.build_function(['a','b','c'], 'a+b')
    assert func([1, 2, 3]) == 3
    func = interpreter.build_function(['a','b','c'], 'a+b;c+b;return b;')
    assert func([1, 2, 3]) == 2
    func = interpreter.build_function(['a','b','c'], 'var d = 1;return d;')
    assert func([1, 2, 3]) == 1
    func = interpreter.build_function(['a','b','c'], 'return a+b+c;')
    assert func([1, 2, 3]) == 6
    func = interpreter.build_function(['a','b','c'], 'b+c;return a;')


# Generated at 2022-06-14 17:49:24.993794
# Unit test for method extract_function of class JSInterpreter
def test_JSInterpreter_extract_function():
    s = JSInterpreter("var name='value'; var array = ['value1', 'value2']; function functionName(arg1, arg2){ var local = 'value'; return local + (arg1+arg2); };")
    f = s.extract_function("functionName")
    assert isinstance(f, types.FunctionType)
    assert f(("value3", "value4")) == "valuevalue7"

# Generated at 2022-06-14 17:49:36.763331
# Unit test for method extract_function of class JSInterpreter

# Generated at 2022-06-14 17:49:45.147327
# Unit test for method interpret_statement of class JSInterpreter
def test_JSInterpreter_interpret_statement():
    jsint = JSInterpreter('', {})

# Generated at 2022-06-14 17:49:53.953376
# Unit test for method call_function of class JSInterpreter
def test_JSInterpreter_call_function():
    js_line = "f('a',b,'c')"
    js_line = js_line.replace('\\', '\\\\')
    js_line = js_line.replace('\'', '\\\'')
    js_code = "function f(x,y,z){return x+y+z;}"
    interpreter = JSInterpreter(js_code)
    res = interpreter.call_function('f', 'a','b','c')
    assert res == 'abc'
    res = interpreter.call_function('f', 'a','b','d')
    assert res == 'abd'

if __name__ == '__main__':
    test_JSInterpreter_call_function()

# Generated at 2022-06-14 17:50:06.482599
# Unit test for method extract_object of class JSInterpreter

# Generated at 2022-06-14 17:50:15.548321
# Unit test for method interpret_statement of class JSInterpreter
def test_JSInterpreter_interpret_statement():
    code = '''
        var a = 0;
        var b = 1;
        var c = "2";
        var d = [3, 4];
        var e = {"5": 5};
        var f = {"6": 6, "7": 7, "8": [8, 9]};

        var g = function() {
            var h = function() { return 10; };
            return h();
        }

        function i(j) {
            return j + 11;
        }

        function k(l, m) {
            m = m || 12;
            return l + m;
        }
    '''

    jsi = JSInterpreter(code)

# Generated at 2022-06-14 17:50:21.135442
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    test_code = '''
        var a = {
            a: function(c, d) {
                return c + d
            }
        }
    '''
    interpreter = JSInterpreter(test_code)
    test_object = interpreter.extract_object('a')
    assert test_object['a'](1, 2) == 3

# Generated at 2022-06-14 17:50:40.911820
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    js_interpreter = JSInterpreter('')

    # Test 1
    funcname = 'a'
    argnames = ['b', 'c']
    code = 'd=5;e=c;f=b'
    args = [1, 2]
    local_vars = dict(zip(argnames, args))
    f = js_interpreter.build_function(funcname, argnames, code)
    assert f.__name__ == funcname
    assert f(args) == 2
    assert local_vars == {'b': 1, 'c': 2, 'd': 5, 'e': 2, 'f': 1}

    # Test 2
    funcname = 'func'
    argnames = ['a', 'b', 'c']
    code = 'a; var b = 10; return c;'

# Generated at 2022-06-14 17:50:54.454482
# Unit test for method interpret_statement of class JSInterpreter
def test_JSInterpreter_interpret_statement():
    # test the return statement
    interpreter = JSInterpreter('var a = 50;return a;')
    assert interpreter.interpret_statement('return a', {}) == 50

    # test the if statement
    interpreter = JSInterpreter('''
                                var a = true;
                                if (a) {
                                    return "a";
                                }
                                ''')
    assert interpreter.interpret_statement('', {}) == 'a'

    # test the while loop statement
    interpreter = JSInterpreter('''
                                var i = 10;
                                var a = 0;
                                while(i >= 0) {
                                    a = a + 1;
                                    i = i - 1;
                                }
                                return a;
                                ''')

# Generated at 2022-06-14 17:51:04.963615
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    interpreter = JSInterpreter('''a="a"; b="b"; c=["a","b", "c"]; a3=3;''', {'a': 'ad', 'b': 'bd', 'c': ['c1', 'c2']})
    assert interpreter.interpret_expression('''"a"''', {}) == interpreter.interpret_expression('''a''', {}) == 'ad'
    assert interpreter.interpret_expression('a+b', {}) == 'adbd'
    assert interpreter.interpret_expression('a+a', {}) == 'adad'
    assert interpreter.interpret_expression('a+a+a', {}) == 'adadad'
    assert interpreter.interpret_expression('a+a+a+b', {}) == 'adadadbd'

# Generated at 2022-06-14 17:51:14.835405
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    code = '''
        function a() {
            var b = 20
            return b + b1
        }
        var b1 = {
            a: function(arg1, arg2) {
                return arg1 - arg2 + b
            },
            b: function(arg1, arg2) {
                return arg1 * arg2 + b
            }
        }
    '''
    jsi = JSInterpreter(code)
    assert jsi.extract_object('b1') == {
        'a': lambda arg1, arg2: arg1 - arg2 + 20,
        'b': lambda arg1, arg2: arg1 * arg2 + 20
    }



# Generated at 2022-06-14 17:51:18.363452
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    # TODO
    return


if __name__ == '__main__':
    test_JSInterpreter_interpret_expression()
    print('Tests Successful...')

# Generated at 2022-06-14 17:51:27.897077
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    js = JSInterpreter("""
        var e="abcdefg";
        var a=1;
        var b=1.1;
        var c=true;
        var d=[1,2,"abc"];
        function myFun1(a,b){return a+b};
        function myFun2(a,b){return a-b};
        var obj1={
            f1:function(a,b){return a+b},
            f2:function(a,b){return a-b},
            f3:[1,2,3],
            f4:4
        };
        var obj2={
            f3:[4,5,6]
        };
    """)

# Generated at 2022-06-14 17:51:37.248503
# Unit test for method call_function of class JSInterpreter
def test_JSInterpreter_call_function():
    tests = [
        ("""
        function test(a,b){
            return a + b;
        }
        """,
         lambda a, b: a + b),
        ("""
        function test(a,b,c){
            return function(d){
                return a*b+c+d;
            }
        }
        """,
         lambda a, b, c: lambda d: a * b + c + d),
    ]
    for test in tests:
        js = JSInterpreter(test[0])
        f = test[1]
        print(f.func_name)
        assert js.call_function(f.func_name, *range(f.func_code.co_argcount)) == f(*range(f.func_code.co_argcount))


# Generated at 2022-06-14 17:51:44.757484
# Unit test for method extract_object of class JSInterpreter

# Generated at 2022-06-14 17:51:50.399463
# Unit test for method call_function of class JSInterpreter

# Generated at 2022-06-14 17:51:57.561961
# Unit test for method build_function of class JSInterpreter

# Generated at 2022-06-14 17:52:14.641757
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    jsi = JSInterpreter("""Object.create = function () {};""")
    f = jsi.build_function([""], """return 0;""")
    assert f([""]) == 0
    f = jsi.build_function(["a"], """return a;""")
    assert f([""]) == ""
    jsi = JSInterpreter("""var a = { b: { c: function () {} } };""")
    f = jsi.build_function([""], """return 0;""")
    assert f([{"h": "k"}]) == 0



# Generated at 2022-06-14 17:52:18.315944
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    func = '''function test_function(var1){
        var1 = 'test';
        return var1;
    }'''
    interpreter = JSInterpreter(func)
    result = interpreter.build_function(['var1'], func)
    assert result is not None
    assert result(['test']) == 'test'
    assert result(['test2']) == 'test'



# Generated at 2022-06-14 17:52:30.203356
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    js_code = """
    var v = {
        "d": function (b) {
            return function (c) {
                return function (a) {
                    if (!a) {
                        return b
                    }
                    return __LSJsonUtil__.stringify(a, b, c)
                }
            }
        }(function (c) {
            return c
        }),
        "e": function (a) {
            return a
        },
        "f": function (a, b) {
            return a + b
        }
    }
    """
    interpreter = JSInterpreter(js_code)
    obj = interpreter.extract_object('v')
    assert isinstance(obj, dict)
    assert len(obj) == 3
    assert obj['d']('a') == '"a"'

# Generated at 2022-06-14 17:52:42.734359
# Unit test for method call_function of class JSInterpreter
def test_JSInterpreter_call_function():
    obj_name = 'xQ_'
    code = '''
    var xQ_="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=";
    function b1(a) {
        if (null == a)return null;
        for (var c = "", b = 0; b < a.length; b++) {
            var e = a.charCodeAt(b),
                f = e >> 2,
                g = (3 & e) << 4 | e >> 4;
            c += xQ_.charAt(f) + xQ_.charAt(g)
        }
        return c
    }
    '''
    i = JSInterpreter(code)

# Generated at 2022-06-14 17:52:48.267167
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    js = JSInterpreter(
        '''function compile() {};
           test = {a: function(b) {}, c: function() {}};''')

    obj = js.extract_object('test')
    assert callable(obj['a'])
    assert callable(obj['c'])
    assert len(obj) == 2

# Generated at 2022-06-14 17:52:59.670123
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    js_interpreter = JSInterpreter('')
    assert js_interpreter.build_function(['a','b','c','d'], 'a + b + c + d')(tuple([1,2,3,4])) == 10
    assert js_interpreter.build_function(['a','b','c','d'], 'a + b + c + d')([1,2,3,4]) == 10
    assert js_interpreter.build_function(['a','b','c','d'], 'a + b + c + d')(1,2,3,4) == 10

if __name__ == '__main__':
    test_JSInterpreter_build_function()

# Generated at 2022-06-14 17:53:13.150961
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    interp = JSInterpreter(0)
    # Test for method interpret_expression for arithmetic operators
    assert interp.interpret_expression('1 + 2', {'a': 0}) == 3
    assert interp.interpret_expression('1 - 2', {'a': 0}) == -1
    assert interp.interpret_expression('1 * 2', {'a': 0}) == 2
    assert interp.interpret_expression('4 / 2', {'a': 0}) == 2
    assert interp.interpret_expression('4 % 2', {'a': 0}) == 0
    assert interp.interpret_expression('1 << 2', {'a': 0}) == 4
    assert interp.interpret_expression('1 >> 2', {'a': 0}) == 0

# Generated at 2022-06-14 17:53:25.096041
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    def assertEqualInterpretationExpression(code, expected):
        interpreter = JSInterpreter(code)
        actual = interpreter.interpret_expression(code, {})
        assert actual == expected

    assertEqualInterpretationExpression('"a".charCodeAt(0)', 97)
    assertEqualInterpretationExpression('"abc".charCodeAt(0)', 97)
    assertEqualInterpretationExpression('"abc".charCodeAt(1)', 98)
    assertEqualInterpretationExpression('"abc".charCodeAt(2)', 99)
    assertEqualInterpretationExpression('"abc".charCodeAt(3)', None)

    assertEqualInterpretationExpression('"abc".indexOf("")', 0)

# Generated at 2022-06-14 17:53:32.923988
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    js = '''
    function test(a, b, c) {
        var d = a + b + c;
        return d;
    }
    '''
    interp = JSInterpreter(js)
    f = interp.build_function(['a', 'b', 'c'], 'var d = a + b + c; return d')
    assert f((1, 2, 3)) == 6, "The function builded is not correct"


# Generated at 2022-06-14 17:53:40.658415
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    code = '''var testobj = {
        "first": function(arg1, arg2) {
            return arg1 + arg2;
        },
        "second": function(arg3, arg4) {
            return arg3 + arg4;
        }
    }'''
    obj = JSInterpreter(code).extract_object('testobj')
    assert obj["first"]([1, 2]) == 3
    assert obj["second"]([1, 2]) == 3



# Generated at 2022-06-14 17:54:14.291225
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    code = '''
        function foo(a,b,c) {
          var d = c[0];
          var e = a.g + d.h;
          return e;
        }
    '''
    interpreter = JSInterpreter(code, {'a': {'g': 2}, 'c': [{'h':1}], 'e': 0})
    assert interpreter.build_function(['a', 'b', 'c'], 'var d = c[0]; var e = a.g + d.h; return e;') == interpreter.extract_function('foo')

# Generated at 2022-06-14 17:54:21.029654
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    jsi = JSInterpreter('''
        var abp = 1, bcp = 2, a = [3, 4, 5];
        var test = function (a, b, c) {
            var d, e = 0;
            return ((e = bcp, a + b - c * d * abp + e), f())[1];
        }
        var f = function() {
            return "test";
        }
    ''')
    f = jsi.build_function(argnames=['a', 'b', 'c'], code='''
            var d, e = 0;
            return ((e = bcp, a + b - c * d * abp + e), f())[1];''')
    assert f([1,4,0]) == "test"


# Generated at 2022-06-14 17:54:32.067481
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    code = r'''
    var result = {
        key1: "value1",
        "key2": "value2",
        key3: function(arg1, arg2) {
            return arg1 + arg2;
        }
    }
    '''
    js_interpreter = JSInterpreter(code)
    assert js_interpreter.interpret_expression('"value1"', {}) == 'value1'
    assert js_interpreter.interpret_expression('result.key1', {}) == 'value1'
    assert js_interpreter.interpret_expression('result.key2', {}) == 'value2'
    assert js_interpreter.interpret_expression('result.key3', {}) == js_interpreter.call_function('result.key3')

# Generated at 2022-06-14 17:54:41.373163
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    inter = JSInterpreter('')

    global_vars = {}
    def alert(args):
        return args[0]
    inter._functions['alert'] = alert

    # Test
    f = inter.build_function(['a', 'b'], '''
        var tmp = a + b;
        alert(tmp);
        return "hello world";
        alert("test");
    ''')
    assert f((1, 2)) == 'hello world'
    assert global_vars['tmp'] is None

    # Test recursion
    f = inter.build_function(['a', 'b'], '''
        for (i = 0; i < 3; i++) {
            a++;
        }
        func();
        return "hello world";
    ''')

    def func():
        global global_v

# Generated at 2022-06-14 17:54:52.704893
# Unit test for method call_function of class JSInterpreter

# Generated at 2022-06-14 17:55:02.003090
# Unit test for method extract_object of class JSInterpreter

# Generated at 2022-06-14 17:55:05.397641
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    code = 'function func(a, b, c) { var d = a + b; var e = d + c; return e; }'
    js_interpreter = JSInterpreter(code)
    func = js_interpreter.build_function(['a', 'b', 'c'], 'var d = a + b; var e = d + c; return e;')
    return func([1, 2, 3]) == 6


# Generated at 2022-06-14 17:55:14.706287
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    local_vars = {}
    js = JSInterpreter("", objects={"a": 1})
    assert js.interpret_expression("a", local_vars) == 1
    assert js.interpret_expression("1", local_vars) == 1
    assert js.interpret_expression("1+1", local_vars) == 2
    assert js.interpret_expression("1+1+1", local_vars) == 3
    assert js.interpret_expression("a+1", local_vars) == 2
    assert js.interpret_expression("a+1+2", local_vars) == 4
    assert js.interpret_expression("a+1+2+3", local_vars) == 7
    assert js.interpret_expression("a+1-2+3", local_vars) == 3
    assert js.interpret_

# Generated at 2022-06-14 17:55:23.391976
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    code = '''
        abc = {
            "x": "y",
            "v": function(){console.log("test");},
            "lol": function(){}
        }
    '''
    e = JSInterpreter(code)
    obj = e.extract_object("abc")
    assert isinstance(obj, dict)
    assert obj['x'] == "y"
    assert isinstance(obj['v'], types.FunctionType)
    assert e.call_function("abc.v") == None
    assert isinstance(obj['lol'], types.FunctionType)
    assert e.call_function("abc.lol") == None
    return obj, e



# Generated at 2022-06-14 17:55:30.969966
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    code = """
    var a = {
        "b": function(p) {
            return function(q) {
                return function(r) {
                    return p + q - r;
                }
            }
        }
    };
    """
    js_interpreter = JSInterpreter(code)
    obj = js_interpreter.extract_object("a")
    assert obj["b"]("x")("y")("z") == "xy-z"


if __name__ == '__main__':
    test_JSInterpreter_extract_object()

# Generated at 2022-06-14 17:56:36.876860
# Unit test for method call_function of class JSInterpreter

# Generated at 2022-06-14 17:56:47.420055
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    test = JSInterpreter("function decode(a,c) { var b = a.split(\"\"); a = b.length; for (var d = \"\"; a--;) { var e = c[b[a]]; d += e ? e : b[a]}; return d };")
    func = test.build_function(["a","c"], "var b = a.split(\"\"); a = b.length; for (var d = \"\"; a--;) { var e = c[b[a]]; d += e ? e : b[a]}; return d ")

# Generated at 2022-06-14 17:56:56.304878
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():

    assert JSInterpreter(None).interpret_expression('1', {}) == 1
    assert JSInterpreter(None).interpret_expression('1+1', {}) == 2
    assert JSInterpreter(None).interpret_expression('1 + 1', {}) == 2
    assert JSInterpreter(None).interpret_expression('a = {}', {}) == {}
    assert JSInterpreter(None).interpret_expression('a = {}', {'a': 1}) == {}
    assert JSInterpreter(None).interpret_expression('a = 1', {'a': 1}) == 1
    assert JSInterpreter(None).interpret_expression('a = 1', {'a': 2}) == 1
    assert JSInterpreter(None).interpret_expression('a += 1', {'a': 1}) == 2

# Generated at 2022-06-14 17:57:05.613523
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    js_interpreter = JSInterpreter("""
!function() {
    return [{
        id: "1",
        method: "GET",
        rnd: Math.round(0 + Math.random() * 9e+9),
        sn: "",
        tn: "",
        w: "",
        x: ""
    }]
};
""")

    funcname = "return[{id:1,method:GET,rnd:Math.round(0+Math.random()*9e+9),sn:,tn:,w:,x:}];"
    argnames = ["args"]
    code = "{return[{id:1,method:GET,rnd:Math.round(0+Math.random()*9e+9),sn:,tn:,w:,x:}];}"

    build_function = js

# Generated at 2022-06-14 17:57:11.798318
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    code = '''
var a = {
  "b": function(p,a,c,k,e,d){
    return e;
  }
}
'''
    interpreter = JSInterpreter(code)
    obj = interpreter.extract_object('a')
    assert len(obj) == 1
    f = obj['b']
    assert f(0, 0, 0, 0, 'i am a test', 0) == 'i am a test'


# Generated at 2022-06-14 17:57:24.331918
# Unit test for method call_function of class JSInterpreter
def test_JSInterpreter_call_function():
    # Arrange
    code = """function f(a, b) {return a + b};
    """
    js_interpreter = JSInterpreter(code)
    f = lambda a, b: a + b
    testCases = []
    testCases.append({'funcname': 'f'})
    testCases.append({'funcname': 'f', 'inputArgs':(1,2), 'expectedArgs':(3,)})
    testCases.append({'funcname': 'f', 'inputArgs':(1,2), 'expectedArgs':(3,)})
    testCases.append({'funcname': 'f', 'inputArgs':(2,-2), 'expectedArgs':(0,)})

# Generated at 2022-06-14 17:57:28.884714
# Unit test for method call_function of class JSInterpreter
def test_JSInterpreter_call_function():
    code = '''
    ;(function(name, alias) {
        return name + alias;
    }('hello', 'world'));

    '''
    js_interpreter = JSInterpreter(code)
    assert js_interpreter.call_function('', 'hello', 'world') == 'helloworld'

    code = '''
    ;(function(name, alias) {
        return alias + name;
    }('hello', 'world'));

    '''
    js_interpreter = JSInterpreter(code)
    assert js_interpreter.call_function('', 'hello', 'world') == 'worldhello'



# Generated at 2022-06-14 17:57:38.464415
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    jsi = JSInterpreter('', {})
    function_to_test = '''
		var a = function(this, b, c) {
			return b + c + "," + this;
		}
		'''
    func = jsi.build_function(['this', 'b', 'c'], function_to_test.split('\n')[3])
    assert func(['this_value', 1, 3]) == "4,this_value"
    assert func([3, 1, '3']) == "13,3"
    assert func(['3', 1, 3]) == "4,3"
    assert func([3, '1', 3]) == "13,3"


# Generated at 2022-06-14 17:57:48.030728
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    # Set up the test environment
    code = '''
        var x = 1;
        var y = 2;
        var arr1 = [3, 4, 5];
        var arr2 = arr1;
        function truc(a) {
            var ab = 'ab';
            var c = {
                "ab": 'ab',
                "abc": ab + 'c',
                "abcd": function() {
                    c = 12;
                    return 'abcd';
                }
            }
            var b = c.abcd();
            return a + b;
        }
        var z = truc(x);
    '''
    local_vars = {'x': 0, 'y': 0, 'arr1': [], 'arr2': []}
    js_interpreter = JSInterpreter(code)
    

# Generated at 2022-06-14 17:57:53.919794
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    js_interpreter = JSInterpreter('')
    js_interpreter.build_function([], '')
    js_interpreter.build_function(['a'], 'a=1')
    js_interpreter.build_function(['a'], 'if(a==1){a=1}')
    js_interpreter.build_function(['a'], 'if(a==1){a=1}else{a=2}')
    js_interpreter.build_function(['a'], 'if(a==1){}else if(a==2){a=2}')
    js_interpreter.build_function(['a'], 'while(true){break}')
    js_interpreter.build_function(['a'], 'while(a==1){break}')
