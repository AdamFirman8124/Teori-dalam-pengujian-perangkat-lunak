

# Generated at 2022-06-13 18:02:28.973372
# Unit test for constructor of class PgenGrammar
def test_PgenGrammar():
    PgenGrammar('')


# Generated at 2022-06-13 18:02:39.735209
# Unit test for method parse_rhs of class ParserGenerator
def test_ParserGenerator_parse_rhs():
    pg = ParserGenerator()

# Generated at 2022-06-13 18:02:46.103327
# Unit test for method addfirstsets of class ParserGenerator
def test_ParserGenerator_addfirstsets():
    pg = ParserGenerator()
    pg.dfas = {"A": [DFAState({}, None), DFAState({}, None)], "B": [DFAState({}, None)]}
    pg.dfas["A"][0].addarc("a", pg.dfas["A"][1])
    pg.dfas["A"][0].addarc("b", pg.dfas["B"][0])
    pg.dfas["B"][0].addarc("c", pg.dfas["A"][1])
    pg.addfirstsets()
    assert pg.first["A"] == {"a", "b"}
    assert pg.first["B"] == {"c"}

# Generated at 2022-06-13 18:02:54.868922
# Unit test for method make_label of class ParserGenerator
def test_ParserGenerator_make_label():
    from .converter import PgenGrammar

    def make_label(pg: ParserGenerator, label: str) -> int:
        c = pg.make_converter(["s"])
        return pg.make_label(c, label)

    assert make_label(ParserGenerator(), "NAME") == 2
    assert make_label(ParserGenerator(), "NUMBER") == 6
    assert make_label(ParserGenerator(), "STRING") == 16
    assert make_label(ParserGenerator(), "'\\n'") == 1
    assert make_label(ParserGenerator(), "'('") == 0
    assert make_label(ParserGenerator(), "'foo'") == 0
    assert make_label(ParserGenerator(), "s") == 0

# Generated at 2022-06-13 18:03:04.916329
# Unit test for method dump_nfa of class ParserGenerator
def test_ParserGenerator_dump_nfa():
    pg = ParserGenerator()
    rule = "abc : 'a' [ b | (c | d) ] 'e' [ 'f' | 'g' ]"
    pg.parsestring(rule)
    _dfas, startsymbol = pg.dfas, pg.startsymbol
    pg.dump_nfa(startsymbol, pg.dfas[startsymbol][0], pg.dfas[startsymbol][-1])

# Generated at 2022-06-13 18:03:12.279556
# Unit test for method parse of class ParserGenerator
def test_ParserGenerator_parse():

    import sys
    from . import grammarparser

    class Dummy(object):
        filename = "<string>"
        first = {}

    pg = Dummy()
    pgen = ParserGenerator(pg, grammarparser.parse_grammar(sys.stdin.read()))
    pgen.addfirstsets()
    pgen.make_parser()



# Generated at 2022-06-13 18:03:13.823628
# Unit test for constructor of class PgenGrammar
def test_PgenGrammar():
    pgen = PgenGrammar()



# Generated at 2022-06-13 18:03:23.850116
# Unit test for method simplify_dfa of class ParserGenerator
def test_ParserGenerator_simplify_dfa():
    # Create a DFA in which one state can be replaced by any of
    # two others (and the same with the replacements)
    a = DFAState({}, False)
    b = DFAState({}, False)
    c = DFAState({}, False)
    b.addarc(b, "b")
    b.addarc(c, "c")
    c.addarc(b, "b")
    c.addarc(c, "c")
    a.addarc(b, "a")
    a.addarc(c, "a")
    states = [a, b, c]
    parser = ParserGenerator()
    parser.simplify_dfa(states)
    # ParserGenerator.dump_dfa("test", states)
    assert len(states) == 2
    aa, b

# Generated at 2022-06-13 18:03:31.557713
# Unit test for method make_dfa of class ParserGenerator
def test_ParserGenerator_make_dfa():
    pgen = ParserGenerator()
    a = NFAState()
    z = NFAState()
    a.addarc(z, "a")
    dfas = pgen.make_dfa(a, z)
    assert dfas == [DFAState({a: 1}, z), DFAState({z: 1}, z)], dfas[0]
    a = NFAState()
    z = NFAState()
    a.addarc(z, "a")
    a.addarc(z, "b")
    dfas = pgen.make_dfa(a, z)
    assert dfas == [DFAState({a: 1}, z)], dfas[0].arcs
    a = NFAState()
    z = NFAState()
    a.addarc(z, None)
    df

