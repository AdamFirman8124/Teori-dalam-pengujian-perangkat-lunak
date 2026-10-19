

# Generated at 2022-06-14 02:39:00.058733
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input_output = InputOutput('input', 'output')
    assert input_output.input == Path('input')
    assert input_output.output == Path('output')

# Generated at 2022-06-14 02:39:04.184872
# Unit test for constructor of class InputOutput
def test_InputOutput():
    inp = '/in/100/a.py'
    outp = '/out/100/a.py'
    io = InputOutput(Path(inp), Path(outp))
    assert io.input == inp
    assert io.output == outp


# Generated at 2022-06-14 02:39:07.796862
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    result = CompilationResult(1, 2, (3, 4), ['a', 'b'])
    assert result.files == 1
    assert result.time == 2
    assert result.target == (3, 4)
    assert result.dependencies == ['a', 'b']


# Generated at 2022-06-14 02:39:11.770294
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    data = CompilationResult(1, 2.0, (3, 4), ['a', 'b', 'c'])
    assert data.files == 1
    assert data.time == 2.0
    assert data.target == (3, 4)
    assert data.dependencies == ['a', 'b', 'c']


# Generated at 2022-06-14 02:39:20.738625
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    test_ast = ast.parse('a = 5')
    assert TransformationResult(test_ast,
                                False,
                                ['ast1']) == \
           TransformationResult(test_ast,
                                False,
                                ['ast1'])

    assert TransformationResult(test_ast,
                                False,
                                ['ast1']) != \
           TransformationResult(test_ast,
                                True,
                                ['ast1'])
    assert TransformationResult(test_ast,
                                False,
                                ['ast1']) != \
           TransformationResult(test_ast,
                                False,
                                ['ast1', 'ast2'])


# Generated at 2022-06-14 02:39:23.382712
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    CompilationResult(1, 1, (1, 1), ['a'])


# Generated at 2022-06-14 02:39:28.692815
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    """Unit test for constructor of class CompilationResult."""
    compilation = CompilationResult(files=1, time=1.0, target=(3, 7), dependencies=[])
    assert(compilation.files == 1)
    assert(compilation.time == 1.0)
    assert(compilation.target == (3, 7))
    assert(compilation.dependencies == [])


# Generated at 2022-06-14 02:39:32.219323
# Unit test for constructor of class InputOutput
def test_InputOutput():
    assert InputOutput(Path('./test.py'), Path('./test.py'))
    assert InputOutput(Path('~/test.py'), Path('~/test.py')).input.expanduser() == Path('~/test.py').expanduser()

# Generated at 2022-06-14 02:39:35.328534
# Unit test for constructor of class InputOutput
def test_InputOutput():
    p = Path('haha')
    io = InputOutput(p, p)
    assert io.input == p
    assert io.output == p
    assert io.output == io.input


# Generated at 2022-06-14 02:39:42.153429
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    result = CompilationResult(files=1,
                               time=42.0,
                               target=(3, 5),
                               dependencies=['dir1', 'dir2', 'dir3'])
    assert result.files == 1
    assert result.time == 42.0
    assert result.target == (3, 5)
    assert result.dependencies == ['dir1', 'dir2', 'dir3']
    assert str(result) == 'CompilationResult(files=1, time=42.0, target=(3, 5), dependencies=["dir1", "dir2", "dir3"])'


# Generated at 2022-06-14 02:39:46.356969
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    assert TransformationResult(None, False, []).tree is None
    assert not TransformationResult(None, False, []).tree_changed
    assert TransformationResult(None, False, []).dependencies == []

# Generated at 2022-06-14 02:39:48.039576
# Unit test for constructor of class CompilationResult
def test_CompilationResult(): # type: () -> None
    assert CompilationResult(
        files=1, time=20.0, target=(3, 5), dependencies=['foo', 'bar'])


# Generated at 2022-06-14 02:39:51.497989
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree = ast.Pass()
    tree_changed = False
    dependencies = []
    tr = TransformationResult(tree, tree_changed, dependencies)
    assert tr.tree == tree
    assert tr.tree_changed == tree_changed
    assert tr.dependencies == dependencies

# Generated at 2022-06-14 02:39:56.762532
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    result = CompilationResult(files=2, time=1.3, target=(3, 7), dependencies=['file1.py'])
    assert result.files == 2
    assert result.time == 1.3
    assert result.target == (3, 7)
    assert result.dependencies == ['file1.py']


