

# Generated at 2022-06-13 18:02:31.252969
# Unit test for method parse_item of class ParserGenerator
def test_ParserGenerator_parse_item():
    pg = ParserGenerator()
    parser_pickle = pg.parse()



# Generated at 2022-06-13 18:02:40.876048
# Unit test for method make_grammar of class ParserGenerator
def test_ParserGenerator_make_grammar():
    def grammar_to_tuple(g: Grammar) -> Tuple[int, List[Tuple[int, Any]], List[List[List[Tuple[int, int]]]], List[List[Tuple[int, int]]], List[Dict[int, int]]]:
        return g.start, g.labels, g.states, g.dfas, g.first
    def tuple_to_grammar(obj: Tuple[int, List[Tuple[int, Any]], List[List[List[Tuple[int, int]]]], List[List[Tuple[int, int]]], List[Dict[int, int]]]) -> Grammar:
        start, labels, states, dfas, first = obj
        return Grammar(start, labels, states, dfas, first)

    # Write a bunch of (name

# Generated at 2022-06-13 18:02:41.400485
# Unit test for constructor of class PgenGrammar
def test_PgenGrammar():
    pass



# Generated at 2022-06-13 18:02:45.989139
# Unit test for method calcfirst of class ParserGenerator
def test_ParserGenerator_calcfirst():
    import doctest
    doctest.testmod(ParserGenerator, optionflags=doctest.IGNORE_EXCEPTION_DETAIL)

test_ParserGenerator_calcfirst()

# Generated at 2022-06-13 18:02:54.584790
# Unit test for method addfirstsets of class ParserGenerator
def test_ParserGenerator_addfirstsets():
    from . import tokens
    lines = ["Arith : a='+' b=Arith c='*' d=Arith | a='+' b=Arith | a='*' b=Arith | '(' a=Arith ')' | a=Atom",
             "Atom : a=NUMBER | a=NAME",
             ""
            ]
    pg = ParserGenerator(tokens)
    pg.input(lines)
    pg.addfirstsets()
    assert pg.first['Arith'].keys() == {'(', 'NUMBER', "'+'", "'*'", 'NAME'}
    assert pg.first['Atom'].keys() == {'NUMBER', 'NAME'}



# Generated at 2022-06-13 18:02:56.162628
# Unit test for method make_grammar of class ParserGenerator
def test_ParserGenerator_make_grammar():
    pg = ParserGenerator()
    grammar = pg.make_grammar()



# Generated at 2022-06-13 18:03:03.698430
# Unit test for method gettoken of class ParserGenerator
def test_ParserGenerator_gettoken():
    from .tokenizer import tokenize
    from io import StringIO
    from .token import tok_name
    from . import ast

    s = StringIO("for x in range(10):\n    print(x)\n")
    g = tokenize(s.readline)
    p = ParserGenerator(g, "<stdin>")

    while p.type != token.ENDMARKER:
        print(p.type, token.tok_name[p.type], repr(p.value))
        p.gettoken()


# Generated at 2022-06-13 18:03:15.149903
# Unit test for method addfirstsets of class ParserGenerator
def test_ParserGenerator_addfirstsets():
    pg = ParserGenerator()
    pg.dfas = {
        'foo': ['start', 'state1', 'state2'],
        'bar': ['start', 'state1', 'state2'],
        'baz': ['start', 'state1', 'state2'],
    }
    pg.first = {'foo': {'a': 1, 'b': 1}, 'bar': {'b': 1, 'c': 1}}
    pg.addfirstsets()
    # print pg.first
    assert pg.first['foo'] == {'a': 1, 'b': 1}
    assert pg.first['baz'] == {'a': 1, 'b': 1, 'c': 1}

# Generated at 2022-06-13 18:03:21.050730
# Unit test for method raise_error of class ParserGenerator
def test_ParserGenerator_raise_error():
    """
    Test for tokenize.tokenize(method raise_error).
    """

    pgen = ParserGenerator(
        ""
    )  # TODO: Not sure how to test this. Need to mock the tokenizer
    with pytest.raises(
        SyntaxError
    ):  # TODO: Not sure what the proper SyntaxError msg should be
        pgen.raise_error("")



# Generated at 2022-06-13 18:03:21.916661
# Unit test for constructor of class PgenGrammar
def test_PgenGrammar():
    pg = PgenGrammar()



