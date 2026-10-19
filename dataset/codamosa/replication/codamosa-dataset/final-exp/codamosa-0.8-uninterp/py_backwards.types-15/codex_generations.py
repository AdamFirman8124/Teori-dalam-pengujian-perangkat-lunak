

# Generated at 2022-06-14 02:39:03.862704
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    result = CompilationResult(
        files=1, time=42,
        target=(3,7),
        dependencies=['a.py'])



# Generated at 2022-06-14 02:39:05.590736
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    CompilationResult(0, 0.0, (0, 0), [])


# Generated at 2022-06-14 02:39:12.667288
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    assert\
        CompilationResult(files=20,
                          time=0.0,
                          target=(3, 7),
                          dependencies=[]) ==\
        CompilationResult(files=20,
                          time=0.0,
                          target=(3, 7),
                          dependencies=[])
    assert\
        CompilationResult(files=20,
                          time=0.0,
                          target=(3, 7),
                          dependencies=[]) !=\
        CompilationResult(files=40,
                          time=0.0,
                          target=(3, 7),
                          dependencies=[])


# Generated at 2022-06-14 02:39:16.442330
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    _ = TransformationResult(tree=None, tree_changed=False, dependencies=[])

# Result for each module
ModuleResult = NamedTuple('ModuleResult', [('name', str),
                                           ('result', CompilationResult)])

# Generated at 2022-06-14 02:39:17.884706
# Unit test for constructor of class InputOutput
def test_InputOutput():
    assert InputOutput(input=Path('input'), output=Path('output'))


# Generated at 2022-06-14 02:39:21.962411
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    ast.If(ast.Num(1), [], [])
    t = TransformationResult(ast.If(ast.Num(1), [], []), False, [])
    assert t.tree == ast.If(ast.Num(1), [], [])
    assert t.tree_changed == False
    assert t.dependencies == []

# Generated at 2022-06-14 02:39:25.293610
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    res = TransformationResult(None, False, None)
    assert res.tree is None
    assert res.tree_changed is False
    assert res.dependencies is None

# Generated at 2022-06-14 02:39:29.327017
# Unit test for constructor of class InputOutput
def test_InputOutput():
    path_input = Path('test_input')
    path_output = Path('test_outpuk')
    input_output = InputOutput(path_input, path_output)
    assert(input_output.input == path_input)
    assert(input_output.output == path_output)


# Generated at 2022-06-14 02:39:31.718120
# Unit test for constructor of class InputOutput
def test_InputOutput():
    assert InputOutput(Path("foo"), Path("bar")).input == Path("foo")
    assert InputOutput(Path("foo"), Path("bar")).output == Path("bar")


# Generated at 2022-06-14 02:39:33.585404
# Unit test for constructor of class InputOutput
def test_InputOutput():
    io = InputOutput(Path('a'), Path('b'))
    assert io.input == Path('a')
    assert io.output == Path('b')

# Generated at 2022-06-14 02:39:38.631745
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input = 1
    output = 2
    result = InputOutput(input, output)
    assert result.input == input
    assert result.output == output
    assert result[0] == input
    assert result[1] == output

# Generated at 2022-06-14 02:39:46.303335
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    python_filename = Path('/tmp/test_transform_tree.py')

# Generated at 2022-06-14 02:39:47.718940
# Unit test for constructor of class InputOutput
def test_InputOutput():
    assert InputOutput(input="a", output="b") == \
        InputOutput(Path("a"), Path("b"))

# Generated at 2022-06-14 02:39:50.582109
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree = ast.AST(body=[])
    TransformationResult(tree=tree, tree_changed=True, dependencies=[])
    TransformationResult(tree=tree, tree_changed=False, dependencies=[])
    TransformationResult(tree=tree, tree_changed=True, dependencies=['a', 'b'])
    TransformationResult(tree=tree, tree_changed=False, dependencies=['a', 'b'])

# Generated at 2022-06-14 02:39:54.753276
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    input_files = 1
    compilation_time = 1.0
    target = (3, 5)
    dependencies = ['stdlib']
    r = CompilationResult(input_files,
                          compilation_time,
                          target,
                          dependencies)
    assert r.files == 1
    assert r.time == 1.0
    assert r.target == (3, 5)
    assert r.dependencies == ['stdlib']