# Generated at 2022-06-14 02:40:00.823954
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    c = CompilationResult(0, 2.5, (3, 5), [])
    assert c.files == 0
    assert c.time == 2.5
    assert c.target == (3, 5)
    assert c.dependencies == []

# Generated at 2022-06-14 02:40:03.861508
# Unit test for constructor of class InputOutput
def test_InputOutput():
    i = Path('/tmp')
    o = Path('/tmp')
    io = InputOutput(input=i, output=o)
    assert io.input == i
    assert io.output == o



# Generated at 2022-06-14 02:40:06.805337
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree = ast.parse("x = 1")
    result = TransformationResult(tree, True, [])
    assert result.tree == tree
    assert result.tree_changed
    assert result.dependencies == []

# Generated at 2022-06-14 02:40:08.793561
# Unit test for constructor of class InputOutput
def test_InputOutput():
    o = InputOutput(Path('.'), Path('..'))
    assert o.input == Path('.')
    assert o.output == Path('..')

# Generated at 2022-06-14 02:40:10.625747
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    CompilationResult(100, 1.23, (3, 7), 10)



# Generated at 2022-06-14 02:40:13.121897
# Unit test for constructor of class InputOutput
def test_InputOutput():
    p1 = Path('p1')
    p2 = Path('p2')

    InputOutput(p1, p2)



# Generated at 2022-06-14 02:40:20.181687
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree = ast.parse('a = 1')
    res = TransformationResult(tree, True, [])

    assert(res.tree_changed == True)
    assert(res.dependencies == [])
    assert(isinstance(res.tree, ast.Module))
    assert(isinstance(res.tree.body[0], ast.Assign))
    assert(isinstance(res.tree.body[0].targets[0], ast.Name))

# Generated at 2022-06-14 02:40:26.108669
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    result = CompilationResult(10, 10.0, (3, 5), ['a', 'b'])
    assert result.files == 10
    assert result.time == 10.0
    assert result.target == (3, 5)
    assert result.dependencies == ['a', 'b']


# Generated at 2022-06-14 02:40:27.706167
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    _ = CompilationResult(1, 1.2, (2, 3), ['a', 'b'])

# Generated at 2022-06-14 02:40:30.658728
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    t = ast.parse('x = 1')
    tr = TransformationResult(t, True, [])
    assert tr.tree == t
    assert tr.tree_changed
    assert not tr.dependencies

# Generated at 2022-06-14 02:40:37.007074
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    import ast
    r = TransformationResult(tree=ast.parse('pass', '<ast>'), tree_changed=True, dependencies=[])
    assert isinstance(r.tree, ast.AST)
    assert r.tree_changed is True
    assert isinstance(r.dependencies, list)
    assert len(r.dependencies) == 0

# Name of python executable
PYTHON = 'python'

# Name of python interpreter
PYTHON_DIST_NAME = 'python'

# Name of python interpreter distribution
PYTHON_DIST_VERSION = '1'

# Name of python interpreter
PYTHON_INTERPRETER = '{}-dist-{}'.format(PYTHON_DIST_NAME, PYTHON_DIST_VERSION)

# Name of python interpreter wheels
PY

# Generated at 2022-06-14 02:40:39.885570
# Unit test for constructor of class InputOutput
def test_InputOutput():
    assert InputOutput(Path('foo'),
                       Path('bar')) == InputOutput(input=Path('foo'),
                       output=Path('bar'))


# Generated at 2022-06-14 02:40:48.544705
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    assert CompilationResult(files=1, time=1.0, target=(3, 6), dependencies=[]).files == 1
    assert CompilationResult(files=1, time=1.0, target=(3, 6), dependencies=[]).time == 1.0
    assert CompilationResult(files=1, time=1.0, target=(3, 6), dependencies=[]).target == (3, 6)
    assert CompilationResult(files=1, time=1.0, target=(3, 6), dependencies=[]).dependencies == []


# Generated at 2022-06-14 02:40:50.849029
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input = Path('a')
    output = Path('b')
    inputoutput = InputOutput(input, output)
    assert inputoutput.input == input
    assert inputoutput.output == output

# Generated at 2022-06-14 02:40:55.118778
# Unit test for constructor of class InputOutput
def test_InputOutput():
    i = Path('i')
    o = Path('o')
    pair = InputOutput(i, o)
    assert pair.input == i
    assert pair.output == o


