

# Generated at 2022-06-14 03:01:34.708094
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    from typed_ast import ast3 as ast
    from . import get_closest_parent_of

    source = '''def foo():
        pass

    if 1:
        pass
    '''

    tree = ast.parse(source)
    closest = get_closest_parent_of(tree, tree.body[1].body[0], ast.FunctionDef)
    assert isinstance(closest, ast.FunctionDef)
    assert closest.name == 'foo'

# Generated at 2022-06-14 03:01:39.272756
# Unit test for function get_parent
def test_get_parent():
    tree = ast.parse('import asyncio')
    tree = tree.body[0]
    _parents[tree] = None
    res = get_parent(tree, tree)
    assert res is None, "Failed to get parent of ast.AST"



# Generated at 2022-06-14 03:01:44.174536
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    tree = ast.parse('a = b + 1')
    plus = tree.body[0].value
    assert get_closest_parent_of(tree, plus, ast.Name) == tree.body[0].targets[0]  # noqa  # type: ignore
    assert get_closest_parent_of(tree, plus, ast.Assign) == tree.body[0]  # type: ignore



# Generated at 2022-06-14 03:01:50.354861
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    code = inspect.cleandoc("""
        def f():
            for i in range(10):
                if i > 5:
                    print(i)
            return i
    """)
    module = ast.parse(code)
    assert isinstance(get_closest_parent_of(module, module.body[0].body[0],
                                            ast.For), ast.For)
    assert isinstance(get_closest_parent_of(module, module.body[0].body[0].body[0],
                                            ast.For), ast.For)
    assert isinstance(get_closest_parent_of(module, module.body[0].body[0].body[0],
                                            ast.FunctionDef), ast.FunctionDef)

# Generated at 2022-06-14 03:01:59.684275
# Unit test for function find
def test_find():
    import textwrap
    code = textwrap.dedent("""
        import math
        import os

        def foo() -> None:
            x = math.pow(5, 2)

            def bar() -> None:
                os.path.join('path', 'to', 'some', 'file')

                if True:
                    def fiz() -> None:
                        pass

                    fiz()
            bar()
        foo()
    """)

    tree = ast.parse(code)
    imports = list(find(tree, ast.Import))
    imports_names = list(find(tree, ast.alias))

    assert len(imports) == 2
    assert len(imports_names) == 4

    for import_ in imports:
        for name in import_.names:
            assert isinstance(name, ast.alias)


#

# Generated at 2022-06-14 03:02:01.270815
# Unit test for function find

# Generated at 2022-06-14 03:02:08.681773
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    ast_tree = ast.parse("for i in range(10): print(i)")
    non_exp_parent, index = get_non_exp_parent_and_index(ast_tree,
                                                         ast_tree.body[0].body[0])
    assert isinstance(non_exp_parent, ast.For), "non_exp_parent should be a For class" \
                                                "instance"
    assert index == 0, "Index should be 0"


# Generated at 2022-06-14 03:02:13.269283
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    def example():
        a = 1
        b = 2
        print(a + b)

    parent, index = get_non_exp_parent_and_index(ast.parse(example.__doc__),
                                                 ast.parse(example.__doc__)
                                                 .body[0].body[1].value)
    assert parent == ast.parse(example.__doc__).body[0]
    assert index == 1



# Generated at 2022-06-14 03:02:22.811961
# Unit test for function find
def test_find():
    # pylint: disable=unused-variable
    foo, foo2, bar, baz = ast.parse(
        "foo(); foo(); class Bar: pass; class Baz: pass;").body
    assert list(find(ast.parse('class Foo: pass'), ast.ClassDef)) == []
    assert list(find(ast.parse('foo()'), ast.ClassDef)) == []
    assert list(find(ast.parse('foo()'), ast.FunctionDef)) == []
    assert list(find(ast.parse('class Foo: pass'), ast.FunctionDef)) == []
    assert list(find(ast.parse('foo()'), ast.Call)) == [ast.parse('foo()').body[0].value]