# Generated at 2022-06-14 02:39:59.048607
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree = ast.parse('def run():\n  return "ok"')

    result = TransformationResult(tree, True, [])

    assert result.tree == tree
    assert result.tree_changed == True
    assert result.dependencies == []

# Tags for nodes in an AST tree

# Generated at 2022-06-14 02:40:03.621611
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    res = CompilationResult(3, 0.3, (3, 7), ['matplotlib'])
    assert res.files == 3
    assert res.time == 0.3
    assert res.target == (3, 7)
    assert res.dependencies == ['matplotlib']


# Generated at 2022-06-14 02:40:05.853310
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    with pytest.raises(TypeError):
        TransformationResult(tree=ast.Module(),
                             tree_changed=True,
                             dependencies=None)

# Generated at 2022-06-14 02:40:10.204917
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    result = CompilationResult(files=10, time=0.005, target=(3, 8),
                               dependencies=['a', 'b', 'c'])
    assert result.files == 10
    assert result.time == 0.005
    assert result.target == (3, 8)
    assert result.dependencies == ['a', 'b', 'c']


# Generated at 2022-06-14 02:40:12.484579
# Unit test for constructor of class InputOutput
def test_InputOutput():
    assert InputOutput(input=Path('input'),
                       output=Path('output')) == \
           InputOutput._make([Path('input'), Path('output')])

# Generated at 2022-06-14 02:40:18.124723
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    # Setup
    t = ast.parse('pass')
    dependencies = []
    # Exercise
    result = TransformationResult(t, True, dependencies)
    # Verify
    assert result.tree is t
    assert result.tree_changed is True
    assert result.dependencies == dependencies

# Generated at 2022-06-14 02:40:23.832175
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    result = CompilationResult(2, 0.5, (3, 7), ['a', 'b'])
    assert result.files == 2
    assert result.time == 0.5
    assert result.target == (3, 7)
    assert result.dependencies == ['a', 'b']


# Generated at 2022-06-14 02:40:28.041684
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree_changed = False
    tree = ast.parse('pass')
    dependencies = ['one', 'two']
    transformer_out = TransformationResult(tree, tree_changed, dependencies)

    assert transformer_out.tree == tree
    assert transformer_out.tree_changed == tree_changed
    assert transformer_out.dependencies == dependencies

# Generated at 2022-06-14 02:40:31.246838
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    t = ast.parse('pass')
    r = TransformationResult(tree=t, tree_changed=True, dependencies=[])
    assert t == r.tree
    assert r.tree_changed
    assert isinstance(r.dependencies, list)

# Generated at 2022-06-14 02:40:35.593942
# Unit test for constructor of class InputOutput
def test_InputOutput():
    assert InputOutput(Path("test/test"), Path("test2/test2")).input.name == "test"
    assert InputOutput(Path("test/test"), Path("test2/test2")).output.name == "test2"
    assert InputOutput(Path("test/test"), Path("test2/test2")).input.parts == ["test", "test"]
    assert InputOutput(Path("test/test"), Path("test2/test2")).output.parts == ["test2", "test2"]


# Generated at 2022-06-14 02:40:41.934018
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    test_result = CompilationResult(files=10, time=42, target=(2, 7),
                                    dependencies=['spam', 'eggs', 'ham'])

    assert test_result.files == 10
    assert test_result.time == 42
    assert test_result.target == (2, 7)
    assert set(test_result.dependencies) == set(['spam', 'eggs', 'ham'])


# Generated at 2022-06-14 02:40:47.341411
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    result = CompilationResult(0, 0.1, (3, 5), [])
    assert result.files == 0
    assert result.time == 0.1
    assert result.target == (3, 5)
    assert result.dependencies == []



# Generated at 2022-06-14 02:40:53.060642
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    assert TransformationResult(ast.Num(1), True, []).tree == ast.Num(1)
    assert TransformationResult(ast.Num(1), True, []).tree_changed == True
    assert TransformationResult(ast.Num(1), True, []).dependencies == []

# By default result of transformers transformation does not change tree
# and there are no dependencies.
DEFAULT_TRANSFORMATION_RESULT = TransformationResult(None, False, [])