# Generated at 2022-06-14 02:40:58.610098
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input = Path("input")
    output = Path("output")
    io = InputOutput(input, output)
    assert io.input == input
    assert io.output == output

# Generated at 2022-06-14 02:41:05.017239
# Unit test for constructor of class InputOutput
def test_InputOutput():
    i1 = InputOutput('input', 'output')
    assert i1.input  == 'input'
    assert i1.output == 'output'

    i2 = InputOutput(Path('input'), Path('output'))
    assert i2.input  == Path('input')
    assert i2.output == Path('output')

# Generated at 2022-06-14 02:41:07.403274
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    assert TransformationResult(
        tree=None,
        tree_changed=True,
        dependencies=[]) is not None

# Generated at 2022-06-14 02:41:17.227625
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    r = CompilationResult(2, 3.4, (3, 2), ['hello'])
    assert r[0] == 2
    assert r[1] == 3.4
    assert r[2] == (3, 2)
    assert r[3] == ['hello']
    assert r.files == 2
    assert r.time == 3.4
    assert r.target == (3, 2)
    assert r.dependencies == ['hello']


# Generated at 2022-06-14 02:41:19.921678
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    c = CompilationResult(files=0, time=0.0, target=(2, 7), dependencies=[])
    assert c.files == 0
    assert c.time == 0.0
    assert c.target == (2, 7)
    assert c.dependencies == []


# Generated at 2022-06-14 02:41:25.548409
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    initial_tree = ast.parse("42")
    result = TransformationResult(tree=initial_tree,
                                  tree_changed=True,
                                  dependencies=[])
    assert(result.tree is initial_tree)
    assert(result.tree_changed is True)
    assert(result.dependencies == [])

# Generated at 2022-06-14 02:41:30.590558
# Unit test for constructor of class InputOutput
def test_InputOutput():
    i = Path('a.py')
    o = Path('b.py')
    input_output = InputOutput(input=i,
                               output=o)
    assert input_output.input == i
    assert input_output.output == o

# Generated at 2022-06-14 02:41:34.220279
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree = ast.parse('a = 6')
    result = TransformationResult(tree, True, [])
    assert result.tree == tree
    assert result.tree_changed
    assert result.dependencies == []

# Generated at 2022-06-14 02:41:43.286077
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    result = TransformationResult(None, False, [])
    assert result.tree is None
    assert not result.tree_changed
    assert result.dependencies == []

# Result of unit test
TestResult = NamedTuple('TestResult',
                        [('test_name', str),
                         ('time', float),
                         ('success', bool),
                         ('output', bytes)])

# Result of unit test with stdin
TestResultWithStdin = NamedTuple('TestResultWithStdin',
                                 [('test_name', str),
                                  ('time', float),
                                  ('success', bool),
                                  ('output', bytes),
                                  ('stdin', bytes)])


# Generated at 2022-06-14 02:41:47.868273
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    # Ignore type of 'mod'
    # pylint: disable=redefined-builtin
    mod = ast.Module()
    trans = TransformationResult(tree=mod, tree_changed=True, dependencies=[
                                 'mod1', 'mod2'])
    assert trans.tree is mod
    assert trans.tree_changed is True
    assert trans.dependencies == ['mod1', 'mod2']

# Generated at 2022-06-14 02:41:49.985522
# Unit test for constructor of class InputOutput
def test_InputOutput():
    a = InputOutput(input=Path('a'), output=Path('b'))
    assert a.input == Path('a')
    assert a.output == Path('b')


# Generated at 2022-06-14 02:41:59.487394
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    # type: () -> None
    cr = CompilationResult(files=1, time=1.5, target=(3, 5), dependencies=['foo'])
    assert cr.files == 1
    assert cr.time == 1.5
    assert cr.target == (3, 5)
    assert cr.dependencies == ['foo']


# Generated at 2022-06-14 02:42:02.909522
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    t = ast.parse('1')
    tr = TransformationResult(t, True, [])
    assert isinstance(tr.tree, ast.AST)
    assert isinstance(tr.tree_changed, bool)
    assert isinstance(tr.dependencies, list)

