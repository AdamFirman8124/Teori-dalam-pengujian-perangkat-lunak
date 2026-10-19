

# Generated at 2022-06-13 17:44:35.236908
# Unit test for method visit_Name of class Resolver
def test_Resolver_visit_Name():
    import abc
    import decimal
    import fractions
    import numbers
    r = Resolver("__main__", {
        "__main__.abc": "abc.ABC",
        "__main__.decimal": "decimal.Decimal",
        "__main__.fractions": "fractions.Fraction",
        "__main__.numbers": "numbers.Number",
    })
    print(unparse(r.visit(parse("abc.ABC").body[0].value)))
    print(unparse(r.visit(parse("decimal.Decimal").body[0].value)))
    print(unparse(r.visit(parse("fractions.Fraction").body[0].value)))
    print(unparse(r.visit(parse("numbers.Number").body[0].value)))



# Generated at 2022-06-13 17:44:44.512847
# Unit test for method imports of class Parser
def test_Parser_imports():
    """
    >>> from .parser import Parser
    >>> from .syntax import Module, Import, ImportFrom, Name
    >>> p = Parser()
    >>> p.imports('', Module(body=[
    ...     ImportFrom(module='os',
    ...                names=[alias('os', 'path')],
    ...                level=2),
    ...     Import(names=[
    ...         alias('os_path', 'join'),
    ...         alias('os_path', 'normpath'),
    ...         alias('os_path', 'basename')])]))
    >>> p.alias
    {'os_path.join': 'os.path.join', 'os_path.normpath': 'os.path.normpath', 'os_path.basename': 'os.path.basename'}
    """

# Generated at 2022-06-13 17:44:51.704365
# Unit test for method class_api of class Parser
def test_Parser_class_api():
    class T:
        def f(self):  # <--
            pass
        @staticmethod
        def f(self):  # <--
            pass
        @classmethod
        def f(cls):  # <--
            pass
        async def f(self):  # <--
            pass
        @staticmethod
        async def f(self):  # <--
            pass
        @classmethod
        async def f(cls):  # <--
            pass
        def __f(self):  # <--
            pass
        def _f(self):  # <--
            pass
        def f_(self):  # <--
            pass
        def __f__(self):  # <--
            pass
    _ = T()
    from ast import ClassDef
    from ast import Assign
    from ast import Ann

# Generated at 2022-06-13 17:44:58.685312
# Unit test for function const_type
def test_const_type():
    # Constant type test
    assert const_type(Constant(None)) == 'NoneType'
    assert const_type(Constant(True)) == 'bool'
    assert const_type(Constant(1)) == 'int'
    assert const_type(Constant(1.0)) == 'float'
    assert const_type(Constant(1 + 1j)) == 'complex'
    assert const_type(Constant("hello")) == 'str'
    # Sequences type test
    assert const_type(Tuple([])) == 'tuple[]'
    assert const_type(Tuple([Constant(1)])) == 'tuple[int]'
    assert const_type(Tuple([Constant(1), Constant(1.0)])) == 'tuple[Any]'
    assert const_type(List([Constant(1)]))

# Generated at 2022-06-13 17:45:08.849906
# Unit test for method func_ann of class Parser
def test_Parser_func_ann():
    """Test case for Parser.func_ann."""
    class TestParser(Parser):
        """Parser for test."""
        alias = {'m.class_': 'type'}
        root = {'m.a': 'm'}
        level = {'m': 0, 'm.a': 1, 'm.b': 1, 'm.class_': 1}
        func_ann = staticmethod(Parser.func_ann.__func__)
    test = TestParser()
    assert test.func_ann('m', (arg('a', None), arg('*b', None), arg('return', None)),
                         has_self=True, cls_method=True) == [
                             'type[Self]', '', '', '']