# Extension of file with python code
SOURCE_EXTENSION = '.py'
DIST_EXTENSION = '.dist'

# Generated at 2022-06-14 02:40:56.554381
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tr = TransformationResult(ast.AST(), True, ['a', 'b'])
    assert tr.tree is not None
    assert tr.tree_changed is True
    assert tr.dependencies == ['a', 'b']

# Generated at 2022-06-14 02:41:00.266726
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    res = TransformationResult(tree=None, tree_changed=False, dependencies=[])
    assert res.tree is None
    assert res.tree_changed is False
    assert len(res.dependencies) == 0


# Generated at 2022-06-14 02:41:08.083653
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input = Path('in')
    output = Path('out')
    io = InputOutput(input, output)
    assert io.input == input
    assert io.output == output


# Generated at 2022-06-14 02:41:12.781034
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input_out = InputOutput(Path('input'), Path('output'))
    assert input_out.input.name == 'input'
    assert input_out.output.name == 'output'


# Generated at 2022-06-14 02:41:14.887987
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    from typed_ast import ast3 as ast
    t = ast.parse('x = 1')
    return TransformationResult(t, False, [])

# Generated at 2022-06-14 02:41:16.236456
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    w = CompilationResult(1, 0.1, (3, 6), ["foo"])
    assert w.files == 1
    assert w.time == 0.1
    assert w.target == (3, 6)
    assert w.dependencies == ["foo"]


# Generated at 2022-06-14 02:41:18.270303
# Unit test for constructor of class CompilationResult
def test_CompilationResult():  # type: () -> None
    _ = CompilationResult(0, 0., (3, 5), [])
    assert True


# Generated at 2022-06-14 02:41:21.873565
# Unit test for constructor of class InputOutput
def test_InputOutput():
    assert InputOutput(input=Path('input.txt'), output=Path('output.txt'))


# Generated at 2022-06-14 02:41:26.882750
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    assert CompilationResult(files=42, time=666, target=(3, 5),
                             dependencies=['a', 'b', 'c'])

# Selection for transformer
TransformerSelection = NamedTuple('TransformerSelection',
                                  [('transformer', str),
                                   ('options', List[str]),
                                   ('files', List[Path]),
                                   ('glob', List[str])])

# Generated at 2022-06-14 02:41:38.265134
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    assert CompilationResult(1, 2.0, (1, 2), ["/path/to/a/file"]).files == 1
    assert CompilationResult(1, 2.0, (1, 2), ["/path/to/a/file"]).time == 2.0
    assert CompilationResult(1, 2.0, (1, 2), ["/path/to/a/file"]).target == (1, 2)
    assert CompilationResult(1, 2.0, (1, 2), ["/path/to/a/file"]).dependencies == ["/path/to/a/file"]


# Generated at 2022-06-14 02:41:42.978037
# Unit test for constructor of class InputOutput
def test_InputOutput():
    assert InputOutput(input=Path('a'),
                       output=Path('b')).input == Path('a')
    assert InputOutput(input=Path('a'),
                       output=Path('b')).output == Path('b')

# Generated at 2022-06-14 02:41:46.857500
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    from hypothesis import given
    from .hypothesis import strategies
    @given(strategies.transformation_result())
    def transformation_result(result):
        assert len(result.dependencies) > 0
        for dep in result.dependencies:
            assert type(dep) is str and len(dep) > 0

    transformation_result()

# Generated at 2022-06-14 02:42:02.142207
# Unit test for constructor of class InputOutput
def test_InputOutput():
    values = [
        (('a', 'b'), ('a', 'b')),
        (('a', 'b'), ('a', Path('b'))),
        (('a', Path('b')), ('a', Path('b'))),
        (('a', Path('b')), ('a', 'b')),
        (('a', 'b'), ('a', 'b')),
        ((Path('a'), 'b'), ('a', 'b')),
        (('a', 'b'), (Path('a'), 'b')),
        ((Path('a'), 'b'), (Path('a'), 'b'))
    ]
    for pair in values:
        assert InputOutput(*pair[0]) == InputOutput(*pair[1])

# Test of transformation of InputOutput to string

