

# Generated at 2022-06-14 17:49:01.385990
# Unit test for method extract_function of class JSInterpreter
def test_JSInterpreter_extract_function():
    test_string = '''function hello(){return "hello"}; function world(){return "world";}'''
    assert JSInterpreter(test_string).extract_function(funcname = 'hello') == JSInterpreter(test_string).extract_function(funcname = 'world')
    test_string = '''var hello = function(){return "hello";} function world(){return "world";}'''
    assert JSInterpreter(test_string).extract_function(funcname = 'hello') == JSInterpreter(test_string).extract_function(funcname = 'world')
    test_string = '''var hello = function(){return "hello";}; var world = function(){return "world";}'''
    assert JSInterpreter(test_string).extract_function(funcname = 'hello') == JSInterpreter

# Generated at 2022-06-14 17:49:10.377613
# Unit test for method extract_object of class JSInterpreter

# Generated at 2022-06-14 17:49:16.976638
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    code = "var func = function(a, b) { return a * b; }"
    interpreter = JSInterpreter(code)
    func = interpreter.build_function(["a", "b"], "return a * b")
    assert func([3, 4]) == 12

    code = "var func = function(a, b) { var c = a; a = b; b = c; return [a, b]; }"
    interpreter = JSInterpreter(code)
    func = interpreter.build_function(["a", "b"], "var c = a; a = b; b = c; return [a, b];")
    assert func([3, 4]) == [4, 3]


if __name__ == '__main__':
    test_JSInterpreter_build_function()

# Generated at 2022-06-14 17:49:22.919037
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    js = """var test = function(a, b, c) {
        return a + b + c;
    };
    """
    js_interpreter = JSInterpreter(js)
    func = js_interpreter.build_function(['a', 'b', 'c'], js[10:-3])
    assert func((1, 2, 3)) == 6

# Generated at 2022-06-14 17:49:30.304004
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    js_interpreter = JSInterpreter("""
    c = function() {
        var a = 3;
        var b = 4;
        return a + b;
    }
    """)
    
    func = js_interpreter.build_function([], "var a = 3; var b = 4; return a + b;")
    assert func([]) == 7

# Generated at 2022-06-14 17:49:35.385573
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    js_interpreter = JSInterpreter('var a=2; a+3;', {})
    assert js_interpreter.build_function(['a'], 'a+3;')((2,)) == 5

# Generated at 2022-06-14 17:49:45.788534
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    interp = JSInterpreter('var testVar = "test";')
    assert interp.interpret_expression('testVar', {}) == 'test'
    assert interp.interpret_expression('testVar.length', {}) == 4

# Generated at 2022-06-14 17:49:55.306314
# Unit test for method extract_function of class JSInterpreter

# Generated at 2022-06-14 17:50:08.540823
# Unit test for method extract_function of class JSInterpreter
def test_JSInterpreter_extract_function():
    from ajpy import JSInterpreter

# Generated at 2022-06-14 17:50:20.202242
# Unit test for method call_function of class JSInterpreter
def test_JSInterpreter_call_function():
    _js_interpreter = JSInterpreter("""
    function test_name_value(a, b, c) {
        return a + b + c;
    }
    function test_name_value_key(a, b, c) {
        return a + b + c;
    }
    function test_no_name(a, b, c) {
        return a + b + c;
    }
    """)
    assert _js_interpreter.call_function(
        'test_name_value', 1, 2, 3) == 6
    assert _js_interpreter.call_function(
        'test_name_value_key',
        1, 2, 3) == 6
    assert _js_interpreter.call_function(
        'test_no_name', 1, 2, 3)

# Generated at 2022-06-14 17:50:49.905719
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    JS = JSInterpreter('', {})
    assert JS.interpret_expression('abc', {'abc': 'abc'}) == 'abc'
    assert JS.interpret_expression('abc + abc2', {'abc': 'abc', 'abc2': 'abc2'}) == 'abcabc2'
    assert JS.interpret_expression('var + abc2', {'var': 'abc', 'abc2': 'abc2'}) == 'abcabc2'
    assert JS.interpret_expression('var + abc', {'var': 'abc', 'abc': 'abc2'}) == 'abcabc2'
    assert JS.interpret_expression('abc', {'abc': ['abc','abc2']}) == ['abc','abc2']

