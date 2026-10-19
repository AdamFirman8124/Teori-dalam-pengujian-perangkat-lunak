

# Generated at 2022-06-13 18:02:25.508446
# Unit test for method dump_dfa of class ParserGenerator
def test_ParserGenerator_dump_dfa():
    parser = ParserGenerator()
    a, z = parser.parse_rhs()
    dfa = parser.make_dfa(a, z)
    parser.dump_dfa("x", dfa)
    assert False # To see the output of this unit test



# Generated at 2022-06-13 18:02:36.432312
# Unit test for method parse_item of class ParserGenerator
def test_ParserGenerator_parse_item():
    generator = ParserGenerator(token_list)

# Generated at 2022-06-13 18:02:43.473488
# Unit test for method addfirstsets of class ParserGenerator
def test_ParserGenerator_addfirstsets():
    for arc in (
        (DFAState(None, None), DFAState(None, None), "y"),
        (DFAState(None, None), DFAState(None, None), "x"),
    ):
        state = arc[0]
        next = arc[1]
        label = arc[2]
        state.addarc(next, label)
    assert state.arcs[0][0] == "x"
    assert state.arcs[1][0] == "y"
    assert len(state.arcs) == 2


# Generated at 2022-06-13 18:02:49.241384
# Unit test for method parse_alt of class ParserGenerator
def test_ParserGenerator_parse_alt():
    # -- ParserGenerator.parse_alt()
    pg = ParserGenerator()
    pg.generator = iter(
        [
            (token.NAME, "a"),
            (token.NAME, "b"),
            (token.OP, "+"),
            (token.NAME, "c"),
        ]
    )
    pg.gettoken()
    a, z = pg.parse_alt()
    assert len(a.arcs) == 1
    assert a.arcs[0][0] is None
    assert len(a.arcs[0][1].arcs) == 1
    assert a.arcs[0][1].arcs[0][0] == "a"
    assert len(a.arcs[0][1].arcs[0][1].arcs) == 1

# Generated at 2022-06-13 18:02:58.313658
# Unit test for method make_first of class ParserGenerator
def test_ParserGenerator_make_first():
    ob = ParserGenerator()
    ob.symbol2number = {'2': 0, '1': 1, '3': 2}
    ob.labels = [(0, None), (1, None), (2, None), (3, None), (4, None)]
    ob.symbol2label = {'2': 0, '1': 1, '3': 2}
    ob.tokens = {3: 4, 4: 3}
    ob.keywords = {'a': 0, 'b': 1, 'c': 2}
    ob.make_label(ob, '')
    ob.make_label(ob, '"')
    ob.make_label(ob, '"abc')
    ob.make_label(ob, '"10')
    ob.make_label(ob, '"10.5')

# Generated at 2022-06-13 18:03:08.945836
# Unit test for method simplify_dfa of class ParserGenerator
def test_ParserGenerator_simplify_dfa():
    pg = ParserGenerator()
    dfa = [DFAState({NFAState(): 1}, None), DFAState({NFAState(): 1}, None)]
    dfa[0].addarc(dfa[1], 'a')
    dfa[0].addarc(dfa[1], 'b')
    dfa[1].addarc(dfa[0], 'c')
    dfa[1].addarc(dfa[0], 'd')
    pg.simplify_dfa(dfa)
    assert dfa == [DFAState({NFAState(): 1, NFAState(): 1}, None)]


if __name__ == "__main__":
    import sys

    def test(fname: Text) -> None:
        with open(fname) as fp:
            pg = ParserGenerator()

# Generated at 2022-06-13 18:03:19.929515
# Unit test for method make_dfa of class ParserGenerator
def test_ParserGenerator_make_dfa():
    print("=== unit test for ParserGenerator.make_dfa() ===")
    pg = ParserGenerator()
    a, z = pg.parse_rhs()
    dfa = pg.make_dfa(a, z)
    pg.dump_dfa("test", dfa)


# Generated at 2022-06-13 18:03:28.333388
# Unit test for method make_first of class ParserGenerator
def test_ParserGenerator_make_first():
    import os
    import tokenize
    import pytest
    import sys
    import inspect

    from py_backwards.tests.support import get_python_path

    with open(get_python_path(), "rb") as f:
        tokens = tokenize.tokenize(f.readline)

        par = ParserGenerator(get_python_path(), tokenize, tokens, None)
        par.parse()
        par.addfirstsets()


