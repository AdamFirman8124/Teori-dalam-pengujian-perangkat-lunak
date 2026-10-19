

# Generated at 2022-06-14 02:39:09.603570
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    TransformationResult(tree=ast.parse(''),
                         tree_changed=True,
                         dependencies=[])


# Name of class to insert
ClassName = NamedTuple('ClassName', [('name', str)])

# Name of variable to insert
VariableName = NamedTuple('VariableName', [('name', str)])

# Name of variable to insert
FunctionName = NamedTuple('FunctionName', [('name', str)])

# Name of variable to insert
MethodName = NamedTuple('MethodName', [('name', str)])

# Method call to insert
MethodCall = NamedTuple('MethodCall', [('method_name', str),
                                       ('args', List[str])])

# Variable passed as argument to method
VariableArg = NamedTuple('VariableArg', [('name', str)])

# Insert a new

# Generated at 2022-06-14 02:39:12.860573
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input_path = "/path/to/input"
    output_path = "/path/to/output"
    input_output = InputOutput(input_path, output_path)
    assert input_output.input == input_path
    assert input_output.output == output_path


# Generated at 2022-06-14 02:39:14.358382
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    TransformationResult(ast.parse(''), False, [])

# Generated at 2022-06-14 02:39:16.828572
# Unit test for constructor of class InputOutput
def test_InputOutput():
    io = InputOutput(Path('/var/f/a'), Path('/var/f/b'))
    assert isinstance(io, InputOutput)



# Generated at 2022-06-14 02:39:18.340433
# Unit test for constructor of class InputOutput
def test_InputOutput():
    assert InputOutput(Path('/tmp/input'), Path('/tmp/output')) is not None

# Generated at 2022-06-14 02:39:21.373183
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    assert TransformationResult(tree=None, tree_changed=False, dependencies=[])

# Result of checkers check
CheckResult = NamedTuple('CheckResult', [('result', bool),
                                         ('violations', List[str])])

# Generated at 2022-06-14 02:39:26.984082
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    res = CompilationResult(1, 2.0, (3, 4), ['a', 'b', 'c'])
    assert(res.files == 1)
    assert(res.time == 2.0)
    assert(res.target == (3, 4))
    assert(res.dependencies == ['a', 'b', 'c'])


# Generated at 2022-06-14 02:39:28.689807
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    CompilationResult(1, 0.5, (3, 7), [])


# Generated at 2022-06-14 02:39:29.358394
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    TransformationResult(None, None, None)

# Generated at 2022-06-14 02:39:31.025409
# Unit test for constructor of class InputOutput
def test_InputOutput():
    assert InputOutput(Path("a"), Path("b")) == \
           InputOutput(input=Path("a"), output=Path("b"))


# Generated at 2022-06-14 02:39:35.798900
# Unit test for constructor of class InputOutput
def test_InputOutput():
    a = Path('test/test_test.py')
    b = Path('test/test_test.pyc')
    assert InputOutput(a, b) == InputOutput(a, b)
    assert InputOutput(a, b) != InputOutput(a, a)

# Generated at 2022-06-14 02:39:36.726590
# Unit test for constructor of class TransformationResult

# Generated at 2022-06-14 02:39:40.290891
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    class Tree(ast.AST):
        a = 42
    assert TransformationResult(tree = Tree(42),
                                tree_changed = False,
                                dependencies = []) == TransformationResult(tree = Tree(42),
                                                                            tree_changed = False,
                                                                            dependencies = [])

# Generated at 2022-06-14 02:39:42.196114
# Unit test for constructor of class InputOutput
def test_InputOutput():
    assert InputOutput(Path('a'), Path('b')).input == Path('a')
    assert InputOutput(Path('a'), Path('b')).output == Path('b')


# Generated at 2022-06-14 02:39:43.471715
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    TransformationResult(ast.Name('test', ast.Load()), True, ['test'])

# Generated at 2022-06-14 02:39:47.320353
# Unit test for constructor of class InputOutput
def test_InputOutput():
    # type: () -> None
    foo = Path('foo')
    bar = Path('bar')
    io = InputOutput(foo, bar)
    assert io.input == foo
    assert io.output == bar



# Generated at 2022-06-14 02:39:49.390572
# Unit test for constructor of class InputOutput
def test_InputOutput():
    inp = Path('/etc/hosts')
    out = Path('/tmp/hosts')
    inout_pair = InputOutput(inp, out)

    assert inout_pair.input == inp
    assert inout_pair.output == out

# Generated at 2022-06-14 02:39:51.279862
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    CompilationResult(files=3,
                      time=5.5,
                      target=(3, 6),
                      dependencies=[])


