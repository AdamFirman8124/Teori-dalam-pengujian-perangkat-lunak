

# Generated at 2022-06-13 18:02:15.929003
# Unit test for method parse_alt of class ParserGenerator
def test_ParserGenerator_parse_alt():
    pg = ParserGenerator()
    pg.addtoken("NAME", r"[a-zA-Z_]\w*")
    pg.addtoken("NUMBER", r"-?\d+(\.\d*)?")
    pg.addtoken("STRING", r"'[^']*'")
    pg.addtoken("[", r"\[")
    pg.addtoken("]", r"\]")
    pg.addtoken("(", r"\(")
    pg.addtoken(")", r"\)")
    pg.addtoken("+", r"\+")
    pg.addtoken("*", r"\*")
    pg.addtoken("|", r"\|")
    pg.addtoken(":", r":")
    pg.addtoken("NEWLINE", r"\n")

# Generated at 2022-06-13 18:02:21.898615
# Unit test for method parse_rhs of class ParserGenerator
def test_ParserGenerator_parse_rhs():
    grammar = '''
        # A Python-like grammar
        expr: expr '+' term | term
        term: term '*' factor | factor
        factor: '(' expr ')' | NAME | NUMBER
    '''
    pg = ParserGenerator()
    generator = pg.parse(grammar)
    for n in range(4):
        a, z = pg.parse_rhs()
        assert len(a.arcs) == 1
        assert len(z.arcs) == 0
        assert len(a.arcs[0][1].arcs) == 4
        assert len(a.arcs[0][1].arcs[0][1].arcs) == 2
        assert len(a.arcs[0][1].arcs[0][1].arcs[0][1].arcs) == 1
       

# Generated at 2022-06-13 18:02:28.347392
# Unit test for method calcfirst of class ParserGenerator
def test_ParserGenerator_calcfirst():
    pg = ParserGenerator()
    pg.dfas = {
        "foo": [DFAState({NFAState(): 1}, NFAState())],
        "bar": [DFAState({NFAState(): 1}, NFAState())],
        "baz": [DFAState({NFAState(): 1}, NFAState())],
        "qux": [DFAState({NFAState(): 1}, NFAState())],
    }
    pg.first = {}
    pg.calcfirst("test")
    assert pg.first == {"test": {"foo": 1, "bar": 1}}, pg.first



# Generated at 2022-06-13 18:02:39.606435
# Unit test for method parse_rhs of class ParserGenerator
def test_ParserGenerator_parse_rhs():
    r = """
a: b c d
b: 'x'
c: 'y'
    """.strip()
    pg = ParserGenerator()
    dfas, startsymbol = pg.parseGrammar(r)
    assert len(dfas) == 3
    assert startsymbol == "a"
    assert pg.first["a"] == {"b": 1, "x": 1, "y": 1}
    assert pg.first["b"] == {"x": 1}
    assert pg.first["c"] == {"y": 1}
    assert pg.first["d"] == {}
    for s in dfas["a"]:
        assert isinstance(s, DFAState)
    assert len(dfas["a"]) == 4
    assert len(dfas["b"]) == 2

# Generated at 2022-06-13 18:02:42.708633
# Unit test for method parse_alt of class ParserGenerator
def test_ParserGenerator_parse_alt():
    pg_inst = ParserGenerator()
    pg_inst._ParserGenerator__last = (0, 0)
    assert pg_inst.parse_alt() == (None, None)
    print("Unit test for ParserGenerator.parse_alt() passed.")


# Generated at 2022-06-13 18:02:48.696161
# Unit test for method parse_rhs of class ParserGenerator
def test_ParserGenerator_parse_rhs():
    p = ParserGenerator()
    p.setup("""
        [0-9]+ | [0-9]+'.'[0-9]* | [0-9]+.[0-9]* | '.'[0-9]+
        """)
    assert p.parse_rhs()


