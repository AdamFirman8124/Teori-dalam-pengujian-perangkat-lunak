

# Generated at 2022-06-13 17:42:36.358251
# Unit test for method parse of class Parser
def test_Parser_parse():
    """Some unit test for method `parse`"""
    parser = Parser()

# Generated at 2022-06-13 17:42:46.743259
# Unit test for function doctest
def test_doctest():
    assert doctest(">>> print(1)") == "\n".join([
        "```python",
        ">>> print(1)",
        "```"
    ])
    assert doctest(">>> print(1)\n    print(1)") == "\n".join([
        "```python",
        ">>> print(1)",
        "    print(1)",
        "```"
    ])
    assert doctest(">>> print(1)\n    print(1)\n>>> print(2)") == "\n".join([
        "```python",
        ">>> print(1)",
        "    print(1)",
        "",
        ">>> print(2)",
        "```"
    ])

# Generated at 2022-06-13 17:42:53.096733
# Unit test for method compile of class Parser
def test_Parser_compile():
    def test(src: str, exp: str) -> None:
        with TemporaryDirectory() as root:
            mod = from_source(src, root, 'test')
            doc = Parser(root, full=True).compile()
            assert doc == exp


# Generated at 2022-06-13 17:43:01.392995
# Unit test for method visit_Name of class Resolver
def test_Resolver_visit_Name():
    r = Resolver("root", {
        "x": "y",
        "root.x": "n",
        "root.n": "o",
        "root.o": "y",
        "root.a.b": "c"
    })
    assert r.visit(parse("x").body[0]) == parse("y").body[0], "not root"
    assert r.visit(parse("a.b").body[0]) == parse("c").body[0], "not root"
    assert r.visit(parse("n").body[0]) == parse("o").body[0]
    assert r.visit(parse("o").body[0]) == parse("y").body[0]
    assert r.visit(parse("x").body[0]) == parse("y").body[0]
   

# Generated at 2022-06-13 17:43:06.775992
# Unit test for method api of class Parser
def test_Parser_api():

    try:
        import pytest

        @pytest.fixture
        def s(capsys):
            yield lambda *a, **kw: capsys.readouterr().out.strip()
    except ImportError:
        from unittest.mock import patch

        @patch('sys.stdout')
        def s(mock_stdout):
            def assert_stdout(s):
                assert mock_stdout.getvalue().strip() == s
            yield assert_stdout
    from datetime import datetime

    p = Parser((), link=False)
    p.add_from_module(datetime)
    assert (s(p.doc['datetime.datetime']) == '# datetime()')

# Generated at 2022-06-13 17:43:14.648581
# Unit test for method api of class Parser
def test_Parser_api():
    class C(object):
        """Test Class."""
        def __init__(self, x: int, y: int) -> None:
            self.x = x
            self.y = y
        def __call__(self, z: int) -> int:
            return self.x + self.y + z
        def __add__(self, other: "C") -> "C":
            if other is None:
                return C(self.x, self.y)
            return C(self.x + other.x, self.y + other.y)
        def __repr__(self) -> str:
            return "C({}, {})".format(self.x, self.y)
        a = C(1, 2)
        b = C(3, 4)
        c = a + b

# Generated at 2022-06-13 17:43:25.452506
# Unit test for function walk_body
def test_walk_body():
    @dataclass
    class _TestBody:
        """Fake AST node."""
        body: list
        orelse: list
        handlers: list
        finalbody: list

    @dataclass
    class _TestAST:
        """Fake AST node."""
        body: list

    @dataclass
    class _TestASTElse:
        """Fake AST node."""
        body: list
        orelse: list

    @dataclass
    class _TestASTTry(Try):
        """Fake AST node."""
        body: list
        orelse: list
        handlers: list
        finalbody: list

    @dataclass
    class _TestHandler:
        """Fake AST node."""
        body: list

    p1 = parse("if a:\n    b", mode='eval')

# Generated at 2022-06-13 17:43:30.171211
# Unit test for function table
def test_table():
    assert table('a', 'b', [['c', 'd'], ['e', 'f']],
                 ['g', [['h', 'i'], 'j']]) == \
        "| a | b |\n"\
        "|:---:|:---:|\n"\
        "| c | d |\n"\
        "| e | f |\n"\
        "| g | h | i |\n"\
        "|   | j |\n"\
        "\n\n"



# Generated at 2022-06-13 17:43:31.580785
# Unit test for method class_api of class Parser
def test_Parser_class_api():
    # Here we check that the types of the attributes are set correctly.
    for attr in Parser.__slots__:
        assert type(getattr(Parser(), attr)) == str  # NoQA



