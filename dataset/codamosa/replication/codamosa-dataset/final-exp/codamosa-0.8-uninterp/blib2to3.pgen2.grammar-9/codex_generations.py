

# Generated at 2022-06-13 17:49:49.120657
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import io

    g = Grammar()
    g.symbol2number = {'special': 257, 'simple': 258}
    g.number2symbol = {257: 'special', 258: 'simple'}
    g.states = [[[(1, 2)], [(3, 4)]]]
    g.dfas = {258: (g.states[0], {1: 1}), 257: (g.states[0], {1: 1})}
    g.labels = [(0, "EMPTY")]
    g.keywords = {'keyword1': 1, 'keyword2': 3}
    g.tokens = {token.PLUS: 1, token.MINUS: 3}
    g.symbol2label = {'special': 257, 'simple': 258}
    g.start = 256

   

# Generated at 2022-06-13 17:49:59.748900
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import ast
    import copy

    g = ast.parse("(a, b)").body[0].value
    g1 = copy.deepcopy(g)
    assert g == g1

    with tempfile.NamedTemporaryFile() as f:
        f.delete = False
        fn = f.name
        try:
            Grammar.dump(g, fn)
            g2 = Grammar()
            Grammar.load(g2, fn)
            assert g == g2
        finally:
            os.remove(fn)


if __name__ == "__main__":
    import sys

    test_Grammar_dump()
    g = Grammar()
    if sys.argv[1:]:
        g.load(sys.argv[1])
    g.report()

# Generated at 2022-06-13 17:50:03.567353
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    import pickle
    unpickled = pickle.loads(pickle.dumps(g, pickle.HIGHEST_PROTOCOL))
    assert unpickled.__dict__ == g.__dict__
    unpickled.dump('/tmp/dontcare.pkl')

# Generated at 2022-06-13 17:50:08.178682
# Unit test for method load of class Grammar
def test_Grammar_load():
    empty_grammar = Grammar()
    empty_grammar.tokens = {1: 2}
    empty_grammar.states = ['a', 'b', 'c']
    empty_grammar.start = 3
    empty_grammar.labels = ['a', 'b', 'c']
    empty_grammar.dfas = {1: ('a', 'b'), 2: ('c', 'd')}
    empty_grammar.symbol2label = {1: 2, 2: 3}
    empty_grammar.keywords = {1: 2}
    empty_grammar.number2symbol = {1: 2, 2: 3}
    empty_grammar.symbol2number = {1: 2, 2: 3}

    f = tempfile.TemporaryFile()

# Generated at 2022-06-13 17:50:19.142658
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import sys
    import unittest

    print("Unit test for method dump of class Grammar")
    g = Grammar()
    g.symbol2number = {"a": 1, "b": 2}
    g.number2symbol = {1: "a", 2: "b"}
    g.states = [[[(1, 2), (0, 1), (3, 4)], [(0, 1), (1, 5), (3, 4)]]]
    g.dfas = {1: ([[(0, 1), (1, 1)], [(0, 2), (1, 2)]], {1: 1, 2: 1})}
    g.labels = [(0, "a"), (1, "b"), (0, "c"), (1, "d")]

# Generated at 2022-06-13 17:50:29.585402
# Unit test for method load of class Grammar
def test_Grammar_load():
    import pickle
    from importlib.util import spec_from_file_location, module_from_spec
    from os.path import dirname, join
    import sys
    import unittest

    here = dirname(__file__)
    pkl_file = join(here, "Grammar.pkl")
    mod_name = "mypy.parse.grammar_mock"
    spec = spec_from_file_location(mod_name, join(here, "Grammar.py"))
    mod = module_from_spec(spec)
    mod.__name__ = mod_name
    sys.modules[mod_name] = mod

# Generated at 2022-06-13 17:50:35.929161
# Unit test for method load of class Grammar
def test_Grammar_load():
    from sys import getrefcount

    grammar1 = Grammar()
    refcnt1 = getrefcount(grammar1)
    for name in ["symbol2number", "number2symbol", "states", "dfas", "labels", "keywords", "tokens", "symbol2label", "start"]:
        assert hasattr(grammar1, name)
        assert getattr(grammar1, name) is None
    grammar2 = Grammar()
    refcnt2 = getrefcount(grammar2)
    filename = "grammar1.pickle"
    grammar2.dump(filename)
    grammar2.load(filename)
    refcnt3 = getrefcount(grammar2)
    assert refcnt1 == refcnt3
    assert refcnt2 == refcnt3