# Generated at 2022-06-13 18:02:56.672781
# Unit test for method addfirstsets of class ParserGenerator
def test_ParserGenerator_addfirstsets():
    import numpy
    numpy.set_printoptions(precision=2)
    py_grammar = nltk.parse_cfg(r"""
    S -> 'NP' 'VP'
    VP -> 'V' 'NP'
    NP -> 'Det' 'N'
    Det -> 'a' | 'the'
    N -> 'dog' | 'cat'
    V -> 'chased' | 'sat'
    """)
    pg = ParserGenerator(py_grammar)
    pg.addfirstsets()
    names = list(pg.dfas.keys())
    names.sort()
    print("Grammar contains %d rules" % len(names))
    for name in names:
        print("For rule %s:" % name)

# Generated at 2022-06-13 18:03:02.512542
# Unit test for method make_dfa of class ParserGenerator
def test_ParserGenerator_make_dfa():
    p = ParserGenerator()
    p.setup()
    p.handle_rule('x', "('a'|'b') 'c'")
    start, finish = p.dfas['x'][0], p.dfas['x'][-1]
    assert len(p.dfas['x']) == 2
    assert start.arcs == {'a': finish, 'b': finish}
    assert finish.arcs == {'c': finish}
    assert finish.isfinal

# Generated at 2022-06-13 18:03:09.567936
# Unit test for method raise_error of class ParserGenerator
def test_ParserGenerator_raise_error():
    pgen = ParserGenerator()
    pgen.input = b"a: b c\n"
    pgen.filename = "foo.py"
    try:
        pgen.gettoken()
        pgen.expect(token.NAME)
        pgen.expect(token.OP, ":")
        pgen.expect(token.NAME)
        pgen.expect(token.NAME)
        pgen.expect(token.NAME, "d")
        assert False
    except SyntaxError as e:
        assert e.msg == "expected NAME, got NAME/c"
        assert e.filename == "foo.py"
        assert e.lineno == 1
        assert e.offset == 6
        assert e.text == "a: b c\n"
test_ParserGenerator_raise_error()

# Generated at 2022-06-13 18:03:18.473588
# Unit test for method make_grammar of class ParserGenerator
def test_ParserGenerator_make_grammar():
    gp = ParserGenerator({"a": (1, 2, 3)}, "a")
    c = gp.make_grammar()
    assert c.labels == [(1, None), (2, None), (3, None)]
    assert c.states == [[(0, 1)]]
    assert c.dfas == {0: (c.states[0], {})}
    assert c.keywords == {}
    assert c.tokens == {}
    assert c.symbol2number == {"a": 0}
    assert c.symbol2label == {"a": 0}
    assert c.start == 0



# Generated at 2022-06-13 18:04:58.235542
# Unit test for method make_grammar of class ParserGenerator
def test_ParserGenerator_make_grammar():
    # XXX Write tests here
    a = ParserGenerator()
    a.make_grammar(
        """
        start: NAME_NAME
        NAME_NAME: NAME_NAME NAME_NAME | NAME
        """
    )
    a.make_grammar(
        """
        # an empty rule
        start:
        """
    )

# Generated at 2022-06-13 18:05:06.567386
# Unit test for method calcfirst of class ParserGenerator
def test_ParserGenerator_calcfirst():
    pg = ParserGenerator()
    pg.calcfirst("_NT_start")
    dfa = pg.dfas["_NT_start"]
    arc = dfa[0].arcs[0]
    assert arc[0] == "|"
    arc = dfa[0].arcs[1]
    assert arc[0] == "|"
    arc = dfa[0].arcs[2]
    assert arc[0] is None
    dfa = pg.dfas["_NT_atoms"]
    assert pg.first["_NT_atoms"]["("] == 1
    assert pg.first["_NT_atoms"]["NAME"] == 1
    assert pg.first["_NT_atoms"]["STRING"] == 1
    arc = dfa[0].arcs[0]
   