# Generated at 2022-06-13 18:03:57.744089
# Unit test for method parse_alt of class ParserGenerator
def test_ParserGenerator_parse_alt():
    from . import Token
    import unittest.mock
    from .. import pgen2
    p = pgen2.ParserGenerator(unittest.mock.MagicMock(filename="f"))
    # without '|'
    p.tokens = iter([
        Token(type=1, string="[", start=(1, 0), prefix="", end=(1, 1), line=''),
        Token(type=1, string="]", start=(1, 1), prefix="", end=(1, 2), line=''),
    ])
    p.value = None
    a, z = p.parse_alt()
    assert isinstance(a, pgen2.NFAState)
    assert isinstance(z, pgen2.NFAState)
    assert a.arcs == {(None, z)}

# Generated at 2022-06-13 18:04:04.473646
# Unit test for method make_grammar of class ParserGenerator
def test_ParserGenerator_make_grammar():
    from .pgen2 import driver
    from .pgen2 import token
    driver.main(["", "Grammar"])
    assert 'make_grammar' in driver.__dict__

    print("Running test_ParserGenerator_make_grammar...")
    pg = ParserGenerator()
    pg.make_grammar(grammar)
    try:
        pg.make_grammar(grammar, False)
        assert False
    except ValueError:
        pass
    try:
        pg.make_grammar(grammar, True)
    except ValueError:
        assert False, "pytest_pgen_make_grammar_ok"
    # print(pg.dfas)
    assert len(pg.dfas) == len(grammar.symbol2number)

# Generated at 2022-06-13 18:04:09.532957
# Unit test for method make_dfa of class ParserGenerator
def test_ParserGenerator_make_dfa():
    import py_grammar as g
    generator = ParserGenerator(g.grammar, g.syms, g.tokens, g.dfas)
    dfas = generator.dfas
    dfa = generator.make_dfa(dfas["factor"][0].nfaset, dfas["factor"][0].nfaset)
    generator.dump_dfa("factor", dfa)


# Generated at 2022-06-13 18:04:17.150583
# Unit test for method dump_dfa of class ParserGenerator
def test_ParserGenerator_dump_dfa():
    import unittest
    import io
    import token as token_module
    class TestParserGenDFA(unittest.TestCase):
        def test_dump_dfa(self):
            p = ParserGenerator()
            dfas, startsymbol = p.parse_grammar(io.StringIO(sample_grammar))
            for name in dfas:
                p.dump_dfa(name, dfas[name])
                states = dfas[name]
                for j, state in enumerate(states):
                    for label, next in state.arcs.items():
                        if isinstance(label, str):
                            label = token_module.STRING

# Generated at 2022-06-13 18:04:27.579741
# Unit test for method parse_rhs of class ParserGenerator
def test_ParserGenerator_parse_rhs():
    pg = None
    def test_parse(s: Text) -> None:
        nonlocal pg
        pg = ParserGenerator()
        pg.parse_rhs.__annotations__ = {
            'return': Tuple[NFAState, NFAState],
        }
        pg.parse_alt.__annotations__ = {
            'return': Tuple[NFAState, NFAState],
        }
        pg.parse_item.__annotations__ = {
            'return': Tuple[NFAState, NFAState],
        }
        pg.parse_atom.__annotations__ = {
            'return': Tuple[NFAState, NFAState],
        }
        pg.parse_rhs.__annotations__ = {
            'return': Tuple[NFAState, NFAState],
        }

# Generated at 2022-06-13 18:04:28.943717
# Unit test for constructor of class PgenGrammar
def test_PgenGrammar():
    pgen = PgenGrammar()
    assert pgen


# Generated at 2022-06-13 18:04:37.183378
# Unit test for method parse_item of class ParserGenerator
def test_ParserGenerator_parse_item():
    parser = ParserGenerator()
    from io import StringIO

    def test_parse_item(s, expected):
        parser.generator = tokenize.generate_tokens(StringIO(s).readline)
        parser.gettoken()
        parser.parse_item()
        assert parser.value == expected

    test_parse_item('[ a | b] ', ']')
    test_parse_item('a+', '+')
    test_parse_item('a*', '*')
    test_parse_item('a ', None)
    test_parse_item('(  ', ')')


# Generated at 2022-06-13 18:04:45.170147
# Unit test for method calcfirst of class ParserGenerator
def test_ParserGenerator_calcfirst():
    pg = ParserGenerator()
    pg.make_rhs = {}
    pg.make_rhs['file_input'] = {('NEWLINE','stmt','file_input'):1}
    pg.make_rhs['eval_input'] = {('exprlist','NEWLINE','NEWLINE'):1}
    pg.make_rhs['simple_stmt'] = {('small_stmt','small_stmt',None,None,None,None,None,None,None,None,None,None,None,None,None,'NEWLINE'):1}
    pg.make_first = {}
    pg.calcfirst('file_input')
    assert pg.first['file_input'] == {'NEWLINE':1}
    pg.calcfirst('eval_input')

