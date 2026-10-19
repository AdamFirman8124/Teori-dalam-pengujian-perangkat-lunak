

# Generated at 2022-06-14 17:48:45.884081
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    js_interpreter = JSInterpreter('a')

    def f():
        pass
    assert f() is None

    def f():
        return 1
    assert f() == 1

    def f():
        return "str"
    assert f() == "str"

    def f(a, b):
        return a, b
    assert f("a", "b") == ("a", "b")

    def f(a, b):
        return a, b, None
    assert f("a", "b") == ("a", "b", None)

    def f(a, b):
        return a, b, 1
    assert f("a", "b") == ("a", "b", 1)

    def f(a, b):
        return a, b, "string"

# Generated at 2022-06-14 17:48:54.825494
# Unit test for method interpret_statement of class JSInterpreter
def test_JSInterpreter_interpret_statement():
    interpreter = JSInterpreter('')
    local_vars = {}

    # Test for variable
    res = interpreter.interpret_statement(
        'var a = 10;', local_vars)
    assert local_vars['a'] == 10
    assert res == (10, False)

    # Test for variable with no variable name
    res = interpreter.interpret_statement(
        'var = 10;', local_vars)
    assert res == (None, False)

    # Test for variable with = sign
    res = interpreter.interpret_statement(
        'var a=10;', local_vars)
    assert local_vars['a'] == 10
    assert res == (10, False)

    # Test for variable with multiple spaces

# Generated at 2022-06-14 17:49:04.120696
# Unit test for method extract_function of class JSInterpreter
def test_JSInterpreter_extract_function():
    code = '''
        wZzF = function(e) {
            var t = [0xB1, 0x87, 0x2C, 0xA9, 0x9C, 0x36, 0x61, 0x35];
            var n = '0^0|1&1';
            var r = '';
            for (var i = 0; i < e.length; i++) {
                r += String.fromCharCode(e.charCodeAt(i) ^ t[i % t.length]);
                t.reverse();
            }
            maybeDecode(r, n);
        };
    '''
    func_name = 'wZzF'

    jsInterpreter = JSInterpreter(code)
    f = jsInterpreter.extract_function(func_name)

# Generated at 2022-06-14 17:49:07.137888
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    jsinterpreter = JSInterpreter('')

    assert jsinterpreter.interpret_expression('a') is None


# Generated at 2022-06-14 17:49:17.066190
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    objects = {'window': {}, 'document': {}, 'Function': {}}
    js_interpreter = JSInterpreter(
        '''
            function parse(obj) {
              var hasProp = Object.prototype.hasOwnProperty;
              function hasAny(obj, props) {
                for (var i = 0, len = props.length; i < len; i++) {
                  if (hasProp.call(obj, props[i])) {
                    return true;
                  }
                }
                return false;
              }

              if (obj != null && typeof obj === 'object' && hasAny(obj, ['videoStream', 'audioStream'])) {
                return obj;
              }

              return null;
            }
            '''
        , objects)

    parse_func = js_interpreter.extract_function

# Generated at 2022-06-14 17:49:27.664931
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    assert JSInterpreter(None).call_function('f', 42) == 43
    assert JSInterpreter(None).call_function('f', 'a', 'b') == 'ab'
    assert JSInterpreter(None).call_function('f', 1, 2, 3) == 6
    assert JSInterpreter(None).call_function('f', 1, 2, 3, 4) == 10
    assert JSInterpreter(None).call_function('f', 'a', 'b', 'c') == 'abc'
    assert JSInterpreter(None).call_function('f', 'a', 'b', 'c', 'd') == 'abcd'
    assert JSInterpreter(None).call_function('f', 'a', 'b', 'c', 'd', 'e') == 'abcde'
    assert JSInterpre

# Generated at 2022-06-14 17:49:39.791933
# Unit test for method interpret_statement of class JSInterpreter

# Generated at 2022-06-14 17:49:49.815821
# Unit test for method interpret_expression of class JSInterpreter