# Generated at 2022-06-13 18:05:12.905654
# Unit test for method dump_dfa of class ParserGenerator
def test_ParserGenerator_dump_dfa():
    pg = ParserGenerator(token)
    dfa = [
        DFAState({"a": 1, "b": 1}, False),
        DFAState({"b": 1}, True),
        DFAState({"c": 1}, False),
        DFAState({"a": 2}, False),
        DFAState({"b": 3}, True),
    ]
    pg.dump_dfa("test", dfa)



# Generated at 2022-06-13 18:05:24.337705
# Unit test for method make_label of class ParserGenerator
def test_ParserGenerator_make_label():
    import parser as _p  # TODO: avoid relying on undocumented interface

    g = _p.ParserGenerator()
    assert g.make_label("abc") == 3
    assert g.make_label("abc") == 3
    assert g.make_label("ABC") == 4
    assert g.make_label("123") == 5
    assert g.make_label("def") == 6
    assert g.make_label("'def'") == 7
    assert g.make_label("'def'") == 7
    assert g.make_label("++") == 8
    assert g.make_label("'a'") == 9

    # Check value of g.labels

# Generated at 2022-06-13 18:05:30.362653
# Unit test for method make_label of class ParserGenerator
def test_ParserGenerator_make_label():
    from pgen2.pgen import ParserGenerator

    pg = ParserGenerator()

    # To define the make_label method, we must provide a data value for c

    c = type(
        "fake_converter",
        (object,),
        {
            "labels": [],
            "tokens": {},
            "keywords": {},
            "symbol2number": {},
            "symbol2label": {},
            "dfas": {},
            "states": [],
        },
    )()

    # It's not possible to call make_label directly,
    # because pg is an instance of ParserGenerator,
    # not an instance of the subclass that provides the method

    pg.make_label = ParserGenerator.make_label

# Generated at 2022-06-13 18:05:45.352909
# Unit test for method parse_atom of class ParserGenerator
def test_ParserGenerator_parse_atom():
    line = "a ( b ) [c]"
    pg = ParserGenerator(line)
    # First token is NAME 'a', so parse_atom() should return a new
    # NFAState as the first node in a new NFA
    a, z = pg.parse_atom()
    assert isinstance(a, NFAState)
    assert a.arcs == {('a', z)}
    assert isinstance(z, NFAState)
    assert z.arcs == set()
    # Second token is OP '(', so parse_atom() should parse a parenthesized
    # expression and return the two ends of the resulting NFA as the
    # two nodes in a new NFA
    a, z = pg.parse_atom()
    assert isinstance(a, NFAState)

# Generated at 2022-06-13 18:05:56.378737
# Unit test for method make_label of class ParserGenerator
def test_ParserGenerator_make_label():
    # XXX Maybe this should be a method on a subclass of converter?
    c = PgenGrammar()
    c.labels = []
    c.keywords = {}
    c.tokens = {}
    c.symbol2number = {}
    c.symbol2label = {}
    label = "NAME"
    print("label is ", label)
    # XXX Maybe this should be a method on a subclass of converter?
    ilabel = len(c.labels)
    print("ilabel is ", ilabel)
    if label[0].isalpha():
        # Either a symbol name or a named token
        print("label isalpha")
        if label in c.symbol2number:
            # A symbol name (a non-terminal)
            print("label in symbol2number")

# Generated at 2022-06-13 18:05:58.809859
# Unit test for constructor of class ParserGenerator
def test_ParserGenerator():
    p = ParserGenerator()

if __name__ == "__main__":
    test_ParserGenerator()

# Generated at 2022-06-13 18:06:07.771494
# Unit test for method parse of class ParserGenerator
def test_ParserGenerator_parse():
    import tokenize
    from io import BytesIO

    def parse(s: str, symbols: Dict[Text, List["DFAState"]]) -> None:
        test_ParserGenerator(BytesIO(s.encode("utf-8")), symbols).parse()

    parse("foo: 'abc'\n", {'foo': [DFAState({NFAState(): 1}, NFAState()),
                                    DFAState({NFAState(): 1}, NFAState())],
                            })