# Generated at 2022-06-14 02:39:54.562186
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    x = CompilationResult(files=2, time=3.14,
                          target=(3, 4), dependencies=['a', 'b'])
    assert x.files == 2
    assert x.time == 3.14
    assert x.target == (3, 4)
    assert x.dependencies == ['a', 'b']


# Generated at 2022-06-14 02:39:59.734503
# Unit test for constructor of class InputOutput
def test_InputOutput():
    path = Path('hello/world')
    input = Path(path.joinpath('input'))
    output = Path(path.joinpath('output'))
    assert InputOutput(input, output) == InputOutput(input, output)
    assert InputOutput(input, output) != InputOutput(output, input)

# Generated at 2022-06-14 02:40:06.698455
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree_changed = False
    tree = ast.parse('[a for a in range(10)]')
    dependencies = []
    TransformationResult(tree, tree_changed, dependencies)


# Result of a single transformer
TransformerResult = NamedTuple('TransformerResult',
                               [('result', TransformationResult),
                                ('transformer', 'Transformer')])


# Generated at 2022-06-14 02:40:11.247579
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    t = ast.parse('x=1')
    tr = TransformationResult(t, True, ['c1', 'c2'])
    assert tr.tree == t
    assert tr.tree_changed
    assert tr.dependencies == ['c1', 'c2']

# Generated at 2022-06-14 02:40:15.214767
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    c = CompilationResult(0, 0, (0, 0), [])
    assert c.files == 0
    assert c.time == 0
    assert c.target == (0, 0)
    assert c.dependencies == []
    assert c.time < 1



# Generated at 2022-06-14 02:40:16.910853
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    assert CompilationResult(1, 1.1, (3, 7), ['foo'])


# Generated at 2022-06-14 02:40:19.552363
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    result = CompilationResult(10, 1.0, (3, 7), ['a'])
    assert result.files == 10
    assert result.time == 1.0
    assert result.target == (3, 7)
    assert result.dependencies == ['a']
    str(result)  # for coverage


# Generated at 2022-06-14 02:40:24.612114
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    with pytest.raises(ValueError):
        TransformationResult(ast.Str('hello'), False, [])
    TransformationResult(ast.Str('hello'), True, [])
    TransformationResult(ast.Str('hello'), False, ['hello'])
    TransformationResult(ast.Str('hello'), True, ['hello'])

# Generated at 2022-06-14 02:40:26.961247
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    assert TransformationResult(tree=None,
                                tree_changed=False,
                                dependencies=[]) == TransformationResult()

# Generated at 2022-06-14 02:40:30.983179
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    t = ast.parse("print('TransformationResult')")  # type: ast.AST
    tr = TransformationResult(tree=t, tree_changed=True, dependencies=[])
    assert type(tr.tree) == ast.Module
    assert tr.tree_changed is True
    assert type(tr.dependencies) == list

# Generated at 2022-06-14 02:40:34.576660
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    cr = CompilationResult(
        files=0,
        time=0,
        target=(3, 5),
        dependencies=[])

    assert cr.files == 0
    assert cr.time == 0
    assert cr.target == (3, 5)
    assert cr.dependencies == []



# Generated at 2022-06-14 02:40:40.582011
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    files = 1
    time = 2.5
    target = (3, 5)
    dependencies = ['a', 'b']
    result = CompilationResult(files, time, target, dependencies)
    assert result.files == 1
    assert result.time == 2.5
    assert result.target == (3, 5)
    assert result.dependencies == ['a', 'b']


# Generated at 2022-06-14 02:40:49.325170
# Unit test for constructor of class TransformationResult
def test_TransformationResult(): # type: () -> None
    assert TransformationResult(ast.parse('pass'), False, [])


# Result of transpilation
TranspilationResult = NamedTuple('TranspilationResult',
                                 [('code', str),
                                  ('code_changed', bool)])


# Generated at 2022-06-14 02:40:54.365458
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    assert CompilationResult(files=1, time=10, target=(2, 7), dependencies=['a', 'b']) == \
           CompilationResult(files=1, time=10, target=(2, 7), dependencies=['a', 'b'])


# Generated at 2022-06-14 02:40:58.609677
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    assert TransformationResult(tree=None,
                                tree_changed=False,
                                dependencies=[]) != TransformationResult(tree=None,
                                                                          tree_changed=False,
                                                                          dependencies=[])

# Generated at 2022-06-14 02:41:01.632320
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    _ = CompilationResult(files=1, time=0.0, target=(3, 7), dependencies=['foo'])



