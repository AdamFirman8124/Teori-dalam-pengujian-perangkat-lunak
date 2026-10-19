

# Generated at 2022-06-13 18:02:22.845917
# Unit test for method parse_item of class ParserGenerator
def test_ParserGenerator_parse_item():
    p = ParserGenerator()
    p.make_scanner()
    p.scanner.input("(expr)")
    p.gettoken()
    assert p.type == token.OP
    assert p.value == "("
    a, z = p.parse_item()
    assert p.type == token.OP
    assert p.value == ")"
    assert len(a.arcs) == 1
    assert len(a.arcs[0][1].arcs) == 1
    assert a.arcs[0][1].arcs[0][1] is z


# Generated at 2022-06-13 18:02:28.308492
# Unit test for method parse_item of class ParserGenerator

# Generated at 2022-06-13 18:02:39.577419
# Unit test for method simplify_dfa of class ParserGenerator
def test_ParserGenerator_simplify_dfa():
    pg = ParserGenerator()

    start = DFAState(None, None)
    dfa = [start, start]
    pg.simplify_dfa(dfa)
    assert len(dfa) == 1

    dfa = [DFAState(None, None), DFAState(None, None)]
    pg.simplify_dfa(dfa)
    assert len(dfa) == 2

    dfa = [DFAState(None, None), DFAState(None, None), DFAState(None, None)]
    dfa[0].addarc(dfa[2], "")
    dfa[1].addarc(dfa[2], "")
    pg.simplify_dfa(dfa)
    assert len(dfa) == 2


# Generated at 2022-06-13 18:02:50.494243
# Unit test for method parse_item of class ParserGenerator
def test_ParserGenerator_parse_item():
    pg_ = ParserGenerator()
    pg_.value = None
    pg_.type = token.OP
    pg_.gettoken = _gettoken
    pg_.raise_error = _raise_error

    def _gettoken():
        if pg_.value == "(":
            pg_.value = ")"
        elif pg_.value == "[":
            pg_.value = "]"
        elif pg_.value in ("+", "*"):
            pg_.type = token.NEWLINE
            pg_.value = "\n"

    def _raise_error(msg: str, *args: Any) -> NoReturn:
        print(msg, args)
        assert False

    # ATOM: '(' RHS ')' | NAME | STRING
    pg_.value = "("
    pg_.gettoken()
    result = pg_.parse_item()


# Generated at 2022-06-13 18:02:57.248470
# Unit test for method calcfirst of class ParserGenerator
def test_ParserGenerator_calcfirst():
    dfas = {}
    dfa = DFAState({}, False)
    dfas["S"] = [dfa]
    dfa.addarc(dfa, "a")
    dfa.addarc(dfa, "b")
    dfa = DFAState({}, False)
    dfas["A"] = [dfa]
    dfa.addarc(dfa, "a")
    dfa = DFAState({}, False)
    dfas["B"] = [dfa]
    dfa.addarc(dfa, "b")
    dfas, startsymbol = dfas, "S"
    pg = ParserGenerator(dfas, startsymbol)
    pg.addfirstsets()

# Generated at 2022-06-13 18:03:05.483134
# Unit test for method simplify_dfa of class ParserGenerator
def test_ParserGenerator_simplify_dfa():
    # This unit test needs updating to cope with the changes in
    # ParserGenerator.simplify_dfa.  For now it's disabled.
    return

    p = ParserGenerator()
    name = "NAME"
    dfa = [DFAState({NFAState(name + " 1"): 1}, NFAState(name + " finish"))]
    for i in range(2, 20):
        nfa = NFAState(name + " " + str(i))
        nfa.addarc(NFAState(name + " " + str(i + 1)))
        dfa.append(DFAState({nfa: 1}, NFAState(name + " finish")))
    p.simplify_dfa(dfa)
    assert len(dfa) == 2

# Generated at 2022-06-13 18:03:11.018332
# Unit test for method dump_nfa of class ParserGenerator
def test_ParserGenerator_dump_nfa():
    pg = ParserGenerator()
    try:
        pg.dump_nfa("a", None, None)
    except Exception as err:
        assert type(err) is AssertionError
        return
    raise Exception("test failed")



# Generated at 2022-06-13 18:03:15.254946
# Unit test for method dump_nfa of class ParserGenerator
def test_ParserGenerator_dump_nfa():
    p = ParserGenerator()
    a = NFAState()
    b = NFAState()
    a.addarc(b, "a")
    b.addarc(a, "b")
    p.dump_nfa("test", a, b)