# Generated at 2022-06-13 18:06:18.017228
# Unit test for method calcfirst of class ParserGenerator
def test_ParserGenerator_calcfirst():
    pg = ParserGenerator()
    pg.dfas = {'a': [DFAState({'b': 1}, False), DFAState({'c': 1, 'd': 2}, False), DFAState({}, True),
     DFAState({}, False)], 'b': [DFAState({'c': 1}, False), DFAState({}, True), DFAState({}, False)],
     'c': [DFAState({'b': 1, 'd': 2}, False), DFAState({}, True), DFAState({}, False)]}
    pg.calcfirst('a')
    assert pg.first['a'] == {'b': 1, 'c': 1, 'd': 1}

# Generated at 2022-06-13 18:07:33.672209
# Unit test for method parse_item of class ParserGenerator
def test_ParserGenerator_parse_item():
    import unittest
    from . import pgen
    from .pgen2 import driver

    class TestCase(unittest.TestCase):
        def check(self, input, expected):
            pg = pgen.ParserGenerator()
            result = pg.parse_item(input)
            self.assertEqual(result, expected)

        def test_accepts_parenthesized_grammar(self):
            input = GrammarParser(
                "(a: 'a' | b: 'b')*"
            )

# Generated at 2022-06-13 18:07:35.437962
# Unit test for method parse_alt of class ParserGenerator
def test_ParserGenerator_parse_alt():
    p = ParserGenerator()
    p.parse_alt()
    assert True, "Unit tests for ParserGenerator parse_alt() passed"

# Generated at 2022-06-13 18:07:44.427924
# Unit test for method parse_alt of class ParserGenerator
def test_ParserGenerator_parse_alt():
    pgen = ParserGenerator("")
    pgen.type = token.NAME
    pgen.value = "foo"
    pgen.gettoken = lambda: None
    pgen.parse_item = mock.MagicMock(side_effect=[("a", "b"), ("c", "d")])
    pgen.parse_atom = mock.MagicMock(side_effect=[("a", "b"), ("c", "d")])
    pgen.value = "("
    pgen.parse_rhs = mock.MagicMock(side_effect=[("a", "b"), ("c", "d")])
    pgen.value = "+"
    pgen.parse_item = mock.MagicMock(return_value=("x", "y"))

# Generated at 2022-06-13 18:07:57.308401
# Unit test for method make_first of class ParserGenerator
def test_ParserGenerator_make_first():
    pg = ParserGenerator({})
    pg.symbol2number = {'S': 0, 'X': 1}

    c = DFAState({0: 1}, False)
    assert pg.make_first(c, 'S') == {0: 1}
    assert c.labels == []
    c = DFAState({0: 1, 1: 1}, False)
    assert pg.make_first(c, 'X') == {1: 1}
    assert c.labels == []

    pg.first = {'S': {'a': 1}, 'X': {'b': 1}}
    c = DFAState({}, False)
    assert pg.make_first(c, 'S') == {0: 1}
    assert c.labels == [(token.NAME, None)]

# Generated at 2022-06-13 18:08:05.770927
# Unit test for constructor of class ParserGenerator
def test_ParserGenerator():
    print("Testing ParserGenerator")
    test_grammar = {}
    test_tokens = {}
    test_start = ""
    test_pgen = ParserGenerator(test_grammar, test_tokens, test_start)

if __name__ == "__main__":
    import sys

    if "-d" in sys.argv:
        del sys.argv[sys.argv.index("-d")]
        debug = 1
    else:
        debug = 0

    if len(sys.argv) == 1:
        print("usage: python pgen.py grammar.txt module.py")
        print("   or: python pgen.py -d grammar.txt module.py")
        sys.exit(2)

# Generated at 2022-06-13 18:08:16.892785
# Unit test for method dump_dfa of class ParserGenerator
def test_ParserGenerator_dump_dfa():
    pg = ParserGenerator()

