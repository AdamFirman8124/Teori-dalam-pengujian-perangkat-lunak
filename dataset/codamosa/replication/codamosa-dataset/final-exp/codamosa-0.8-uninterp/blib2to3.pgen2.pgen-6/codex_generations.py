

# Generated at 2022-06-13 18:02:48.133102
# Unit test for constructor of class PgenGrammar
def test_PgenGrammar():
    pg = PgenGrammar(grammar.Grammar())
    assert pg.grammar.grammar == pg.grammar.grammar
    assert pg.init_actions == {1: 'p_file_input'}
    assert pg.rule2number == {1: 1}
    assert pg.number2rule == {1: 1}
    assert pg.dfas == {}
    assert pg.states == {}
    assert pg.error_func == 'p_error'
    assert pg.pgen_grammar is pg.grammar.grammar



# Generated at 2022-06-13 18:02:56.124546
# Unit test for constructor of class PgenGrammar
def test_PgenGrammar():
    # Test by creating a PgenGrammar instance from the input file
    g = PgenGrammar(
        "include/grammar/Grammar.txt",
        "include/grammar/Grammar.txt")
    assert repr(g)
    assert str(g)
    # Test by creating an empty PgenGrammar instance
    g2 = PgenGrammar(None, None)
    assert repr(g2)
    assert str(g2)
    g3 = PgenGrammar(None, None, True)
    assert repr(g3)
    assert str(g3)


# Generated at 2022-06-13 18:03:05.944339
# Unit test for method simplify_dfa of class ParserGenerator
def test_ParserGenerator_simplify_dfa():
    # Test the simplify_dfa method of ParserGenerator.
    import pgen2.tokenize
    import pickle

    def dumptree(name: Text, tree: Any) -> None:
        print("\nDumping", name)
        for k, v in tree.items():
            print(k, v)

    def dumpdfa(name: Text, dfa: List["DFAState"]) -> None:
        print("\nDumping DFA for", name)
        for i, state in enumerate(dfa):
            print("  State", i, state.isfinal and "(final)" or "")
            for label, next in sorted(state.arcs.items()):
                print("    %s -> %d" % (label, dfa.index(next)))


# Generated at 2022-06-13 18:03:16.701327
# Unit test for method parse_alt of class ParserGenerator
def test_ParserGenerator_parse_alt():
    pg = ParserGenerator()
    s = []
    def gettoken():
        s.append(next(pg.generator))

    pg.generator = tokenize.generate_tokens(StringIO("a b").readline)
    for x in range(3): gettoken()
    pg.type, pg.value, pg.begin, pg.end, pg.line = s[2]
    assert pg.parse_alt() == ([NFAState(arcs=[(None, NFAState(arcs=[('b', NFAState())]))]), NFAState(arcs=[(None, NFAState())])], NFAState())


# Generated at 2022-06-13 18:03:26.192414
# Unit test for method make_grammar of class ParserGenerator
def test_ParserGenerator_make_grammar():
    from pgen import ParserGenerator
    from test.support import captured_stdout
    ca_pgen = ParserGenerator()
    # Test for a bug #19045 in make_grammar()
    comment = """
    # Grammar produced by pgen2
    # From parsing package
    # Timestamp: Mon Mar  5 11:32:33 2001

    """

# Generated at 2022-06-13 18:03:33.098772
# Unit test for method dump_dfa of class ParserGenerator
def test_ParserGenerator_dump_dfa():
    p = ParserGenerator()
    # State 0
    dfa0 = DFAState({NFAState(0, [(None, NFAState(0, []))]),
                     NFAState(1, [(None, NFAState(1, []))])}, NFAState(1, []))
    dfa0.addarc(dfa0, 'e')
    dfa0.addarc(dfa0, 'E')
    dfa0.addarc(dfa0, '.')
    dfa0.addarc(dfa0, '0')
    dfa0.addarc(dfa0, '1')
    dfa0.addarc(dfa0, '2')
    dfa0.addarc(dfa0, '3')
    dfa0.addarc(dfa0, '4')


# Generated at 2022-06-13 18:03:35.046681
# Unit test for function generate_grammar
def test_generate_grammar():
    p = ParserGenerator()
    assert str(p.make_grammar()).startswith("Grammar(start=")