# Generated at 2022-06-14 17:51:01.808493
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    # Given
    js_code = '''
        var o1={
                h:function(p){
                    return p.split("").reverse().join("");
                },
                s:function(p){
                    var q='';
                    for(var i=0;i<p.length;i++){
                        q+=p.charAt(i);
                        q+=p.charAt(i);
                    }
                    return q;
                },
                g:function(p){
                    var q='';
                    for(var i=0;i<p.length;i++){
                        q+=String.fromCharCode(p.charCodeAt(i)-1);
                    }
                    return q;
                }
            };
    '''
    # When
    interpreter = JSInterpreter(js_code)

# Generated at 2022-06-14 17:51:14.421966
# Unit test for method interpret_expression of class JSInterpreter

# Generated at 2022-06-14 17:51:24.487491
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    J = JSInterpreter('test')
    f = J.build_function(['a','b'], 'a;b')
    assert f('c','d') == 'c'
    f = J.build_function(['a','b'], ';a;b;')
    assert f('c','d') == 'd'
    f = J.build_function(['a','b'], 'var c; a;b')
    assert f('d','e') == 'e'
    f = J.build_function(['a','b'], 'var c; c = a;c')
    assert f('f','g') == 'f'
    f = J.build_function(['a','b'], 'var c; c = a+b;c')
    assert f('f','g') == 'fg'
   

# Generated at 2022-06-14 17:51:31.696749
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    code = """
        var a = 0;
        var b = 1;
        var c = "2";
        var d = [3, 4];
        var e = 5;
        var f = 6;
        var g = {
            'h': 7,
            'i': 8
        };
        var j = 9;
        var k = function(l) {
            return l;
        }
        var m = function(n) {
            return n;
        }
    """
    objects = {
        'a': [1, 2, 3],
        'b': [4, 5, 6]
    }
    # Create interpreter
    interpreter = JSInterpreter(code, objects)
    result = interpreter.interpret_expression("a[1]", {}, 100)
    assert result == 2


# Generated at 2022-06-14 17:51:37.197588
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    js = '''var ytplayer = {
            "config": {"args": {"url_encoded_fmt_stream_map": "", "adaptive_fmts": ""}},
            "annotations": [],
            "ttsurl": "",
            "videoDetails": {"thumbnail": {"thumbnails": []}},
            "microformat": {"playerMicroformatRenderer": {"embed": {"flashVars": "allow_embed=1", "iframes": []}}}
        };'''

    objname = 'ytplayer'
    obj = JSInterpreter(js).extract_object(objname)
    assert obj['config']['args']['adaptive_fmts'] == ''


# Generated at 2022-06-14 17:51:43.072241
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    jsinterpreter = JSInterpreter("""\
    (function(n){
       a = 1;
       b = 2;
       return a+b;
    })""")
    func = jsinterpreter.build_function([], "a = 1; b = 2; return a+b;")
    assert(func([]) == 3)

# Generated at 2022-06-14 17:51:52.165830
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    def get_value(expr, context, **kwargs):
        return JSInterpreter(None).interpret_expression(expr, context, **kwargs)

    assert get_value('var a = [1, 2, 3]; a[1]', {'var': [1, 2, 3]}) == 2
    assert get_value('var a = [1, 2, 3]; a.length', {'var': [1, 2, 3]}) == 3
    assert get_value('var a = 10; a', {'var': 10}) == 10
    assert get_value('var a = 10; a ^ 3', {'var': 10}) == 9
    assert get_value('var a = 10; a | 3', {'var': 10}) == 11
    assert get_value('var a = 10; a << 3', {'var': 10})

# Generated at 2022-06-14 17:51:55.577893
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    js_interp = JSInterpreter(code='')
    js_interp.build_function(
        argnames=['a', 'b'],
        code='return a + b;')

# Generated at 2022-06-14 17:52:06.112777
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    # Example from https://github.com/rg3/youtube-dl/blob/master/youtube_dl/extractor/youtube.py
    # Expected to return '4' for argument '-1234'
    code = '''
                    var b = function (a) {
                        a = a.split("");
                        a = a.reverse();
                        a = a.join("");
                        return a
                    };
                    return b(a);
                    '''

    js_interpreter = JSInterpreter(code)
    func = js_interpreter.build_function(['a'], code)
    assert func('-1234') == '4'

# Generated at 2022-06-14 17:52:29.881355
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    local_vars = {
        'a': 1,
        'b': 2,
        'c': 'abc',
        'd': {
            'e': 'a',
        },
        'f': [1, 2, 3],
    }
    interp = JSInterpreter('', None)
    assert interp.interpret_expression('1', local_vars, 100) == 1
    assert interp.interpret_expression('0xFF', local_vars, 100) == 255
    assert interp.interpret_expression('True', local_vars, 100) is True
    assert interp.interpret_expression('false', local_vars, 100) is False
    assert interp.interpret_expression('   1+1', local_vars, 100) == 2