# Generated at 2022-06-13 17:50:41.024031
# Unit test for method load of class Grammar
def test_Grammar_load():
    g = Grammar()
    print(g.symbol2number)
    print(g.number2symbol)
    print(g.states)
    print(g.dfas)
    print(g.labels)
    print(g.keywords)
    print(g.tokens)
    print(g.symbol2label)
    print(g.start)
    print(g.async_keywords)


# Generated at 2022-06-13 17:50:45.813836
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import os
    import ast
    from .conv import parse_grammar_source

    with open(os.path.join(os.path.dirname(__file__), "Grammar.txt")) as f:
        gr = parse_grammar_source(f.read(), ast)
    with open(os.path.join(os.path.dirname(__file__), "Grammar.pkl"), "wb") as f:
        gr.dump(f)



# Generated at 2022-06-13 17:50:56.474294
# Unit test for method load of class Grammar
def test_Grammar_load():
    from .conv import convert_grammar

    gr = convert_grammar("Grammar/Grammar", "3.7")
    gr.dump("Grammar/Grammar.pkl")
    gr2 = Grammar()
    gr2.load("Grammar/Grammar.pkl")

    # XXX It would be better to compare the generated pickled data
    # directly with the expected data, but then we'd have to have the
    # expected data in another file to be compared with.  If we could
    # be assured that the pickle data is independent of the order of
    # dicts and lists, we could do the comparison by first converting
    # both structures to JSON and then comparing the JSON strings.
    assert gr.symbol2number == gr2.symbol2number

# Generated at 2022-06-13 17:51:09.642875
# Unit test for method load of class Grammar
def test_Grammar_load():
    from .tokenize import generate_tokens
    from .parse import PyCF_ONLY_AST
    #
    # Create a file-like object to be parsed
    #
    test_source = textwrap.dedent("""
    def foo():
        return None
    def bar():
        return foo()
    """)
    #
    # Step 1: prepare the grammar
    #
    g = Grammar()
    g.start = 'file_input'
    #
    # Step 2: build the symbol2label dictionary
    #
    symbol2label = {}
    max_label = 0
    for t in generate_tokens(test_source.splitlines()):
        ttype, tstr, _, _, _ = t

# Generated at 2022-06-13 17:51:16.118766
# Unit test for method load of class Grammar
def test_Grammar_load():
    grammar = Grammar()

    # Test that Grammar._update can take a dict
    grammar._update({'key': 'value'})
    assert grammar.key == 'value'

    # Test that Grammar._update doesn't barf when the key is not in __dict__
    grammar._update({'some_other_key': 'some_value'})
    assert grammar.some_other_key == 'some_value'

# Generated at 2022-06-13 17:51:24.868737
# Unit test for method load of class Grammar
def test_Grammar_load():
    g = Grammar()

    # Create a grammar with tokens and symbols
    [tok_a, tok_b] = sorted([g.tokens.setdefault(i, len(g.labels))
                             for i in [1, 2]])
    sym_a = g.symbol2number["sym_a"] = 256
    sym_b = g.symbol2number["sym_b"] = 257
    g.number2symbol.update({sym_a: "sym_a", sym_b: "sym_b"})

    # Create a new empty Grammar object
    h = Grammar()
    assert len(h.labels) == 0

    # Load the grammar
    h.load(g.dump("test.pkl"))

    # Check that the grammar has been loaded correctly
    assert h.tokens

# Generated at 2022-06-13 17:51:34.743784
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import pytest
    from .conv import Converter
    from .parse import Parser

    # create a temporary grammar file, write data to it and read it back in
    with tempfile.NamedTemporaryFile(delete=False) as f:
        filename = f.name
    tables = Grammar()
    Converter(tables).make_grammar()
    with open(filename, "wb") as f:
        tables.dump(f)
    with open(filename, "rb") as f:
        g = Grammar()
        g.load(f)

    # try to parse a simple expression and check the result
    p = Parser(g, "a + b")
    result = p.parse()
    assert result.to_tuple() == (['s', 'b', [3, None]])

    # delete temporary file


# Generated at 2022-06-13 17:51:43.110727
# Unit test for method load of class Grammar
def test_Grammar_load():
    g = Grammar()
    g.load("Grammar.txt")
    assert g.states[1] == [
        [(0, 1), (1, 2), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)],
        [],
        [],
        [(8, -1)],
    ]