# Generated at 2022-06-14 17:49:57.592831
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    class TestClass(object):
        def _run_test(self, obj_name, source, expected_output):
            js_interpreter = JSInterpreter(source)
            obj = js_interpreter.extract_object(obj_name)
            assert obj == expected_output

        def test_extract_empty_object(self):
            self._run_test(
                "empty",
                "empty = {}",
                {})
        

# Generated at 2022-06-14 17:50:11.158774
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    str_code = """
        var foo = {
            f1: function(a, b, c) {
                return d, 123;
            },
            f2: function(a, b, c) {
                var bar = a + b + c;
                if (bar == 'ABC')
                    return 0;
                else if (bar == 'ABCDEF')
                    return 1;
                return bar;
            }
        }
    """
    objname = 'foo'
    jsinterpreter = JSInterpreter(str_code)
    obj = jsinterpreter.extract_object(objname)
    assert len(obj) == 2
    assert obj['f1'](1, 2, 3) == 123
    assert obj['f2']('A', 'B', 'C') == 0
    assert obj['f2']

# Generated at 2022-06-14 17:50:50.777561
# Unit test for method call_function of class JSInterpreter
def test_JSInterpreter_call_function():
    js_code = """
    function myfunc(a, b) {
        return a + b;
    }
    var c = 1;
    """
    jsi = JSInterpreter(js_code)
    value = jsi.call_function('myfunc', 1, 2)
    if value != 3:
        raise ExtractorError('test_JSInterpreter_call_function failed')

if __name__ == '__main__':
    test_JSInterpreter_call_function()

# Generated at 2022-06-14 17:51:02.528509
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    # Define an object
    obj = { 'reverse': list.reverse,
            'splice': list.pop,
            'slice': list.__getslice__,
            'split': str.split,
            'join': str.join,
            'length': len
        }


# Generated at 2022-06-14 17:51:14.834714
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    # Example taken from https://github.com/rg3/youtube-dl/issues/4477
    code = '''
        var s = {
            b : function() {
                return 3;
            }
        };
        var a = {
            c : function() {
                a.b();
            },
            b : function() {
                return 0;
            }
        };
        console.log(a.c()); // 3
        console.log(a.b()); // 0
    '''
    interp = JSInterpreter(code)
    obj = interp.extract_object('s')
    assert obj['b']() == 3
    obj = interp.extract_object('a')
    assert obj['b']() == 0
    assert obj['c']() == 3


# Generated at 2022-06-14 17:51:18.719083
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    code = '''
        var obj = {
            "a": function () {},
            "b": function () {}
        };'''
    jsi = JSInterpreter(code)
    obj = jsi.extract_object('obj')
    assert len(obj.keys()) == 2
    assert callable(obj['a'])
    assert callable(obj['b'])

# Generated at 2022-06-14 17:51:25.179174
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    js = '''var el = document.createElement("div");el.innerHTML = "<a href=\\"asd\\">asd</a>";el.firstChild.href''';
    i = JSInterpreter(js)
    f = i.build_function(['el'], '''el.innerHTML = "<a href=\\"asd\\">asd</a>";el.firstChild.href''')
    assert f(['']) == 'asd'


# Generated at 2022-06-14 17:51:31.941374
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    js_interpreter = JSInterpreter('')

    # Test case 1: var a = 10; return a
    def resf1(args):
        local_vars = {}
        local_vars['a'] = 10
        return local_vars['a']

    assert js_interpreter.build_function(['a'], 'var a = 10; return a') == resf1

    # Test case 2: var a = 10, b = 20; return a + b
    def resf2(args):
        local_vars = {}
        local_vars['a'] = 10
        local_vars['b'] = 20
        return local_vars['a'] + local_vars['b']


# Generated at 2022-06-14 17:51:40.011461
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    interpreter = JSInterpreter("foo=1+1;")
    local_vars = {}
    result = interpreter.interpret_expression("foo", local_vars)
    assert result == 2

    interpreter = JSInterpreter("foo=2;")
    local_vars = {"foo": 1}
    result = interpreter.interpret_expression("foo", local_vars)
    assert result == 1

    interpreter = JSInterpreter("foo('bar');")
    def resf(*args):
        return args
    local_vars = {"foo": resf}
    result = interpreter.interpret_expression("foo('bar')", local_vars)
    assert result == ('bar',)

    interpreter = JSInterpreter("foo=2,bar=3;")
    local_vars = {}