# Generated at 2022-06-13 18:03:36.757735
# Unit test for method parse_item of class ParserGenerator
def test_ParserGenerator_parse_item():
    a, b = ParserGenerator().parse_item()
    # nothing to do


# Generated at 2022-06-13 18:03:43.106339
# Unit test for method parse_alt of class ParserGenerator
def test_ParserGenerator_parse_alt():
    import sys
    from io import StringIO

    terminal_nodes = []
    for i in range(26):
        terminal_nodes.append(NFAState())
    X_start = NFAState()
    Y_start = NFAState()
    E_start = NFAState()

    def X_start_transitions():
        X_start.addarc(terminal_nodes[0])

    def terminal_nodes0_transitions():
        terminal_nodes[0].addarc(terminal_nodes[1])

    def terminal_nodes1_transitions():
        terminal_nodes[1].addarc(terminal_nodes[2])

    def terminal_nodes2_transitions():
        terminal_nodes[2].addarc(terminal_nodes[3])


# Generated at 2022-06-13 18:03:57.659192
# Unit test for method dump_nfa of class ParserGenerator
def test_ParserGenerator_dump_nfa():
    from mypy_extensions import NoReturn
    from typing import Tuple, List, Any, Optional, Text
    from typing import cast
    from typing import TYPE_CHECKING
    if TYPE_CHECKING:
        from _ast import AST
    #
    # ParserGenerator.dump_nfa
    #
    pg = ParserGenerator()
    #
    # The code below asserts that http://bugs.python.org/issue6633 is
    # still present.  That issue is present in Python 3.2.2.
    #

# Generated at 2022-06-13 18:04:28.529519
# Unit test for method make_grammar of class ParserGenerator
def test_ParserGenerator_make_grammar():
    import sys, os
    # This won't work until we have converted the whole of Python
    # into this new format.  I'll get round to it one day!
    #name = 'Grammar/Grammar'
    #name = 'Python/Grammar/Python'
    #name = os.path.join(sys.base_prefix, name)
    #c = ParserGenerator.make_grammar(open(name).readline)
    #c.dump()
    #c.write_c()
    #c.write_python()
    return
nfa_state_counter = 1

# Generated at 2022-06-13 18:04:33.237134
# Unit test for method parse of class ParserGenerator
def test_ParserGenerator_parse():
    pg = ParserGenerator()
    filename = "./data/grammar"
    dfa, start = pg.parse_grammar(filename)
    assert isinstance(start, str), start  # start symbol
    assert isinstance(dfa, dict), dfa  # DFA for each non-terminal



# Generated at 2022-06-13 18:04:39.217688
# Unit test for method make_grammar of class ParserGenerator
def test_ParserGenerator_make_grammar():
    print("test_ParserGenerator_make_grammar ...")
    # compiler/pgen2/pgen.py: make_grammar(...)
    parser_gen = ParserGenerator()
    parser_gen.make_grammar("Grammar/Python.3.7.grammar")
    print(
        "test_ParserGenerator_make_grammar passed:",
        parser_gen.dfas.keys(),
        parser_gen.startsymbol,
    )


# Generated at 2022-06-13 18:04:45.380906
# Unit test for method dump_dfa of class ParserGenerator
def test_ParserGenerator_dump_dfa():
    pg = ParserGenerator()
    try:
        pg.parsestring("""\
expr: x='(' expr ')'
    | NUMBER
    | NAME
    | expr '+' expr
    | expr '*' expr
    """)
    except ValueError as e:
        print("Oops", e)
        return
    # dfa0 is the DFA for rule expr
    dfa0 = pg.dfas["expr"]
    # dfa1 is the DFA for rule x
    dfa1 = pg.dfas["x"]

    

test_ParserGenerator_dump_dfa()
 


# Generated at 2022-06-13 18:04:55.912375
# Unit test for method make_grammar of class ParserGenerator

# Generated at 2022-06-13 18:05:03.131521
# Unit test for method __eq__ of class DFAState
def test_DFAState___eq__():
    assert DFAState({}, None) == DFAState({}, None)
    assert DFAState({}, None) != DFAState({object(): 1}, None)
    s1 = DFAState({}, None)
    assert s1 == s1
    s2 = DFAState({object(): 1}, None)
    assert s1 != s2
    s3 = DFAState({}, s2)
    assert s1 != s3
    assert s2 != s3
    s4 = DFAState({}, s2)
    assert s3 == s4