# Generated at 2022-06-14 02:42:05.521823
# Unit test for constructor of class InputOutput
def test_InputOutput():
    assert InputOutput(Path('input'), Path('output')).input.name == 'input'
    assert InputOutput(Path('input'), Path('output')).output.name == 'output'

if __name__ == '__main__':
    t = test_InputOutput()

# Generated at 2022-06-14 02:42:12.792132
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    import itertools
    target = (3, 7)
    dependencies = ["dependency_1",
                    "dependency_2"]
    result = CompilationResult(1, 2, target, dependencies)
    assert result.files == 1
    assert result.time == 2
    assert result.target == target
    assert result.dependencies == dependencies
    assert result == CompilationResult(*result)
    assert result == CompilationResult(*itertools.chain(result))


# Generated at 2022-06-14 02:42:15.295256
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input = Path.cwd()
    output = Path.home()
    result = InputOutput(input=input, output=output)

    assert result.input == input
    assert result.output == output


# Generated at 2022-06-14 02:42:17.980396
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree = ast.parse("assert True")
    tuple = TransformationResult(tree, False, [])
    assert tuple.tree == tree
    assert not tuple.tree_changed
    assert tuple.dependencies == []

# Generated at 2022-06-14 02:42:27.085087
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    try:
        CompilationResult(1, 'bad_time', (2, 3), [])
        raise Exception('CompilationResult constructor requires int for files')
    except:
        pass
    try:
        CompilationResult(1, 123.4, 'bad_target', [])
        raise Exception('CompilationResult constructor requires Tuple[int, int] for target')
    except:
        pass
    try:
        CompilationResult(1, 123.4, (2, 3), 'bad_deps')
        raise Exception('CompilationResult constructor requires List[str] for dependencies')
    except:
        pass

    # Should pass
    c = CompilationResult(1, 123.4, (2, 3), [])


# Generated at 2022-06-14 02:42:32.349264
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input_path = Path('test_input.in')
    output_path = Path('test_output.out')
    pair = InputOutput(input_path, output_path)

    assert pair.input == input_path
    assert pair.output == output_path


# Generated at 2022-06-14 02:42:34.062178
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    TranslationResult(tree=None, tree_changed=False, dependencies=[])

# Generated at 2022-06-14 02:42:41.318892
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    result = CompilationResult(files=4,
                               time=12.3,
                               target=(3, 4),
                               dependencies=['lib1', 'lib2'])
    assert result.files == 4
    assert result.time == 12.3
    assert result.target == (3, 4)
    assert result.dependencies == ['lib1', 'lib2']

# Generated at 2022-06-14 02:42:54.925827
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input = Path('input')
    output = Path('output')
    input_output = InputOutput(input=input, output=output)
    assert input_output.input == input
    assert input_output.output == output
    assert str(input_output) == '<input, output>'


# Generated at 2022-06-14 02:42:57.810799
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    # pylint: disable=unused-variable
    transformation_result = TransformationResult(tree=None,
                                                 tree_changed=None,
                                                 dependencies=None)

# Generated at 2022-06-14 02:42:59.885548
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    CompilationResult(files=1, time=1.0,
                      target=(2, 3), dependencies=[])


# Generated at 2022-06-14 02:43:06.970539
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    compilation_result = CompilationResult(files = 1, time = 1.0,
                                           target = (3,7),
                                           dependencies = ['dep1', 'dep2'])
    assert compilation_result.files == 1
    assert compilation_result.time == 1.0
    assert compilation_result.target == (3,7)
    assert compilation_result.dependencies == ['dep1', 'dep2']


# Generated at 2022-06-14 02:43:10.206575
# Unit test for constructor of class InputOutput
def test_InputOutput():
    inputoutput = InputOutput(Path('input.path'), Path('output.path'))
    assert inputoutput.input == Path('input.path')
    assert inputoutput.output == Path('output.path')


# Generated at 2022-06-14 02:43:13.557641
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree = ast.parse('pass')

    def transform(node: ast.AST) -> TransformationResult:
        return TransformationResult(node, True, ['foo'])

    tree2 = transform(tree)
    assert isinstance(tree2, TransformationResult)

# Generated at 2022-06-14 02:43:18.254595
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    result = CompilationResult(files=1, time=1.0, target=(3, 7),
                               dependencies=[])
    assert result.files == 1
    assert result.time == 1.0
    assert result.target == (3, 7)



