

# Generated at 2022-06-13 17:44:23.675253
# Unit test for function esc_underscore
def test_esc_underscore():
    """docstring: test for function esc_underscore"""
    assert "foo" == esc_underscore("foo")
    assert r"foo_bar" == esc_underscore("foo_bar")
    assert r"foo\_bar" == esc_underscore(r"foo_bar")



# Generated at 2022-06-13 17:44:34.015355
# Unit test for method visit_Name of class Resolver
def test_Resolver_visit_Name():
    e = Name('Some', Load())
    assert Resolver('', {}).visit(e) is e
    e = Name('self', Load())
    assert Resolver('', {}, 'self').visit(e) is Name('Self', Load())
    e = Name('typing', Load())
    assert Resolver('', {}).visit(e) is e
    e = Name('typing.Callable', Load())
    assert Resolver('', {}).visit(e) is e
    e = Name('typing.Callable', Load())
    assert cast(Name, Resolver('',
                {'a': 'typing.Callable'}).visit(e)).id == 'Callable'
    e = Name('typing.Callable', Load())

# Generated at 2022-06-13 17:44:39.166608
# Unit test for method func_api of class Parser
def test_Parser_func_api():
    p = Parser()
    root = "Ba"
    name = "Baz"
    node = parse("def foo(a: A, *b, c: C = 0, d: D = 1, **e): ...",
                 mode="single").body[0]
    p.func_api(root, name, node.args, None)

# Generated at 2022-06-13 17:44:42.837402
# Unit test for function esc_underscore
def test_esc_underscore():
    assert esc_underscore('_') == '_'
    assert esc_underscore('__') == r'\_\_'
    assert esc_underscore('test_test') == r'test\_test'
    assert esc_underscore('test_test_test') == r'test\_test\_test'



# Generated at 2022-06-13 17:44:50.112945
# Unit test for method func_ann of class Parser
def test_Parser_func_ann():
    parser = Parser(level=0, link=False, toc=False,
                    strict=True, type_hints=True)
    # Test for call of func_ann method
    def func(p, n, a, *, opt=None):
        return None
    args = [arg('param', None), arg('*args', None)]
    anns = list(parser.func_ann('name', args))
    assert anns == ['param', 'List[Any]'], "Test failed"
    args = [arg('param', None), arg('*args', None),
            arg('kwargs', None)]
    anns = list(parser.func_ann('name', args))
    assert anns == ['param', 'List[Any]', 'Dict[str, Any]'], "Test failed"
    # Test for call of func_

# Generated at 2022-06-13 17:44:56.264784
# Unit test for method class_api of class Parser
def test_Parser_class_api():
    def check(bases: list[expr], body: list[stmt], *,
              expect: str) -> None:
        root, node = 'root', ClassDef('cls', bases, body)
        parser, _ = Parser(None), dict()
        parser.class_api(root, root, node)
        assert parser.doc[root] == expect
    check([], [], expect="""\
#### class cls

*Full name:* `root`

""")

# Generated at 2022-06-13 17:45:06.720405
# Unit test for function walk_body
def test_walk_body():
    code_body = '''\
# Test if.
if a:
    if b:
        c = d
    else:
        e = f
    g = h
else:
    i = j
# Test try.
try:
    if c:
        d = e
    else:
        f = g
    h = i
except Exception:
    j = k
except ValueError:
    l = m
else:
    if n:
        o = p
    else:
        q = r
    s = t
finally:
    u = v
a = b
'''
    code_body = [s for s in walk_body(ast_parse(code_body).body) if isinstance(s, Assign)]
    assert len(code_body) == 10
# End of the unit test