# Generated at 2022-06-13 18:05:12.781022
# Unit test for method parse_atom of class ParserGenerator
def test_ParserGenerator_parse_atom():
    t = ParserGenerator
    t.raise_error = lambda s,*a: print('ERROR', s % a)
    t.gettoken = lambda: None
    for a,b in (
        ("(", None),
        ("NAME", "NAME"),
        ("'string'", "string"),
        ("'('", None),
        ("[']", None),
    ):
        t.type = token.OP
        t.value = a
        try:
            print(t.parse_atom())
        except:
            pass
        else:
            if b is None:
                print('Expected error')
    return


# Generated at 2022-06-13 18:05:18.894019
# Unit test for method expect of class ParserGenerator
def test_ParserGenerator_expect():
    from .token import token, tokenize
    from .parsing import ParserGenerator

    grammar = """
        x:
            ( "[" "]" ) |
            ( "(" ")" ) |
            "{" "}"
    """

    generator = ParserGenerator()
    generator.parse_grammar(grammar)



# Generated at 2022-06-13 18:05:25.111609
# Unit test for method dump_nfa of class ParserGenerator
def test_ParserGenerator_dump_nfa():
    pg = ParserGenerator()
    filename = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "graminit.txt",
    )
    with open(filename) as fp:
        pg.parse_grammar(fp)
    # print repr(pg.dfas)
    for name, dfa in sorted(pg.dfas.items()):
        pg.dump_dfa(name, dfa)

# Generated at 2022-06-13 18:05:35.598288
# Unit test for constructor of class ParserGenerator
def test_ParserGenerator():
    pg = ParserGenerator()
    pg.add_symbol("name", ["a", "b", "c"])
    pg.add_symbol("expr", ["name", "(", "expr", ")"])
    pg.add_symbol("x", "a | b | c")
    pg.add_symbol("z", "!=\"")
    pg.add_symbol("y", "int", "float")
    pg.add_symbol("w", ["and", "or"])
    pg.add_symbol("v", ["y", "|", "w"])
    pg.add_symbol("u", ["v", "(", "x", ")"])
    pg.add_symbol("start", ["u", "?", "z"])
    pg.build()


# Generated at 2022-06-13 18:06:38.071532
# Unit test for method simplify_dfa of class ParserGenerator
def test_ParserGenerator_simplify_dfa():
    # The input to simplify_dfa is a list of DFAState instances.
    # This method modifies the list in place.
    pg = ParserGenerator()
    dfa = [
        DFAState({1: 1}, None),
        DFAState({2: 1}, None),
        DFAState({3: 1}, None),
        DFAState({4: 1}, None),
        DFAState({5: 1}, None),
        DFAState({6: 1}, None),
    ]
    dfa[0].addarc(dfa[1], "a")
    dfa[0].addarc(dfa[2], "b")
    dfa[1].addarc(dfa[2], "c")
    dfa[1].addarc(dfa[3], "d")

# Generated at 2022-06-13 18:06:49.043778
# Unit test for method gettoken of class ParserGenerator
def test_ParserGenerator_gettoken():
    pg = ParserGenerator()
    g = pg.get_generator([])
    def t(tup):
        pg.type, pg.value, pg.begin, pg.end, pg.line = tup
    # Issue #12901: detect whether the NL token is treated as a comment
    t(tokenize.generate_tokens(b'\n').__next__())
    assert pg.type == token.NAME, "Expected NAME after NL, got {}".format(token.tok_name[pg.type])
    # Issue #26406: detect whether the COMMENT token is skipped or not
    t(tokenize.generate_tokens(b'# comment').__next__())

# Generated at 2022-06-13 18:06:57.272738
# Unit test for method dump_nfa of class ParserGenerator
def test_ParserGenerator_dump_nfa():
    generator = ParserGenerator()
    parser_config = ConfigParser()
    parser_config.read_string(parser_config_str)
    parser_config.read(tests_dir / "grammar.cfg", encoding="utf-8")
    generator.prepare(parser_config)
    print("-" * 10, "dump_nfa of ParserGenerator", "-" * 10)
    print(generator)
    print("-" * 10, "end dump_nfa of ParserGenerator", "-" * 10)

