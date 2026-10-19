

# Generated at 2022-06-14 17:49:03.748390
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    from .utils import parse_json
    code = '''
            a = {
                b: function(){},
                c: function(d,e,f){return d + e + f;}
            };'''

    interpreter = JSInterpreter(code)
    obj = interpreter.extract_object('a')

    assert len(obj) == 2

    assert callable(obj['b'])
    assert obj['b'](), None

    assert callable(obj['c'])
    assert obj['c'](1, 2, 3), 6

    test_code = '''
            a = {
                b: {
                    c1: function(){return 1;}
                },
                c: function(d){return a.b.c1() + d;}
            };'''
    interpreter = JSInterpreter(test_code)


# Generated at 2022-06-14 17:49:15.102838
# Unit test for method call_function of class JSInterpreter
def test_JSInterpreter_call_function():
    # Testing for extract_function method

    js_interpreter = JSInterpreter('''
        function func1(a,b,c) {
            return a + b + c;
        }
    ''')
    res = js_interpreter.call_function('func1', 1,2,3)
    assert res == 6

    js_interpreter = JSInterpreter('''
        var func2 = function(a,b,c){
            return a + b + c;
        }
    ''')
    res = js_interpreter.call_function('func2', 1,2,3)
    assert res == 6


# Generated at 2022-06-14 17:49:26.756005
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    code = '''
        function function_0(arg0) {
            var a = 1;
            var b = arg0;
            var c = 3;
            var d = 4;
        }

        var object_1 = {
            member_0: function(arg0, arg1) {
                var a = 1;
                var b = arg0;
                var c = arg1;
            },
            member_1: function(arg0) {
                var a = 1;
                var b = arg0;
            },
            member_2: function() {
                var a = 1;
            }
        };
    '''
    obj = JSInterpreter(code).extract_object('object_1')
    assert obj['member_0']('a', 'b') == None
    assert obj['member_1']

# Generated at 2022-06-14 17:49:38.273861
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    _VIDEO_INFO_RE = r'''["']?url_encoded_fmt_stream_map["']?\s*:\s*["'](?P<url_encoded_fmt_stream_map>[^"']+)'''

    code = '''
        var A = function(a,b){
            return a + b;
        };
        var B = {
            a: A,
            b: 2
        };
        var C = {
            c: 3
        };
    '''
    objects = {}
    js = JSInterpreter(code, objects)
    js.extract_object('B')
    assert objects['B'] == {'a': objects['B']['a'], 'b': 2}


# Generated at 2022-06-14 17:49:40.935882
# Unit test for method call_function of class JSInterpreter
def test_JSInterpreter_call_function():
    jsint = JSInterpreter(code='')
    jsint.interpret_statement = lambda *args: ['test']
    assert(jsint.call_function('func_name') == ['test'])


# Generated at 2022-06-14 17:49:50.961247
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    js_inter = JSInterpreter('var a = 10; var b = 20; var c = 30;')
    assert js_inter.interpret_expression('a', {}) == 10
    assert js_inter.interpret_expression('a + b', {}) == 30
    assert js_inter.interpret_expression('a + b + c', {}) == 60
    assert js_inter.interpret_expression('a * 10', {}) == 100
    assert js_inter.interpret_expression('''
        "abcdef".split("")
        ''', {}) == ['a', 'b', 'c', 'd', 'e', 'f']
    assert js_inter.interpret_expression('''
        "abcdef".slice(6)
        ''', {}) == ''

# Generated at 2022-06-14 17:49:57.685766
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    # js code copied from http://en.wikipedia.org/wiki/Operators_in_JavaScript
    test_js_code = """
        var x = 5;
        var y = 3;
        var z = x + y;
        var a = x - y;
        var b = x * y;
        var c = x / y;
        var d = x % y;
    """

    js_interpreter = JSInterpreter(test_js_code, objects={'Math': {'floor': {}}, 'x':{}})
    js_interpreter.interpret_expression('Math.floor(x)', {})

if __name__ == '__main__':
    test_JSInterpreter_interpret_expression()

# Generated at 2022-06-14 17:50:11.247098
# Unit test for method interpret_expression of class JSInterpreter

# Generated at 2022-06-14 17:50:21.171802
# Unit test for method interpret_expression of class JSInterpreter

