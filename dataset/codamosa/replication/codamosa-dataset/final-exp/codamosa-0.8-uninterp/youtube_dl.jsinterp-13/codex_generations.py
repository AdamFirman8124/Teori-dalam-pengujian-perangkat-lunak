

# Generated at 2022-06-14 17:48:42.395294
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    js_interpreter = JSInterpreter('')

    # Test 1
    test_code = 'somevar=somevar+1'
    func = js_interpreter.build_function(['somevar'], test_code)
    result = func([3])
    assert result == 4

    # Test 2
    test_code = '''somearray[somevar-1]=somearray[somevar-1]+1;
        somevar=somevar+1'''
    func = js_interpreter.build_function(['somearray', 'somevar'], test_code)
    result = func([[0,0,0],1])
    assert result == 1

    # Test 3

# Generated at 2022-06-14 17:48:48.679784
# Unit test for method call_function of class JSInterpreter
def test_JSInterpreter_call_function():
    code = r'''
        rab = "4";
        rad = "5";
        function a(rab, rad) {
            return (rab + rad)
        };

        function b(a,c) {
            return a(c)
        };

        function d(e) {
            return b(a, e)
        };'''
    interpreter = JSInterpreter(code)
    need_result = interpreter.call_function('d', '5')
    print(need_result)
    assert need_result == '45'


if __name__ == '__main__':
    test_JSInterpreter_call_function()

# Generated at 2022-06-14 17:48:58.949213
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    code = '''
    var toString = function() {
        var a = this.charCodeAt(0)
        var b = ge('charCodeAt')(1)
        return a + b
    }
    '''
    js_interp = JSInterpreter(code)
    toString = js_interp.build_function(['this'], "var a = this.charCodeAt(0); var b = ge('charCodeAt')(1); return a + b;")
    assert toString(['AB']) == 65 + 66


# Generated at 2022-06-14 17:49:03.500735
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    def _test(code, expected):
        js = JSInterpreter(code)
        expr = code[code.index('return') + 6:code.rindex(';')].strip()
        print('Testing: %s == %s' % (expr, expected))
        try:
            result = js.interpret_expression(expr, {})
            assert (result == expected)
        except ExtractorError as e:
            print('Test failed, expected %s but got: %s' % (expected, e))
    _test('''return "test";''', 'test')
    _test('''return test;''', 'test2')
    _test('''return 10 + 10;''', 20)
    _test('''return true ? 1 : 2;''', 1)

# Generated at 2022-06-14 17:49:10.457974
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    i = JSInterpreter('''function abc() {
    foo = {
        bar: function() { return 1 + 2 },
        baz: function(n, m) { return n + m }
    }}}''')
    res = i.extract_object('foo')
    assert len(res) == 2
    assert res['bar']() == 3
    assert res['baz'](4, 5) == 9


# Generated at 2022-06-14 17:49:17.263950
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    from .utils import ordered_set

    js_interpreter = JSInterpreter('')

    # test1: expression with parenthesis
    assert js_interpreter.interpret_expression('(1+5)*5', {}) == 30

    # test2: expression with list index
    assert js_interpreter.interpret_expression(
        'a[0]+a[1]', {'a': [1, 2]}) == 3

    # test3: expression with member variable
    assert js_interpreter.interpret_expression(
        'b.length', {'b': [1, 2]}) == 2

    # test4: array join
    assert js_interpreter.interpret_expression(
        'b.join(",").length', {'b': [1, 2]}) == 3

    # test5: function call


# Generated at 2022-06-14 17:49:27.776209
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    objects = {}
    jsi = JSInterpreter(code,objects=objects)