# Generated at 2022-06-13 18:03:33.978907
# Unit test for function generate_grammar
def test_generate_grammar():
    g = generate_grammar()
    g.dump()


# Generated at 2022-06-13 18:04:43.341656
# Unit test for method make_grammar of class ParserGenerator

# Generated at 2022-06-13 18:04:54.120339
# Unit test for method make_grammar of class ParserGenerator

# Generated at 2022-06-13 18:05:04.115497
# Unit test for method raise_error of class ParserGenerator
def test_ParserGenerator_raise_error():
    assert False, "unimplemented"
    import unittest
    import StringIO
    import tokenize

    class FakeTokens:
        filename = "filename.py"
        nl_lineno = 9999

    class ParserGeneratorTestCase(unittest.TestCase):
        def test_raise_error(self):
            parser = ParserGenerator()


# Generated at 2022-06-13 18:05:09.955211
# Unit test for method addfirstsets of class ParserGenerator
def test_ParserGenerator_addfirstsets():
    source = r"""
        %ignore COMMA
        %start doc
        %%
        doc: name stuff | stuff;      // two alternatives
        name: NAME;
        stuff: NAME stuff | NUMBER;   // two alternatives
    """
    pg = ParserGenerator()
    pg.parse(source)
    pg.addfirstsets()


# Generated at 2022-06-13 18:05:13.607535
# Unit test for method gettoken of class ParserGenerator
def test_ParserGenerator_gettoken():
    import pgen2.grammar
    gen = pgen2.grammar.ParserGenerator(None)
    gen.gettoken() # Tests that SyntaxError is not raised


# Generated at 2022-06-13 18:05:24.750106
# Unit test for method dump_dfa of class ParserGenerator
def test_ParserGenerator_dump_dfa():
    pg = ParserGenerator()
    dfa = [
        DFAState({NFAState()}, NFAState()),
        DFAState({NFAState(), NFAState()}, NFAState()),
        DFAState({NFAState(), NFAState(), NFAState()}, NFAState()),
    ]
    dfa[0].addarc(dfa[0], 'a')
    dfa[0].addarc(dfa[0], 'a')
    dfa[0].addarc(dfa[1], 'b')
    dfa[0].addarc(dfa[2], 'c')
    dfa[1].addarc(dfa[0], 'a')
    dfa[1].addarc(dfa[1], 'a')

# Generated at 2022-06-13 18:05:26.427586
# Unit test for method addfirstsets of class ParserGenerator
def test_ParserGenerator_addfirstsets():
    pg = ParserGenerator(Grammar())
    pg.addfirstsets()


# Generated at 2022-06-13 18:05:36.482260
# Unit test for method addfirstsets of class ParserGenerator
def test_ParserGenerator_addfirstsets():
    pg = ParserGenerator()
    pg.dfas = {
        "a": [DFAState({0, 1}), DFAState({2, 3}, True)],
        "b": [DFAState({4, 5}), DFAState({6})],
        "c": [DFAState({7})],
    }
    pg.dfas["a"][0].addarc(pg.dfas["b"][0], "b")
    pg.dfas["a"][0].addarc(pg.dfas["c"][0], "c")
    pg.dfas["b"][1].addarc(pg.dfas["c"][0], "c")
    pg.startsymbol = "a"
    pg.addfirstsets()

# Generated at 2022-06-13 18:05:41.434324
# Unit test for constructor of class ParserGenerator
def test_ParserGenerator():
    pg = ParserGenerator([], {})
    assert pg.pgen_grammar.start == 0
    start = pg.pgen_grammar.states[0][0]
    assert start[0] == (pg.pgen_grammar.symbol2number["alternatives"], None)
    assert len(start) == 1



# Generated at 2022-06-13 18:05:53.201119
# Unit test for method calcfirst of class ParserGenerator
def test_ParserGenerator_calcfirst():
    pgen = ParserGenerator()
    pgen.make_dfas({
        "expr" : [
            ["expr", "expr", "+", "expr"], 
            ["expr", "expr", "-", "expr"], 
            ["expr", "expr", "*", "expr"], 
            ["expr", "expr", "/", "expr"], 
            ["(", "expr", ")"], 
            ["__NONTERM__0+1"]
        ], 
        "__NONTERM__0+1" : [
            ["__NONTERM__0+1", "__NONTERM__0+1"], 
            ["("], 
            [")"]
        ]
        },
        "expr")