# Generated at 2022-06-13 18:08:26.975176
# Unit test for method expect of class ParserGenerator
def test_ParserGenerator_expect():
    filename = "ParserGenerator_test_expect"
    lines = ["#  py3[/]:", "py3[a:]  'a'", "py3[b:]  'b'", "py3[a+b:]  py3[a] ( '+' py3[b] )?", "py3[a*b:]  py3[a] ( '*' py3[b] )?"]
    with open(filename, "w") as f:
        f.write("\n".join(lines) + "\n")
    p = ParserGenerator(filename)
    first_token = token.NAME
    first_value = "py3"
    assert p.type == first_token
    assert p.value == first_value
    p.gettoken()
    assert p.type == token.OP
    assert p

# Generated at 2022-06-13 18:08:40.581258
# Unit test for method parse_alt of class ParserGenerator
def test_ParserGenerator_parse_alt():
    print("Test method parse_alt of class ParserGenerator")
    # Test 1
    pg = ParserGenerator(None)
    pg.value = "foo"
    pg.type = token.NAME
    a, b = pg.parse_alt()
    assert a.arcs == [(None, b)]
    assert b.arcs == [("foo", b)]
    # Test 2
    pg = ParserGenerator(None)
    pg.value = "|"
    pg.type = token.OP
    pg.gettoken = lambda: None
    pg.parse_alt = lambda: (NFAState(), NFAState())
    a, b = pg.parse_alt()
    assert a.arcs == [(None, NFAState()), (None, NFAState())]

# Generated at 2022-06-13 18:08:48.118885
# Unit test for method parse of class ParserGenerator
def test_ParserGenerator_parse():
    pg = ParserGenerator()
    assert pg is not None
    assert len(pg.stream) == 0

# Generated at 2022-06-13 18:09:04.511390
# Unit test for method parse of class ParserGenerator
def test_ParserGenerator_parse():
    import sys
    import pprint
    from io import StringIO

    import token
    import tokenize

    class DummyFile:
        def __init__(self, lines):
            self.lines = lines
            self.lineno = 0

        def readline(self):
            self.lineno += 1
            try:
                return self.lines[self.lineno - 1]
            except IndexError:
                return ""

    def gramedit(text):
        return text + "\n"

    def check(text):
        parser = ParserGenerator()
        pprint.pprint(parser.parse(text))

    # Start symbol is last name listed

# Generated at 2022-06-13 18:10:31.589576
# Unit test for method parse of class ParserGenerator
def test_ParserGenerator_parse():

    parser_generator = ParserGenerator()  # type: ignore
    rules = r"""
    filelog       : NAME ':' (file_rule | NAME)+ NEWLINE
    file_rule     : '^' NAME NAME NAME?
                  | '^' NAME NAME '->' NAME
                  | '^' NAME NAME '(' NAME ')' '->' NAME
                  | '^' NAME NAME '(' NAME ')' '->' NAME NAME
    """
    parser_generator.add_rules(rules)
    dfas, startsymbol = parser_generator.parse()
    assert startsymbol == "filelog"  # from end of first line
    assert len(dfas) == 2  # filelog + file_rule
    assert len(dfas["filelog"]) == 3
    assert len(dfas["file_rule"]) == 5


# Generated at 2022-06-13 18:10:47.381348
# Unit test for method raise_error of class ParserGenerator
def test_ParserGenerator_raise_error():
    def _raise_error(
        msg: str,
        args: Tuple[Any, ...],
        _globals: Mapping[str, Any],
        _locals: Mapping[str, Any],
    ) -> NoReturn:
        try:
            parser = ParserGenerator(StringIO(""))
            raise_error = parser.raise_error
        except:
            raise
        try:
            raise_error(msg, *args)
        except SyntaxError as e:
            assert e.msg == msg % args
            raise