# Generated at 2022-06-14 03:02:24.144839
# Unit test for function insert_at
def test_insert_at():
    insert_at(1, None, None)

# Generated at 2022-06-14 03:02:41.006445
# Unit test for function replace_at
def test_replace_at():
    def func1():
        def func2():
            pass

    tree = ast.parse('def _a(t):\n  _b = t\n  _c = 2 * t\n  _d = t + _c',
                     mode='exec')
    _build_parents(tree)

    target_node = tree.body[0].body[0].targets[0]
    parent = get_parent(tree, target_node)
    index = parent.body.index(target_node)

    def _test(new_node: ast.AST, expected: str) -> None:
        replace_at(index, parent, new_node)
        assert ast.dump(tree) == expected


# Generated at 2022-06-14 03:02:53.193634
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    """Test function get_noe_exp_parent_and_index."""
    # (1) Test a If node.
    if_node = ast.parse('if a == 10:\n    pass').body[0] # type: ignore
    parent, index = get_non_exp_parent_and_index(if_node, if_node.test)
    assert if_node.test == parent.body[index]

    # (2) Test a FunctionDef node.
    func_node = ast.parse('def f():\n    pass').body[0] # type: ignore
    parent, index = get_non_exp_parent_and_index(func_node, func_node.body[0])
    assert func_node.body[0] == parent.body[index]



# Generated at 2022-06-14 03:02:55.664643
# Unit test for function find
def test_find():
    class_ast = ast.parse("class A: pass").body[0]
    assert isinstance(find(class_ast, ast.ClassDef).__next__(), ast.ClassDef)

# Generated at 2022-06-14 03:02:57.856844
# Unit test for function get_parent
def test_get_parent():
    from typed_ast import ast3


# Generated at 2022-06-14 03:03:07.967301
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    tree = ast.parse("""
    def func1(a:int, b:int, c:int) -> int:
        def func2(d: int) -> int:
            return d
        return a + b + c
    """)
    node = tree.body[0].body[0].body[0].value
    type_ = ast.FunctionDef
    assert get_closest_parent_of(tree, node, type_) == tree.body[0].body[0]
    type_ = ast.Module
    assert get_closest_parent_of(tree, node, type_) == tree

# Generated at 2022-06-14 03:03:09.218315
# Unit test for function find

# Generated at 2022-06-14 03:03:13.374470
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    tree = ast.parse('def a():\n    b = 1\n    c = b')
    assert(get_closest_parent_of(tree, tree.body[0].body[1], ast.FunctionDef) == tree.body[0])


# Generated at 2022-06-14 03:03:16.077867
# Unit test for function find
def test_find():
    src = """
    def foo(a):
        pass

    def bar():
        pass
    """

    mod = ast.parse(src)
    funcs = list(find(mod, ast.FunctionDef))

    assert len(funcs) == 2
    assert funcs[0].name == 'foo'
    assert funcs[1].name == 'bar'

# Generated at 2022-06-14 03:03:22.176773
# Unit test for function find
def test_find():
    test_file = open('test_find.txt', 'r')
    t = ast.parse(test_file.read())
    test_file.close()
    res = list(find(t, ast.Import))
    expected_list = ["import os", "import sys"]
    assert len(res) == 2
    for i in range(len(res)):
        assert (res[i].names[0].name == expected_list[i])


# Generated at 2022-06-14 03:03:26.994712
# Unit test for function find
def test_find():
    import astor
    source = """def hello(name):
    print("Hello {}".format(name))

hello("world")
"""
    tree = ast.parse(source)
    nodes = find(tree, ast.Str)
    assert "world" in [astor.to_source(node) for node in nodes]

# Generated at 2022-06-14 03:03:39.499881
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    TREE = ast.parse('''
        for i in range(0):
            for j in range(1):
                pass

        if 0 == 1:
            if 2 == 3:
                pass
    ''')
    parents = []
    nodes = []
    for node in ast.walk(TREE):
        nodes.append(node)
        parents.append(get_non_exp_parent_and_index(TREE, node))

    assert parents[0][1] == 0
    assert parents[0][0] is TREE
    assert parents[1][1] == 0
    assert parents[1][0] is parents[0][0].body[0]
    assert parents[2][1] == 0
    assert parents[2][0] is parents[1][0].body[0]