# Generated at 2022-06-13 18:03:25.095850
# Unit test for method make_grammar of class ParserGenerator
def test_ParserGenerator_make_grammar():

    grammar = """
        # Rules
        start: expression
        expression: expression '+' expression
                 | expression '-' expression
                 | expression '*' expression
                 | expression '/' expression
                 | expression '//' expression
                 | expression '%' expression
                 | expression '**' expression
                 | '-' expression
                 | '+' expression
                 | '~' expression
                 | atom
        atom:   '(' expression ')'
                 | NAME
        NAME: "[a-zA-Z_][a-zA-Z0-9_]*"
    """

    pg = ParserGenerator(grammar, {})


# Generated at 2022-06-13 18:03:29.377677
# Unit test for method addfirstsets of class ParserGenerator
def test_ParserGenerator_addfirstsets():
    a = ParserGenerator()
    assert a.first == {}
    a.addfirstsets()
    assert a.first == {
        'start': {'x': 1},
        'x': {'x': 1},
        'y': {'z': 1},
        'z': {'x': 1, 'y': 1},
        'single': {'z': 1},
    }

# Generated at 2022-06-13 18:04:37.056950
# Unit test for method calcfirst of class ParserGenerator
def test_ParserGenerator_calcfirst():
    # A sample grammar, from Python 2.2
    a = ParserGenerator()
    a.add_rhs(["file_input", "NEWLINE", "ENDMARKER"])
    a.add_rhs(["NEWLINE", "stmt", "NEWLINE", "stmt_list"])
    a.add_rhs(["NEWLINE", "stmt", "NEWLINE"])
    a.add_rhs(["NEWLINE"])
    a.add_rhs(["stmt", "stmt_list"])
    a.add_rhs(["stmt"])
    a.add_rhs(["compound_stmt"])
    a.add_rhs(["simple_stmt"])
    a.add_rhs(["expr_stmt"])
    a.add_r

# Generated at 2022-06-13 18:04:42.449467
# Unit test for method calcfirst of class ParserGenerator
def test_ParserGenerator_calcfirst():
    g = ParserGenerator()
    g.dfas = {
        'a': [DFAState({}, False), DFAState({}, False)],
        'b': [DFAState({}, False), DFAState({}, False)],
        'c': [DFAState({}, False), DFAState({}, False)],
        'd': [DFAState({}, False), DFAState({}, False)],
        'e': [DFAState({}, False), DFAState({}, False)],
        'f': [DFAState({}, False), DFAState({}, False)],
        'g': [DFAState({}, False), DFAState({}, False)],
    }

# Generated at 2022-06-13 18:04:53.283398
# Unit test for method make_dfa of class ParserGenerator
def test_ParserGenerator_make_dfa():
    a = NFAState()
    b = NFAState()
    c = NFAState()
    d = NFAState()
    f = NFAState()
    g = NFAState()
    a.addarc(b, "a")
    b.addarc(c, "a")
    b.addarc(c, "b")
    b.addarc(b)
    c.addarc(d, "b")
    c.addarc(c)
    f.addarc(g)

    dfa = ParserGenerator().make_dfa(a, d)

    def label(state: DFAState) -> str:
        label = "S%d" % id(state)
        for st in dfa:
            if st is state:
                label += "*"
                break
        return label



# Generated at 2022-06-13 18:04:55.425368
# Unit test for method dump_dfa of class ParserGenerator
def test_ParserGenerator_dump_dfa():
    p = ParserGenerator()
    dfa = p.dfas["expr_stmt"]
    p.dump_dfa("expr_stmt", dfa)


# Generated at 2022-06-13 18:05:04.221323
# Unit test for method dump_nfa of class ParserGenerator
def test_ParserGenerator_dump_nfa():
    g = ParserGenerator()
    name = "expr"
    a = NFAState()
    b = NFAState()
    c = NFAState()
    d = NFAState()
    e = NFAState()
    f = NFAState()
    a.addarc(b, "x")
    b.addarc(c, None)
    b.addarc(d)
    c.addarc(f, "y")
    d.addarc(e, "z")
    e.addarc(f, "z")
    f.addarc(a, "x")
    z = f
    g.dump_nfa(name, a, z)

# Generated at 2022-06-13 18:05:08.634802
# Unit test for method make_dfa of class ParserGenerator
def test_ParserGenerator_make_dfa():
    filename = "spam.g"
    with open(filename) as f:
        try:
            ParserGenerator(f, filename)
        except:
            traceback.print_exc()
            raise SystemExit(1)