# Generated at 2022-06-14 17:52:42.461276
# Unit test for method interpret_expression of class JSInterpreter

# Generated at 2022-06-14 17:52:45.752706
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    assert JSInterpreter('', {}).build_function(["a", "b"], "return a+b;")((1, 2)) == 3



# Generated at 2022-06-14 17:52:52.612424
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    code = "function c(a,b){return function(){return a+b}};c(4,6)"
    jsi = JSInterpreter(code)
    func = jsi.build_function(['a', 'b'], "return function(){return a+b};")
    res = func([4, 6])
    assert res() == 10



# Generated at 2022-06-14 17:53:03.196243
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    objects = {}
    js_interpreter = JSInterpreter('', objects)

# Generated at 2022-06-14 17:53:14.071032
# Unit test for method interpret_statement of class JSInterpreter
def test_JSInterpreter_interpret_statement():
    i = JSInterpreter('')
    i.interpret_statement('var x', dict())
    
    i.interpret_statement('var x = 3', dict())
    i.interpret_statement('var x = 63', dict())
    i.interpret_statement('var x = 63', dict())
    i.interpret_statement('var x = 0x3f', dict())
    i.interpret_statement('var x = 3 + 5', dict())
    i.interpret_statement('var x = 3 + 5 * 2', dict())
    i.interpret_statement('var x = (3 + 5) * 2', dict())
    i.interpret_statement('var x = "3" + "5"', dict())
    i.interpret_statement('var x = "abc".length', dict())

# Generated at 2022-06-14 17:53:25.761864
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    import unittest
    from .utils import parse_qsl
    # Test for the method build_function in module youtube_dl.jsinterp
    class BuildFunctionTest(unittest.TestCase):
        def setUp(self):
            self.interpreter = JSInterpreter('', {})

        def test_build_function(self):
            audio_config_code = '''
            a = new Array(b.length);
            for(c = 0; c < b.length; c++) {
                a[c] = b.charCodeAt(c);
            }
            return a;
            '''
            audio_config_func = self.interpreter.build_function(['b'], audio_config_code)

# Generated at 2022-06-14 17:53:37.554123
# Unit test for method interpret_expression of class JSInterpreter

# Generated at 2022-06-14 17:53:50.826430
# Unit test for method call_function of class JSInterpreter

# Generated at 2022-06-14 17:54:00.188813
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    interpreter = JSInterpreter(code)
    f = interpreter.build_function(['a'], ';'.join([
        'var b = a',
        'var c = 1234',
        'var d = ""',
        'return b + c + d']))
    assert f(['"coucou"', ]) == "coucou1234"
    f = interpreter.build_function(['a', 'b'], ';'.join([
        'var c = a',
        'var d = 1234',
        'var e = b',
        'return c + d + e']))
    assert f(['"coucou"', '" toto"']) == "coucou1234 toto"

# m = JSInterpreter(code)
# m.extract_function(m.

# Generated at 2022-06-14 17:54:21.177794
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    func_str = 'function(searchString, position) { position = position || 0; return this.substr(position, searchString.length) === searchString; }'
    js_interpreter = JSInterpreter('','','')
    f = js_interpreter.build_function(['searchString','position'],func_str.split('{')[1].split('}')[0])
    assert f('abc','01') == False
    assert f('abc','0') == True
    assert f('abc','1') == False



# Generated at 2022-06-14 17:54:32.184621
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    jsi = JSInterpreter('')

    assert jsi.interpret_expression('0', {}) == 0
    assert jsi.interpret_expression('1', {}) == 1
    assert jsi.interpret_expression('true', {}) == True
    assert jsi.interpret_expression('false', {}) == False
    assert jsi.interpret_expression('[]', {}) == []
    assert jsi.interpret_expression('[0,1]', {}) == [0, 1]
    assert jsi.interpret_expression('[false,true]', {}) == [False, True]
    assert jsi.interpret_expression('[[]]', {}) == [[]]
    assert jsi.interpret_expression('["a"]', {}) == ['a']

    assert jsi.interpret_expression('0+1', {}) == 1
    assert j