# Generated at 2022-06-13 17:45:15.195922
# Unit test for method compile of class Parser
def test_Parser_compile():
    def do_test(*, code) -> str:
        code = inspect.cleandoc(code)
        with tempfile.TemporaryDirectory() as tmpdir_name:
            with open(tmpdir_name + '/test.py', 'w') as f:
                f.write(code)
            p = Parser(tmpdir_name)
            return p.compile()
    test_case(
        do_test,
        None,
        src="""
        def f(x): ...
        """,
        expected="""<BLANKLINE>""",
    )
    test_case(
        do_test,
        None,
        src="""
        f = lambda x: ...
        """,
        expected="""<BLANKLINE>""",
    )

# Generated at 2022-06-13 17:45:20.826729
# Unit test for method func_api of class Parser
def test_Parser_func_api():
    p = Parser()
    p.func_api('__main__', '__main__.f', arguments(
        [], [arg('x', ast_parse('str'))], None, [], []),
        ast_parse('typing.List[str]'), has_self=False, cls_method=False)
    assert p.doc == {
        '__main__.f': '# f()\n\n*Full name:* `__main__.f`\n\n'
                      '| x | |\n'
                      '| - | - |\n'
                      '| `str` | |\n'
                      '| `return` | `typing.List[str]` |'
                      '\n\n'
    }
    p.doc.clear()

# Generated at 2022-06-13 17:45:28.897902
# Unit test for method func_api of class Parser
def test_Parser_func_api():
    """Test method func_api of class Parser."""
    import pytest
    from pytypeutils import typeassert
    from lark import Tree, Token
    from xotl.tools.objects import AttrDict

    p = Parser(None, None, None)
    func_def = AttrDict(name='f', args=arguments(args=[], defaults=[]),
                        body=[], decorator_list=[], returns=None, type_comment=None,
                        lineno=3, col_offset=5, end_lineno=3, end_col_offset=6)
    alias = {'a': 'ast.Name'}
    root = 'mod.f'
    name = 'mod.f'

    # no type comment, no type annotation
    args = [arg('a', None), arg('return', None)]

# Generated at 2022-06-13 17:46:27.134118
# Unit test for method visit_Subscript of class Resolver

# Generated at 2022-06-13 17:46:35.543117
# Unit test for method func_ann of class Parser
def test_Parser_func_ann():
    args = [
        arg('self', None),
        arg('a', None),
        arg('b', None),
        arg('*args', None),
        arg('kwargs', None),
        arg('return', None),
    ]
    p = Parser(load_plugins=False)
    assert list(p.func_ann('a', args, has_self=False, cls_method=False)) == [
        '', '', '', '', '', '',
    ]
    assert list(p.func_ann('a', args, has_self=True, cls_method=False)) == [
        'Self', '', '', '', '', '',
    ]

# Generated at 2022-06-13 17:46:43.678318
# Unit test for method is_public of class Parser
def test_Parser_is_public():
    """Test is_public"""
    parser = Parser([])
    parser.imp['import'] = {'import'}
    # Test whether the names in the __all__ is public
    assert parser.is_public('import')
    assert parser.is_public('import.name')
    # Test whether the names in __all__ are public
    assert parser.is_public('import.__all__')
    assert parser.is_public('import.__all__.name')
    # Test whether the names are public
    assert parser.is_public('import.a')
    assert parser.is_public('import.b')
    assert parser.is_public('import.c')
    logger.info("Method is_public tested.")


# Generated at 2022-06-13 17:46:53.398098
# Unit test for method visit_Subscript of class Resolver
def test_Resolver_visit_Subscript():
    """Unit test for method visit_Subscript of class Resolver."""
    rzr = Resolver("random", {})
    assert unparse(rzr.visit(Subscript(Name("Union", Load()),
                                       Tuple(elts=[Constant(1), Constant(2)], ctx=Load()), Load()))) == 'Union[1, 2]'
    assert unparse(rzr.visit(Subscript(Name("Optional", Load()), Constant("a"), Load()))) == 'v = a or None'
    assert unparse(rzr.visit(Subscript(Name("abc", Load()), Constant("a"), Load()))) == 'abc["a"]'

    rzr = Resolver("random", {"random.abc": "typing.Union"})