# Generated at 2022-06-14 02:42:05.050915
# Unit test for constructor of class InputOutput
def test_InputOutput():
    i, o = Path(__file__).with_suffix('.pyi'), Path(__file__).with_suffix('.py')
    io = InputOutput(i, o)
    assert io.input == i
    assert io.output == o


# Generated at 2022-06-14 02:42:15.712124
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree = ast.parse('a = 1')
    tr = TransformationResult(tree, True, ['dep1'])
    assert tr.tree is tree
    assert tr.tree_changed
    assert tr.dependencies == ['dep1']

#______________________________________________________________________________

# Command line arguments

# Generated at 2022-06-14 02:42:19.501987
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree = ast.parse('x=2')
    assert TransformationResult(tree, True, []) == TransformationResult(
        tree, True, [])


# Information about transformer
TransformerInfo = NamedTuple('TransformerInfo', [('name', str),
                                                 ('version', str)])


# Generated at 2022-06-14 02:42:23.748207
# Unit test for constructor of class InputOutput
def test_InputOutput():
    i = InputOutput(Path('./test.py'), Path('./test.pyc'))
    assert i.input.suffix == '.py'
    assert i.output.suffix == '.pyc'



# Generated at 2022-06-14 02:42:26.817732
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    result = CompilationResult(1, 0.5, (3, 6), [])
    assert result.files == 1
    assert result.time == 0.5
    assert result.target == (3, 6)
    assert result.dependencies == []


# Generated at 2022-06-14 02:42:32.890237
# Unit test for constructor of class InputOutput
def test_InputOutput():
    with pytest.raises(AssertionError):
        InputOutput(None, Path('/tmp'))

    with pytest.raises(AssertionError):
        InputOutput(Path('/tmp'), None)

    assert InputOutput(Path('/tmp'), Path('/tmp'))


# Generated at 2022-06-14 02:42:37.535738
# Unit test for constructor of class InputOutput
def test_InputOutput():
    test_i = Path("hello")
    test_o = Path("world")
    try_io = InputOutput(test_i, test_o)
    assert try_io.input == test_i
    assert try_io.output == test_o


# Generated at 2022-06-14 02:42:43.104369
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree = ast.Module([])
    dependencies = ['/path/to/file']
    result = TransformationResult(tree, True, dependencies)
    assert result.tree_changed == True
    assert result.dependencies == dependencies
    assert result.tree == tree

# Generated at 2022-06-14 02:42:45.657345
# Unit test for constructor of class InputOutput
def test_InputOutput():
    i = Path('foo/bar')
    o = Path('baz/qux')
    p = InputOutput(i, o)

    assert p.input == i
    assert p.output == o

# Generated at 2022-06-14 02:43:08.040480
# Unit test for constructor of class InputOutput
def test_InputOutput():
    i = InputOutput(Path("foo"), Path("bar"))
    assert i.input.__class__ == Path
    assert i.output.__class__ == Path



# Generated at 2022-06-14 02:43:09.942670
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    CompilationResult(1, 1.2, (2, 3), ['a', 'b'])



# Generated at 2022-06-14 02:43:13.305627
# Unit test for constructor of class InputOutput
def test_InputOutput():
    path1 = Path('test2/test3/test4.py')
    path2 = Path('test2/test_output/test4.pyc')
    io = InputOutput(input=path1, output=path2)



# Generated at 2022-06-14 02:43:15.246657
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    assert TransformationResult(tree=None, tree_changed=False,
                                dependencies=[])

# Generated at 2022-06-14 02:43:22.225914
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    result = CompilationResult(1, 12.0, (3, 5), ['a.py', 'b.py'])
    assert result.files == 1
    assert result.time == 12.0
    assert result.target == (3, 5)
    assert result.dependencies == ['a.py', 'b.py']


# Generated at 2022-06-14 02:43:24.464772
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    CompilationResult(files=3, time=12, target=(3, 6), dependencies=["a", "b"])

# Generated at 2022-06-14 02:43:28.049297
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    result = CompilationResult(files=1, time=0.0, target=(3, 5), dependencies=[])
    assert result.files == 1
    assert result.time == 0.0
    assert result.target == (3, 5)
    assert result.dependencies == []



# Generated at 2022-06-14 02:43:29.685539
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    CompilationResult(10, 10.0, (3, 5), [])