# Generated at 2022-06-13 18:03:37.436828
# Unit test for method raise_error of class ParserGenerator
def test_ParserGenerator_raise_error():
    generator = iter([(token.NAME, "x"), (token.OP, ":")])
    parser = ParserGenerator(generator, "test_ParserGenerator_raise_error.txt", None)
    try:
        parser.expect(token.NAME, "y")
    except SyntaxError as e:
        filename, lineno, offset, text = e.args[1]
        assert lineno == 1
        assert offset == 1
        assert text == "x :"
        assert e.args[0] == "expected NAME/y, got NAME/x"
    else:
        assert False, "Expected SyntaxError"



# Generated at 2022-06-13 18:03:49.912990
# Unit test for method make_dfa of class ParserGenerator
def test_ParserGenerator_make_dfa():
    class NFAState:
        def __init__(self):
            self.arcs = []

        def addarc(self, next, label=None):
            self.arcs.append((label, next))

    class DFAState:
        def __init__(self, nfaset, finish):
            self.nfaset = nfaset
            self.isfinal = finish in nfaset
            self.arcs = {}

        def __eq__(self, other):
            return self.arcs == other.arcs

        def addarc(self, next, label=None):
            if label in self.arcs:
                assert self.arcs[label] == next, (self, label, next, self.arcs)
            else:
                self.arcs[label] = next


# Generated at 2022-06-13 18:04:26.718273
# Unit test for method raise_error of class ParserGenerator
def test_ParserGenerator_raise_error():
    pg = ParserGenerator()
    pg.filename = 1
    pg.end = (2, 3)
    pg.line = 4
    try:
        pg.raise_error("test")
    except SyntaxError as e:
        assert e.args == ("test", (1, 2, 3, 4)), e.args
    else:
        assert False, "no syntax error"

# Generated at 2022-06-13 18:04:37.098945
# Unit test for constructor of class ParserGenerator
def test_ParserGenerator():
    """
    >>> def get_parser_generator():
    ...     g = ParserGenerator(
    ...         r"""

# Generated at 2022-06-13 18:04:45.113205
# Unit test for method gettoken of class ParserGenerator
def test_ParserGenerator_gettoken():
    import io
    from . import parser
    from . import tokenize
    s = """
# A comment to be ignored
x = 3
    # Another comment
y = 5
"""
    f = io.StringIO(s)
    g = parser.ParserGenerator()
    g.generator = g.tokenize(f.readline)
    g.gettoken()
    assert g.type == token.NAME
    assert g.value == "x"
    g.gettoken()
    assert g.type == token.OP
    assert g.value == "="
    g.gettoken()
    assert g.type == token.NUMBER
    assert g.value == "3"
    g.gettoken()
    assert g.type == token.NEWLINE
    assert g.value == "\n"
    g.gettoken()
   

# Generated at 2022-06-13 18:04:51.469622
# Unit test for method parse_item of class ParserGenerator
def test_ParserGenerator_parse_item():
    from .grammar import ParserGenerator
    g = ParserGenerator("""\
    a: '1'
    """)
    assert g.parse_item() == (g.nfas[0][0], g.nfas[0][1])


if __name__ == "__main__":
    test_ParserGenerator_parse_item()

# Generated at 2022-06-13 18:04:59.993794
# Unit test for method make_grammar of class ParserGenerator
def test_ParserGenerator_make_grammar():
    import pickle
    fn = "pgen_test.out"
    f = open(fn, "wb")
    pg = ParserGenerator()
    pg.make_grammar("Python.asdl")
    pickle.dump(pg, f, 1)
    f.close()
    f = open(fn, "rb")
    pg2 = pickle.load(f)
    f.close()
    import os
    os.remove(fn)
    assert pg == pg2