# Generated at 2022-06-13 17:51:53.792933
# Unit test for method load of class Grammar
def test_Grammar_load():
    from .grammar_parser import pgen

    # Test by loading a parse grammar and its dump
    g = Grammar()
    g.load(pgen.grammar)
    g2 = Grammar()
    g2.loads(g.dumps())
    assert g == g2

    # Test by loading a pickle dump of an unparsed grammar
    g3 = Grammar()

# Generated at 2022-06-13 17:52:04.370236
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    # Test dump, load
    f = tempfile.NamedTemporaryFile(mode="w+b", delete=False)
    f.close()

# Generated at 2022-06-13 17:52:05.387369
# Unit test for method load of class Grammar
def test_Grammar_load():
    # It appears that this class does not contain a unit test for method load.
    pass

# Generated at 2022-06-13 17:52:09.123523
# Unit test for method load of class Grammar
def test_Grammar_load():
    grammar = Grammar()
    grammar.load(os.path.join(os.path.dirname(__file__), "Grammar.pickle"))
    assert isinstance(grammar, Grammar)
    # Grammar is not a readable object so no point in testing the content

# Generated at 2022-06-13 17:52:12.794065
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    class MyClass(object):
        def __getstate__(self):
            return {'d': 0}

    g = Grammar()
    g.m = MyClass()
    g.dump('dump_test.pkl')


# Generated at 2022-06-13 17:52:27.312378
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    from types import SimpleNamespace
    from unittest import mock

    import pytest

    g = Grammar()
    setattr(g, "symbol2number", {"foo": 1, "bar": 2})
    setattr(g, "number2symbol", {1: "foo", 2: "bar"})
    setattr(g, "states", [([(1, 1)], {1: 1})])
    setattr(g, "dfas", {3: ([], {})})
    setattr(g, "labels", [(5, "baz")])
    setattr(g, "keywords", {"baz": 5})
    setattr(g, "tokens", {5: 5})
    setattr(g, "symbol2label", {"foo": 1, "bar": 2})

# Generated at 2022-06-13 17:52:31.674831
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import unittest.mock

    def check_Grammar_dump(self, f):
        def dump(d, filename):
            f.write(pickle.dumps(d))

        with unittest.mock.patch.object(pickle, 'dump', dump):
            self.dump(self)

    Grammar.test_dump = check_Grammar_dump


__all__ = ["Grammar", "Label", "opmap"]

# Generated at 2022-06-13 17:52:39.775432
# Unit test for method load of class Grammar
def test_Grammar_load():
    import unittest
    from . import pygram
    from . import pytree

    class Token:
        pass

    class Grammar(unittest.TestCase):
        def test_load(self):
            #    def load(self, filename):
            #        """Load the grammar tables from a pickle file."""
            #        with open(filename, 'rb') as f:
            #            d = pickle.load(f)
            #        self._update(d)
            # use pygram.python_grammar, don't use pygram.python_grammar_no_print_statement
            pygram.python_grammar.dump(b'python_grammar.pickle')
            g = Grammar()
            g.load(b'python_grammar.pickle')

# Generated at 2022-06-13 17:52:51.371898
# Unit test for method load of class Grammar
def test_Grammar_load():
    from .conv import conv

    path = os.path.join(os.path.dirname(__file__), "Grammar.dump")
    grammar = Grammar()
    grammar.load(path)

# Generated at 2022-06-13 17:52:53.360411
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    filename = "DumpFile.txt"
    g = Grammar()
    g.dump(filename)

# Generated at 2022-06-13 17:52:56.972759
# Unit test for method load of class Grammar
def test_Grammar_load():
    g = Grammar()
    g.load(os.path.join(os.path.dirname(__file__), 'Grammar.pkl'))


# Generated at 2022-06-13 17:53:01.771359
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    grammar = Grammar()
    filename = "a_temp_file.pkl"
    grammar.dump(filename)
    with open(filename, "rb") as f:
        s = f.read()
    assert s[:7] == b"\x80\x03c_parser"
    os.remove(filename)


# Generated at 2022-06-13 17:53:08.067200
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    from .conv import parse_grammar
    from .pgen import driver
    driver.main(["-op", "file.pkl", "Grammar/Grammar"])
    g = parse_grammar("file.pkl")
    assert isinstance(g, Grammar)
    assert g.start == 256
    assert g.symbol2number["STMT"] == 258
    assert g.number2symbol[258] == "STMT"
    assert g.states[0][0][0][0] == token.NEWLINE
    assert g.states[0][0][0][1] == 1
    assert g.states[0][1][0][0] == 257
    assert g.states[0][1][0][1] == 1
    assert g.states[0][1][1][0] == 258