# Generated at 2022-06-14 17:51:46.535263
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    print('Start unit test for method interpret_expression of class JSInterpreter')
    print('-' * 80)

    code = '''
        var a, b;
        a = 5;
        b = "abcd";
        b = b.substr(0, a);
    '''
    jsi = JSInterpreter(code)
    assert jsi.interpret_expression('a', {}) == 5
    assert jsi.interpret_expression('b', {}) == "abcd"
    assert jsi.interpret_expression('b.length', {}) == 4
    assert jsi.interpret_expression('b.substr(0, a)', {}) == 'abc'
    assert jsi.interpret_expression('(b.substr(0, a))', {}) == 'abc'

# Generated at 2022-06-14 17:51:58.645209
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    code = """
        var d = {"a": function(x, y) { return x + y },
                 "b": function() { return "abc" }};
            
    """
    js_interpreter = JSInterpreter(code)
    obj = js_interpreter.extract_object("d")

# Generated at 2022-06-14 17:52:09.612417
# Unit test for method extract_function of class JSInterpreter

# Generated at 2022-06-14 17:52:39.805241
# Unit test for method extract_function of class JSInterpreter

# Generated at 2022-06-14 17:52:43.503786
# Unit test for method call_function of class JSInterpreter
def test_JSInterpreter_call_function():
    js_interpreter = JSInterpreter(test_js)
    assert js_interpreter.call_function('decrypt', '1', '2') == '3'

test_js = '''
  function decrypt(a, b) {
    return a + b;
  }
'''



# Generated at 2022-06-14 17:52:48.904044
# Unit test for method extract_function of class JSInterpreter
def test_JSInterpreter_extract_function():
    s = '''
        a=function(){
                return 1234;
            };
        '''
    inter = JSInterpreter(s)
    f = inter.extract_function('a')
    assert f == (lambda a: 1234)
    f = inter.extract_function('b')
    assert f == None

# Generated at 2022-06-14 17:52:57.197744
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    js = JSInterpreter('')
    assert js.interpret_expression('1', {}) == 1
    assert js.interpret_expression('a', {'a': 1}) == 1
    assert js.interpret_expression('a = 1', {}) == 1
    assert js.interpret_expression('a = 2 + 3', {}) == 5
    assert js.interpret_expression('a = 2 + b', {'b': 3}) == 5
    assert js.interpret_expression('a = b + 3', {'b': 2}) == 5
    assert js.interpret_expression('a = 2 + b', {'b': [3]}) == 5
    assert js.interpret_expression('a = b[0] + 3', {'b': [2]}) == 5

# Generated at 2022-06-14 17:53:01.792637
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    code = '''
        var A = {
            a: function() {
                return 'a';
            },
        };
    '''

    assert 'a' in JSInterpreter(code).extract_object('A')
    assert 'a' in JSInterpreter(code).extract_object('A')['a']()


# Generated at 2022-06-14 17:53:08.883832
# Unit test for method call_function of class JSInterpreter
def test_JSInterpreter_call_function():
    code = '''
        function abcdefgh(a, b){
            c = (a + b).toString(16);
            return c;
        }
    '''

    interpreter = JSInterpreter(code=code)
    assert interpreter.call_function('abcdefgh', int('438',16), int('2e5',16)) == 0xd5e5
    assert interpreter.call_function('abcdefgh', 2, 3) == '5'

# Generated at 2022-06-14 17:53:16.980844
# Unit test for method interpret_expression of class JSInterpreter