# Generated at 2022-06-13 18:05:11.418479
# Unit test for method make_dfa of class ParserGenerator
def test_ParserGenerator_make_dfa():
    # NB. This is not intended to be a full test; merely to provide some
    # coverage of the method that's not otherwise covered.
    pg = ParserGenerator()
    a = pg.make_state()
    b = pg.make_state()
    c = pg.make_state()
    d = pg.make_state()
    a.addarc(b, "a")
    a.addarc(b, "b")
    b.addarc(c, "c")
    b.addarc(c, "d")
    c.addarc(d)
    d.addarc(c)
    dfa = pg.make_dfa(a, d)
    assert len(dfa) == 2

# Generated at 2022-06-13 18:05:21.903042
# Unit test for method parse_alt of class ParserGenerator
def test_ParserGenerator_parse_alt():
    generator = ParserGenerator(StringIO.StringIO("(test1 | test2)"), "<test>")
    # We don't care about the details of the state and NFA objects,
    # just the topology, which we can check by stringifying.
    start1, finish1 = generator.parse_alt()
    start2, finish2 = generator.parse_alt()
    print(start1)
    print(start2)
    assert str(start1) == str(start2)
    assert str(finish1) == str(finish2)
    print("Test passed")


# Generated at 2022-06-13 18:05:30.747597
# Unit test for constructor of class ParserGenerator
def test_ParserGenerator():
    p = ParserGenerator()
    p.add_rhs(["symbol"], None)
    p.add_rhs(["symbol"], None)
    p.add_rhs(["token"], None)
    p.add_rhs(["string", "token"], None)
    p.add_rhs(["symbol", "string"], None)
    p.add_rhs(["symbol", "symbol"], None)
    p.add_rhs([], None)
    p.compile()


# Generated at 2022-06-13 18:05:32.446058
# Unit test for method calcfirst of class ParserGenerator
def test_ParserGenerator_calcfirst():
    p = ParserGenerator("a: b | c")
    p.calcfirst("a")
    assert p.first["a"] == {"b": 1, "c": 1}


# Generated at 2022-06-13 18:05:39.141899
# Unit test for method parse_rhs of class ParserGenerator
def test_ParserGenerator_parse_rhs():
    pg = ParserGenerator()
    pg.setup([(token.NAME, "a"), (token.NEWLINE, "\n"), (token.NAME, "b"), (token.OP, "|"), (token.NAME, "c"), (token.NEWLINE, "\n")])
    assert pg.parse_rhs() == ([(None, 1)], 2)
    assert pg.parse_rhs() == ([(None, 3)], 4)
    assert pg.parse_rhs() == ([(None, 1), ('|', 3)], 4)
    pg.setup([(token.NAME, "a"), (token.OP, "|"), (token.NAME, "b"), (token.OP, "|"), (token.NAME, "c")])
    assert pg.parse_rhs() == ([(None, 1)], 2)
   

# Generated at 2022-06-13 18:06:46.977027
# Unit test for method make_first of class ParserGenerator
def test_ParserGenerator_make_first():
    py_grammar = get_python_grammar()
    parser = ParserGenerator(py_grammar, printdebug=False)
    parser.addfirstsets()
    PgenGrammar(parser).make_first(parser, "if_stmt")


# Generated at 2022-06-13 18:06:57.514464
# Unit test for method expect of class ParserGenerator
def test_ParserGenerator_expect():

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")

        class PyCF_Generator(ParserGenerator): pass

        parser = PyCF_Generator([], "foo.py", "utf-8")
        x = token.NAME
        y = "3"
        parser.type = x
        parser.value = y

        result = parser.expect(token.NAME, 3)
        assert result == "3"

        x = token.NUMBER
        y = "3"
        parser.type = x
        parser.value = y

        with pytest.raises(SyntaxError):
            parser.expect(token.NAME, 3)


# Generated at 2022-06-13 18:07:05.879719
# Unit test for method simplify_dfa of class ParserGenerator
def test_ParserGenerator_simplify_dfa():
    # In the following DFAs, the NFA states are named a, b, ...
    #
    # 1. Empty language (two states -- start and finish -- but no
    #    NFAs reach the finish state)
    a = NFAState()
    z = NFAState()
    dfa = [DFAState({a: 1}, z), DFAState({z: 1}, z)]
    pg = ParserGenerator()
    pg.simplify_dfa(dfa)
    assert dfa == [DFAState({a: 1}, z), DFAState({z: 1}, z)]
    #
    # 2. Same DFA, but no overlap between sets of NFA states in the
    #    states.
    a = NFAState()
    b = NFAState()
    c = NFAState()