# Generated at 2022-06-13 17:53:13.180146
# Unit test for method load of class Grammar
def test_Grammar_load():
    from . import pgen2

    g = Grammar()
    g.load(pgen2.__file__.replace(".pyc", ".pkl"))


if __name__ == "__main__":
    import unittest

    unittest.main()

# Generated at 2022-06-13 17:53:16.553800
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    sourcename = "<test>"
    grammar = Grammar()
    with open(sourcename, "w") as f:
        pickle.dump(grammar, f)

# Generated at 2022-06-13 17:53:29.588334
# Unit test for method load of class Grammar
def test_Grammar_load():
    # Simple test: make sure that Grammar can load a file.
    g = Grammar()
    g.load(Grammar.__module__.replace(".", os.path.sep) + ".txt")
    g.report()


if __name__ == "__main__":
    import sys
    g = Grammar()
    g.load(Grammar.__module__.replace(".", os.path.sep) + ".txt")
    g.report()

# Generated at 2022-06-13 17:53:32.885399
# Unit test for method load of class Grammar
def test_Grammar_load():
    """
    test load() function of Grammar class
    """
    g = Grammar()
    assert g.number2symbol == {}
    g.load("Parser/Grammar.pickle")
    assert g.number2symbol != {}

# Generated at 2022-06-13 17:53:39.868648
# Unit test for method load of class Grammar
def test_Grammar_load():
    grammar = Grammar()
    grammar.states = [[(257, 0)], [(0, 1)], [(0, 1)], [(258, 2)]]
    grammar.dfas = {257: ([(0, 0)], {257: 1}), 258: ([(0, 2)], {258: 1})}
    grammar.symbol2number = {'root': 257, 'ENDMARKER': 258}
    grammar.number2symbol = {257: 'root', 258: 'ENDMARKER'}
    grammar.start = 257
    grammar.labels = [(0, 'EMPTY'), (257, None), (258, None)]

# Generated at 2022-06-13 17:53:47.252193
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import pickle
    from typing import Dict, List, Tuple
    from . import token

    # Create a test Grammar
    # (See the conv and pgen modules for more details)
    g = Grammar()
    g.symbol2number = {"start": 0, "definition": 1, "NAME": 2}
    g.number2symbol = {y: x for x, y in g.symbol2number.items()}
    g.states = [[(1, 1)], [(1, 2)], []]
    g.dfas = {0: (g.states[0], {token.NAME: 1}), 1: (g.states[1], {token.NAME: 1})}
    g.labels = [(0, "EMPTY"), (token.NAME, None), (256, "start")]

# Generated at 2022-06-13 17:54:00.084187
# Unit test for method load of class Grammar
def test_Grammar_load():
    """Verify that Grammar.load() can pickle and unpickle."""
    # Create a dummy grammar, since we know that otherwise the
    # comparison won't work.  At least we'll test that the pickle
    # format hasn't changed.
    g = Grammar()
    g.number2symbol[1] = "ONE"
    g.symbol2number["ONE"] = 1
    g.states = [[[(0, 1)]]]
    g.labels = [(0, "NOOP"), (1, None)]
    g.start = 1
    g.dfas = {1: (g.states[0], {1: 1})}
    with tempfile.TemporaryDirectory() as d:
        g.dump(os.path.join(d, "test_pgen"))
        p = Grammar()
       

# Generated at 2022-06-13 17:54:07.059432
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    from .pgen2 import driver

    g = driver.load_grammar("/home/wen/Desktop/python3.7/Parser/Grammar/Grammar/Python.gram")
    g.dump("grammar.dump")
    g.report()
    g.load("grammar.dump")
    g.report()

if __name__ == '__main__':
    test_Grammar_dump()

# Generated at 2022-06-13 17:54:10.790274
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import pickle
    import tempfile
    import shutil
    from typing import cast
    from .pgen2 import grammar

    g = grammar.Grammar()
    g.load(cast(grammar.Grammar, pickle.loads(
        g.dumps(pickle.HIGHEST_PROTOCOL))).pgen_pickle)
    g.dump(tempfile.mktemp())
    g.dump(tempfile.mktemp()+'.pickle')
    shutil.rmtree(tempfile.mkdtemp())