# Generated at 2022-06-13 18:05:14.090281
# Unit test for method expect of class ParserGenerator
def test_ParserGenerator_expect():
    # Test version of 'expect' that has no arguments
    def expect(type: int, value: Optional[Any] = None) -> Text:
        ...
    # Test version of 'gettoken' that has no arguments
    def gettoken() -> None:
        ...
    # Test version of 'raise_error' that has no arguments
    def raise_error(msg: str, *args: Any) -> NoReturn:
        ...

# Generated at 2022-06-13 18:05:19.972043
# Unit test for method parse of class ParserGenerator
def test_ParserGenerator_parse():
    pg = ParserGenerator()
    dfas, startsymbol = pg.parse(
        """
        start: first second
        first: 'a'+ 'b'
        second: 'c' 'd'+
        """
    )
    assert sorted(dfas) == ["first", "second", "start"]
    assert startsymbol == "start"



# Generated at 2022-06-13 18:05:31.027942
# Unit test for method parse_item of class ParserGenerator
def test_ParserGenerator_parse_item():
    pg = ParserGenerator()

# Generated at 2022-06-13 18:05:37.310518
# Unit test for method gettoken of class ParserGenerator
def test_ParserGenerator_gettoken():
    from io import StringIO

    parser = ParserGenerator(StringIO('python: "python"\n'))
    parser.gettoken()
    assert parser.type == token.NAME
    assert parser.value == "python"
    parser.gettoken()
    assert parser.type == token.OP
    assert parser.value == ":"
    parser.gettoken()
    assert parser.type == token.STRING
    assert parser.value == '"python"'
    parser.gettoken()
    assert parser.type == token.NEWLINE
    parser.gettoken()
    assert parser.type == token.ENDMARKER



# Generated at 2022-06-13 18:06:34.931559
# Unit test for method parse_alt of class ParserGenerator
def test_ParserGenerator_parse_alt():
    fname = '<string>'
    s = "a | b"
    generator = tokenize.generate_tokens(StringIO(s).readline)
    parser = ParserGenerator(generator, fname)
    parser.gettoken()
    a, b = parser.parse_alt()
    assert a.arcs == {(None, b)}
    assert b.arcs == {('a', None)}
    parser.gettoken()
    a, b = parser.parse_alt()
    assert a.arcs == {(None, b)}
    assert b.arcs == {('b', None)}

# Generated at 2022-06-13 18:06:37.582535
# Unit test for method parse_item of class ParserGenerator
def test_ParserGenerator_parse_item():
    start = NFAState()
    finish = NFAState()
    start.addarc(finish, "label")
    pg = ParserGenerator()
    a, z = pg.parse_item()
    assert a.arcs == [('label', finish)]
    assert z is finish


# Generated at 2022-06-13 18:06:48.672508
# Unit test for method make_dfa of class ParserGenerator
def test_ParserGenerator_make_dfa():
    from _ast import PyCF_ONLY_AST as COMPILER_FLAGS
    import builtins
    import os
    import token
    import tokenize
    import unittest

    class ParserGeneratorTests(unittest.TestCase):
        def test_make_dfa(self):
            # This test needs to be a function because we need to control
            # the __name__ of the class we're defining.
            class ParserGeneratorMock(ParserGenerator):
                def __init__(self, grammar: str):
                    self.grammar = grammar

                def gettoken(self):
                    self.type, self.value = next(self.generator)
                    if self.type == token.ENDMARKER:
                        self.type = None


# Generated at 2022-06-13 18:06:51.267556
# Unit test for method raise_error of class ParserGenerator
def test_ParserGenerator_raise_error():
    """
        p = ParserGenerator(None, None)
        try:
            p.raise_error("a %s b %s %s", 1, 2, 3)
        except SyntaxError as e:
            assert str(e) == "a 1 b 2 3"
    """
    pass


# Generated at 2022-06-13 18:06:58.585618
# Unit test for method parse_rhs of class ParserGenerator
def test_ParserGenerator_parse_rhs():
  pg = ParserGenerator()
  # A very simple grammar with just one token and a parsing rule
  grammar_rules = """
  start: 'starttime' { return start; }
  """
  # Add the rules to the parser generator
  pg.add_rules( grammar_rules )
  # Generate the parser
  parser = pg.build_parser()
  # Parse a simple string
  ast = parser.parse('starttime')
  # The expected ast should be just a constant 'start'
  assert ast == 'start'