# Generated at 2022-06-14 17:49:39.941129
# Unit test for method call_function of class JSInterpreter
def test_JSInterpreter_call_function():
    """
    test_JSInterpreter_call_function
    """
    js_code = """
            function test0() {
                var ox = 0;
                var i = 0;
                while (i < 3) {
                    ox += i;
                    i++;
                }
                return ox;
            }
            function test1(a, b) {
                return a + b;
            }
            function test2(a, b, c) {
                return a * b * c + 34;
            }
        """
    interpreter = JSInterpreter(js_code)
    assert interpreter.call_function('test0') == 3
    assert interpreter.call_function('test1', 1, 2) == 3
    assert interpreter.call_function('test2', 1, 2, 3) == 40


# Generated at 2022-06-14 17:49:45.655978
# Unit test for method call_function of class JSInterpreter
def test_JSInterpreter_call_function():
    code = '''function func(arg1, arg2) {
    var var1 = arg1;
    var var2 = arg2;
    return var1 + var2;
}'''

    js = JSInterpreter(code)
    assert js.call_function('func', 1, 2) == 3

if __name__ == '__main__':
    import sys
    import doctest
    sys.exit(doctest.testmod().failed)

# Generated at 2022-06-14 17:49:51.226934
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    code = """
    function function_name(a, b) {
        c = b+5;
        return c;
    }
    """
    js = JSInterpreter(code)
    f = js.build_function(['a', 'b'], 'c = b+5;return c;')
    assert f((4, 5)) == 9
    assert f((4, 1)) == 6

# Generated at 2022-06-14 17:50:27.753892
# Unit test for method extract_object of class JSInterpreter

# Generated at 2022-06-14 17:50:33.426728
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    code = '''
    var a = {
        "b": function() {},
        "c": function() {}
    }'''
    interpreter = JSInterpreter(code)
    obj = interpreter.extract_object('a')
    assert obj == {
        "b": None,
        "c": None
    }
    code = '''
    var a = {
        "b": "a",
        "c": "hello"
    }'''
    interpreter = JSInterpreter(code)
    obj = interpreter.extract_object('a')
    assert obj == {
        "b": "a",
        "c": "hello"
    }



# Generated at 2022-06-14 17:50:38.577095
# Unit test for method extract_object of class JSInterpreter

# Generated at 2022-06-14 17:50:50.115717
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    jsint = JSInterpreter('anything')
    # Check f correctly returns the first argument
    f = jsint.build_function(['a'], 'return a;')
    assert f(['b']) == 'b'

    # Check f correctly returns the second argument
    f = jsint.build_function(['a', 'b'], 'return b;')
    assert f(['a', 'b']) == 'b'

    # Check f correctly returns the sum of the arguments
    f = jsint.build_function(['a', 'b'], 'return (a+b);')
    assert f([1, 2]) == 3
    assert f(['a', 'b']) == 'ab'

    # Check f correctly returns the sum of the arguments after a local assignment

# Generated at 2022-06-14 17:50:57.619391
# Unit test for method interpret_expression of class JSInterpreter

# Generated at 2022-06-14 17:51:04.193080
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    js_code = """
        var a = 0;
        while( a < 10 )
        {
            a = a + 1;
        }
        """
    jsi = JSInterpreter(js_code)
    jsi.interpret_expression('a < 10', {'a':0})
    assert jsi.interpret_expression('a + 1', {'a':0}) == 1

# Generated at 2022-06-14 17:51:15.953299
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    def test_comp(funcname, code, args, expected):
        jsi = JSInterpreter(code)
        g = jsi.build_function([funcname], code)
        result = g(args)
        print("result: ",result)
        assert result == expected
    test_comp("a", "return a;",(6,),6)
    test_comp("a", "return a-a;",(6,),0)
    test_comp("a","return a;",(3,2),3)
    test_comp("a", "return a+a;",(3,2),5)
    test_comp("a","return a*a;",(3,2),9)
    test_comp("a","return a*2;",(3,2),6)