# Generated at 2022-06-14 02:43:31.142731
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    CompilationResult(1, 1.0, (3, 5), ['a'])


# Generated at 2022-06-14 02:43:36.668506
# Unit test for constructor of class InputOutput
def test_InputOutput():
    # Given
    input = Path("/tmp/my_input.txt")
    output = Path("/tmp/my_output.txt")

    # When
    io = InputOutput(input, output)

    # Then
    assert io.input == input
    assert io.output == output


# Generated at 2022-06-14 02:44:29.924688
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    cr = CompilationResult(files=1, time=1.0, target=(2, 7),
                           dependencies=['a'])
    assert cr.files == 1
    assert cr.time == 1.0
    assert cr.target == (2, 7)
    assert cr.dependencies == ['a']


# Generated at 2022-06-14 02:44:32.297370
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    CompilationResult(files=1, time=2.0, target=(3, 4),
                      dependencies=['a', 'b'])



# Generated at 2022-06-14 02:44:36.339370
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    res = CompilationResult(files=5, time=5.5, target=(3, 6), dependencies=[])
    assert res.files == 5
    assert res.time == 5.5
    assert res.target == (3, 6)
    assert res.dependencies == []


# Generated at 2022-06-14 02:44:43.763920
# Unit test for constructor of class InputOutput
def test_InputOutput():
    src = 'src.py'
    dst = 'dst.py'
    input = Path(src)
    output = Path(dst)

    io = InputOutput(input, output)
    assert io.input == input
    assert io.output == output
    assert io.input.name == src
    assert io.output.name == dst

# Generated at 2022-06-14 02:44:46.862445
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tr = TransformationResult(None, True, [])
    assert tr.tree is None
    assert tr.tree_changed is True
    assert tr.dependencies == []


# Generated at 2022-06-14 02:44:49.285643
# Unit test for constructor of class InputOutput
def test_InputOutput():
    p = InputOutput(Path("/"), Path("/"))
    assert p.input == Path("/")
    assert p.output == Path("/")


# Generated at 2022-06-14 02:44:51.333889
# Unit test for constructor of class InputOutput
def test_InputOutput():
    i = Path('')
    o = Path('a')
    InputOutput(i, o)

# Generated at 2022-06-14 02:44:57.608637
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input_val = Path('input')
    output_val = Path('output')
    input_output = InputOutput(input=input_val, output=output_val)
    assert input_val in (input_output.input, input_output.output)
    assert output_val in (input_output.input, input_output.output)


# Generated at 2022-06-14 02:45:03.998924
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    res = CompilationResult(files=4, time=5.0, target=(3, 7), dependencies=['some'])
    assert res.files == 4
    assert res.time == 5.0
    assert res.target == (3, 7)
    assert res.dependencies == ['some']


# Generated at 2022-06-14 02:45:07.254264
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    CompilationResult(1, 0.25, (3, 7), ['requests', 'aiohttp'])


# Generated at 2022-06-14 02:46:00.990486
# Unit test for constructor of class InputOutput
def test_InputOutput():
    _i = Path("a/b/c.py")
    _o = Path("d/e/f.py")
    _pair = InputOutput(input=_i, output=_o)
    assert _pair.input == _i
    assert _pair.output == _o


# Generated at 2022-06-14 02:46:07.681921
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    compilation_result = CompilationResult(1, 2, (3, 4), ['a', 'b'])
    assert compilation_result.files == 1
    assert compilation_result.time == 2
    assert compilation_result.target == (3, 4)
    assert compilation_result.dependencies == ['a', 'b']



# Generated at 2022-06-14 02:46:11.777670
# Unit test for constructor of class InputOutput
def test_InputOutput():
    # Input/output pair
    io = InputOutput(input='a.py', output='b/c.py')
    assert io.input == 'a.py'
    assert io.output == 'b/c.py'

# Generated at 2022-06-14 02:46:16.759138
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    assert CompilationResult(1, 2.3, (3, 4), ['a', 'b']) == \
           CompilationResult(files=1, time=2.3, target=(3, 4),
                             dependencies=['a', 'b'])
    assert CompilationResult(files=1, time=2.3, target=(3, 4),
                             dependencies=['a', 'b']) == \
           (1, 2.3, (3, 4), ['a', 'b'])