# Generated at 2022-06-13 17:43:39.537308
# Unit test for function esc_underscore
def test_esc_underscore():
    assert esc_underscore('_') == "\\_"
    assert esc_underscore('a') == "a"
    assert esc_underscore('_a') == "\\_a"
    assert esc_underscore('a_') == "a\\_"
    assert esc_underscore('a_b') == "a\\_b"
    assert esc_underscore('aaa') == "aaa"
    assert esc_underscore('a_a_') == "a\\_a\\_"
    assert esc_underscore('__') == "\\_\\_"



# Generated at 2022-06-13 17:46:05.357156
# Unit test for method load_docstring of class Parser
def test_Parser_load_docstring():
    assert Parser().load_docstring('a','a') is None
test_Parser_load_docstring()

# Generated at 2022-06-13 17:46:12.396073
# Unit test for function const_type
def test_const_type():
    assert const_type(parse('1').body[0].value) == 'int'
    assert const_type(parse('1.1').body[0].value) == 'float'
    assert const_type(parse('1j').body[0].value) == 'complex'
    assert const_type(parse('True').body[0].value) == 'bool'
    assert const_type(parse('False').body[0].value) == 'bool'
    assert const_type(parse('None').body[0].value) == 'NoneType'
    assert const_type(parse('["a", "b"]').body[0].value) == 'list[str]'
    assert const_type(parse('{"a", "b"}').body[0].value) == 'set[str]'

# Generated at 2022-06-13 17:46:17.838841
# Unit test for method compile of class Parser
def test_Parser_compile():
    class M(ModuleType):
        __all__ = ('A', 'B', 'C')
        B = int
        C = int

        class A(int):
            pass

# Generated at 2022-06-13 17:46:26.340061
# Unit test for method func_ann of class Parser
def test_Parser_func_ann():
    res = """\
1: func()
2: a, b=<default>, /, *args, c=<default>, *, d=<default>, **kwargs, return: str
"""
    p = Parser('', '', '', '')
    p.alias['self.root'] = '.'
    # Nullable type (Default)
    assert '\n'.join(p.func_ann(
        'self.root',
        [arg('', None), arg('a', None), arg('b', None), arg('/', None),
         arg('*args', None), arg('c', None), arg('*', None),
         arg('d', None), arg('**kwargs', None), arg('return', None)],
        has_self=True)) == res
    # Nullable type (TypeNone)

# Generated at 2022-06-13 17:46:35.247980
# Unit test for method visit_Subscript of class Resolver
def test_Resolver_visit_Subscript():
    """Resolver unit test."""
    # Union
    assert isinstance(Resolver('', {}).visit_Subscript(
        Subscript(Name("Union", Load()), Tuple([]))), Tuple)
    # Optional
    assert isinstance(Resolver('', {}).visit_Subscript(
        Subscript(Name("Optional", Load()), Name("a", Load()))), BinOp)
    # Dict
    assert isinstance(Resolver('', {}).visit_Subscript(
        Subscript(Name("Dict", Load()), Tuple([]))), Tuple)
    # Generic
    assert isinstance(Resolver('', {}).visit_Subscript(
        Subscript(Name("Generic", Load()), Tuple([]))), Tuple)

# Generated at 2022-06-13 17:46:36.325901
# Unit test for method imports of class Parser
def test_Parser_imports():
    assert True

# Generated at 2022-06-13 17:46:44.563674
# Unit test for function const_type
def test_const_type():
    def assert_ct(n, t):
        assert const_type(parse(n).body[0].value) == t
    assert_ct("True", "bool")
    assert_ct("1", "int")
    assert_ct("1.0", "float")
    assert_ct("1j", "complex")
    assert_ct("'abc'", "str")
    assert_ct("frozenset()", "frozenset")
    assert_ct("frozenset([])", "frozenset")
    assert_ct("frozenset([1, 2, 3])", "frozenset[int]")
    assert_ct("frozenset([1, 2, 3.0])", "frozenset[Any]")
    assert_ct("set()", "set")
    assert_ct

# Generated at 2022-06-13 17:46:47.233479
# Unit test for method imports of class Parser
def test_Parser_imports():
    from .parser import Parser
    assert Parser._imports is Parser.imports
    assert Parser._imports.__doc__ == Parser.imports.__doc__


# Generated at 2022-06-13 17:46:55.867440
# Unit test for method func_ann of class Parser
def test_Parser_func_ann():
    parser = Parser()
    assert list(parser.func_ann('a', [arg('*', None)])) == ['']
    assert list(parser.func_ann('a', [arg('*', 'List[str]')])) == ['List[str]']
    assert list(parser.func_ann('a', [arg('*args', 'List[str]')])) == ['*args']
    assert list(parser.func_ann('a', [arg('**kwargs', 'Dict[str, int]')])) == ['**kwargs']
    assert list(parser.func_ann('a', [arg('arg1', None), arg('arg2', None)])) == ['ANY', 'ANY']

# Generated at 2022-06-13 17:47:01.408689
# Unit test for method imports of class Parser
def test_Parser_imports():
    """Testing imports"""