# Generated at 2022-06-14 17:51:27.530439
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    # Operators
    assert JSInterpreter('2').interpret_expression('0 + 2', {}) == 2
    assert JSInterpreter('2').interpret_expression('2 - 0', {}) == 2
    assert JSInterpreter('2').interpret_expression('4 - 2', {}) == 2
    assert JSInterpreter('2').interpret_expression('2 * 1', {}) == 2
    assert JSInterpreter('2').interpret_expression('6 / 3', {}) == 2
    assert JSInterpreter('2').interpret_expression('3 / 2', {}) == 1.5
    assert JSInterpreter('2').interpret_expression('2 | 1', {}) == 3
    assert JSInterpreter('2').interpret_expression('2 ^ 3', {}) == 1

# Generated at 2022-06-14 17:51:35.233506
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    js = '''
        var A={b:1,c:function(){return 2},d:function(i){return i+3}};
        var E={f:1,g:function(){return 2},h:function(i){return i+3}};
    '''
    js_interpreter = JSInterpreter(js)
    obj_A = js_interpreter.extract_object('A')
    assert obj_A['b'] == 1
    assert obj_A['c']() == 2
    assert obj_A['d'](3) == 6
    obj_E = js_interpreter.extract_object('E')
    assert obj_E['f'] == 1
    assert obj_E['g']() == 2
    assert obj_E['h'](3) == 6


# Generated at 2022-06-14 17:51:48.126295
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    js_code = '''
    var obj = {
        f1: function (arg1, arg2) {
            var a = arg1;
            var b = arg2;
        },
        f2: function (arg1, arg2, arg3) {
            var a = arg1;
            var b = arg2;
            var c = arg3;
        }
    }
    '''
    # obj is a dict, f1 and f2 are members of obj
    interpreter = JSInterpreter(js_code)
    obj = interpreter.extract_object('obj')
    assert isinstance(obj, dict)
    assert 'f1' in obj
    assert 'f2' in obj
    for func in obj:
        expected_args = func.replace('f', 'arg')
        expected_args = expected_args

# Generated at 2022-06-14 17:52:44.247180
# Unit test for method interpret_expression of class JSInterpreter

# Generated at 2022-06-14 17:52:53.651615
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    _js = '''function foo(){};
    foo = {
        "a": 1,
        "b": function(x){
            return x;
        }
    }'''
    _interpreter = JSInterpreter(code=_js)
    _obj = _interpreter.extract_object("foo")
    print(json.dumps(_obj, indent=4))
    _obj = _interpreter.extract_object("foo")
    print(json.dumps(_obj, indent=4))


# Generated at 2022-06-14 17:53:03.266003
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    # Extracted object must be the same as the original object
    code = '''{
        a: function(){},
        b: function(arg1) {
            if (arg1 == "hola") {
                return 18;
            }
            return 11;
        },
        c: function(arg1) {}
    }'''

    objects = {}
    interpreter = JSInterpreter(code, objects)
    obj = interpreter.extract_object('obj_name')
    assert obj == {
        'a': objects['obj_name']['a'],
        'b': objects['obj_name']['b'],
        'c': objects['obj_name']['c'],
    }


# Generated at 2022-06-14 17:53:07.349387
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    ji = JSInterpreter("", {})
    assert ji.build_function(["x", "y"], "return x + y;")([1, 2]) == 3


# Test for extract_function of class JSInterpreter

# Generated at 2022-06-14 17:53:13.961293
# Unit test for method interpret_statement of class JSInterpreter
def test_JSInterpreter_interpret_statement():
    code = """
        function f(a, b, c) {
            var d = f1(a, b);
            var e = [3, 4];
            var v = d + e[1];
            return v;
        }
        function f1(a, b) {
            return a + b;
        }
    """
    i = JSInterpreter(code)
    res = i.call_function('f', 1, 2, 3)
    assert res == 7