# Generated at 2022-06-14 17:54:41.406188
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    # Can't test _extract_function() and _extract_object()
    # because we don't have any JavaScript code
    code = """
        function xxx(a,b) {
            return a * b;
        }
    """
    obj = {
        "yyy": {
            "zzz": lambda args: args[0] * args[1],
            "add": lambda args: args[0] + args[1],
            "length": lambda args: len(args[0]),
        },
        "length": lambda args: len(args[0]),
    }
    inter = JSInterpreter(code, obj)
    print(inter.interpret_expression("xxx(3,5)", {}))
    print(inter.interpret_expression("yyy.zzz(3,5)", {}))

# Generated at 2022-06-14 17:54:51.172382
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    code = 'var t={};t.split=function(a){return a.split();};t.join=function(a){return a.join();};t.slice=function(a,b){return a.slice(b);};t.reverse=function(){this.reverse();};'
    jsinter = JSInterpreter(code)
    func = jsinter.build_function(['a','b'], 'var c=a.slice(b);return c;')
    result = func([1,2])
    assert(result == 2)

# Generated at 2022-06-14 17:54:55.727363
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    # Test of interpret_expression method with simple expressions
    interpreter = JSInterpreter('')
    assert interpreter.interpret_expression('1', {}) == 1
    assert interpreter.interpret_expression('3+3', {}) == 6
    assert interpreter.interpret_expression('2^10', {}) == 1024
    assert interpreter.interpret_expression('-1', {}) == -1
    assert interpreter.interpret_expression('"(1, 2)"', {}) == '(1, 2)'

    # Test of interpret_expression method with complex expressions
    interpreter = JSInterpreter('')
    assert interpreter.interpret_expression(
        '"abc".split("")', {}) == ['a', 'b', 'c']

# Generated at 2022-06-14 17:55:01.530344
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    js_code = open("test.js", "r").read()

    js_interpreter = JSInterpreter(js_code)
    print("\nTesting JS function 'extract_object' of class 'JSInterpreter':\n")

    print(js_interpreter.extract_object("w.yt"))
    print(js_interpreter.extract_object("ytplayer"))
    print(js_interpreter.extract_object("ytplayer.config"))


# Generated at 2022-06-14 17:55:09.390778
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    js_interp = JSInterpreter("function f(arg1, arg2){\n"
                              "return arg1 + arg2;\n"
                              "}\n")
    function_to_test = js_interp.build_function(['arg1', 'arg2'], "return arg1 + arg2")
    assert function_to_test([1, 2]) == 3
    assert function_to_test([1, -1]) == 0
    assert function_to_test([0, 0]) == 0

# Generated at 2022-06-14 17:55:22.221212
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    js_interpreter = JSInterpreter("""
            var a = { b: function(p, q) { return p + q; }, c: function() { return 3; } };
            """)
    expected_results = {'b': {'args_count': 2, 'result': 3}, 'c': {'args_count': 0, 'result': 3}}
    result = js_interpreter.extract_object('a')
    for func_name, expected_result in expected_results.items():
        func = result[func_name]
        actual_result = func(*[1 for i in range(expected_result['args_count'])])
        assert(actual_result == expected_result['result'])

if __name__ == '__main__':
    test_JSInterpreter_extract_object()

# Generated at 2022-06-14 17:55:31.009825
# Unit test for method call_function of class JSInterpreter
def test_JSInterpreter_call_function():
    jsinterpreter = JSInterpreter('''
        function b(c, a) {
            if (3 * a < c) {
                return c
            }
            else {
                return 3 * a
            }
        }
        function f(a, b) {
            return b(a, 1)
        }
    ''')
    assert jsinterpreter.call_function('f', 3, 'b') == 3
    assert jsinterpreter.call_function('f', 4, 'b') == 3
    assert jsinterpreter.call_function('f', 5, 'b') == 6


# Generated at 2022-06-14 17:55:38.972476
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    example_code = r'''
        var a = {
            b: function(p, a, c, k, e, d) {
            },
            c: function(p, a, c, k, e, d) {
            }
        }
    '''
    js = JSInterpreter(example_code)
    assert len(js._objects) == 0
    assert len(js._functions) == 0
    obj = js.extract_object('a')
    assert len(obj) == 2
    assert sorted(obj.keys()) == ['b', 'c']

# Generated at 2022-06-14 17:56:10.724670
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    js = JSInterpreter('''{
        function(a,b,c){
            var d = a;
            var e = b; 
            var f = c;
        }
    }''')
    f = js.build_function(["a", "b", "c"], '''
            var d = a;
            var e = b; 
            var f = c;
        ''')
    assert f((1,2,3)) is None