# Generated at 2022-06-13 18:07:06.533179
# Unit test for method parse_rhs of class ParserGenerator
def test_ParserGenerator_parse_rhs():
    from . import token
    from .tokenize import generate_tokens
    import io
    import unittest

    def do_test(grammar: str, dfa: List[DFAState]) -> None:
        with io.StringIO(grammar) as f:
            tokens = generate_tokens(f.readline)
            pg = ParserGenerator()
            pg.prepare_grammar(tokens)
            # dump_dfa(pg.dfa)
            # self.assertEqual(pg.dfa, dfa)
            assert pg.dfas == {"expr": dfa}

    def dump_dfa(dfa: List[DFAState]) -> None:
        print("Dump of DFA")

# Generated at 2022-06-13 18:07:16.000114
# Unit test for method parse of class ParserGenerator
def test_ParserGenerator_parse():
    import io
    import unittest
    import sys

    sys.path[:] = [""]
    import grammar_sample
    import pgen2.parse

    class ParseGrammarTest(unittest.TestCase):
        def setUp(self) -> None:
            self.pgen = pgen2.parse.ParserGenerator(grammar_sample.grammar)
            self.pgen.parse()
            self.pgen.addfirstsets()
            self.converter = self.pgen.make_pgen_grammar()

        def test_symbol2number(self):
            self.assertEqual(self.converter.symbol2number["term"], 0)
            self.assertEqual(self.converter.symbol2number["factor"], 1)

# Generated at 2022-06-13 18:07:22.960995
# Unit test for method parse_atom of class ParserGenerator
def test_ParserGenerator_parse_atom():
    # Arrange
    dicttokens: Dict[Text, int] = {}
    dicttokens["NAME"] = token.NAME
    dicttokens["STRING"] = token.STRING
    dicttokens["("] = token.OP
    dicttokens[")"] = token.OP
    dicttokens["["] = token.OP
    dicttokens["]"] = token.OP
    dicttokens["|"] = token.OP
    dicttokens["+"] = token.OP
    dicttokens["*"] = token.OP
    dicttokens[":"] = token.OP
    dicttokens["\n"] = tokenize.NL
    dicttokens["#"] = tokenize.COMMENT
    # Act

# Generated at 2022-06-13 18:07:31.146814
# Unit test for method parse_item of class ParserGenerator
def test_ParserGenerator_parse_item():
    pg = ParserGenerator(tokenize.generate_tokens("""
        asdf asdf
    """))
    pg.gettoken()
    a, z = pg.parse_item()
    print(a, z)
    print(list(a.arcs))
    print(list(z.arcs))
    assert a.arcs == ((None, z),)
    assert z.arcs == ()
    pg.gettoken()
    a, z = pg.parse_item()
    print(a, z)
    print(list(a.arcs))
    print(list(z.arcs))
    assert a.arcs == ((None, z),)
    assert z.arcs == ()
    pg.gettoken()
    print(pg.type)
    print(pg.value)
    print

# Generated at 2022-06-13 18:07:37.829291
# Unit test for method make_label of class ParserGenerator
def test_ParserGenerator_make_label():
    from pgen2.pgen import ParserGenerator
    from test.test_pgen2.conftest import grammar, symbols

    for t in symbols:
        for name in (
            "NAME",
            "NUMBER",
            "STRING",
            "'if'",
            "'else'",
            '"if"',
            '"else"',
            '"("',
            '")"',
        ):
            for label in (
                getattr(token, t),
                grammar.opmap[symbols[t]],
                t,
                name,
            ):
                print("Testing make_label(%s, %s)" % (t, label))
                c = ParserGenerator()
                c.make_label(c, label) # type: ignore



# Generated at 2022-06-13 18:09:26.345242
# Unit test for method addfirstsets of class ParserGenerator
def test_ParserGenerator_addfirstsets():
    r"""Test method addfirstsets of class ParserGenerator."""
    name = 'test_ParserGenerator_addfirstsets'
    print('Unittest for %s' % name)
    filename = '%s.py' % name
    grammar_filename = '%s.g' % name
    with open(grammar_filename, 'w') as fd:
        fd.write(
            '''
        A: "foo"
        B: "bar"
        C: "tar"
        D: A B | C
        '''
        )
    pgen = ParserGenerator(open(grammar_filename, 'r'), filename)
    pgen.addfirstsets()  # Call method to test
    assert pgen.first['A'] == {'foo': 1}
    assert pgen.first['B']