# Generated at 2022-06-13 18:07:08.085342
# Unit test for method make_grammar of class ParserGenerator
def test_ParserGenerator_make_grammar():
    pg = ParserGenerator()
    pg.make_grammar("","")



# Generated at 2022-06-13 18:07:16.886707
# Unit test for method make_grammar of class ParserGenerator
def test_ParserGenerator_make_grammar():
    import unittest

    class TestParserGenerator(unittest.TestCase):
        def test_make_grammar(self):
            import pgen2.pgen

            class MockPGen:
                def __init__(self) -> None:
                    self.grammar = None

                def loadgrammar(self, filename: Text) -> None:
                    with open(filename, "rt") as fp:
                        self.grammar = pgen2.pgen.ParserGenerator().parse(fp)
                    # print repr(self.grammar)

                def printgrammar(self, stream: IO[Any]) -> None:
                    self.grammar.dump(stream)

                def printfirst(self, stream: IO[Any]) -> None:
                    self.printgrammar(stream)
                    self.grammar.addfirstsets()


# Generated at 2022-06-13 18:07:19.089249
# Unit test for function generate_grammar
def test_generate_grammar():
    g = generate_grammar(Path(__file__).with_name("Grammar.txt"))
    assert g.start == symbol.file_input
test_generate_grammar()

# Generated at 2022-06-13 18:07:35.705777
# Unit test for method dump_nfa of class ParserGenerator
def test_ParserGenerator_dump_nfa():
    from pgen2 import driver
    gram = driver.load_grammar("Grammar/Grammar")
    parser = ParserGenerator(gram)
    for name in parser.dfas:
        print("Rule", name)
        dfa = parser.dfas[name]
        parser.dump_dfa(name, dfa)
test_ParserGenerator_dump_nfa()

if __name__ == "__main__":
    import sys
    from pgen2 import driver

    if "--help" in sys.argv:
        print(
            "Usage: %s [<grammar.txt> <output.pgen>] | --help | --dump"
            % sys.argv[0]
        )
        sys.exit(0)
    elif "--dump" in sys.argv:
        test

# Generated at 2022-06-13 18:07:40.535415
# Unit test for method parse_rhs of class ParserGenerator
def test_ParserGenerator_parse_rhs():
    pg = ParserGenerator(r"""
        comment: '#' /[^\r\n]*/
        """)
    pg.build()
    pg.make_pgen()
    pgen = pg.make_grammar()
    assert isinstance(pgen, PgenGrammar)

# Generated at 2022-06-13 18:07:52.209517
# Unit test for method simplify_dfa of class ParserGenerator
def test_ParserGenerator_simplify_dfa():
    # Test that simplify_dfa works as intended
    p = ParserGenerator()
    # Create a DFA with two states which are identical
    a = DFAState({}, None)
    b = DFAState({}, None)
    a.addarc(b, '0')
    a.addarc(b, '1')
    dfa = [a, b]
    p.simplify_dfa(dfa)
    # The DFA must still have two states, but now the first one must be final
    assert len(dfa) == 2
    assert a.isfinal and not b.isfinal



# Generated at 2022-06-13 18:07:58.202978
# Unit test for method parse of class ParserGenerator
def test_ParserGenerator_parse():
    import parser
    import tokenize
    parser_generator = ParserGenerator()

# Generated at 2022-06-13 18:10:11.116156
# Unit test for constructor of class PgenGrammar
def test_PgenGrammar():
    PgenGrammar({'x': [('a', )]})



# Generated at 2022-06-13 18:10:20.794671
# Unit test for method parse_item of class ParserGenerator
def test_ParserGenerator_parse_item():
    parser = ParserGenerator()
    g = parser.make_grammar()

    class Tokenizer(tokenize.Tokenizer):

        def __init__(self, string: str):
            self.string = string
            self.index = 0

        def __iter__(self) -> Iterator[Tuple[int, str, Tuple[int, int], Tuple[int, int], str]]:
            return self

        def __next__(self) -> Tuple[int, str, Tuple[int, int], Tuple[int, int], str]:
            if self.index >= len(self.string):
                raise StopIteration
            c = self.string[self.index]
            tok_type = token.STRING if c == '"' else token.OP
            tok_string = '"' if c == '"' else c