# Generated at 2022-06-14 17:50:27.233940
# Unit test for method interpret_statement of class JSInterpreter
def test_JSInterpreter_interpret_statement():
    code = """
        function is_in(arr, key) {
            for (var i = 0; i < arr.length; i++) {
                if (arr[i] === key) {
                    return true;
                }
            }
            return false;
        }
    """

    interpreter = JSInterpreter(code)
    test_stmt = "for (var i = 0; i < arr.length; i++)"
    test_stmt2 = "if (arr[i] === key)"
    test_stmt3 = "return true"
    test_stmt4 = "return false"

    assert interpreter.interpret_statement(test_stmt, {'arr': [1, 2, 3], 'i': None}) == (None, False)

# Generated at 2022-06-14 17:50:53.857001
# Unit test for method interpret_statement of class JSInterpreter
def test_JSInterpreter_interpret_statement():
    s = JSInterpreter('function this_is_useless(a){}')
    result1, _ = s.interpret_statement('a = 5', {'a': 0})
    assert result1 == 5

    result2, _ = s.interpret_statement('b = a', {'a': 0})
    assert result2 == 5

    result3, _ = s.interpret_statement('return a', {'a': 0})
    assert result3 == 5


# Generated at 2022-06-14 17:50:59.275304
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    code = r"""function test(){
  var a = 6;
  var b = a + 7;
  return b + c;
}"""
    interpreter = JSInterpreter(code)
    local_vars = {'c': 3}
    assert(interpreter.interpret_expression('a + b', local_vars) == 12)



# Generated at 2022-06-14 17:51:09.255905
# Unit test for method extract_function of class JSInterpreter
def test_JSInterpreter_extract_function():
    js_code = (
        '''
        var funcName = function(arg1, arg2) {
            var var1 = 3;
            return arg1 + var1 + arg2;
        }''')

    interpreter = JSInterpreter(js_code, {})
    assert callable(interpreter.extract_function('funcName'))


if __name__ == '__main__':
    import sys
    import os

    # test_JSInterpreter_extract_function()

    if len(sys.argv) < 4:
        print('Usage: %s file.sig function "arg1, arg2, ..."' % sys.argv[0])
        sys.exit(1)

    sigfilename = sys.argv[1]
    funcname = sys.argv[2]
    args = sys

# Generated at 2022-06-14 17:51:21.339704
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    import re
    def find_obj_by_name(code, obj_name):
        """
        >>> find_obj_by_name('var a = {b: 1};', 'a').group('fields')
        'b:1'
        """
        return re.search('(?<!this\.)%s\s*=\s*{\s*(?P<fields>(%s\s*:\s*function\s*\(.*?\)\s*{.*?}(?:,\s*)?)*)}' % (re.escape(obj_name), _FUNC_NAME_RE), code)

    def test_get_object():
        code = 'var a = {b: 1};'
        obj = JSInterpreter(code).extract_object('a')
        assert obj['b'] == 1


# Generated at 2022-06-14 17:51:29.611017
# Unit test for method interpret_statement of class JSInterpreter
def test_JSInterpreter_interpret_statement():
    js = JSInterpreter('')
    lv = {'a': 2, 'b': 1, 'c': 3}
    assert js.interpret_statement('a', lv)[0] == 2
    assert js.interpret_statement('a=b', lv)[0] == 1 and lv['a'] == 1
    assert js.interpret_statement('a==b', lv)[0] == False
    assert js.interpret_statement('a!=b', lv)[0] == True
    assert js.interpret_statement('a>=b', lv)[0] == True
    assert js.interpret_statement('a<=b', lv)[0] == False
    assert js.interpret_statement('a<b', lv)[0] == False

# Generated at 2022-06-14 17:51:38.155368
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    js1 = '''var a = "hello";
    b = {"f" : function(k) {var v = a + " " + k; return v;}}'''
    jsi = JSInterpreter(js1, {'a' : 'world'})
    f = jsi.build_function(['k'], '''var v = a + " " + k; return v;''')
    assert f(['good']) == 'world good'

    js2 = 'k = {' \
        '"a": 1,' \
        '"b": "c",' \
        '"c": function(a, b){return a === b;},' \
        '"d": function(a, b){return a + " - " + b;}}'

# Generated at 2022-06-14 17:51:43.236560
# Unit test for method call_function of class JSInterpreter
def test_JSInterpreter_call_function():
    test_object = '''
                return{
                    "a":function(b){return b}
                }
                '''
    interp = JSInterpreter(test_object)
    obj2 = interp.call_function("return", None)["a"]("abc")
    assert obj2 == "abc"

# Generated at 2022-06-14 17:51:52.275377
# Unit test for method interpret_statement of class JSInterpreter

# Generated at 2022-06-14 17:51:56.893174
# Unit test for method extract_function of class JSInterpreter
def test_JSInterpreter_extract_function():
    js_code = """
        function foobar(a,b){
            return a*b;
        }
    """
    jsi = JSInterpreter(js_code)
    f = jsi.extract_function('foobar')
    assert 2 == f((1,2))