# Generated at 2022-06-13 18:09:39.981923
# Unit test for method gettoken of class ParserGenerator
def test_ParserGenerator_gettoken():
    # _input is a sample from tokenize.generate_tokens
    gen = ParserGenerator("test", _input)
    gen.gettoken()
    assert gen.type == token.NAME
    assert gen.value == "foo"
    assert gen.begin == (1, 0)
    assert gen.end == (1, 3)
    assert gen.line == "foo = 42\n"
    gen.gettoken()
    assert gen.type == token.OP
    assert gen.value == "="
    assert gen.begin == (1, 4)
    assert gen.end == (1, 5)
    gen.gettoken()
    assert gen.type == token.NUMBER
    assert gen.value == "42"
    assert gen.begin == (1, 6)
    assert gen.end == (1, 8)


# Generated at 2022-06-13 18:09:44.147874
# Unit test for method make_label of class ParserGenerator
def test_ParserGenerator_make_label():
    # Setup
    g = ParserGenerator()
    c = g.make_converter()
    # Exercise
    tp0 = g.make_label(c, 'foo_bar')
    tp1 = g.make_label(c, 'NAME')
    tp2 = g.make_label(c, '"NAME"')
    # Verify
    assert_equal(tp0, 0)
    assert_equal(tp1, 0)
    assert_equal(tp2, 1)
    # Cleanup - done automatically


# Generated at 2022-06-13 18:09:50.081024
# Unit test for method make_grammar of class ParserGenerator
def test_ParserGenerator_make_grammar():
    g = ParserGenerator()
    g.add_production("S", ("a", "S", "b"), 1)
    g.add_production("S", ("a", "b"), 2)
    g.add_production("S", ("b", "a"))
    g.set_start("S")
    grammar = g.make_grammar()
    keys = list(grammar.keys())
    keys.sort()
    assert keys == ["S"]
    assert grammar["S"] == ([0, 1], [1])



# Generated at 2022-06-13 18:09:57.538931
# Unit test for constructor of class ParserGenerator
def test_ParserGenerator():
    pgen = ParserGenerator(grammar)
    template = "xxaabbbcccddddxxxxxeeeeefffffggggggggghhhhhhhhhhiiiii"
    assert len(template) == len(pgen.labels)
    assert len(template) == len(pgen.dfas)
    i = 0
    for name, dfa in sorted(pgen.dfas.items()):
        assert len(name) == len(template[i])
        assert name[0] == template[i][0]
        i += 1
    assert i == len(template)



# Generated at 2022-06-13 18:10:03.236033
# Unit test for method calcfirst of class ParserGenerator
def test_ParserGenerator_calcfirst():
    pg = ParserGenerator()
    G = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
    G = G.split()

# Generated at 2022-06-13 18:10:13.421948
# Unit test for method make_label of class ParserGenerator
def test_ParserGenerator_make_label():
    pg = ParserGenerator()
    c = pg.converter.__class__()
    c.labels = []
    c.keywords = {}
    c.tokens = {}
    c.symbol2label = {}
    def _test(label):
        print(label)
        return pg.make_label(c, label)
    # A symbol name
    _test("file_input")
    # An operator
    _test("'+'")
    # A keyword
    _test('"for"')
    # A named token
    _test("STRING")
    print(c.labels)
    assert len(c.labels) == 5
    assert c.symbol2label["file_input"] == 0
    assert c.tokens[token.STRING] == 3

# Generated at 2022-06-13 18:10:22.852885
# Unit test for method __eq__ of class DFAState
def test_DFAState___eq__():
    class DFAStateForTest(DFAState): ...

# Generated at 2022-06-13 18:10:23.557522
# Unit test for method calcfirst of class ParserGenerator
def test_ParserGenerator_calcfirst():
    # XXX Write me
    pass

# Generated at 2022-06-13 18:10:33.923708
# Unit test for method calcfirst of class ParserGenerator
def test_ParserGenerator_calcfirst():
    pg = ParserGenerator()
    pg.dfas = {"A": [DFAState({}, False), DFAState({}, True)], "B": []}
    pg.calcfirst("A")
    pg.calcfirst("B")
    assert pg.first == {"A": {}, "B": {}}
    pg.dfas = {"A": [DFAState({"A": 1, "B": 1}, False)], "B": [DFAState({}, False)]}
    pg.calcfirst("A")
    pg.calcfirst("B")
    assert pg.first == {"A": {}, "B": {}}
    pg.dfas = {"A": [DFAState({"A": 1, "B": 1}, False), DFAState({}, True)], "B": []}
    pg.calc