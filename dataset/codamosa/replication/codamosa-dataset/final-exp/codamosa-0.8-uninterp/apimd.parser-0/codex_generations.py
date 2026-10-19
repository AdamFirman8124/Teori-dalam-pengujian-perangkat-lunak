

# Generated at 2022-06-13 17:46:31.387635
# Unit test for method class_api of class Parser

# Generated at 2022-06-13 17:46:42.504145
# Unit test for method func_api of class Parser
def test_Parser_func_api():
    p = Parser()
    func = FunctionDef(arguments(args=[],
                                 vararg=arg('a', None),
                                 kwonlyargs=[arg('b', int)],
                                 kw_defaults=[NameConstant(None)],
                                 kwarg=arg('c', None)),
                        returns=int)
    body = p.func_ann('m', func.args, has_self=True, cls_method=True)
    body = list(body)
    assert body[0] == 'type[Self]'
    assert body[1] == '...'
    assert body[2] == 'int'
    assert body[3] == 'int'
    assert body[4] == '...'
    assert body[5] == 'int'
    assert body[6] == 'int'



# Generated at 2022-06-13 17:46:51.556515
# Unit test for method compile of class Parser
def test_Parser_compile():
    p = Parser(DEFAULT_FILE_CONTENT,
               "test.py",
               DEFAULT_LINK,
               DEFAULT_TOC)
    res = p.compile()
    assert re.search(r'\+ \[test\.test\.test\(\)', res) is not None
    assert re.search(r'### test.test.test\(\)', res) is not None
    assert re.search(r'\+ \[test\.test\.Test', res) is not None
    assert re.search(r'#### class test.test.Test', res) is not None
    assert re.search(r'@test\.test\.annotation', res) is None

# }}}

# Parser {{{
# Build documentation from module and return as string

# Generated at 2022-06-13 17:46:59.181471
# Unit test for method visit_Subscript of class Resolver
def test_Resolver_visit_Subscript():
    """Test function: test_Resolver_visit_Subscript."""
    resolver = Resolver('typing', {})
    node1 = Subscript(
        Name('typing', Load()),
        Slice(Name('typing', Load()), Name('typing', Load()), None),
        Load())
    node2 = Subscript(
        Name('typing', Load()),
        Slice(Name('typing', Load()),
              Subscript(Name('typing', Load()),
                        Slice(Name('typing', Load()), Name('typing', Load()), None),
                        Load()), None), Load())
    ast1 = resolver.visit(node1)
    ast2 = resolver.visit(node2)
    assert ast1 == node1
    assert ast2 == node1


# Generated at 2022-06-13 17:47:06.201550
# Unit test for function walk_body
def test_walk_body():
    """Unit test for function walk_body."""
    # pylint: disable=no-value-for-parameter
    code = """
if True:
    a = 1
else:
    b = 2
    try:
        print(1)
    except:
        print(2)
    finally:
        print(3)
    """
    body = parse(code).body
    assert len(list(walk_body(body))) == 9
test_walk_body()



# Generated at 2022-06-13 17:47:12.393630
# Unit test for method visit_Subscript of class Resolver
def test_Resolver_visit_Subscript():
    cases = (
        ('typing.Union[int, str]', 'Union[int, str]'),
        ('typing.Optional[int]', 'Union[int, None]'),
        ('typing.Type[int]', 'Type[int]'),
        ('int.__mro__.__next__', 'Any')
    )
    for given, expected in cases:
        resolver = Resolver('any_namespace', PEP585)
        node = cast(Subscript, parse(given).body[0].value)
        result = resolver.visit(node)
        assert unparse(result) == expected



# Generated at 2022-06-13 17:47:19.155039
# Unit test for method visit_Name of class Resolver
def test_Resolver_visit_Name():
    foo_bar = parse("foo_bar").body[0]
    assert isinstance(foo_bar, Expr)
    assert isinstance(foo_bar.value, Name)
    assert foo_bar.value.id == "foo_bar"
    assert Resolver(root="test", alias=dict()).visit(foo_bar) == foo_bar

    c = parse("abs").body[0]
    assert isinstance(c, Expr)
    assert isinstance(c.value, Name)
    assert c.value.id == "abs"
    d = Resolver(root="test", alias=dict()).visit(c)
    assert isinstance(d, Expr)
    assert isinstance(d.value, Name)
    assert d.value.id == "abs"

    c = parse("T").body[0]

# Generated at 2022-06-13 17:47:25.690710
# Unit test for method load_docstring of class Parser
def test_Parser_load_docstring():
    import types

    class a():
        x: int
        def f(self): ...

    class b(a):
        def f(self) -> None: ...

    m = types.ModuleType("test")
    m.a, m.b = a, b

    p = Parser(link=False)
    p.api('test', type_hint(a))
    p.api('test', type_hint(b))
    p.load_docstring('test', m)
    exp = 'class a:\n\n*Full name:* `test.a`\n'
    act = p.doc['test.a']
    assert act == exp, f"Expected {exp}, but got {act}"

# Generated at 2022-06-13 17:47:33.973448
# Unit test for method compile of class Parser
def test_Parser_compile():
    assert Parser('').compile() == '\n'
    assert Parser('a').compile() == '\n'

# Generated at 2022-06-13 17:47:40.473925
# Unit test for method func_api of class Parser
def test_Parser_func_api():
    r = Parser(True)
    r.func_api('root', 'root.*', arguments(args=[], vararg=arg('args', None)),
               None, has_self=False, cls_method=False) == (
                   "root.\\*(args: *args, return: Any)   \n:   \n\n"
                   "*Full name:* `root.*`\n"
                   "<a id=\"root.\"></a>\n\n"
                   "|Arguments|Type        |\n"
                   "|-|-|\n"
                   "|args|*args|\n"
                   "|return|Any|\n"
               )

# Generated at 2022-06-13 17:48:39.305329
# Unit test for method globals of class Parser
def test_Parser_globals():
    with mock.patch('sys.path', []):
        import doctester
        import pyglic

    parser = pyglic.Parser(doctester, None, False)

# Generated at 2022-06-13 17:48:48.829966
# Unit test for method api of class Parser
def test_Parser_api():
    # Method docstring
    assert Parser.api.__doc__ == \
    """Create API doc for only functions and classes.
    Where `name` is the full name.
    """
    # Unit test: _ = parser.api(root, node), setup
    # Importing packages
    from pycat.antlr import parse
    from pycat.grammar import convert
    # Case 1
    root = "p1"
    node = parse("def f(): pass")[0]
    parser = Parser()
    parser.api(root, node)
    # Checking parser.doc

# Generated at 2022-06-13 17:48:56.542746
# Unit test for method visit_Name of class Resolver

# Generated at 2022-06-13 17:49:05.355246

# Unit test for method visit_Subscript of class Resolver
def test_Resolver_visit_Subscript():
    res = Resolver('test', {})
    r = res.visit(parse('Union[1, 2, 3, 4]').body[0].value)
    assert unparse(r) == '(1 | (2 | (3 | 4)))'
    r = res.visit(parse('Optional[1]').body[0].value)
    assert unparse(r) == '(1 | None)'
    r = res.visit(parse('List[int]').body[0].value)
    assert unparse(r) == 'List[int]'
    res = Resolver('test', {'test.a': '0'})
    r = res.visit(parse('a').body[0].value)
    assert unparse(r) == '0'