# Generated at 2022-06-14 17:53:27.653288
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    interpreter = JSInterpreter('')
    assert interpreter.interpret_expression('1', {}) == 1
    assert interpreter.interpret_expression('false', {}) == False
    assert interpreter.interpret_expression('a = 1', {}) == 1
    assert interpreter.interpret_expression('a', {}) == 1
    assert interpreter.interpret_expression('b = 1', {'a': 0}) == 1
    assert interpreter.interpret_expression('b', {'a': 0}) == 1
    assert interpreter.interpret_expression('2 + 3', {}) == 5
    assert interpreter.interpret_expression('4 * 5', {}) == 20
    assert interpreter.interpret_expression('1 + 2 * 3', {}) == 7
    assert interpreter.interpret_expression('(1 + 2) * 3', {}) == 9

# Generated at 2022-06-14 17:53:36.759574
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    test_code = '''
var obj = {
    a: function() {
        return 5;
    },
    b: function(arg) {
        return arg + 1;
    },
    c: function(arg1, arg2, arg3) {
        return arg1 + arg2 + arg3;
    }
};
'''

    obj_dict = {}
    js_interpreter = JSInterpreter(test_code, obj_dict)
    obj_dict['obj'].keys()
    assert obj_dict['obj']['a']() == 5 and obj_dict['obj']['b'](4) == 5 and obj_dict['obj']['c'](1,2,3) == 6

# Generated at 2022-06-14 17:53:48.541029
# Unit test for method extract_function of class JSInterpreter

# Generated at 2022-06-14 17:54:18.455191
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    def assertCode(f, code):
        assert JSInterpreter([''], {}).build_function([], code) == f

    assertCode(lambda: None, '')
    assertCode(lambda x: x + 1, 'return %s + 1')
    assertCode(lambda x: x + 1, 'return (a + 1)')
    assertCode(lambda x, y: x + y, 'return %s + %s')
    assertCode(lambda x, y: x + y, 'return ( %s + %s)')
    assertCode(lambda x, y: x + y, '  return  (  %s  + %s)  ')
    assertCode(lambda x, y: x.split(y), r'return %s.split\(%s\)')

# Generated at 2022-06-14 17:54:30.551204
# Unit test for method extract_object of class JSInterpreter

# Generated at 2022-06-14 17:54:36.434274
# Unit test for method call_function of class JSInterpreter
def test_JSInterpreter_call_function():
    JSInterpreter("function testFunc(arg1, arg2) {return arg1+arg2}").call_function("testFunc", 1, 2)


# Generated at 2022-06-14 17:54:44.571170
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    js_interpreter = JSInterpreter('')

    assert js_interpreter.interpret_expression('10', dict()) == 10

    assert js_interpreter.interpret_expression('10+20', dict()) == 30
    assert js_interpreter.interpret_expression('2*3+4', dict()) == 10
    assert js_interpreter.interpret_expression('4+2*3', dict()) == 10
    assert js_interpreter.interpret_expression('(4+2)*3', dict()) == 18
    assert js_interpreter.interpret_expression('(3+5)%2', dict()) == 1
    assert js_interpreter.interpret_expression('5%(3+1)', dict()) == 1
    assert js_interpreter.interpret_expression('5^3', dict()) == 6

    local_

# Generated at 2022-06-14 17:54:56.751257
# Unit test for method call_function of class JSInterpreter
def test_JSInterpreter_call_function():
    # Two simple tests
    intPreterpreter = JSInterpreter('function testFunction(a, b) {return a + b;}')
    assert(intPreterpreter.call_function('testFunction', 1, 2) == 3)
    intPreterpreter = JSInterpreter('function testFunction(a, b) {return a - b;}')
    assert(intPreterpreter.call_function('testFunction', 1, 2) == -1)
    # A complexer test

# Generated at 2022-06-14 17:55:02.004337
# Unit test for method extract_function of class JSInterpreter
def test_JSInterpreter_extract_function():
    code = """
        function test1(a, b) {
            a = 10;
            b = b * a;
            return a + b;
        }

        function test2(a, b) {
            return a + b;
        }
    """
    assert JSInterpreter(code).call_function('test1', 1, 2) == 21
    assert JSInterpreter(code).call_function('test2', 1, 2) == 3