# Generated at 2022-06-14 03:03:49.902728
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    mod = ast.parse("""
    def test1(a, b):
        a = 1
        b = 2
        def test2(c, d):
            return 1
    """)
    node = ast.parse("a = 1").body[0]
    assert isinstance(get_closest_parent_of(mod, node, ast.FunctionDef), ast.FunctionDef)
    node = ast.parse("def test2(c, d): return 1").body[0]
    assert isinstance(get_closest_parent_of(mod, node, ast.Module), ast.Module)
    node = ast.parse("return 1").body[0]
    assert isinstance(get_closest_parent_of(mod, node, ast.FunctionDef), ast.FunctionDef)

# Generated at 2022-06-14 03:03:53.482244
# Unit test for function find
def test_find():
    node = ast.parse('import math;x = math.sin(2)')
    res = list(find(node, ast.Name))
    assert res == [ast.Name(id='math', ctx=ast.Load(), lineno=1, col_offset=7)]

# Generated at 2022-06-14 03:03:59.027029
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    x = 3
    y = 4
    z = 5
    q = 6
    # z = 6

    tree = ast.parse("""
    for i in range(x):
        for j in range(y):
            z = q
    """).body[0]

    parent, index = get_non_exp_parent_and_index(tree, tree.body[0].body[0].body[0])

    assert isinstance(parent, ast.For)
    assert parent == tree.body[0].body[0]
    assert index == 0

# Generated at 2022-06-14 03:04:08.368774
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    class Obj:
        pass

    obj = Obj()
    obj.a = Obj()

    obj.b = [Obj(), Obj(), Obj(), Obj(), Obj(), Obj(), Obj(), Obj()]

    obj.b[2].c = [Obj(), Obj(), Obj()]
    obj.b[3].c = [Obj(), Obj(), Obj()]
    obj.b[4].c = [Obj(), Obj(), Obj()]
    obj.b[5].c = [Obj(), Obj(), Obj()]

    obj.d = list(range(10))

    print(get_non_exp_parent_and_index(obj, obj.b[2].c[1]))

# Generated at 2022-06-14 03:04:09.538109
# Unit test for function get_non_exp_parent_and_index

# Generated at 2022-06-14 03:04:11.894729
# Unit test for function find
def test_find():
    tree = ast.parse('print("Hello")')
    nodes = find(tree, ast.Call)
    for node in nodes:
        assert isinstance(node, ast.Call)

# Generated at 2022-06-14 03:04:15.424018
# Unit test for function find
def test_find():
    import doctest, asttools
    failed, total = doctest.testmod(asttools)
    assert failed == 0, "Failed {}/{} tests".format(failed,total)

# Generated at 2022-06-14 03:04:18.116378
# Unit test for function get_parent
def test_get_parent():
    code = 'for i in range(10):'
    root = ast.parse(code)

    for_node = None
    for node in ast.walk(root):
        if isinstance(node, ast.For):
            for_node = node

    assert get_parent(root, for_node)



# Generated at 2022-06-14 03:04:20.988402
# Unit test for function find
def test_find():
    tree = ast.parse('a = 1')
    print(list(find(tree, ast.AST)))
    print(list(find(tree, ast.Assign)))



# Generated at 2022-06-14 03:04:30.539796
# Unit test for function find
def test_find():
    import astor
    source = "def foo():\n    x = 1\n    print(x)"
    tree = ast.parse(source)

    for node in find(tree, ast.Name):
        print(astor.to_source(node))
    # x
    # x



# Generated at 2022-06-14 03:04:32.064542
# Unit test for function get_non_exp_parent_and_index