# Generated at 2022-06-14 02:41:13.759233
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    assert CompilationResult(10, 3.0, (3, 6), ['a.py', 'b.py']).files == 10
    assert CompilationResult(10, 3.0, (3, 6), ['a.py', 'b.py']).time == 3.0
    assert CompilationResult(10, 3.0, (3, 6), ['a.py', 'b.py']).target == (3, 6)
    assert CompilationResult(10, 3.0, (3, 6), ['a.py', 'b.py']).dependencies == ['a.py', 'b.py']


# Generated at 2022-06-14 02:41:18.335636
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    target = (3, 5)
    dependencies = ['a', 'b']
    result = CompilationResult(files=1, time=2.0, target=target,
                               dependencies=dependencies)
    assert result.files == 1
    assert result.time == 2.0
    assert result.target == target
    assert result.dependencies == dependencies

# Generated at 2022-06-14 02:41:24.720935
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    v = CompilationResult(42, 3.14, (3, 4), [])
    assert(v.files == 42)
    assert(v.time == 3.14)
    assert(v.target == (3, 4))
    assert(v.dependencies == [])


# Generated at 2022-06-14 02:41:31.593108
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    res = CompilationResult(files=1,
                            time=1.0,
                            target=(3, 5),
                            dependencies=['dep1'])
    assert res.files == 1
    assert res.time == 1.0
    assert res.target == (3, 5)
    assert res.dependencies == ['dep1']



# Generated at 2022-06-14 02:41:37.985995
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    res = CompilationResult(files=1, time=2.0, target=(3, 4), dependencies=["5"])
    assert res.files == 1
    assert res.time == 2.0
    assert res.target == (3, 4)
    assert res.dependencies[0] == "5"


# Generated at 2022-06-14 02:41:41.042839
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input = Path('prefix')
    output = input.with_suffix('.py')
    pair = InputOutput(input, output)
    assert pair.input == input
    assert pair.output == output

# Generated at 2022-06-14 02:41:53.428363
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree = ast.parse("x = 'abc'", mode='eval')
    tree_changed = True
    dependencies = []

    TransformationResult(tree, tree_changed, dependencies)

# Generated at 2022-06-14 02:41:55.432607
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    assert TransformationResult(None, None, None) == (None, None, None)


# Generated at 2022-06-14 02:41:58.414776
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input_path = Path('/tmp/a.py')
    output_dir = Path('/tmp/out')
    output_path = Path('/tmp/out/a.py')
    pair = InputOutput(input_path, output_dir)
    assert pair.input == input_path
    assert pair.output == output_path

# Generated at 2022-06-14 02:42:00.325569
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    TransformationResult(None, False, [])

# Generated at 2022-06-14 02:42:03.128278
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    assert CompilationResult(12, 5, (3, 4), [os.path.abspath('dep.py')]) ==\
        CompilationResult(12, 5, (3, 4), [os.path.abspath('dep.py')])


# Generated at 2022-06-14 02:42:12.145432
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tr = TransformationResult(ast.Module(), True, [])
    assert isinstance(tr.tree, ast.AST)

# Result of transformer
TransformerResult = NamedTuple('TransformerResult',
                               [('status', bool),
                                ('data', str),
                                ('data_type', type)])

# Result of transformer with tree
TreeTransformerResult = NamedTuple('TreeTransformerResult',
                                   [('status', bool),
                                    ('data', str),
                                    ('data_type', type),
                                    ('tree', ast.AST)])

# Generated at 2022-06-14 02:42:15.008305
# Unit test for constructor of class InputOutput
def test_InputOutput():
    res = InputOutput(input=Path('input'),
                      output=Path('output'))
    assert len(res) == 2
    assert res.input == Path('input')
    assert res.output == Path('output')


# Generated at 2022-06-14 02:42:25.224007
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    t1 = ast.Module()
    t2 = ast.Module()
    assert TransformationResult(t1, True, []).tree is t1
    assert TransformationResult(t1, False, []).tree is t1
    assert TransformationResult(t2, True, []).tree is t2
    assert TransformationResult(t2, False, []).tree is t2
    assert TransformationResult(t1, False, []) == TransformationResult(t1, False, [])
    assert TransformationResult(t1, True, []) == TransformationResult(t1, True, [])
    assert TransformationResult(t1, True, []) != TransformationResult(t1, False, [])
    assert TransformationResult(t1, True, []) != TransformationResult(t2, True, [])

# Generated at 2022-06-14 02:42:29.319348
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input_path = Path('aa')
    output_path = Path('bb')
    io = InputOutput(input_path, output_path)
    assert io.input == input_path
    assert io.output == output_path