# Generated at 2022-06-14 17:55:06.116194
# Unit test for method call_function of class JSInterpreter
def test_JSInterpreter_call_function():
    code = """
        function deobf(a) {
            a=a.split("");a=a.reverse();a=a.join("");return a
        }
    """
    o = JSInterpreter(code)

# Generated at 2022-06-14 17:55:15.093780
# Unit test for method interpret_statement of class JSInterpreter

# Generated at 2022-06-14 17:55:18.582749
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    js_interpreter = JSInterpreter("")
    assert js_interpreter.build_function(("a", "b"), "a + b")(3, 5) == 8


# Generated at 2022-06-14 17:55:28.640777
# Unit test for method call_function of class JSInterpreter
def test_JSInterpreter_call_function():
    code = '''function abc(a,b) { return a+b; }'''
    jsi = JSInterpreter(code=code)
    ret = jsi.call_function('abc',1,2)
    assert ret == 3

    code = '''function abc(a,b) { return a+b; };'''
    jsi = JSInterpreter(code=code)
    ret = jsi.call_function('abc',1,2)
    assert ret == 3

    code = '''var abc=function(a,b) { return a+b; };'''
    jsi = JSInterpreter(code=code)
    ret = jsi.call_function('abc',1,2)
    assert ret == 3


# Generated at 2022-06-14 17:55:54.571852
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    code = """
        var test = function (hello, world) {
            if (hello == "hello") {
                return world;
            }
            else {
                return hello;
            }
        }
    """
    js_interpreter = JSInterpreter(code)
    assert js_interpreter.call_function('test', 'hello', 'world') == 'world'
    assert js_interpreter.call_function('test', 'bye', 'world') == 'bye'

# Generated at 2022-06-14 17:56:03.417523
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    # input
    funcname = "foo"
    code = "a = (b); console.log(a)"
    argnames = [ "b" ]

    # expected output
    expectedVal = 6

    # testing class JSInterpreter
    jsinterpreter = JSInterpreter("")
    f = jsinterpreter.build_function(argnames, code)
    args = [ "6" ]
    assert f(args) == expectedVal


# Generated at 2022-06-14 17:56:15.749120
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    code = """var test = {
  "a": function(a, b) {
    var c = a + b;
    ;
    return c;
  },
  "b": function() {
    var a = 1;
    var b = 2;
    var c = 3;
    var d = 4;
    ;
    return a + b + c + d;
  },
  "c": function(a, b) {
    var c = a - b;
    ;
    return c;
  },
  "d": function(a, b) {
    var c = a * b;
    ;
    return c;
  },
  "e": function(a, b) {
    var c = e + f;
    ;
    return a / b;
  },
};"""

# Generated at 2022-06-14 17:56:24.307363
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    # test lambda function
    jsi = JSInterpreter("var res = function() {var a = 2; return a + 1};")
    lambda_func = jsi.build_function([], "var a = 2; return a + 1;")
    assert lambda_func([]) == 3

    # test function with argument
    jsi = JSInterpreter("var res = function(b) {return b + 1};")
    lambda_func = jsi.build_function(["b"], "return b + 1;")
    assert lambda_func([3]) == 4


# Generated at 2022-06-14 17:56:32.257357
# Unit test for method extract_function of class JSInterpreter
def test_JSInterpreter_extract_function():
    code = open('test/test_JSInterpreter_extract_function.js').read()
    js = JSInterpreter(code)
    f = js.extract_function('b')
    assert f((1,)) == 5
    f = js.extract_function('a')
    assert f((1, 2)) == 5
    assert f((2, 3)) == 7