# Generated at 2022-06-13 18:07:23.765260
# Unit test for method make_grammar of class ParserGenerator
def test_ParserGenerator_make_grammar():
    pg = ParserGenerator()
    pg.addproduction('big', 'a', 'b')
    pg.addproduction('small', 'c', 'd')
    pg.addproduction('micro', 'e')
    grammar = pg.make_grammar()
    assert grammar == {'big': [['a', 'b']], 'small': [['c', 'd']], 'micro': [['e']]}

# Generated at 2022-06-13 18:07:31.947687
# Unit test for method simplify_dfa of class ParserGenerator
def test_ParserGenerator_simplify_dfa():
    gram = ParserGenerator()

# Generated at 2022-06-13 18:07:41.185911
# Unit test for method make_first of class ParserGenerator

# Generated at 2022-06-13 18:07:48.558544
# Unit test for method expect of class ParserGenerator
def test_ParserGenerator_expect():
    pg = ParserGenerator()
    pg.gettoken()
    pg.expect(token.NAME, "spam")
    pg.expect(token.OP, ":")
    pg.expect(token.STRING, "eggs")
    pg.expect(token.NEWLINE)
    pg.expect(token.ENDMARKER)
    print("done")

# Unit test

# Generated at 2022-06-13 18:07:57.876733
# Unit test for method make_dfa of class ParserGenerator
def test_ParserGenerator_make_dfa():
    pg = ParserGenerator()
    # for name in 'a', 'ab', 'abc', 'abcde':
    for name in 'abc':
        a = NFAState()
        z = NFAState()
        for c in name:
            n = NFAState()
            a.addarc(n, c)
            a = n
        a.addarc(z)
        dfa = pg.make_dfa(a, z)
        assert [state.label() for state in dfa] == [name and name[0] or ''] + name + ['']



# Generated at 2022-06-13 18:07:59.516142
# Unit test for method dump_nfa of class ParserGenerator
def test_ParserGenerator_dump_nfa():
    myparser = ParserGenerator()
    myparser.dump_nfa(1, 2, 3)

# Generated at 2022-06-13 18:08:08.691304
# Unit test for method dump_nfa of class ParserGenerator
def test_ParserGenerator_dump_nfa():
    import io
    import unittest
    import pgen

    # If there is a SyntaxError in the argument to ParserGenerator (here, the
    # grammar source string), it gets propagated out.  Unfortuantely here we
    # drop the SyntaxError to IOError conversion.
    class TestCase(unittest.TestCase):
        def assertRaises(self, exc, func, *args):
            try:
                func(*args)
            except exc:
                return
            else:
                raise AssertionError("%s did not raise %s" % (func, exc))

    class FakeStderr:
        def write(self, s: object) -> int:
            assert isinstance(s, str)
            self.output.append(s)

    pg = pgen.ParserGenerator()
    pg

# Generated at 2022-06-13 18:08:15.563077
# Unit test for method expect of class ParserGenerator
def test_ParserGenerator_expect():
    from . import grammar
    pgen = ParserGenerator(grammar)
    pgen.gettoken = lambda: None
    pgen.type = token.NAME
    pgen.value = '"test"'
    t = pgen.expect(token.NAME, '"test"')
    assert t == '"test"'
    pgen.expect(token.NAME, '"test"', "TEST")
    None
    # raises(SyntaxError, pgen.expect, token.OP, '"test"')
    pgen.filename = 'test'
    pgen.end = (1, 1)
    # raises(SyntaxError, pgen.expect, token.OP, '"test"')
    pgen.expect(token.NAME, '"test"')
    # raises(SyntaxError, p

# Generated at 2022-06-13 18:08:23.198303
# Unit test for method parse_alt of class ParserGenerator
def test_ParserGenerator_parse_alt():
    '''Unit test for method parse_alt of class ParserGenerator'''
    # Initialise the ParserGenerator object
    pg = ParserGenerator()
    test_string = '"if" NAME ":" suite'
    state_list = pg.split(test_string)
    a, b = pg.parse_alt()
    print(state_list)
    assert (b == join_states(state_list[5:7]))
    assert (a == join_states(state_list[0:5]))


# Generated at 2022-06-13 18:08:30.421182
# Unit test for function generate_grammar
def test_generate_grammar():
    grammar = generate_grammar()
    grammar.check_all()
    pprint(grammar.dfas)
    pprint(grammar.first)
    print(grammar.start)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Unit test for class ParserGenerator
        class TestParserGenerator(unittest.TestCase):
            def test_check_all(self):
                grammar = generate_grammar()
                grammar.check_all()
                pprint(grammar.dfas)
                pprint(grammar.first)
                print(grammar.start)

        unittest.main(exit=False)
    else:
        generate_grammar()
# generate_grammar()