# Generated at 2022-06-13 18:04:55.793712
# Unit test for method addfirstsets of class ParserGenerator
def test_ParserGenerator_addfirstsets():
    import pickle

    def test(pg: ParserGenerator, expected_first: Dict[Text, Dict[Text, int]]) -> None:
        pg.addfirstsets()
        # print "First sets:", pg.first
        assert pg.first == expected_first

    pg = ParserGenerator()

# Generated at 2022-06-13 18:05:05.112857
# Unit test for method addfirstsets of class ParserGenerator
def test_ParserGenerator_addfirstsets():
    # Test case for method "addfirstsets" of class "ParserGenerator"
    pg = ParserGenerator()
    pg.add_dfa('a', [{'x': 1, 'y': 1, 'z': 1}])
    pg.add_dfa('b', [{'x': 1, 'y': 1, 'z': 1}, {'z': 1, 'p': 2}, {'q': 1}])
    pg.add_dfa('c', [{'a': 1, 'b': 1}, {'c': 1, 'd': 2, 'e': 2}])
    pg.addfirstsets()
    assert pg.first['a'] == {'x': 1, 'y': 1, 'z': 1}

# Generated at 2022-06-13 18:05:55.933938
# Unit test for method parse_rhs of class ParserGenerator
def test_ParserGenerator_parse_rhs():
    pg = ParserGenerator()
    def gettoken():
        t = next(tokenize.generate_tokens(StringIO(text).readline))
        while t[0] in (tokenize.COMMENT, tokenize.NL):
            t = next(tokenize.generate_tokens(StringIO(text).readline))
        type, value, begin, end, line = t
        # print(token.tok_name[type], repr(value), begin)
        return type, value, begin, end, line
    pg.gettoken = gettoken
    def expect(type, value=None):
        t = next(tokenize.generate_tokens(StringIO(text).readline))
        type_, value_ = t[:2]

# Generated at 2022-06-13 18:06:03.168555
# Unit test for method parse_atom of class ParserGenerator
def test_ParserGenerator_parse_atom():
    global ParserGenerator
    class DFA:
        def __init__(self) -> None:
            self.arcs: Dict[Any, int] = {}

        def addarc(self, next: int, label: Any) -> None:
            self.arcs[label] = next

        def __eq__(self, other: Any) -> bool:
            return isinstance(other, DFA) and other.arcs == self.arcs

    class NFA:
        def __init__(self) -> None:
            self.arcs: Dict[Any, DFA] = {}

        def __eq__(self, other: Any) -> bool:
            return isinstance(other, NFA) and other.arcs == self.arcs


# Generated at 2022-06-13 18:06:11.650015
# Unit test for method raise_error of class ParserGenerator
def test_ParserGenerator_raise_error():
    msg = "msg"
    filename = "filename"
    end = (1, 1)
    line = "line"
    exc = None
    try:
        pg = ParserGenerator("")
        pg.filename = filename
        pg.end = end
        pg.line = line
        pg.raise_error(msg)
    except SyntaxError as ex:
        exc = ex
    assert exc.msg == msg
    assert exc.filename == filename
    assert exc.lineno == 2
    assert exc.offset == 2
    assert exc.text == line + "\n"

    exc = None

# Generated at 2022-06-13 18:06:18.530921
# Unit test for method dump_dfa of class ParserGenerator
def test_ParserGenerator_dump_dfa():
    from . import convert
    try:
        convert.grammar_pgen_file(None, "f.pgen", "f.ast")
        parser = convert.ParserGenerator("f.ast")
    except Exception:
        print("Skipped test for issue #901 due to failure to convert f.ast")
        return
    for dfa in parser.dfas.values():
        parser.dump_dfa("test", dfa)
test_ParserGenerator_dump_dfa.unittest = [".ast"]



# Generated at 2022-06-13 18:06:29.208184
# Unit test for method raise_error of class ParserGenerator
def test_ParserGenerator_raise_error():
    import tempfile, sys, io
    fd, filename = tempfile.mkstemp()
    f = open(fd, "w+t")

# Generated at 2022-06-13 18:06:38.609348
# Unit test for method parse of class ParserGenerator
def test_ParserGenerator_parse():
    from tokenize import generate_tokens, COMMENT, NL, NAME, OP, STRING
    from io import StringIO

    def srctotokens(src: Text) -> Iterable[Tuple[int, Text, Tuple[int, int], Tuple[int, int], Text]]:
        return generate_tokens(StringIO(src).readline)

    def tok_name(token: int) -> Text:
        return token.tok_name[token]

    def tokens(src: Text) -> Iterable[Tuple[int, Text]]:
        for token in srctotokens(src):
            typ, val, begin, end, line = token
            if typ in (COMMENT, NL):
                continue
            yield typ, val

    # Note: the parser generator (rightly) objects to non-unique token