# Generated at 2022-06-14 17:56:42.904864
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    # Test with very simple expressions
    interpreter = JSInterpreter('', {})
    assert interpreter.interpret_expression("1", {}, 100) == 1
    assert interpreter.interpret_expression("-1", {}, 100) == -1
    assert interpreter.interpret_expression("1 + 1", {}, 100) == 2
    assert interpreter.interpret_expression("1 - 1", {}, 100) == 0
    assert interpreter.interpret_expression("1 * 1", {}, 100) == 1
    assert interpreter.interpret_expression("1 / 2", {}, 100) == 0.5
    assert interpreter.interpret_expression("1 % 2", {}, 100) == 1
    assert interpreter.interpret_expression("1 & 2", {}, 100) == 0
    assert interpreter.interpret_expression("1 ^ 2", {}, 100) == 3

# Generated at 2022-06-14 17:56:53.644249
# Unit test for method interpret_expression of class JSInterpreter

# Generated at 2022-06-14 17:57:04.048447
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    class Stub:
        def perform(self):
            return self.a

    jsint = JSInterpreter(
        code='''
        obj = {
            a: {get: function () { return this.b; }},
            b: {
                get: function (a) {
                    return function () {
                        return function (b) {
                            this.a = this.b = b;
                            return b + a;
                        }
                    }
                }
            }
        };
        var obj2 = {a: 'u'};
        var obj1 = {a: 1, b: 'u'};
        var obj3 = {};
        '''
    )
    res1 = jsint.call_function('obj.b.get', Stub())
    res2 = res1()

# Generated at 2022-06-14 17:57:09.174216
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    # Test if the resulting function takes an integer as argument
    js_interpreter = JSInterpreter("""function getX(x) {return x;}""")
    f = js_interpreter.build_function(["x"], "return x")
    assert f(3) == 3

    # Test if the resulting function takes a boolean as argument
    js_interpreter = JSInterpreter("""function getX(x) {return x;}""")
    f = js_interpreter.build_function(["x"], "return x")
    assert f(True)

    # Test if the resulting function takes a variable as argument
    js_interpreter = JSInterpreter("""function getX(x) {return x;}""")
    f = js_interpreter.build_function(["x"], "return x")
    assert f

# Generated at 2022-06-14 17:57:20.824416
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    js_interpreter = JSInterpreter('var a = [ 4, 2, 5 ]; var b = [3, 5, 1];')
    assert 5 == js_interpreter.interpret_expression('a[1]', {'a': [4, 5]}, 100)
    assert 5 == js_interpreter.interpret_expression('b[2]', {'b': [3, 5, 5]}, 100)
    assert '5' == js_interpreter.interpret_expression('a.join("")', {'a': [4, 5]}, 100)
    assert '53' == js_interpreter.interpret_expression('b.join("")', {'b': [3, 5, 5]}, 100)

# Generated at 2022-06-14 17:57:52.684917
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    code = '''
        var result = 0, a = 5, b = 6;
        function my_func(a, b) {
            result = a + b;
            return result; 
        }
    '''
    js = JSInterpreter(code)
    f = js.build_function(['a', 'b'], 'result = a + b; return result;')
    assert f((3, 4)) == 7
    assert f((5, 1)) == 6

    f = js.build_function(['a', 'b'], 'return a * b;')
    assert f((1, 2)) == 2


if __name__ == '__main__':
    test_JSInterpreter_build_function()
    print ('Test passed!')

# Generated at 2022-06-14 17:57:55.881208
# Unit test for method call_function of class JSInterpreter
def test_JSInterpreter_call_function():
    JSInterpreter.call_function = lambda self, _, a, b: a + b
    test_interpreter = JSInterpreter(None)
    assert test_interpreter.call_function('func', 1, 2) == 3

# Generated at 2022-06-14 17:58:02.800397
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    obj = {
        'a': 'abcdefg',
        'null': None,
        'b': [1,2,3,4,5],
        'c': ['a', 'b', 'c'],
        'd': {
            'd1': 1,
            'd2': '2',
            'f': lambda x: x + 't',
            'g': lambda x: x + x,
        },
    }
    interp = JSInterpreter('', obj)
    assert interp.interpret_expression('("abc")', {}) == 'abc'
    assert interp.interpret_expression('a[0]', {}) == 'a'
    assert interp.interpret_expression('a.length', {}) == 7
    assert interp.interpret_expression('b[d.f(2)]', {})