# Generated at 2022-06-14 17:53:25.677824
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    js_code = '''
        var x = 2;
        var y = 'abc';
        function g(a, b) {
            return a + b;
        }
        var z = {
            'a': 1,
            'b': 2,
            'c': g
        };
    '''
    inter = JSInterpreter(js_code)
    assert inter.interpret_expression('2 + 3 - 5', {}) == 0
    assert inter.interpret_expression('2 * 3 + 5', {}) == 11
    assert inter.interpret_expression('6 / 2', {}) == 3
    assert inter.interpret_expression('x * y.length', {}) == 6
    assert inter.interpret_expression('g(3, z.a)', {}) == 4

# Generated at 2022-06-14 17:53:37.446340
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    assert JSInterpreter('').build_function([], ';')() is None
    assert JSInterpreter('').build_function([], 'x = 42;')() == 42
    assert JSInterpreter('').build_function(['x'], 'return x;')(42) == 42
    assert JSInterpreter('var a = [1, 2, 3];').build_function([], 'return a[0];')() == 1
    assert JSInterpreter('').build_function(['a', 'b'], 'return a + b;')(1, 2) == 3
    assert JSInterpreter('').build_function(['a', 'b'], 'b = 7; return a + b;')(5) == 12

# Generated at 2022-06-14 17:53:49.311141
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    jsi = JSInterpreter('')
    assert jsi.interpret_expression('return !!false', {}) == False
    assert jsi.interpret_expression('return +(!+[]+!![]+[+!+[]]+(![]+[])[!+[]+!![]]+[!+[]+!![]+!![]]+[+[]])', {}) == 3
    assert jsi.interpret_expression('a=[]', {}) == []
    assert jsi.interpret_expression('b=a.join(3)', {}) == '3'

if __name__ == '__main__':
    test_JSInterpreter_interpret_expression()

# Generated at 2022-06-14 17:53:54.312876
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    def f1(x0):
        return x0 + 3;
    def f2(x0, x1):
        return x0 + x1;
    def f3(x0):
        return x0[0] + x0[1];
    def f4(x0, x1):
        return (x0 + x1) * x1;

    js = JSInterpreter('A')
    assert js.build_function(['x0'], 'return x0 + 3;')([1]) == f1(1)
    assert js.build_function(['x0', 'x1'], 'return x0 + x1;')([1, 2]) == f2(1, 2)

# Generated at 2022-06-14 17:54:02.295703
# Unit test for method interpret_expression of class JSInterpreter

# Generated at 2022-06-14 17:55:42.673771
# Unit test for method interpret_expression of class JSInterpreter

# Generated at 2022-06-14 17:55:45.753400
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    JSInterpreter.interpret_expression('1 + 2', {}, 100)
    JSInterpreter.interpret_expression('1 + 2', {}, 100)



# Generated at 2022-06-14 17:55:56.869519
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    code = '''
    function function1(){
        var object = {"Key1": "Value1", "Key2": "Value2"};
    }

    function function2(){
        var object = {"Key1": "Value1", "functionKey2": function(){return "Value2";}};
    }

    function function3(){
        var object = {"Key1": "Value1", "functionKey2":
            function(input){
                return input;
            }};
    }

    function function4(){
        var object = {"Key1": "Value1", "functionKey2":
            function(input){
                var internalObject = {
                    "Key3": "Value3"
                }

                return internalObject;
            }};
    }
    '''
    interpreter = JSInterpreter(code)
    object = interpreter.ext

# Generated at 2022-06-14 17:56:07.933075
# Unit test for method interpret_statement of class JSInterpreter
def test_JSInterpreter_interpret_statement():
    js_interpreter = JSInterpreter('', {})

    # Test assignment
    local_vars = {}
    res, abort = js_interpreter.interpret_statement(
        'x = y = 1', local_vars)
    assert res == 1
    assert local_vars == {'x': 1, 'y': 1}

    # Test assignment also works for array
    local_vars = {}
    res, abort = js_interpreter.interpret_statement(
        'x = [1, 2]', local_vars)
    assert res == [1, 2]
    assert local_vars == {'x': [1, 2]}

    local_vars = {}
    res, abort = js_interpreter.interpret_statement(
        'return x + y', local_vars)