# Generated at 2022-06-14 02:43:22.955191
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    value = TransformationResult(ast.parse('print(3)'),
                                 True,
                                 ['foo.py', 'bar.py'])
    assert value[0] is not None
    assert value[1] is True
    assert value[2] == ['foo.py', 'bar.py']

# Generated at 2022-06-14 02:43:29.789017
# Unit test for constructor of class InputOutput
def test_InputOutput():
    # Test default value
    io1 = InputOutput(None, None)
    assert io1.input is None
    assert io1.output is None

    # Test initialized constructor
    io2 = InputOutput(Path('foo.py'), Path('bar.py'))
    assert io2.input == Path('foo.py')
    assert io2.output == Path('bar.py')
    assert io2.input is not None
    assert io2.output is not None

# Generated at 2022-06-14 02:43:34.014522
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    t = ast.parse('pass')
    tr = TransformationResult(t, True, ['a'])
    assert tr.tree is t
    assert tr.tree_changed is True
    assert tr.dependencies == ['a']



# Generated at 2022-06-14 02:44:00.364255
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    cr = CompilationResult(0, 0.0, (0, 0), [])
    assert cr.files == 0
    assert cr.time == 0.0
    assert cr.target == (0, 0)
    assert cr.dependencies == []


# Generated at 2022-06-14 02:44:04.034303
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input = Path("./input.txt")
    output = Path("./output.txt")

    input_output_pair = InputOutput(input, output)
    assert input_output_pair.input == input
    assert input_output_pair.output == output



# Generated at 2022-06-14 02:44:05.930451
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tr = TransformationResult(ast.parse(""), True, [])
    assert isinstance(tr, TransformationResult)

# Generated at 2022-06-14 02:44:11.327458
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    result = CompilationResult(5, 10.5, (3, 7), ['test.py'])
    assert result.files == 5
    assert result.time == 10.5
    assert result.target == (3, 7)
    assert result.dependencies == ['test.py']



# Generated at 2022-06-14 02:44:15.486098
# Unit test for constructor of class InputOutput
def test_InputOutput():
    test_input = Path('a/b/c')
    test_output = Path('c/d/e')
    test_pair = InputOutput(test_input, test_output)

    assert test_pair.input == test_input
    assert test_pair.output == test_output

# Generated at 2022-06-14 02:44:18.094744
# Unit test for constructor of class InputOutput
def test_InputOutput():
    iop = InputOutput(Path("A"), Path("B"))
    assert iop.input == Path("A")
    assert iop.output == Path("B")


# Generated at 2022-06-14 02:44:20.868776
# Unit test for constructor of class InputOutput
def test_InputOutput():
    # Test that an input/output pair can be constructed
    input = Path('example/input.py')
    output = Path('example/output.py')
    InputOutput(input, output)


# Generated at 2022-06-14 02:44:22.765121
# Unit test for constructor of class InputOutput
def test_InputOutput():
    i, o = Path('/tmp/foo'), Path('/tmp/bar')
    io = InputOutput(i, o)
    assert io.input == i
    assert io.output == o



# Generated at 2022-06-14 02:44:24.856153
# Unit test for constructor of class InputOutput
def test_InputOutput():
    test = InputOutput(input=Path('input'),
                       output=Path('output'))
    assert test.input == Path('input')
    assert test.output == Path('output')

# Generated at 2022-06-14 02:44:29.866238
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    target = (3, 6)
    dependencies = ['a', 'b']
    r = CompilationResult(1, 2.0, target, dependencies)
    assert r.files == 1
    assert r.time == 2.0
    assert r.target == target
    assert r.dependencies == dependencies

# Generated at 2022-06-14 02:45:18.550321
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    assert TransformationResult(ast.AST(), False, [])

# Generated at 2022-06-14 02:45:20.621046
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    # type: () -> None
    assert TransformationResult(ast.Module([]), False, [])

# Generated at 2022-06-14 02:45:23.059660
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input = Path('/test/test')
    output = Path('/test/test.pyc')
    test = InputOutput(input, output)

    assert test.input == input
    assert test.output == output

# Generated at 2022-06-14 02:45:25.669813
# Unit test for constructor of class InputOutput
def test_InputOutput():
    _ = InputOutput(input=Path('foo'), output=Path('bar'))



# Generated at 2022-06-14 02:45:27.651148
# Unit test for constructor of class InputOutput
def test_InputOutput():
    assert InputOutput('foo.py', 'bar.py') == InputOutput(
        Path('foo.py'), Path('bar.py'))