# Generated at 2022-06-14 17:56:17.045131
# Unit test for method call_function of class JSInterpreter
def test_JSInterpreter_call_function():
    code = """
    var f = function(a,b) {
        return a*b;
    }
    
    var g = function(c) {
        return c + 100;
    }
    
    var h = function() {
        return 5 + 10;
    }
    """
    js = JSInterpreter(code)
    assert js.call_function('f', 5, 10) == 50
    assert js.call_function('g', 5) == 105
    assert js.call_function('h') == 15


# Generated at 2022-06-14 17:56:24.154381
# Unit test for method call_function of class JSInterpreter
def test_JSInterpreter_call_function():
    js_code = """
var ab = function(a, b) {
    return a + b
}
var cd = function(c, d) {
    return ab(c, d) * ab(c, b)
}
cd(1, 2)
"""
    js_interpreter = JSInterpreter(js_code)
    # Calls two internal functions with two argumens each
    assert js_interpreter.call_function('cd', 1, 2) == 9


# Generated at 2022-06-14 17:56:31.714022
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    test_code = '''
                 var s={};
                 s.foo=function(a,b){return a+b};
                 s.bar=function(a){return a};
                 '''
    interpreter = JSInterpreter(test_code)
    interpreter.extract_object('s')
    assert len(interpreter._objects) == 1
    assert interpreter._objects['s']['foo'](1,2) == 3
    assert interpreter._objects['s']['bar'](3) == 3


# Generated at 2022-06-14 17:56:37.781020
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    js_interpreter = JSInterpreter('')
    func = js_interpreter.build_function([], 'a = b; return a+c')
    assert func((1, 2)) == 3

    func = js_interpreter.build_function([], 'a = b; return a+c')
    assert func((1,)) == None


# Generated at 2022-06-14 17:56:49.165345
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    # Test case #1: evaluate unary function call on a string, e.g. 'abc'.split('')
    interpreter = JSInterpreter('', {'abc': 'abc'})
    assert interpreter.interpret_expression('abc.split("")', {}, 100) == ['a', 'b', 'c']

    # Test case #2: evaluate unary function call on a string and binary function call on a string,
    # e.g. 'abc'.split('').join('.')
    interpreter = JSInterpreter('', {'abc': 'abc'})
    assert interpreter.interpret_expression('abc.split("").join(".")', {}, 100) == 'a.b.c'

    # Test case #3: evaluate unary function call on a list and binary function call on a list,
    # e.g. [1, 2

# Generated at 2022-06-14 17:56:58.780916
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    code = """
    foo(a, b, c) {
        var d, e;
        d = a + b;
        e = c;
        a = bar.split(",");
        return d;
    }"""

    def test_func(a, b, c, bar):
        d = a + b
        e = c
        a = bar.split(",")
        return d

    jsinter = JSInterpreter(code)
    test_func2 = jsinter.build_function(["a", "b", "c", "bar"], code)
    assert test_func(1, 2, 3, "a,b") == test_func2(1, 2, 3, "a,b")


# Generated at 2022-06-14 17:57:07.106440
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    code = '''
        $=function(a){
            return a
        };
        a="id";
        e=function(a){
            a=a.split("");
            a=a.reverse();
            a=a.join("");
            return a
        };
    '''
    inter = JSInterpreter(code)
    func = inter.build_function(['a'], '''
        d=a.split("");
        d=e(d);
        d=d.splice(5,7);
        d=d.reverse();
        d=d.join("");
        return d
    ''')
    assert func(('abc',)) == 'fedcb'

# Generated at 2022-06-14 17:57:16.905247
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    def build_function(argnames, code):
        def resf(args):
            local_vars = dict(zip(argnames, args))
            for stmt in code.split(';'):
                res, abort = JSInterpreter(None).interpret_statement(stmt, local_vars)
                if abort:
                    break
            return res
        return resf
    assert build_function(["a", "b", "c"], "return a+b+c")([1, 2, 3]) == 6
    assert build_function(["a", "b", "c"], "return a+b+c;")([1, 2, 3]) == 6
    assert build_function(["a", "b", "c"], "return a+b+c")([1, 2, 3]) == 6

# Generated at 2022-06-14 17:57:21.959577
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    a = JSInterpreter(code='''
        function test(a, b) {
            return a + b;
        }
    ''')
    func = a.build_function(argnames=['a', 'b'], code='''
        return a + b;
    ''')
    assert func([1, 2]) == 3