# Generated at 2022-06-14 03:04:35.827189
# Unit test for function find
def test_find():
    tree_str = "def f():\n  print('hello world')"
    tree = ast.parse(tree_str)
    result = list(find(tree, ast.FunctionDef))
    assert len(result) == 1
    assert result[0].name == "f"

# Generated at 2022-06-14 03:04:37.850598
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    import astor

# Generated at 2022-06-14 03:04:42.755003
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    node = ast.Expr(value=ast.Num(n=1))
    parent = ast.Expr(value=ast.BinOp(
        left=ast.Num(n=1), op=ast.Add(lineno=1, col_offset=7), right=node))
    assert get_non_exp_parent_and_index(parent, node) == (parent, 0)

# Generated at 2022-06-14 03:04:55.666671
# Unit test for function replace_at
def test_replace_at():
    class A(ast.AST):
        _fields = ('body',)

    class B(ast.AST):
        pass

    class C(ast.AST):
        pass

    class D(ast.AST):
        pass

    class E(ast.AST):
        pass

    a = A()
    b = B()
    c = C()
    d = D()
    e = E()

    a.body = [b]
    replace_at(0, a, c)
    assert a.body == [c]

    a.body = [b, d]
    replace_at(1, a, e)
    assert a.body == [b, e]

# Generated at 2022-06-14 03:04:59.470005
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    # Non-Exp parrent
    class Parent:
        def body():
            pass

    class Child:
        pass
    tree = Parent()
    node = Child()
    get_non_exp_parent_and_index(tree, node)

# Generated at 2022-06-14 03:05:06.973919
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    class A(ast.AST):
        _fields = ("a", "b", "body")

    a = A(a=ast.Num(n=1), b=ast.Num(n=2), body=[ast.Num(n=2), ast.Num(n=2)])

    print(get_non_exp_parent_and_index(a, a.b))
    print(get_non_exp_parent_and_index(a, a.body[1]))
    print(get_non_exp_parent_and_index(a, a.body[0]))


# Generated at 2022-06-14 03:05:11.047593
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    code = 'a + b + c'
    module = ast.parse(code)

    i = len(module.body) - 1

    while i >= 0:
        if isinstance(module.body[i], ast.Expr):
            break
        i -= 1

    parent, index = get_non_exp_parent_and_index(module, module.body[i])
    assert module.body[index] == module.body[i]
    assert module.body[index + 1] == parent.body[index]  # type: ignore

# Generated at 2022-06-14 03:05:18.067029
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    tree = ast.parse("""\
import datetime
if (1==1)\
    print("hi")""")
    parent_and_index = get_non_exp_parent_and_index(tree, tree.body[0])
    parent = parent_and_index[0]
    expected_parent = tree.body
    assert parent == expected_parent, "Parent is not same as expected"
    index = parent_and_index[1]
    expected_index = 0
    assert index == expected_index, "Index is not same as expected"


# Generated at 2022-06-14 03:05:41.615444
# Unit test for function find
def test_find():
    assert list(find(ast.parse('a = 1'), ast.Assign)) == [
        ast.Assign(targets=[ast.Name(id='a', ctx=ast.Store())],
                   value=ast.Num(n=1))]
    assert list(find(ast.parse('a = 1'), ast.Num)) == [
        ast.Num(n=1)]
    assert list(find(ast.parse('a = 1'), ast.Store)) == []
    assert list(find(ast.parse('a = 1'), ast.AST)) == [
        ast.Assign(targets=[ast.Name(id='a', ctx=ast.Store())],
                   value=ast.Num(n=1))]



# Generated at 2022-06-14 03:05:43.723920
# Unit test for function find
def test_find():
    source = """
    for i in range(10):
        pass
    """
    tree = ast.parse(source)
    for_loop = tree.body[0]
    assert for_loop == list(find(tree, ast.For))[0]

# Generated at 2022-06-14 03:05:47.345853
# Unit test for function get_parent
def test_get_parent():
    def foo():
        foo()

    tree = ast.parse(dedent(inspect.getsource(foo)))
    tree.body[0].body[0].func.parent = None  # type: ignore
    parent = get_parent(tree, tree.body[0].body[0].func)
    assert parent == tree.body[0].body[0]