# Generated at 2022-06-13 17:54:20.965137
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    import pickle
    import io
    
    f = io.BytesIO()
    g.dump(f) # ~NotImplementedError~
    f.seek(0)
    unpickled = pickle.loads(f.getvalue())
    assert unpickled["symbol2number"] == g.symbol2number
    assert unpickled["number2symbol"] == g.number2symbol
    assert unpickled["states"] == g.states
    assert unpickled["dfas"] == g.dfas
    assert unpickled["labels"] == g.labels
    assert unpickled["keywords"] == g.keywords
    assert unpickled["tokens"] == g.tokens
    assert unpickled["symbol2label"] == g.symbol2label


# Generated at 2022-06-13 17:54:29.406062
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    from os import path
    from . import conv, pgen

    dirname, _ = path.split(__file__)
    fname = path.join(dirname, "Grammar.dump")

    g = Grammar()
    p = pgen.load_parser(fname)
    t = conv.make_tables(p)
    g.set_tables(t, p.start)
    g.dump(fname)

    g1 = Grammar()
    g1.load(fname)
    assert g == g1


# Generated at 2022-06-13 17:54:36.695229
# Unit test for method load of class Grammar
def test_Grammar_load():
    import pgen2
    # Note: we use an ordinary absolute path:
    # a) it should work on all systems
    # b) it should work on all filesystem layouts
    # c) it should work if run inside or outside the Python source tree
    # The pickle file is created by running Grammar.dump(fn) in
    # Lib/test/test_pgen2.py
    fn = os.path.join(os.path.dirname(__file__), 'Grammar.pkl')
    g = pgen2.Grammar()
    g.load(fn)
    assert g.start == 256
    assert g.dfas[256] == ([[(257, 1)]], {256: 0})
    assert g.states[0] == [(257, 1)]

# Generated at 2022-06-13 17:54:56.374877
# Unit test for method load of class Grammar
def test_Grammar_load():
    g = Grammar()
    g.load(os.path.join(os.path.dirname(__file__), "Grammar.pkl"))
    assert g.symbol2number["and_expr"] == 268
    assert g.symbol2number["NAME"] == 261
    assert g.number2symbol[268] == "and_expr"
    assert g.number2symbol[261] == "NAME"
    assert g.keywords["if"] == 260
    assert g.keywords["False"] == 261
    assert g.keywords["None"] == 261
    assert g.tokens[token.DEDENT] == 259
    assert g.start == 256

# Generated at 2022-06-13 17:55:07.223592
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    from . import pgen2
    from . import pygram

    g = Grammar()
    g.dump("Grammar.dump")
    g2 = Grammar()
    g2.load("Grammar.dump")

    g3 = Grammar()
    g3.loads(g.dumps())
    g4 = Grammar()
    g4.loads(g2.dumps())

    assert g == g2 == g3 == g4

    pygram.init()
    pgen2.main(pygram)  # Coverage.
    pgen2.main(pygram, "-o", "Grammar.dump")

    p = pygram.python_grammar
    p2 = pygram.python_grammar

    p3 = Grammar()
    p3.load("Grammar.dump")
    p4

# Generated at 2022-06-13 17:55:15.089718
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    from .pgen2 import driver

    filename = "Grammar.dump.pickle"
    g = driver.load_grammar("/home/python/cpython/Grammar.txt")
    try:
        g.dump(filename)
        g2 = Grammar()
        g2.load(filename)
    finally:
        try:
            os.remove(filename)
        except OSError:
            pass
    assert g.symbol2number == g2.symbol2number
    assert g.number2symbol == g2.number2symbol
    assert g.states == g2.states
    assert g.dfas == g2.dfas
    assert g.labels == g2.labels
    assert g.keywords == g2.keywords

# Generated at 2022-06-13 17:55:23.354614
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    class A(object):
        def __init__(self, op: bool) -> None:
            self.a = 1
            self.b = 2
            self.op = op

        def __getstate__(self) -> Dict[str, Any]:
            return {'a': self.a, 'b': self.b, 'op': self.op}

        def __setstate__(self, state: Dict[str, Any]) -> None:
            self.a = state['a']
            self.b = state['b']
            self.op = state['op']

    g = A(opmap)

    g.dump('test_Grammar_dump.pkl')
    with open('test_Grammar_dump.pkl', 'rb') as f:
        d = pickle.load(f)
   

# Generated at 2022-06-13 17:55:28.366353
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    from . import driver
    from .conv import pgen

    path = "Parser/Python.asdl"
    parser = pgen.ParserGenerator(path, path)
    grammar = parser.build_grammar()
    grammar.dump(driver.find_grammar(path))
    input()