# Generated at 2022-06-13 18:10:31.618086
# Unit test for method make_grammar of class ParserGenerator
def test_ParserGenerator_make_grammar():

    class TestConverter:
        def __init__(self) -> None:
            self.tokens = {
                token.STRING: 0,
                token.NAME: 1,
                token.LPAR: 2,
                token.RPAR: 3,
                token.COLON: 4,
                token.VBAR: 5,
                token.RARROW: 6,
                token.INDENT: 7,
                token.DEDENT: 8,
                token.NEWLINE: 9,
                token.ENDMARKER: 10,
            }
            self.keywords = {"False": 11, "None": 12, "True": 13}
            self.labels: List[Tuple[int, Optional[str]]] = []
            self.symbol2label: Dict[str, int] = {}
            self.sy

# Generated at 2022-06-13 18:10:38.452506
# Unit test for method parse_alt of class ParserGenerator
def test_ParserGenerator_parse_alt():
    import pprint

    # Make an instance
    PG = ParserGenerator()
    # Make some input
    input = "a | b"
    # Prepare the generator
    PG.make_pgen_grammar(input)
    # Invoke the method
    output = PG.parse_alt()
    # Check the output

# Generated at 2022-06-13 18:10:44.791402
# Unit test for method simplify_dfa of class ParserGenerator
def test_ParserGenerator_simplify_dfa():
    import io
    from ..pgen2 import token

    def create_states(states_desc: List[Tuple[List[Tuple[int, int]], bool]]) -> List:
        states = []
        for state_desc in states_desc:
            arcs = {arc_desc: arc for arc_desc, arc in state_desc[0]}
            states.append(DFAState(arcs, state_desc[1]))
        return states

    class MockParserGenerator(ParserGenerator):
        def simplify_dfa(self, dfa: List[DFAState]) -> None:
            ParserGenerator.simplify_dfa(self, dfa)
            self.dfas[self.startsymbol] = dfa


# Generated at 2022-06-13 18:10:52.615057
# Unit test for constructor of class PgenGrammar
def test_PgenGrammar():
    # grammar_file is a filehandle
    g = PgenGrammar(grammar_file=open("./pgen2.g", "r"))

# Generated at 2022-06-13 18:10:57.145534
# Unit test for method make_grammar of class ParserGenerator
def test_ParserGenerator_make_grammar():
    pg = ParserGenerator("<test>")
    pg.add("foo", [("name", "'a'"), ("name", "'b'")], None)
    pg.add("bar", [("name", "foo")], None)
    pg.make_grammar()
    # XXX

# Generated at 2022-06-13 18:11:00.759524
# Unit test for method dump_nfa of class ParserGenerator
def test_ParserGenerator_dump_nfa():
    """RST Source: :download:`/test/test_ParserGenerator.py`"""
    start = NFAState()
    finish = NFAState()
    start.addarc(finish, "x")
    start.addarc(finish, "y")

    pg = ParserGenerator("test")
    pg.dump_nfa("t1", start, finish)



# Generated at 2022-06-13 18:11:08.896027
# Unit test for method calcfirst of class ParserGenerator
def test_ParserGenerator_calcfirst():
    pg = ParserGenerator()
    pg.adddfa('file_input', [[None, '(', [0]], ['(', None, [1]], [')', None, [2]], ['|', None, [3]]])
    pg.addfirst('file_input', {None: 1})
    pg.calcfirst('file_input')
    assert pg.first["file_input"] == {'(': 1, '|': 1}
    pg.adddfa('eval_input', [['|', None, [0]], ['(', None, [1]]])
    pg.addfirst('eval_input', {None: 1})
    pg.addfirst('eval_input', {None: 1})
    pg.calcfirst('eval_input')

# Generated at 2022-06-13 18:11:13.395545
# Unit test for method dump_nfa of class ParserGenerator
def test_ParserGenerator_dump_nfa():
    # From the example grammar, what happens on "foo = bar baz"
    p = ParserGenerator()
    a = NFAState()
    b = NFAState()
    c = NFAState()
    a.addarc(b, "bar")
    b.addarc(c, "baz")
    p.dump_nfa("foo", a, c)