# Generated at 2022-06-13 18:10:53.722077
# Unit test for method expect of class ParserGenerator
def test_ParserGenerator_expect():
    from tokenize import generate_tokens, untokenize, OP

    generator = generate_tokens(iter(["soMe", "inValid", "vaLue"]).__next__)
    parser = ParserGenerator([], "some_file")
    parser.generator = generator

    assert parser.value == "some"

    parser.expect(OP, "soMe")
    parser.expect(OP, "inValid")
    parser.expect(OP, "vaLue")

    assert parser.value == "invalid"

# Generated at 2022-06-13 18:11:03.476302
# Unit test for method make_label of class ParserGenerator
def test_ParserGenerator_make_label():
    import sys
    argv = sys.argv[1:]
    if argv and argv[0] == "--debug":
        argv.pop(0)
        _log.setLevel(logging.DEBUG)
    filename = argv.pop(0)
    if argv:
        raise ValueError("Extra arguments")
    with open(filename, "rb") as f:
        data = f.read()
    #
    from typing import Dict
    from . import pgen
    tokens = tokenize.tok_name
    keywords = keyword.kwlist

# Generated at 2022-06-13 18:11:10.692747
# Unit test for method calcfirst of class ParserGenerator
def test_ParserGenerator_calcfirst():
    print('Testing calcfirst');
    import os
    import sys
    import random
    curdir = os.path.dirname(os.path.abspath(__file__)) or os.curdir
    py_file = os.path.join(curdir, "graminit.py")
    with open(py_file) as f:
        pg = ParserGenerator()
        pg.setup()
        pg.add_file(f, py_file)
        assert len(pg.dfas)
        pg.addfirstsets()
        assert pg.first
        # Do it again to make sure nothing is messed up
        old = pg.first.copy()
        pg.addfirstsets()
        assert old == pg.first, "addfirstsets() mutated pg.first"
        # Do a random check

# Generated at 2022-06-13 18:11:13.611762
# Unit test for method calcfirst of class ParserGenerator
def test_ParserGenerator_calcfirst():
    pg = ParserGenerator()
    pg.all_symbols = {'a', 'b', 'c'}
    pg.first = {'b': {'b': 1}}
    pg.calcfirst('a')



# Generated at 2022-06-13 18:11:20.120511
# Unit test for method make_first of class ParserGenerator
def test_ParserGenerator_make_first():
    # ParserGenerator.make_first(c: PgenGrammar, name: Text) -> Dict[int, int]

    # setup
    import unittest
    import token
    import tokenize

    class MockPgenGrammar:

        def __init__(self):
            self.labels = []
            self.symbol2label = {}
            self.tokens = {}
            self.keywords = {}

        def symbol2number(self, name):
            return int(name.split('_')[-1])

    class MockToken(int):

        def __init__(self, value):
            self.value = value

        def isalpha(self):
            return self.value.isalpha()

        def __repr__(self):
            return self.value


# Generated at 2022-06-13 18:11:23.312493
# Unit test for method make_first of class ParserGenerator
def test_ParserGenerator_make_first():
    for name in ('NAME', 'classdef', 'varargslist', 'fpdef', 'typedargslist'):
        pg = ParserGenerator(debug=True)
        pg.make_parser(name)
        pg.addfirstsets()
#        print name, pg.first[name]



# Generated at 2022-06-13 18:11:38.727369
# Unit test for method make_grammar of class ParserGenerator
def test_ParserGenerator_make_grammar():
    # If a unit test is tagged as "skip", then it will be skipped
    # when running the tests.
    # pytest.skip('skipping a test')
    #assert False
    # assert <expr>
    pg = ParserGenerator()
    test_pg_grammar = (
        "keyword : NAME ':' '\\n'\n"
        ":"
        "    NAME ':' '\\n'\n"
        "    | NAME ':' '\\n'\n"
        "    ;"
    )
    pg_tokens = tokenize.tokenize(io.BytesIO(test_pg_grammar.encode('utf-8')).readline)
    c = pg.make_grammar(pg_tokens, "test_make_grammar")