if __name__ == "__main__":
    test_Grammar_dump()

# Generated at 2022-06-13 17:55:38.343206
# Unit test for method load of class Grammar
def test_Grammar_load():
    import unittest
    import pickle
    import io
    import copy

    class X:
        def __getstate__(self):
            return self.__dict__

        def __initattr__(self, a, v):
            self.__setattr__(a, v)

    class TestGrammar(unittest.TestCase):
        def test_getstate__(self):
            data = {'a': 1, 'b': 2}
            x = X()
            x.__dict__.update(data)
            self.assertEqual(data, x.__getstate__())

        def test_setattr__(self):
            data = {'a': 1, 'b': 2}
            x = X()

# Generated at 2022-06-13 17:55:42.340261
# Unit test for method load of class Grammar
def test_Grammar_load():
    g = Grammar()
    s = g.load(os.path.join(os.path.dirname(__file__), "Grammar.txt"))
    assert s is None

if __name__ == "__main__":
    test_Grammar_load()

# Generated at 2022-06-13 17:55:57.740784
# Unit test for method load of class Grammar
def test_Grammar_load():
    import pickle
    import sys

    def make_grammar():
        # Create a grammar object
        file = open("Grammar.pickle", "wb")
        grammar = Grammar()
        pickle.dump(grammar, file, -1)
        file.close()

    def check_file_type():
        # Check if the file type is correct
        file = open("Grammar.pickle", "rb")
        magic = file.read(4)
        file.close()
        assert magic == b"\x80\x03\x04\x00"

    def load_grammar():
        # Load the grammar from the file Grammar.pickle
        file = open("Grammar.pickle", "rb")
        grammar = pickle.load(file)
        file.close()


# Generated at 2022-06-13 17:56:03.112829
# Unit test for method load of class Grammar
def test_Grammar_load():
    g = Grammar()
    filename = './Grammar/Grammar.pickle'
    if os.path.isfile(filename):
        g.load(filename)

if __name__ == "__main__":
    test_Grammar_load()
# Grammar.load('./Grammar/Grammar.pickle')

# Generated at 2022-06-13 17:56:13.817416
# Unit test for method load of class Grammar
def test_Grammar_load():
    import io, sys
    import tokenize
    import tokenize as tk

    class TokenClass(tk.TokenInfo):
        def __init__(self, *args, **kwds):
            super().__init__(*args, **kwds)
            self.prev = None

        def tok_name(self):
            return self.exact_type
            #return self.type
    class Tokenizer:
        def __init__(self, input, out=sys.stdout):
            self.input = input
            self.out = out
            self.parser = Grammar()
            self.parser.loads(input)
            self.analysis = Analyser(self.parser)
            self.analysis.build_analysis()
            self.start = self.parser.start
            self.tokens = self.parser.tokens

# Generated at 2022-06-13 17:56:29.148703
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    """
    Create a Grammar instance and dump it to a pickle file.
    """

    test_grammar = Grammar()
    test_grammar.dfas = {1: ([[(4, 1), (2, 3)]], {1: 1}), 2: ([[(4, 1), (2, 3)]], {1: 1})}
    test_grammar.keywords = {"test": 1}
    test_grammar.labels = [(0, "EMPTY"), (1, "test")]
    test_grammar.number2symbol = {1: "test"}
    test_grammar.start = 256
    test_grammar.states = [[[(2, 1)], [(2, 1)]], [[(1, 1)]]]
    test_grammar.symbol2label = {"test": 1}

# Generated at 2022-06-13 17:56:34.933856
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    c = Grammar()
    from .pgen import Driver
    imp = Driver().load_grammar("python2")
    c.copy_grammar(imp)
    c.dump("Grammar_dump.pickle")
    d = Grammar()
    d.load("Grammar_dump.pickle")
    assert c.symbol2number == d.symbol2number
    assert c.number2symbol == d.number2symbol
    assert c.states == d.states
    assert c.dfas == d.dfas
    assert c.labels == d.labels
    assert c.keywords == d.keywords
    assert c.tokens == d.tokens
    assert c.symbol2label == d.symbol2label
    assert c.start == d.start

    # Unit test

# Generated at 2022-06-13 17:56:39.437759
# Unit test for method load of class Grammar
def test_Grammar_load():
    import test.test_grammar as test

    g = test.test_grammar()
    with tempfile.NamedTemporaryFile(prefix='test_grammar', suffix='.g') as f:
        g.dump(f.name)
        gg = Grammar()
        gg.load(f.name)
        assert gg == g