# Generated at 2022-06-13 17:47:00.217695
# Unit test for method is_public of class Parser
def test_Parser_is_public():
    """Unit test for method is_public of class Parser."""
    p = Parser()
    p.doc['a.b.c'] = ""
    p.root['a.b.c'] = 'a.b'
    p.imp['a.b'] = {'a.b.c'}
    assert p.is_public('a')
    assert p.is_public('a.b')
    assert p.is_public('a.b.c')
    p.imp['a.b'] = set()
    assert not p.is_public('a.b')
    assert not p.is_public('a.b.c')
    p.doc['a.b.d'] = ""
    p.root['a.b.d'] = 'a.b'

# Generated at 2022-06-13 17:47:09.208732
# Unit test for method visit_Name of class Resolver
def test_Resolver_visit_Name():
    assert Resolver("", {}, "").visit(Name("Type", Load())) == Name("Type", Load())
    assert Resolver("", {"Type": "int"}, "").visit(Name("Type", Load())) == Name("int", Load())
    assert Resolver("", {}, "").visit(Name("Self", Load())) == Name("Self", Load())
    assert Resolver("", {}, "typing").visit(Name("Self", Load())) == Name("typing", Load())
    assert Resolver("", {}, "Self").visit(Name("Type", Load())) == Name("Type", Load())
    assert Resolver("", {"Type": "int"}, "Self").visit(Name("Type", Load())) == Name("int", Load())


# Generated at 2022-06-13 17:47:13.456473
# Unit test for method func_ann of class Parser
def test_Parser_func_ann():
    p = Parser()
    assert list(p.func_ann('_', [arg('*', None), arg('a', None)])) == ['', ANY]
    assert list(p.func_ann('_', [arg('a', Name('A', Load())),
                                 arg('b', Name('B', Load()))])) == ['A', 'B']

# Generated at 2022-06-13 17:47:20.222963
# Unit test for method func_ann of class Parser
def test_Parser_func_ann():
    p = Parser(0, {}, {}, {}, {}, True, False)
    assert list(p.func_ann('my_module', [arg('a', None),
                                         arg('b', None),
                                         arg('*', None),
                                         arg('**kw', None),
                                         arg('return', None)])) == ['Any',
                                                                   'Any',
                                                                   '',
                                                                   'Dict[str, Any]',
                                                                   'Any']

# Generated at 2022-06-13 17:47:30.649040
# Unit test for method visit_Name of class Resolver
def test_Resolver_visit_Name():
    import typing
    class A:
        a: typing.List[int]
        b: int
        @property
        def c(self) -> typing.List[float]:
            ...
        @classmethod
        def d(cls, x: int) -> typing.List[complex]:
            ...
    alias = cast(dict[str, str], {k: v for k, v in A.__annotations__.items()})
    root = 'test_Resolver_visit_Name'
    r = Resolver(root, alias, 'A')
    # Type inferrence
    assert parse('typing.List[int]').body[0] == r.visit(parse('a').body[0])
    assert parse('typing.List[float]').body[0] == r.visit(parse('c').body[0])

# Generated at 2022-06-13 17:47:37.431753
# Unit test for method func_ann of class Parser
def test_Parser_func_ann():
    p = Parser()
    p.root["a"] = ""
    p.alias["a"] = ""
    p.alias["b"] = ""
    p.alias["c"] = ""
    p.alias["d"] = ""
    p.alias["e"] = ""
    p.alias["f"] = ""
    p.alias["g"] = ""
    p.alias["h"] = ""
    p.alias["i"] = ""
    p.alias["j"] = ""
    p.alias["k"] = ""
    p.alias["l"] = ""
    p.alias["m"] = ""
    p.alias["n"] = ""
    p.alias["o"] = ""
    p.alias["p"] = ""
    p.alias["q"] = ""
    p.alias["r"] = ""
    p