# Generated at 2022-06-14 02:42:35.379814
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    res = CompilationResult(files=1, time=1, target=(3, 5), dependencies=[])
    assert isinstance(res, NamedTuple)
    assert res.files == 1
    assert res.time == 1
    assert res.target[0] == 3
    assert res.target[1] == 5
    assert len(res.dependencies) == 0


# Generated at 2022-06-14 02:42:54.555739
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    CompilationResult(0, 0.0, (3, 8), [])


# Generated at 2022-06-14 02:43:01.387200
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    # pylint: disable=line-too-long
    res = CompilationResult(files=2, time=1.2, target=(3, 5), dependencies=['a', 'b'])
    assert res.files == 2
    assert res.time == 1.2
    assert res.target == (3, 5)
    assert res.dependencies == ['a', 'b']
    assert str(res) == "2 files compiled to python 3.5 with dependencies ['a', 'b'] in 1.2 seconds"

# Test constructor of class InputOutput

# Generated at 2022-06-14 02:43:03.852839
# Unit test for constructor of class InputOutput
def test_InputOutput():
    assert InputOutput(Path('input.py'), Path('output.py'))


# Generated at 2022-06-14 02:43:06.772414
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input_ = Path('input')
    output = Path('output')
    assert InputOutput(input=input_, output=output) == InputOutput(input_, output)

# Generated at 2022-06-14 02:43:10.850008
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input = Path('__init__.py')
    output = Path('__init__.c')
    pair = InputOutput(input, output)
    assert pair.input == input
    assert pair.output == output
    assert pair.input != output


# Generated at 2022-06-14 02:43:13.713631
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    x = ast.parse('x = 1')
    result = TransformationResult(tree=x,
                                  tree_changed=False,
                                  dependencies=[])
    assert isinstance(result, TransformationResult)

# Generated at 2022-06-14 02:43:17.374827
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    obj = TransformationResult(tree=None,
                               tree_changed=False,
                               dependencies=[])
    assert obj.tree is None
    assert obj.tree_changed is False
    assert obj.dependencies == []

# Generated at 2022-06-14 02:43:24.006156
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    import astor
    ast_tree = ast.parse("True")
    dependencies = ['file1', 'file2']
    tr = TransformationResult(ast_tree, True, dependencies)
    assert tr.tree_changed
    assert tr.dependencies == dependencies
    assert astor.to_source(tr.tree).strip() == "True"

# Generated at 2022-06-14 02:43:32.262622
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    res = TransformationResult(ast.parse('x = 1', mode='eval'), True, [])
    assert isinstance(res, NamedTuple)
    assert len(res) == 3
    assert res.tree_changed is True

# Supported python versions
PYTHON27 = (2, 7)
PYTHON34 = (3, 4)
PYTHON35 = (3, 5)
PYTHON36 = (3, 6)
PYTHON37 = (3, 7)

# Casing for compiling python 2 to python 3

# Generated at 2022-06-14 02:43:38.720874
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    d = CompilationResult(2, 0.1, (3, 6), ['./a.py', './b.py'])
    assert d.files == 2
    assert d.time == 0.1
    assert d.target == (3, 6)
    assert d.dependencies == ['./a.py', './b.py']


# Generated at 2022-06-14 02:44:25.749774
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    target = (3, 7)
    r = CompilationResult(2, 3.4, target, ["dep1.py", "dep2.py"])
    assert r.files == 2
    assert r.time == 3.4
    assert r.target == target
    assert r.dependencies == ["dep1.py", "dep2.py"]


# Generated at 2022-06-14 02:44:32.990540
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tr = TransformationResult(None, None, None)


# Result of the static analyser
AnalyserOutput = NamedTuple('AnalyserOutput',
                            [('success', bool),
                             ('type', str),
                             ('line', int),
                             ('column', int),
                             ('length', int),
                             ('message', str),
                             ('filename', str),
                             ('code', str)])


# Generated at 2022-06-14 02:44:36.795334
# Unit test for constructor of class InputOutput
def test_InputOutput():
    in_path = Path('.')
    out_path = Path('./out.txt')
    io = InputOutput(in_path, out_path)
    assert io.input == in_path
    assert io.output == out_path


# Generated at 2022-06-14 02:44:41.584682
# Unit test for constructor of class InputOutput
def test_InputOutput():
    path1 = Path('/tmp/1')
    path2 = Path('/tmp/2')
    t1 = InputOutput(path1, path2)
    t2 = InputOutput(input=path1, output=path2)
    assert t1 == t2
    assert t1.input == path1
    assert t1.output == path2