# Generated at 2022-06-13 18:07:23.744718
# Unit test for method make_label of class ParserGenerator
def test_ParserGenerator_make_label():
    pg = ParserGenerator()
    pg.labels = []              # type: List[Tuple[int, Optional[str]]]
    pg.symbol2label = {}        # type: Dict[str, int]
    pg.symbol2number = {}       # type: Dict[str, int]
    pg.tokens = {}              # type: Dict[int, int]
    pg.keywords = {}            # type: Dict[str, int]
    c = pg.make_converter()
    assert c.make_label(c, "expr") == 0
    assert c.make_label(c, "expr") == 0
    assert c.make_label(c, "expr") == 0
    assert c.make_label(c, "NAME") == 1

# Generated at 2022-06-13 18:07:27.310953
# Unit test for constructor of class PgenGrammar
def test_PgenGrammar():
    print("test_PgenGrammar()")
    pgen_grammar_obj = PgenGrammar()
    assert isinstance(pgen_grammar_obj, PgenGrammar)
    assert isinstance(pgen_grammar_obj, grammar.Grammar)



# Generated at 2022-06-13 18:07:34.367139
# Unit test for method raise_error of class ParserGenerator
def test_ParserGenerator_raise_error():
    """Tests for ParserGenerator.raise_error"""
    parser = ParserGenerator()
    with pytest.raises(SyntaxError) as excinfo:
        parser.raise_error('test', '1', 2)
    assert excinfo.match('expected 1, got 2')
    with pytest.raises(SyntaxError) as excinfo:
        parser.raise_error('test', 'x', 'y')
    assert excinfo.match('expected x, got y')
    with pytest.raises(SyntaxError) as excinfo:
        parser.raise_error('test', 'a', 'b', 'c')
    assert excinfo.match('expected a b, got c')


# xfail: Python 2.6

# Generated at 2022-06-13 18:07:43.241827
# Unit test for method expect of class ParserGenerator
def test_ParserGenerator_expect():
    # Exercise the expect method of ParserGenerator
    def do_test(expect_type, expect_value, input_value):
        class my_ParserGenerator(ParserGenerator):
            def gettoken(self):
                self.type = token.STRING
                self.value = input_value

        pg = my_ParserGenerator(grammar.symbol2number, [], [], None, None)
        pg.expect(expect_type, expect_value)
    # Normal cases
    do_test(token.STRING, "1", "1")
    # Error cases
    def do_bad_expect(expect_type, expect_value, input_value):
        class my_ParserGenerator(ParserGenerator):
            def gettoken(self):
                self.type = token.STRING
                self.value

# Generated at 2022-06-13 18:07:53.298264
# Unit test for method addfirstsets of class ParserGenerator
def test_ParserGenerator_addfirstsets():
    g = ParserGenerator()
    g.add_nonterminal("XXX", ["YYY", "[", "ZZZ", "]"])
    g.add_nonterminal("YYY", ["NAME"])
    g.add_nonterminal("ZZZ", ["NAME", "=", "test"])
    g.addfirstsets()
    assert g.first["XXX"] == {"NAME": 1, "[": 1}
    assert g.first["YYY"] == {"NAME": 1}
    assert g.first["ZZZ"] == {"NAME": 1}



# Generated at 2022-06-13 18:07:58.794434
# Unit test for method dump_dfa of class ParserGenerator
def test_ParserGenerator_dump_dfa():
    filename = "Grammar.txt"
    f = open(filename)
    pg = ParserGenerator()
    dfas, startsymbol = pg.parsesuite(f)
    f.close()
    pg.addfirstsets()
    for name, dfa in dfas.items():
        pg.dump_dfa(name, dfa)
    return dfas, startsymbol

# Generated at 2022-06-13 18:08:04.123002
# Unit test for method calcfirst of class ParserGenerator
def test_ParserGenerator_calcfirst():
    pg = ParserGenerator(["root"], ["a b"])
    assert pg.first["root"] == {"a": 1}

    pg = ParserGenerator(["root"], ["a b", "a"])
    assert pg.first["root"] == {"a": 1}