# Generated at 2022-06-14 03:05:53.071213
# Unit test for function find
def test_find():
    import os
    import ast
    import sys
    import inspect

    filename = os.path.abspath(inspect.getsourcefile(sys.modules[__name__]))
    tree = ast.parse(open(filename).read())
    print(list(find(tree, ast.FunctionDef)))
    print(list(find(tree, ast.Call)))
    print(list(find(tree, ast.Name)))


if __name__ == '__main__':
    test_find()

# Generated at 2022-06-14 03:06:00.208902
# Unit test for function find

# Generated at 2022-06-14 03:06:01.625039
# Unit test for function get_closest_parent_of

# Generated at 2022-06-14 03:06:12.656914
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    # case 1: a function definition has function and Module as parents,
    # if we want to get the closest parent that is of type FunctionDef,
    # then we will get the only FunctionDef node.
    t = ast.parse("""
    def abc():
        print('in abc')
    """)
    abc = t.body[0]
    assert isinstance(get_closest_parent_of(t, abc, ast.FunctionDef), ast.FunctionDef)
    assert not isinstance(get_closest_parent_of(t, abc, ast.Module), ast.Module)

    # case 2: a function call has a function definition as parent, and module
    # as grandparent. If we want to get the closest parent that is of type Module,
    # then we will get the only Moudle node.


# Generated at 2022-06-14 03:06:20.088275
# Unit test for function find
def test_find():
    test = ast.parse('import os; import sys; x = 1; y = 2;')
    imports = list(find(test, ast.Import))
    assert len(imports) == 2
    assert imports[0].names[0].name == 'os'
    assert imports[1].names[0].name == 'sys'

    assigns = list(find(test, ast.Assign))
    assert len(assigns) == 2
    assert assigns[0].targets[0].id == 'x'
    assert assigns[1].targets[0].id == 'y'

# Generated at 2022-06-14 03:06:32.363469
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    test_string = """
    def foo(x):
        return x
    """

    py_ast = ast.parse(test_string)  # type: ignore
    non_exp_parent, child_index = get_non_exp_parent_and_index(py_ast, py_ast.body[0])

    assert isinstance(non_exp_parent, ast.Module)
    assert child_index == 0

    test_string = """
    def foo(x):
        if x == 5:
            return x
    """

    py_ast = ast.parse(test_string)  # type: ignore
    non_exp_parent, child_index = get_non_exp_parent_and_index(py_ast, py_ast.body[0].body[0])


# Generated at 2022-06-14 03:06:35.769547
# Unit test for function find
def test_find():
    from typed_ast.ast3 import Assign, Name, expr
    tree = Assign(targets=[Name('x', expr)], value=Name('y', expr))
    assert list(find(tree, Name)) == [Name('x', expr), Name('y', expr)]

# Generated at 2022-06-14 03:06:52.081021
# Unit test for function find

# Generated at 2022-06-14 03:07:02.572261
# Unit test for function replace_at

# Generated at 2022-06-14 03:07:07.448516
# Unit test for function find
def test_find():
    """
    Unit test to check that function find gets all the nodes in an AST of the
    required type
    """
    assert list(find(ast.parse("import numpy as np\nimport os"), ast.Import)) == \
            [ast.parse("import numpy as np", mode='exec').body[0],
             ast.parse("import os", mode='exec').body[0]]
    assert list(find(ast.parse("a = 2\nb = 2"), ast.Assign)) == \
            [ast.parse("a = 2", mode='exec').body[0]]

# Generated at 2022-06-14 03:07:10.894266
# Unit test for function find
def test_find():
    from typed_ast import ast3 as ast
    tree = ast.parse('a = 2')
    assert [n.id for n in find(tree, ast.Name)] == ['a']


# Generated at 2022-06-14 03:07:13.438294
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    tree = ast.parse('def func(): pass')
    assert get_closest_parent_of(tree, tree.body[0], ast.FunctionDef) == tree.body[0]