# Generated at 2022-06-14 17:52:08.955024
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    code = '''
        var $ = {
            foo: function() {},
            bar: function() {},
            quux: function() { return -1; },
            baz: {}
        };
        var s = 'string';
        var o = {a: 1};
        var f = function() {};
        window.ytd = {
            player: {
                embed: function(id) {}
            }
        };
    '''
    obj = JSInterpreter(code).extract_object('$')
    assert(len(obj) == 4)
    assert('foo' in obj)
    assert('bar' in obj)
    assert('quux' in obj)
    assert('baz' in obj)
    assert(isinstance(obj['foo'], type(lambda x: None)))

# Generated at 2022-06-14 17:52:43.676213
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    # Test the basic operators
    js = JSInterpreter('', {})
    assert js.interpret_expression('1', {}) == 1
    assert js.interpret_expression('2', {}) == 2
    assert js.interpret_expression('2/2', {}) == 1
    assert js.interpret_expression('1+1', {}) == 2
    assert js.interpret_expression('1-1', {}) == 0
    assert js.interpret_expression('1*1', {}) == 1
    assert js.interpret_expression('2 >> 1', {}) == 1
    assert js.interpret_expression('2 << 1', {}) == 4
    assert js.interpret_expression('2 & 1', {}) == 0
    assert js.interpret_expression('1 | 1', {}) == 1
    assert js.interpret_expression('1 == 1', {})

# Generated at 2022-06-14 17:52:54.282669
# Unit test for method build_function of class JSInterpreter

# Generated at 2022-06-14 17:52:57.912060
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    jsinterp = JSInterpreter(''.join(open('logic.txt').readlines()))
    obj = jsinterp.extract_object('u')
    print(obj)


# Generated at 2022-06-14 17:53:06.083621
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    print('Testing method "build_function" with args [\'left\', \'right\', \'step\'], \'\'...')
    interpreter = JSInterpreter('', {})
    args = ['left', 'right', 'step']
    code = ''
    function = interpreter.build_function(args, code)
    print('\tExpecting a function...')
    if isinstance(function, types.FunctionType):
        print('\tFound function!')
    else:
        print('\tNOT A FUNCTION!')
    print('Testing method "build_function" with args [\'a\', \'b\', \'c\'], \'var a = 1.5, b = 2.5, c = 2;\''
          'var d = a + b - c; d;\'...')

# Generated at 2022-06-14 17:53:16.028209
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    class UnitTest(object):
        def __init__(self, function_code, function_args, function_output):
            self.code = function_code
            self.args = function_args
            self.result = function_output

        def assert_function(self):
            jsi = JSInterpreter(self.code)
            interpreter_result = js.build_function(
                ['arg1', 'arg2', 'arg3'], self.code)(self.args)
            assert(self.result == interpreter_result)

    # Test for simple function
    js = JSInterpreter('var abc = function(arg1, arg2) { return arg1*2 + arg2; }')
    assert(js.call_function('abc', 3, 4) == 11)

    # Test for simple function with array access
    js = JS

# Generated at 2022-06-14 17:53:26.993227
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    _objects = {'r': {'k': 'v'}}
    _code = r'''
        r = {
            k: function(arg1, arg2) { console.log(arg1, arg2); return 'v'; },
            l: function(arg) { return arg; }
        };
    '''
    interpreter = JSInterpreter(_code, _objects)
    interpreter.extract_object('r')
    assert _objects['r']['k']('a', 'b') == 'v'
    assert _objects['r']['l']('c') == 'c'

    _objects = {'r': {'k': 'v'}}

# Generated at 2022-06-14 17:53:34.219299
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    code = """
        var b = {
            "id":null,
            "h":null,
            "f":{
                1:1
            },
            "g": function(a) {
                this.id = a
            },
            "k": function(a, b) {
                this.h = a;
                this.f = b
            }
        };
    """

    print(JSInterpreter(code).extract_object('b'))


# Generated at 2022-06-14 17:53:46.022335
# Unit test for method build_function of class JSInterpreter

# Generated at 2022-06-14 17:53:54.211107
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    test_func_codes = [
"""
var a = 1234;
var b = function(x,y){
    var z = '';
    for(n=0;n<y.length;n++){
        if(n == x){
            z += "%s";
        }else{
            z += y[n];
        }
    }
    return z;
};
return b;
""",
"""
var signature = "%s";
var a = signature.split("");
a.reverse();
var b = a.join("");
return b;
"""
    ]