# Generated at 2022-06-14 02:45:37.715160
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    ast_tree = ast.parse('x=3')
    ast_dependencies = [Path('deptest.txt'), Path('deptest1.txt')]
    res = TransformationResult(ast_tree, True, ast_dependencies)
    assert res.tree == ast_tree
    assert res.tree_changed == True
    assert res.dependencies == ['deptest.txt', 'deptest1.txt']

# Result of walker transformation
WalkerResult = NamedTuple('WalkerResult',
                          [('files', int),
                           ('dependencies', List[str])])


# Generated at 2022-06-14 02:45:39.898702
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    TransformationResult(None, False, [])

# Generated at 2022-06-14 02:45:42.944174
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    files = 0
    time = 0.0
    target = (3, 5)
    dependencies = []
    cr = CompilationResult(files, time, target, dependencies)
    assert isinstance(cr, CompilationResult)


# Generated at 2022-06-14 02:45:49.733088
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    res = CompilationResult(files=1,
                            time=2.0,
                            target=(3, 4),
                            dependencies=['a', 'b'])
    assert res.files == 1
    assert res.time == 2.0
    assert res.target == (3, 4)
    assert res.dependencies == ['a', 'b']

# Generated at 2022-06-14 02:45:56.367707
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    ast_node = ast.parse('foo()')
    assert TransformationResult(ast_node, True, ['foo']).tree == ast_node
    assert TransformationResult(ast_node, True, ['foo']).tree_changed == True
    assert TransformationResult(ast_node, True, ['foo']).dependencies == ['foo']

# Generated at 2022-06-14 02:47:44.009496
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    ast_node = ast.parse('print(1)')
    transform_result = TransformationResult(ast_node, True, [])
    assert ast_node == transform_result.tree
    assert True == transform_result.tree_changed
    assert [] == transform_result.dependencies

# Generated at 2022-06-14 02:47:46.593864
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree = ast.parse('123')
    assert(TransformationResult(tree, False, ['a']).tree_changed == False)

# Generated at 2022-06-14 02:47:52.125775
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    compilation_result = CompilationResult(1, 1.5, (3, 6), ['a', 'b', 'c'])

    assert compilation_result.files == 1
    assert compilation_result.time == 1.5
    assert compilation_result.target == (3, 6)
    assert compilation_result.dependencies == ['a', 'b', 'c']


# Generated at 2022-06-14 02:47:55.702092
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tr = TransformationResult(ast.AST(), True, [])
    assert tr.tree == ast.AST()
    assert tr.tree_changed == True
    assert tr.dependencies == []

# Generated at 2022-06-14 02:48:01.295603
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    result = CompilationResult(1, 2.0, (3, 4), ['a'])
    assert result.files == 1
    assert result.time == 2.0
    assert result.target == (3, 4)
    assert result.dependencies == ['a']


# Generated at 2022-06-14 02:48:05.329538
# Unit test for constructor of class InputOutput
def test_InputOutput():
    i = InputOutput(input=Path('input.py'), output=Path('output.py'))
    assert i.input == Path('input.py')
    assert i.output == Path('output.py')

# Generated at 2022-06-14 02:48:08.105925
# Unit test for constructor of class InputOutput
def test_InputOutput():
    p1 = Path('/tmp/a')
    p2 = Path('/tmp/b')
    io = InputOutput(p1, p2)
    assert io != None
    assert io.input == p1
    assert io.output == p2


# Generated at 2022-06-14 02:48:11.566071
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tr = TransformationResult(None, False, [])
    assert isinstance(tr.tree, ast.AST)
    assert isinstance(tr.tree_changed, bool)
    assert isinstance(tr.dependencies, List)

# Generated at 2022-06-14 02:48:17.888839
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    res = CompilationResult(files=10, time=3.14, target=(3, 7), dependencies=['foo/bar.py'])
    assert res.files == 10
    assert res.time == 3.14
    assert res.target == (3, 7)
    assert res.dependencies == ['foo/bar.py']


# Generated at 2022-06-14 02:48:22.562932
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    result = CompilationResult(1, 2, (3, 4), ['5'])
    assert result.files == 1
    assert result.time == 2
    assert result.target == (3, 4)
    assert result.dependencies == ['5']