# Generated at 2022-06-13 17:45:12.724900
# Unit test for method func_ann of class Parser
def test_Parser_func_ann():
    p = Parser(b_level=0)
    class a:
        def b(self, *, t: type = None) -> int:
            pass
    for v in p.func_ann("root.mod", get_args(a.b)):
        print(v)

test_Parser_func_ann()



# Generated at 2022-06-13 17:45:15.602696
# Unit test for function table
def test_table():
    table_unit = table('a', 'b', [['c', 'd'], ['e', 'f']])
    assert table_unit == "| a | b |\n|:---:|:---:|\n| c | d |\n| e | f |\n\n"



# Generated at 2022-06-13 17:45:23.481024
# Unit test for method load_docstring of class Parser
def test_Parser_load_docstring():
    print("Testing method load_docstring of class Parser...", end="")
    test_data = [
        (
            '# CliX\nA command-line interface utility.',
            'test.test_data.test_Parser_load_docstring',
        ),
        (
            '# CliX\n\nA command-line interface utility.',
            'test.test_Parser_load_docstring'
        ),
        (
            'CliX = "A command-line interface utility."',
            'CliX = "A command-line interface utility."',
            'CliX'
        ),
    ]
    for doc, root, *name in test_data:
        p = Parser()
        p.docstring[root] = doc

# Generated at 2022-06-13 17:45:29.907421
# Unit test for method visit_Subscript of class Resolver
def test_Resolver_visit_Subscript():
    R = Resolver('', {})
    # Union
    assert unparse(R.visit(parse('typing.Union[int, float]').body[0])).strip() \
        == 'Union[int, float]'
    assert unparse(R.visit(parse('Union[int, float]').body[0])).strip() == 'Or[int, float]'
    # Optional
    assert unparse(R.visit(parse('typing.Optional[int]').body[0])).strip() \
        == 'Optional[int]'
    assert unparse(R.visit(parse('Optional[int]').body[0])).strip() == 'Or[int, None]'


# Generated at 2022-06-13 17:45:41.278880
# Unit test for method func_api of class Parser
def test_Parser_func_api():
    root = 'a'
    name = 'a.b'
    args = [
        arg('x', Name(id='a.T')),
        arg('y', Constant(value='type[List[a.T]]')),
        arg('*', arg('z', Constant(value='type[Dict[str,a.T]]'))),
        arg('**', arg('w', Constant(value='List[int]'))),
        arg('return', Name(id="a.R"))
    ]
    alias = {'a.T': 'a.T', 'a.R': 'a.R'}
    par = Parser(link=True, alias=alias)
    par.func_api(root, name, args, None, has_self=False, cls_method=False)
    assert par.doc[name]

# Generated at 2022-06-13 17:49:01.149057
# Unit test for function is_public_family
def test_is_public_family():
    assert is_public_family('a')
    assert is_public_family('_a') is False
    assert is_public_family('a.b')
    assert is_public_family('a.__b__')
    assert is_public_family('a._b') is False



# Generated at 2022-06-13 17:49:03.814224
# Unit test for method visit_Name of class Resolver
def test_Resolver_visit_Name():
    s = "int[3]"
    r = Resolver('__main__', {'__main__': 'typing', 'typing': '{"List":"List"}'})
    print(unparse(r.visit(parse(s).body[0])))
test_Resolver_visit_Name()


# Generated at 2022-06-13 17:49:09.875281
# Unit test for method api of class Parser
def test_Parser_api():
    import os
    import io
    import sys
    import tempfile
    import traceback
    import unittest
    import py_compile

    import pdoc

    class TestParser(unittest.TestCase):
        """Test suite for class Parser."""

        def setUp(self):
            _stdout = sys.stdout
            sys.stdout = io.StringIO()
            self.__print = sys.stdout
            self.__main_print = _stdout
            self.__module_path = os.path.join(tempfile.gettempdir(), 'pdoc-test')

        def tearDown(self):
            if os.path.exists(self.__module_path):
                py_compile.compile(self.__module_path, doraise=True)