# Generated at 2022-06-13 18:06:49.231800
# Unit test for method make_first of class ParserGenerator
def test_ParserGenerator_make_first():
    pg = ParserGenerator()
    c = PgenGrammar()
    # 1) a label that is a symbol name
    assert pg.make_label(c, "expr") == 0
    assert c.symbol2number["expr"] == 0
    assert not c.labels
    assert not c.tokens
    assert not c.keywords
    # 2) a label that is a keyword
    assert pg.make_label(c, "'for'") == 1
    assert c.labels == [(token.NAME, "for")]
    assert c.tokens == {}
    assert c.keywords == {'for': 1}
    # 3) a label that is an operator
    assert pg.make_label(c, "'+'") == 2

# Generated at 2022-06-13 18:07:00.548610
# Unit test for method simplify_dfa of class ParserGenerator
def test_ParserGenerator_simplify_dfa():
    # MSTART: (NEWLINE | RULE)* ENDMARKER
    # RULE: NAME ':' RHS NEWLINE
    # RHS: ALT ('|' ALT)*
    # ALT: ITEM+
    # ITEM: '[' RHS ']' | ATOM ['+' | '*']
    # ATOM: '(' RHS ')' | NAME | STRING
    a = NFAState()
    b = NFAState()
    c = NFAState()
    d = NFAState()
    e = NFAState()
    f = NFAState()
    g = NFAState()
    h = NFAState()
    i = NFAState()
    j = NFAState()
    k = NFAState()
    l = NFAState()
    m = NFAState()
    a

# Generated at 2022-06-13 18:07:17.131428
# Unit test for method make_first of class ParserGenerator
def test_ParserGenerator_make_first():
    from grammar_parser import ParserGenerator
    from dfa_builder import DFAState, NFAState
    from converter import PgenGrammar

    def make_nfa(dfa: List[DFAState], finish: "NFAState") -> "NFAState":
        nfa = NFAState()
        label, state = dfa[0].arcs[0]
        nfa.addarc(state, label)
        label, state = state.arcs[0]
        nfa.addarc(state, label)
        nfa.addarc(finish, None)
        label, state = state.arcs[0]
        nfa.addarc(state, label)
        state.addarc(finish)
        return nfa

    pg = ParserGenerator()

# Generated at 2022-06-13 18:07:22.765914
# Unit test for method parse_item of class ParserGenerator
def test_ParserGenerator_parse_item():
    import textwrap
    from .pgen2 import _get_grammar_rules
    from .driver import Driver
    from . import token
    from . import parser

    class RandomParser:
        grammar = textwrap.dedent(
            """
        eval        : expr ENDMARKER
        expr        : x=expr '+' y=expr  -> add(x,y)
                    | x=expr '-' y=expr  -> sub(x,y)
                    | INT
        """
        )

        def __init__(self):
            self.driver = Driver(self.grammar, parser.ParserGenerator, parser.Parser, 0, 0)
            self.rules = _get_grammar_rules(self.driver)

        def parse_expr(self):
            return self.rules["expr"].parse_item()


# Generated at 2022-06-13 18:08:49.882314
# Unit test for method make_label of class ParserGenerator
def test_ParserGenerator_make_label():
    from . import token
    from . import grammar
    pg = ParserGenerator()
    grammar.opmap[""] = 0

    class C(object):
        labels = []
        symbol2number = {}
        symbol2label = {}
        tokens = {}
        keywords = {}

    c = C()
    pg.make_label(c, "foo")
    assert c.symbol2label["foo"] == 0
    assert c.labels == [(0, None)]

    pg.make_label(c, "i")
    assert c.symbol2label["i"] == 0
    assert c.labels == [(0, None)]

    pg.make_label(c, "\"a\"")
    assert c.keywords["a"] == 1

# Generated at 2022-06-13 18:09:05.245720
# Unit test for method gettoken of class ParserGenerator
def test_ParserGenerator_gettoken():
    import tokenize, io
    pgen = ParserGenerator()
    pgen.filename = "<pgen>"
    pgen.generator = tokenize.generate_tokens(io.StringIO("Hello, world!\n").readline)
    assert pgen.gettoken() == (token.NAME, 'Hello')
    assert pgen.value == 'Hello'
    assert pgen.gettoken() == (token.OP, ',')
    assert pgen.value == ','
    assert pgen.gettoken() == (token.NAME, 'world')
    assert pgen.value == 'world'
    assert pgen.gettoken() == (token.OP, '!')
    assert pgen.value == '!'
    assert pgen.gettoken() == (token.ENDMARKER, '')