# Generated at 2022-06-14 17:54:02.253002
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    s = '''
        var test = "test";
        var c = 'c';
        var c = 'c';
        var a = '1';
        var b = '2';
        var f = function () {
            var c = 'c';
            var d = 'd';
            var g = function () {
                var e = 'e';
            }
        }
        function h (b, x, y) {
            var d = 'd';
            var l = 'l';
        }
        var i = {
            j: function (x, d) {
                var k = 'k';
            }
        }
    '''
    local_vars = {'a':'1', 'b':'2', 'c':'c'}

# Generated at 2022-06-14 17:54:32.553710
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    i = JSInterpreter("""
    function function_name(arg1,arg2,arg3) {
        var local_var = arg1;
        return local_var*arg3+local_var*arg2;
    }
    """)
    f = i.build_function(["arg1","arg2","arg3"], """
        var local_var = arg1;
        return local_var*arg3+local_var*arg2;
    """)
    print(f([1,2,3]))


# Generated at 2022-06-14 17:54:43.307397
# Unit test for method extract_object of class JSInterpreter

# Generated at 2022-06-14 17:54:53.152490
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    code = ('function foo(a,b,c){'
            'return a;'
            'return b;'
            'return c;'
            '};')
    argnames = ['a','b','c']
    interp = JSInterpreter(code)
    resf = interp.build_function(argnames, code)
    assert(resf([1,2,3]) == 1)
    assert(resf([4,5,6]) == 4)

if __name__ == '__main__':
    test_JSInterpreter_build_function()

# Generated at 2022-06-14 17:55:02.245991
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    assert JSInterpreter.build_function(
        [], "; return 1")() == 1
    assert JSInterpreter.build_function(
        ['a'], "a; return 1")(1) == 1
    assert JSInterpreter.build_function(
        ['a', 'b'], "; return a + b")(1, 2) == 3
    assert JSInterpreter.build_function(
        ['a', 'b'], "; return a + b")(1, b=2) == 3
    assert JSInterpreter.build_function(
        ['a', 'b'], "; return a + b")(a=1, b=2) == 3
    assert JSInterpreter.build_function(
        [], "; return 1")() == 1

# Generated at 2022-06-14 17:55:13.030627
# Unit test for method build_function of class JSInterpreter

# Generated at 2022-06-14 17:55:19.449130
# Unit test for method call_function of class JSInterpreter

# Generated at 2022-06-14 17:55:31.486328
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    test_code = """
    var ytplayer = {
        "a":function(arg){
            return arg
        },
        "b":function(arg1,arg2){
            return arg1+arg2
        },
        "c":function(){
            return "just string"
        }
    }
    var hello = {
        "e":function(arg){
            return arg+"a"
        },
        "f":function(arg1,arg2){
            return arg1+"b"+arg2
        },
        "g":function(){
            return "just string"
        }
    }
    """
    js_interpreter = JSInterpreter(test_code)
    obj = js_interpreter.extract_object("ytplayer")

# Generated at 2022-06-14 17:55:41.549613
# Unit test for method call_function of class JSInterpreter
def test_JSInterpreter_call_function():
    js_intepreter = JSInterpreter(
        '''
            if (typeof window !== 'undefined') {
            function yt(a, b) {
                if (window.spf && spf.script) {
                    if (spf.script.load) {
                        var c = spf.script.load(a, b);
                        return c
                    }
                    return null
                }
                return null
            }
            function zt(d, e) {
                var f = spf.script.get(d);
                if (f && f.loaded) {
                    e();
                    return true;
                } else {
                    return false;
                }
            }
            }
        ''')

# Generated at 2022-06-14 17:55:53.573857
# Unit test for method interpret_statement of class JSInterpreter
def test_JSInterpreter_interpret_statement():
    i = JSInterpreter('var a = function(){var b = function(){return 1;};var c = function(){return 2;};return b() + c();}; a();')
    x, abort = i.interpret_statement('var a = function(){var b = function(){return 1;};var c = function(){return 2;};return b() + c();};', dict())
    assert x == 3

    i = JSInterpreter('var a = function(){var b = function(){return 1;};var c = function(){return 2;};return b() - c();}; a();')
    x, abort = i.interpret_statement('var a = function(){var b = function(){return 1;};var c = function(){return 2;};return b() - c();};', dict())
    assert x == -1


# Generated at 2022-06-14 17:56:05.991469
# Unit test for method interpret_expression of class JSInterpreter