# Generated at 2022-06-13 17:56:46.737377
# Unit test for method load of class Grammar
def test_Grammar_load():
    class TestClass(Grammar):
        pass
    a = TestClass()
    a.load(graminit.__file__.replace(".py", "Py.gram"))
    print(a.__dict__)

_Operator: Dict[str, int] = opmap  # Silly alias for lookup via token module
del opmap
del opmap_raw


# Generated at 2022-06-13 17:56:56.522358
# Unit test for method load of class Grammar
def test_Grammar_load():
    # NOTE: this is not the intended use of load, but can be used for testing
    # It works by extracting the data to be pickled from an already loaded Grammar instance
    g = Grammar()

# Generated at 2022-06-13 17:57:03.741052
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    from . import pgen

    def dump_save_load(grammar: Grammar, filename: Path) -> None:
        try:
            os.remove(filename)
        except FileNotFoundError:
            pass
        grammar.dump(filename)
        grammar.load(filename)

    grammar = pgen.pgen("test.test_grammar")
    new = pgen.pgen(tempfile.NamedTemporaryFile().name)
    new.load("test.test_grammar")
    grammar.dump(tempfile.NamedTemporaryFile().name)
    grammar2 = pgen.pgen(tempfile.NamedTemporaryFile().name)
    dump_save_load(grammar, tempfile.NamedTemporaryFile().name)

# Generated at 2022-06-13 17:57:17.475575
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    test_dict = {}
    for k in Grammar().__dict__:
        test_dict[k] = 1

    test_grammar = Grammar()
    test_grammar._update(test_dict)
    changed = []
    with tempfile.TemporaryFile() as test_file:
        test_grammar.dump(test_file)
        test_file.seek(0)
        test_grammar2 = Grammar()
        test_grammar2.load(test_file)
        for k in test_grammar.__dict__:
            if not getattr(test_grammar, k) == getattr(test_grammar2, k):
                changed.append(k)
    if changed:
        raise AssertionError("Some tables are not dumped correctly: " + ",".join(changed))

# Generated at 2022-06-13 17:57:24.776665
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import pprint
    def check_Grammar(filename: Path) -> None:
        with open(filename, "rb") as f:
            d = pickle.load(f)
        pprint.pprint(d, width=1)

    grammar = Grammar()
    grammar.number2symbol = {256: 'foo'}
    grammar.start = 256
    filename = "foo.pickle"
    try:
        os.remove(filename)
    except OSError:
        pass
    grammar.dump(filename)
    check_Grammar(filename)
    grammar.load(filename)
    assert grammar.start == 256
    assert grammar.number2symbol == {256: 'foo'}
    grammar.dump(filename)
    check_Grammar(filename)

# Generated at 2022-06-13 17:57:35.561327
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    # This used to crash, see http://bugs.python.org/issue7384
    # or http://bugs.python.org/issue7375
    filename = os.path.join(os.path.dirname(__file__), "Grammar.dump")
    Grammar().dump(filename)
    try:
        g = Grammar()
        g.load(filename)
        assert g.dfas == {}
        assert g.symbol2label == {}
        assert g.symbol2number == {}
        assert g.keywords == {}
        assert g.labels == [(0, "EMPTY")]
        assert g.number2symbol == {}
        assert g.states == []
        assert g.tokens == {}
    finally:
        os.unlink(filename)

# Generated at 2022-06-13 17:57:38.028345
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    fp = tempfile.NamedTemporaryFile()
    g.dump(fp.name)
    assert os.path.exists(fp.name)
    fp.close()

# Generated at 2022-06-13 17:57:59.063358
# Unit test for method load of class Grammar
def test_Grammar_load():
    def _check_new_load(pickle_path: Path) -> None:
        # Read the pickle
        with open(pickle_path, "rb") as f:
            data = f.read()
        # Check the pickle can be loaded as a Grammar
        g = Grammar()
        g.loads(data)
        # Check g.symbol2number is a dict
        assert isinstance(g.symbol2number, dict)
        # Check len(g.symbol2number) > 0
        assert len(g.symbol2number) > 0
        # Check g.number2symbol is a dict
        assert isinstance(g.number2symbol, dict)
        # Check len(g.number2symbol) > 0
        assert len(g.number2symbol) > 0
        # Check g.