# Unit test

# Generated at 2022-06-13 18:09:16.098362
# Unit test for method make_first of class ParserGenerator
def test_ParserGenerator_make_first():
    for grammar in ("""\
expr:
    (expr '+'|'-' expr)
    | '(' expr ')'
    | NAME
    | NUMBER
""", """\
expr:
    (('-'|'+')? expr)
    | '(' expr ')'
    | NAME
    | NUMBER
"""):
        g = ParserGenerator()
        g.parse_grammar(StringIO(grammar))
        g.addfirstsets()
        expr_first = g.first["expr"]
        assert isinstance(expr_first, dict)
        assert ("-" in expr_first) + ("+" in expr_first) == 1



# Generated at 2022-06-13 18:09:25.784733
# Unit test for constructor of class ParserGenerator
def test_ParserGenerator():
    s = """
    expr: comp_op
        | comp_op '+' expr
        | comp_op '-' expr
        | '-' expr
    comp_op: '='
        | '/'
        | '*'
        | '+'
        | '-'
    """
    pg = ParserGenerator(s)
    pg.dump()
    s = """
    expr: comp_op bin_op_expr*
    bin_op_expr: '+' expr
        | '-' expr
    comp_op: '='
        | '/'
        | '*'
        | '+'
        | '-'
    """
    pg = ParserGenerator(s)
    pg.dump()

##class FakeConverter:
##  def __init__(self):
##      self.tokens

# Generated at 2022-06-13 18:09:39.356235
# Unit test for method simplify_dfa of class ParserGenerator
def test_ParserGenerator_simplify_dfa():
    from .pgen2 import parsetok
    from .pygram import python_symbols as syms
    from .pgen2 import tokenize, token

    # Make a list of all the constants in the token module(s)
    constants: List[Text] = []
    for name in dir(token):
        if name[0].isupper():
            constants.append(name)

    # Make a grammar out of that list
    grammar = "G: T* ; T: '%s' ;" % "|".join(constants)

    # Add the dotted rules
    dotted_rules = []
    for name in constants:
        dotted_rules.append("T.%s: '%s' ;" % (name, name))
    grammar += " ".join(dotted_rules)

    # Parse the grammar, and convert to D

# Generated at 2022-06-13 18:09:49.497002
# Unit test for method addfirstsets of class ParserGenerator
def test_ParserGenerator_addfirstsets():
    # XXX Should be autogenerated
    from . import ParserGenerator

    pg = ParserGenerator()
    pgen_grammar = pg.parse_grammar(grammar)

# Generated at 2022-06-13 18:09:53.932367
# Unit test for method make_first of class ParserGenerator
def test_ParserGenerator_make_first():
    parser_generator = ParserGenerator(src="")
    parser_generator.dfas = {}
    parser_generator.first = {}
    converter = Converter()
    from pgen2.grammar import Grammar

    grammar = Grammar(converter, src="")
    parser_generator.make_first(grammar, "foo")

# Generated at 2022-06-13 18:09:56.397154
# Unit test for method make_grammar of class ParserGenerator
def test_ParserGenerator_make_grammar():
    pg = ParserGenerator()
    pg.add_production(("S", "S + S"), ("S", "S * S"), ("S", "S % S"), ("S", "S / S"))
    pg.add_production(("S", "( S )"), ("S", "number"))
    pg.make_grammar()

# Generated at 2022-06-13 18:10:04.293442
# Unit test for method make_grammar of class ParserGenerator
def test_ParserGenerator_make_grammar():
    import graminit
    pgen = ParserGenerator("spam", "eggs")
    pgen.add_production("start", ("start", "start", "start"))
    pgen.add_production("start", ("start", "end", "end"))
    pgen.add_nonterminal("start")
    pgen.add_token("end", "END")
    pgen.add_token("others", "NUMBER")
    pgen.make_dfa("start")
    pgen.make_dfa("others")
    pgen.make_grammar()
    assert isinstance(pgen.grammar, PgenGrammar)
    assert isinstance(pgen.grammar.symbol2number, Dict)
    assert isinstance(pgen.grammar.tokens, Dict)

# Generated at 2022-06-13 18:10:07.264839
# Unit test for method calcfirst of class ParserGenerator
def test_ParserGenerator_calcfirst():
    pgen = ParserGenerator()
    pgen.pgen(StringIO(GRAMMAR))
    pgen.addfirstsets()
    pgen.write_tables(StringIO())