# Generated at 2022-06-14 03:07:25.873363
# Unit test for function replace_at
def test_replace_at():
    # Define sample code:
    code = """
        # Define a function
        def test_func(num):
            if num == 0:
                print(0)
            elif num == 1:
                print(1)
            else:
                print(2)
        """

    # Parse AST
    parsed = ast.parse(code)

    # Find the "if" statement
    if_stmt = find(parsed, ast.If).__next__()  # type: ignore

    # Find the "else" statement
    else_stmt = find(parsed, ast.If).__next__().orelse[0]  # type: ignore

    # Insert "print(3)" into "else" statement
    new_stmt = ast.parse("print(3)")

# Generated at 2022-06-14 03:07:32.056080
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    from typed_ast import ast3 as ast

    tree = ast.parse("""
    def test(a):
        for i in range(10):
            for j in range(10):
                a = i
    """)

    assert isinstance(get_closest_parent_of(tree, tree.body[0].body[0].body[0].body[0].value, ast.FunctionDef), ast.FunctionDef)


# Generated at 2022-06-14 03:07:41.927914
# Unit test for function get_parent
def test_get_parent():
    # type: () -> None
    code1 = "print('Hello World')"
    tree1 = ast.parse(code1)
    node1 = tree1.body[0].value  # 'Hello World'
    parent1 = tree1.body[0]

    assert get_parent(tree1, node1) is parent1

    code2 = "def foo():\n    print('Hello World')"
    tree2 = ast.parse(code2)
    node2 = tree2.body[0].body[0].value  # 'Hello World'
    parent2 = tree2.body[0].body[0]

    assert get_parent(tree2, node2) is parent2


# Generated at 2022-06-14 03:07:43.270955
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    import astor

# Generated at 2022-06-14 03:07:46.806775
# Unit test for function find
def test_find():
    txt = "min(a, b) + max(c, d)"
    tree = ast.parse(txt)
    for call_ in find(tree, ast.Call):
        print(call_.args)

# Generated at 2022-06-14 03:08:27.448750
# Unit test for function find
def test_find():
    code = open('example.py', 'r').read()
    tree = ast.parse(code)
    number_of_functions = len(list(find(tree, ast.FunctionDef)))
    assert number_of_functions == 4

# Generated at 2022-06-14 03:08:37.028933
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    import astor
    a = ast.parse("""def a():
    if x == 0:
        if y == 1:
            a = 1
            b = 2
            c = 3
        else:
            a = 1
            b = 2
    elif x == 1:
        if y == 0:
            a = 1
            b = 2
        else:
            a = 1
            b = 2
    else:
        if y == 0:
            a = 1
            b = 2
        else:
            a = 1
            b = 2
""")
    # For example, our goal is insert a = 1 before `b = 2`
    # So, we must find the parent of `b = 2`.
    # The parent of `b = 2` is `Assign()`
    # The parent of `Assign()`

# Generated at 2022-06-14 03:08:48.379689
# Unit test for function replace_at
def test_replace_at():
    root = ast.parse("def foo():\n    x = 1 + 2 + 3")
    parent = get_closest_parent_of(root, node=root.body[0].body[0],
                                   type_=ast.FunctionDef)
    node = parent.body[0]
    assert isinstance(node, ast.Assign)
    assert len(parent.body) == 1
    assert ast.dump(node) == "Assign(targets=[Name(id='x', ctx=Store())], " \
                             "value=BinOp(left=BinOp(left=Num(n=1), " \
                             "op=Add(), right=Num(n=2)), op=Add(), right=Num(n=3)))"

# Generated at 2022-06-14 03:09:00.221541
# Unit test for function get_non_exp_parent_and_index