# Generated at 2022-06-14 02:44:47.683061
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    compilation_result = CompilationResult(files=1,
                                           time=0.0,
                                           target=(2, 7),
                                           dependencies=['a', 'b', 'c'])
    assert compilation_result.files == 1
    assert compilation_result.time == 0.0
    assert compilation_result.target == (2, 7)
    assert compilation_result.dependencies == ['a', 'b', 'c']


# Generated at 2022-06-14 02:44:50.478397
# Unit test for constructor of class InputOutput
def test_InputOutput():
    io = InputOutput(Path('input.py'), Path('output.py'))
    assert io.input == Path('input.py')
    assert io.output == Path('output.py')


# Generated at 2022-06-14 02:44:53.632029
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input = Path('/input')
    output = Path('/output')
    data = InputOutput(input, output)

    assert data.input == input
    assert data.output == output


# Generated at 2022-06-14 02:44:54.498461
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    TransformationResult(ast.AST(), False, [])

# Generated at 2022-06-14 02:44:59.589891
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    CompilationResult(files=5,
                      time=5.5,
                      target=(3, 6),
                      dependencies=['file1.py', 'file2.py'])


# Generated at 2022-06-14 02:45:09.362697
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    t = ast.Module([])

    # Normal case
    r = TransformationResult(t, True, ['a', 'b'])
    assert isinstance(r.tree, ast.AST)
    assert r.tree_changed is True
    assert r.dependencies == ['a', 'b']

    # When tree unchanged
    r = TransformationResult(t, False, ['a', 'b'])
    assert isinstance(r.tree, ast.AST)
    assert r.tree_changed is False
    assert r.dependencies == ['a', 'b']

# Generated at 2022-06-14 02:46:44.341965
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree = ast.Module()
    result = TransformationResult(tree, False, [])
    assert result.tree is tree
    assert result.tree_changed is False
    assert result.dependencies == []

# Generated at 2022-06-14 02:46:48.436982
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    assert TransformationResult(tree = None,
                                tree_changed = False,
                                dependencies = []).tree == None


# List of transformations
Transformations = List[TransformationResult]

# Generated at 2022-06-14 02:46:58.013005
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input1_path = Path("~/test/input.py")
    output1_path = Path("~/test/output.py")
    input_output1 = InputOutput(input1_path, output1_path)
    assert input_output1.input == input1_path
    assert input_output1.output == output1_path

    output2_path = Path("~/test/output2.py")
    input_output2 = input_output1._replace(output=output2_path)
    assert input_output2.input == input1_path
    assert input_output2.output == output2_path

    input_output3 = input_output2._replace(input=output2_path,
                                           output=input1_path)
    assert input_output3.input == output2_path
    assert input_

# Generated at 2022-06-14 02:47:03.510070
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    compilation_result = CompilationResult(files=10,
                                           time=1.0,
                                           target=(3, 5),
                                           dependencies=["a", "b"])
    assert isinstance(compilation_result.files, int)
    assert isinstance(compilation_result.time, float)
    assert isinstance(compilation_result.target, tuple)
    assert isinstance(compilation_result.dependencies, list)
    assert isinstance(compilation_result.dependencies[0], str)
    assert compilation_result.dependencies == ["a", "b"]
    

# Generated at 2022-06-14 02:47:08.132041
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    result = TransformationResult(tree=ast.parse('None'),
                                  tree_changed=True,
                                  dependencies=['/this/is/a/path.py'])
    assert result.tree == ast.parse('None')
    assert result.tree_changed == True
    assert '/this/is/a/path.py' in result.dependencies


# Generated at 2022-06-14 02:47:09.465393
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    CompilationResult(1, 1.1, (1, 2), ['foo'])


# Generated at 2022-06-14 02:47:12.334170
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    assert CompilationResult(files=3, time=0.5, target=(3, 6), dependencies=[''])



# Generated at 2022-06-14 02:47:17.253739
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tr = TransformationResult(None, False, None)


# Result of transformer
TransformerResult = NamedTuple('TransformerResult',
                               [('code', str),
                                ('time', float),
                                ('target', CompilationTarget),
                                ('dependencies', List[str])])


# Generated at 2022-06-14 02:47:21.743227
# Unit test for constructor of class InputOutput
def test_InputOutput():
    '''Test for constructor of class InputOutput'''
    input_before = Path('test.py')
    output_before = Path('test.py')

    input_after = input_before
    output_after = output_before

    inputoutput = InputOutput(input_after, output_after)

    assert inputoutput.input == input_before
    assert inputoutput.output == output_before


# Generated at 2022-06-14 02:47:24.871875
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    result = TransformationResult(tree=None, tree_changed=False, dependencies=[])
    assert result.tree == None
    assert not result.tree_changed
    assert result.dependencies == []