# Generated at 2022-06-14 17:56:46.043280
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    # Method build_function of class JSInterpreter should translate
    # the function func as defined below into python function func_
    def func(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z):
        a=a*b+c
        d=d*e+f+98-g
        g=a+d
        h=i*j*k+l
        m=n+o*p
        q=r+s
        t=u*v
        w=x+y
        z=g+h+m+q+t+w+3
        z=z+1

# Generated at 2022-06-14 17:56:54.446781
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    # This test needs 2 JS functions to run, one defined in JS and the second in Python
    # In JS :
    # a = function(args) {...};
    # In Python :
    # def b(args): ...;
    code_a = '''
        a = function(arg) {
            var e_0x566e=['param1','param2','param3'];
            return e_0x566e[arg];
        };
    '''
    # Function b
    def b(args):
        e_0x566e=['param1','param2','param3']
        return e_0x566e[args]

    # This is where we instantiate the interpreter (test_JSInterpreter_build_function's interpreter)
    interpreter = JSInterpreter(code_a)

    #

# Generated at 2022-06-14 17:57:00.280179
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    code = """
        var A = {x: "a", y: function() {return "b"}, z: function(a, b) {return b}};
        console.log(A.x);
        return A.y();
    """
    interpreter = JSInterpreter(code)
    res = interpreter.call_function('', {})
    assert res == 'b'

# Generated at 2022-06-14 17:57:06.325078
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    js_code = '''
    var a = {length:5};
    a[5-5] = function(b){return b+1};
    a[5-5](a[parseInt('0xa')-10+1] = a[0]);'''
    res = JSInterpreter(js_code).interpret_expression('''a[0](a[1]=10)''', {})
    assert res == 11

if __name__ == '__main__':
    test_JSInterpreter_interpret_expression()

# vim:sw=4:sts=4:et

# Generated at 2022-06-14 17:57:07.674174
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    assert JSInterpreter({}, '').build_function(["a","b"], "return a+b")([1,2])==3

# Generated at 2022-06-14 17:57:10.853280
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    js_code = "var obj = {a: 0, b: 1, c: function(){return function(){return 'c';}}};"
    js_obj = JSInterpreter(js_code).extract_object('obj')
    assert js_obj['a'] == 0
    assert js_obj['b'] == 1
    assert js_obj['c']()() == 'c'


# Generated at 2022-06-14 17:57:19.352511
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    def test_interpret_expression(expr, expected, js_globals=None):
        interpreter = JSInterpreter('return %s;' % expr, default_globals(js_globals))
        assert interpreter.interpret_expression(expr, {}) == expected

    test_interpret_expression('"abc" + (123)', 'abc123')
    test_interpret_expression('123 + "cba"', '123cba')
    test_interpret_expression('"cba" + 123', 'cba123')
    test_interpret_expression('123.toString(2)', '1111011')
    test_interpret_expression('123.toString(8)', '173')
    test_interpret_expression('123.toString()', '123')

# Generated at 2022-06-14 17:57:28.190493
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    def _test_decode(funcname, code, *args, **kwargs):
        expected = kwargs.pop('expected', None)
        assert expected, 'Expected result must be set!'
        if 'obj' in kwargs:
            i = JSInterpreter('', objects=kwargs.pop('obj'))
        else:
            i = JSInterpreter('')
        f = i.build_function(kwargs.pop('argnames', []), code)
        res = f(args)
        assert res == expected, '%s(%s) = %s != %s' % (funcname, ', '.join(map(repr, args)), res, expected)

    _test_decode('test1', 'var a=function(){return 1+2};a()', expected=3)
    _test_dec

# Generated at 2022-06-14 17:57:37.265537
# Unit test for method call_function of class JSInterpreter
def test_JSInterpreter_call_function():
    js_interpreter = JSInterpreter(
        '''
        a = 1;
        b = 'fuck';
        c = {a: 10, b: 20};
        d = function(a, b) {
            return a + b;
        }
        function e(c) {
            return a * b * c * d(a, b);
        }
        ''')
    assert js_interpreter.call_function('e', 1) == 200
    assert js_interpreter.call_function('e', 2) == 400
    assert js_interpreter.call_function('d', 2, 3) == 5


# Generated at 2022-06-14 17:57:42.708936
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    '''
        JSInterpreter.build_function:
        f1(a, b) {
            return a * b;
        }
    '''
    assert JSInterpreter.build_function(['a', 'b'], 'return a * b')([4, 5]) == 20
    assert JSInterpreter.build_function(['a', 'b'], 'return (a * b)')([4, 5]) == 20
    assert JSInterpreter.build_function(['a', 'b'], 'return (a - b)')([4, 5]) == -1
    assert JSInterpreter.build_function(['a', 'b'], 'return (a + b)')([4, 5]) == 9