# Generated at 2022-06-14 03:09:10.308197
# Unit test for function get_parent
def test_get_parent():
    t1 = ast.parse('from math import  sqrt\nsqrt(5)')
    t2 = ast.parse('from math import \nsqrt\nsqrt(5)')

    assert get_parent(t1, t1) is None
    assert isinstance(get_parent(t1, t1.body[0]), ast.Module)
    assert isinstance(get_parent(t2, t2.body[1]), ast.Module)
    assert isinstance(get_parent(t2, t2.body[1].names[0]), ast.ImportFrom)
    assert isinstance(get_parent(t2, t2.body[1].names[0]), ast.ImportFrom)
    assert isinstance(get_parent(t2, t2.body[2].func), ast.Name)

# Generated at 2022-06-14 03:09:15.315837
# Unit test for function find
def test_find():
    def for_test():
        pass

    def for_test2():
        print(1)
        for_test()

    tree = ast.parse(inspect.getsource(for_test2))

    functions = list(find(tree, ast.FunctionDef))

    assert for_test2 == functions[-1]
    assert for_test == functions[0]



# Generated at 2022-06-14 03:09:19.287736
# Unit test for function get_parent
def test_get_parent():
    tree = ast.parse('def f(x: int = None, *y) -> None:\n  pass\n  pass')
    _build_parents(tree)
    node = tree.body[0].body[0]


# Generated at 2022-06-14 03:09:25.063806
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    # Given
    code = """def f():
    if True:
        print(1)
        return
    print(0)

if __name__ == '__main__':
    f()
    """
    expected_node_type = ast.FunctionDef
    module = ast.parse(code)
    # When
    node = module.body[0].body[0].body[0]
    result = get_closest_parent_of(module, node, expected_node_type)
    # Then
    assert isinstance(result, expected_node_type)

# Generated at 2022-06-14 03:09:30.640234
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    tree = ast.parse(
        """
        def foo():
            for i in range(10):
                if i == 5:
                    print(5)
        """
    )
    node = tree.body[0].body[0].body[0].body[0]
    assert isinstance(get_co_closest_parent_of(tree, node, ast.While), ast.While)

# Generated at 2022-06-14 03:09:45.860668
# Unit test for function get_parent
def test_get_parent():
    from typing import List
    from .mock_ast import AstMock

    tree = AstMock.get_module()
    assert isinstance(get_parent(tree, tree), ast.Module)
    assert isinstance(get_parent(tree, tree.body[0]), ast.Module)
    assert isinstance(get_parent(tree, tree.body[0].body[0]), ast.FunctionDef)
    assert isinstance(get_parent(tree,
                                 tree.body[0]
                                 .body[0]
                                 .body[0]
                                 .body[0]
                                 .orelse[0]
                                 .body[0]
                                 .body[0]
                                 .body[0]
                                 .value),
                      ast.Call)

# Generated at 2022-06-14 03:11:06.984180
# Unit test for function find
def test_find():
    pass

# Generated at 2022-06-14 03:11:21.425003
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    # Test with a For node
    for_node = ast.For(ast.Name('x', ast.Store()), ast.Name('x', ast.Load()),
                       [], [])
    target_node = ast.Name('x', ast.Store())
    parent, index = get_non_exp_parent_and_index(for_node, target_node)
    assert(isinstance(parent, ast.For))
    assert(index == 0)

    # Test with an If node
    if_node = ast.If(ast.Name('x', ast.Load()), [for_node], [])
    target_node = for_node
    parent, index = get_non_exp_parent_and_index(if_node, target_node)
    assert(isinstance(parent, ast.If))

# Generated at 2022-06-14 03:11:28.685208
# Unit test for function find
def test_find():
    """Unit test for the function find."""
    import random
    import string
    import os
    import astor
    import tempfile

    with open(os.path.join(os.path.dirname(__file__),
                           'test_find.py.py.txt')) as f:
        source = f.read()

    temp_dir = tempfile.mkdtemp()
    temp_file = os.path.join(temp_dir, 'test.py')
    with open(temp_file, 'w', encoding='utf-8') as f:
        f.write(source)

    with open(temp_file, 'r', encoding='utf-8') as f:
        tree = ast.parse(f.read())