# Generated at 2022-06-13 17:58:15.925005
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import os
    from . import pgen2
    from .conv import convert
    from .pgen import driver

    path = os.path.split(__file__)[0]
    for filename in ["Grammar.txt", "Grammar2.txt"]:
        g = Grammar()
        g.start = "start"
        pgen2.pgen(open(os.path.join(path, filename)), g)
        driver.write_tables(g)
        convert.dump_pickle(g, os.path.join(path, "Grammar.pickle"))

        h = Grammar()
        h.load(os.path.join(path, "Grammar.pickle"))

        assert h.symbol2number == g.symbol2number
        assert h.number2symbol == g.number2

# Generated at 2022-06-13 17:58:20.474007
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    # test attribute dump
    # grammar has no __getstate__
    g = Grammar()
    g.dump("/fake/")
    g.load("/fake/")

    # grammar has __getstate__
    class GrammarWithGetstate(Grammar):
        def __getstate__(self):
            return {}
    g = GrammarWithGetstate()
    g.dump("/fake/")
    g.load("/fake/")

# Generated at 2022-06-13 17:58:22.119426
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    filename = "grammar.pkl"
    grammar = Grammar()
    grammar.dump(filename)
    os.remove(filename)

# Generated at 2022-06-13 17:58:23.606410
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    parse_grammar = Grammar()
    parse_grammar.dump('/tmp/parse_grammar.dump')

# Generated at 2022-06-13 17:58:32.429039
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    from . import pgen
    from . import token

    # create a grammar
    with tokenize.open(__file__) as f:
        tokens = list(tokenize.generate_tokens(f.readline))

    g = pgen.generate_grammar()
    assert g != None

    # dump the grammar
    g.dump(__file__ + '.dump')

    # load the dumped grammar
    h = Grammar()
    h.load(__file__ + '.dump')

    # check that the two grammars represent the same data
    assert g.symbol2number == h.symbol2number
    assert g.number2symbol == h.number2symbol
    assert g.states == h.states
    assert g.dfas == h.dfas
    assert g.labels == h.labels

# Generated at 2022-06-13 17:58:41.440242
# Unit test for method load of class Grammar
def test_Grammar_load():
    import pytest
    from . import pgen2 as pgen
    from . import Driver as parser_Driver
    from .pgen2 import pgen
    from .parser import Driver as parser_Driver

    # Create a Grammar instance
    grammar = pgen.make_grammar(debug=False)
    
    # Pickle the grammar
    f = tempfile.mkstemp(dir='/', prefix='Grammar_load')[1]
    grammar.dump(f)

    # Load the grammar
    loaded_grammar = pgen.Grammar()
    loaded_grammar.load(f)

    # Remove the pickle file
    os.unlink(f)

    # Check attributes
    assert isinstance(loaded_grammar.symbol2number, dict)

# Generated at 2022-06-13 17:58:48.730138
# Unit test for method load of class Grammar
def test_Grammar_load():
    """
    Unit test for the method load of the class Grammar.
    """

    import ast
    import unittest

    from . import pgen2
    from . import conv

    def create_grammar(pickle_filename: Optional[Path] = None) -> Grammar:
        """
        Create a new grammar object.
        """

        grammar = Grammar()
        conv.initialize_grammar(grammar)
        if pickle_filename is not None:
            grammar.dump(pickle_filename)
        return grammar

    def load_grammar(pickle_filename: Path) -> Grammar:
        """
        Load the grammar object from a pickle file.
        """

        grammar = Grammar()
        grammar.load(pickle_filename)
        return grammar


# Generated at 2022-06-13 17:58:51.629532
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import pgen2.parser
    # table = pgen2.parser.pgen()
    # table.dump('Grammar.txt')
    # table.dump(b'Grammar.txt')
    with open('Grammar.txt', 'rb') as f:
        table = pickle.load(f)
    assert isinstance(table, Grammar)
    table.report()

# Generated at 2022-06-13 17:59:00.825634
# Unit test for method load of class Grammar
def test_Grammar_load():
    """
    Check that loading a pickled grammar works, and an invalid one raises
    an exception with the right name.
    """
    filename = os.path.join(
        os.path.dirname(__file__), "Grammar.pickle"
    )
    with open(filename, "rb") as f:
        g = pickle.load(f)
    assert g.async_keywords == False

    # Test that a pickle file that is too old raises the right exception
    filename = os.path.join(
        os.path.dirname(__file__), "Grammar.27.pickle"
    )
    with open(filename, "rb") as f:
        try:
            pickle.load(f)
        except pickle.UnpicklingError as e:
            name = e.args