# Generated at 2022-06-14 02:46:20.514933
# Unit test for constructor of class InputOutput
def test_InputOutput():
    assert InputOutput(Path('a'), Path('b')) == \
        InputOutput(Path('a'), Path('b'))
    assert InputOutput(Path('a'), Path('b')) != \
        InputOutput(Path('a'), Path('c'))

# Unit tests for constructor of class CompilationResult

# Generated at 2022-06-14 02:46:29.201886
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    assert TransformationResult(ast.Module(), False, [])

# Definition of type-hint for function that returns output path
# (input and output type)
OutputFunc = Callable[[Path], Path]

# Definition of type-hint for function that transforms file
# (input and output type)
Transformer = Callable[[Path], TransformationResult]

# Definition of type-hint for function that generates transformers and input-output pairs
# (input and output type)
InputOutputs = Callable[[], List[InputOutput]]

# Definition of type-hint for function that compiles input-output pairs and returns
# CompilationResult
Compilation = Callable[[List[InputOutput]], CompilationResult]

# Definition of type-hint for function that compares input to output
# and returns True if they are the same

# Generated at 2022-06-14 02:46:34.740186
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    res = CompilationResult(2, 10, (3, 8), ['a', 'b'])
    assert res.files == 2
    assert res.time == 10
    assert res.target == (3, 8)
    assert res.dependencies == ['a', 'b']


# Generated at 2022-06-14 02:46:39.705065
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    compilation_result = CompilationResult(1, 2.0, (3, 4), ['a'])
    assert compilation_result.files == 1
    assert compilation_result.time == 2.0
    assert compilation_result.target == (3, 4)
    assert compilation_result.dependencies == ['a']


# Generated at 2022-06-14 02:46:41.687096
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    t = ast.parse('a = 1', mode='eval')
    tr = TransformationResult(t, True, [])
    assert tr.tree_changed is True
    assert len(tr.dependencies) == 0

# Generated at 2022-06-14 02:46:44.677816
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    CompilationResult(files=2, time=5,
                      target=(3, 1), dependencies=[])


# Generated at 2022-06-14 02:48:37.834928
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree = ast.Str('foo')
    result = TransformationResult(tree, False, [])
    assert result.tree == tree
    assert result.tree_changed == False
    assert result.dependencies == []

# Generated at 2022-06-14 02:48:46.702407
# Unit test for constructor of class TransformationResult
def test_TransformationResult():  # pylint: disable=W0612
    assert issubclass(TransformationResult, NamedTuple)
    assert TransformationResult._fields == ('tree', 'tree_changed', 'dependencies')  # noqa: E501,W0212


# Name of the class that is used as the root of the module
# (i.e. when `tree == None`)
ROOT_CLASSNAME = '__Root'

# Name of the module attribute that is used as the name of
# the module (i.e. when `tree == None`)
MODULE_NAME_ATTRIBUTE = '__module_name'

# Name of the module attribute that is used as the name of
# the source code file of the module (i.e. when `tree == None`)
SOURCE_FILE_ATTRIBUTE = '__code__'

# Generated at 2022-06-14 02:48:49.087011
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input_file = './test.in'
    output_file = './test.out'

    input_output = InputOutput(Path(input_file), Path(output_file))
    assert input_output.input == input_file
    assert input_output.output == output_file



# Generated at 2022-06-14 02:48:53.411494
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input = Path('input')
    output = Path('output')
    io = InputOutput(input, output)

    assert io.input == input
    assert io.output == output


# Generated at 2022-06-14 02:48:56.362248
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    try:
        CompilationResult(files=3, time=3.1415926535, target=(3, 6),
                          dependencies=None)
    except:
        assert False, 'CompilationResult constructor failed'


# Generated at 2022-06-14 02:48:58.367211
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    TransformationResult(ast.parse('a = 5'), True, ['a', 'b'])

# Generated at 2022-06-14 02:49:04.604993
# Unit test for constructor of class InputOutput
def test_InputOutput():
    # Given
    path = Path(__file__)
    expected_value = path.parent / path.name

    # When
    io = InputOutput(str(expected_value), str(expected_value))

    # Then
    assert io.input == expected_value
    assert io.output == expected_value