# Generated at 2022-06-14 17:56:14.270898
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    def run_test(js_interpreter, expression, expected, local_vars=None):
        if local_vars is None:
            local_vars = {}
        result = js_interpreter.interpret_expression(expression, local_vars)
        # If the tested parameter is an array, compare item by item.
        # This is because list's equality test checks whether the memory address
        # of two objects are the same.
        if isinstance(expected, list) and isinstance(result, list):
            assert len(result) == len(expected)
            for actual, exp in zip(result, expected):
                assert actual == exp
        else:
            assert result == expected


# Generated at 2022-06-14 17:56:26.186897
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    js = JSInterpreter("""
        var r = new RegExp("abc")
    """)

    # Test for number
    js.interpret_expression("r.test(1)", {})

    # Test for character
    js.interpret_expression("r.test(a)", {})

    # Test for string
    js.interpret_expression("r.test('1')", {})

    # Test for test function
    assert js.interpret_expression("r.test('abc')", {})

    # Test for array
    js.interpret_expression("var a = []; a[0] = '1'; a", {})

    # Test for object
    js.interpret_expression("var a = {}; a[1] = '1'; a", {})

    # Test for object method

# Generated at 2022-06-14 17:56:36.058839
# Unit test for method build_function of class JSInterpreter
def test_JSInterpreter_build_function():
    js_code = '''
    var a = 'text_a';
    var b = 'text_b';
    var test_function = function(a, b) {
        var c = a + b;
        return c;
    }
    '''
    interpreter = JSInterpreter(js_code)
    func = interpreter.build_function(['a', 'b'], 'var c = a + b;return c;')
    assert func(['a', 'b']) == 'ab'
    assert func(['text_a', 'text_b']) == 'text_atext_b'

# Generated at 2022-06-14 17:56:47.031417
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    code = '''
        testObject={
            dec:function(a){
                return --a;
            },
            hex:function(a){
                return a.toString(16);
            },
            toObj:function(a){
                var b={};
                for(var c=0;c<a.length;c++)b[a[c]]=c;
                return b;
            }
        };
    '''
    expected_result = {
            'dec': lambda x: x-1,
            'hex': lambda x: x.toString(16),
            'toObj': lambda x: dict([(y, i) for (i, y) in enumerate(x)])
        }
    interpreter = JSInterpreter(code)
    result = interpreter.extract_object('testObject')
    assert result

# Generated at 2022-06-14 17:56:56.260449
# Unit test for method extract_object of class JSInterpreter
def test_JSInterpreter_extract_object():
    example_code = """var x = {
        "a": function (b){return b},
        "c": $d,
        "e": "f",
        "g": 1,
        "join": [].join,
        "split": "",
        "h": {"i": function(){return "j"}, "k": "l"},
        "m": function (b) {return b.n},
        "o": function (b) {return b.p},
    };"""
    interpreter = JSInterpreter(example_code)

# Generated at 2022-06-14 17:57:05.304727
# Unit test for method interpret_expression of class JSInterpreter
def test_JSInterpreter_interpret_expression():
    interp = JSInterpreter('')
    assert interp.interpret_expression('1 + 2 + 3', {}) == 6
    assert interp.interpret_expression('3 * 4 / 2', {}) == 6
    assert interp.interpret_expression('100 % 11', {}) == 1
    assert interp.interpret_expression('1 + 2 * 3', {}) == 7
    assert interp.interpret_expression('(1 + 2) * 3', {}) == 9
    assert interp.interpret_expression('4 * (1 + 2) * 3', {}) == 36
    assert interp.interpret_expression(
        'var a = 1 + 2; a * 3;', {}) == 9

if __name__ == '__main__':
    test_JSInterpreter_interpret_expression()