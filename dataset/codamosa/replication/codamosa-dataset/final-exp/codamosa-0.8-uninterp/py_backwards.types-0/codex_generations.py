

# Generated at 2022-06-14 02:39:03.815055
# Unit test for constructor of class InputOutput
def test_InputOutput():
    file_name = 'aaa'
    InputOutput(file_name, file_name)


# Generated at 2022-06-14 02:39:06.315040
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input = Path('input.py')
    output = Path('output.py')
    pair = InputOutput(input, output)
    assert pair.input == input
    assert pair.output == output

# Generated at 2022-06-14 02:39:08.410335
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    assert isinstance(TransformationResult(ast.ASTRoot(ast.ASTNode()),
                                           True,
                                           []),
                      TransformationResult)

# Generated at 2022-06-14 02:39:10.859238
# Unit test for constructor of class InputOutput
def test_InputOutput():
    assert InputOutput(Path('/home/bar/foo.py'),
                       Path('/home/bar/bar.py'))



# Generated at 2022-06-14 02:39:16.201480
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    res = TransformationResult(ast.AST(), True, ['a', 'b', 'c'])
    assert isinstance(res, TransformationResult)
    assert isinstance(res.tree, ast.AST)
    assert res.tree_changed
    assert isinstance(res.dependencies, list)
    assert len(res.dependencies) == 3
    assert all(isinstance(x, str) for x in res.dependencies)

# Generated at 2022-06-14 02:39:20.516670
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    t = ast.parse("def foo(): pass")
    tr = TransformationResult(tree=t, tree_changed=False, dependencies=[])
    assert tr.tree == t
    assert not tr.tree_changed
    assert not tr.dependencies

# Generated at 2022-06-14 02:39:28.471442
# Unit test for constructor of class InputOutput
def test_InputOutput():
    name = "file.py"
    i = InputOutput(input=Path("a/%s" % name), output=Path("a/b/%s" % name))
    assert i.input  == Path("a/%s" % name)
    assert i.output == Path("a/b/%s" % name)
    i.output = Path("c/%s" % name)
    assert i.input  == Path("a/%s" % name)
    assert i.output == Path("c/%s" % name)

# Generated at 2022-06-14 02:39:30.885685
# Unit test for constructor of class InputOutput
def test_InputOutput():
    assert InputOutput(Path('/hello/world'), Path('/hello/to_you')) \
                  == InputOutput(input=Path('/hello/world'),
                                 output=Path('/hello/to_you'))


# Generated at 2022-06-14 02:39:35.679008
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    assert CompilationResult(files=1,
                             time=0.0,
                             target=(3, 6),
                             dependencies=[]) == \
           CompilationResult(files=1,
                             time=0.0,
                             target=(3, 6),
                             dependencies=[])


# Generated at 2022-06-14 02:39:41.831937
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    with pytest.raises(TypeError):
        TransformationResult()

    with pytest.raises(TypeError):
        TransformationResult(tree=None)

    with pytest.raises(TypeError):
        TransformationResult(tree_changed=None)

    with pytest.raises(TypeError):
        TransformationResult(dependencies=None)

    with pytest.raises(TypeError):
        TransformationResult(None, None, None)

    TransformationResult(ast.parse('pass'), True, ['a', 'b'])


# Generated at 2022-06-14 02:39:44.087444
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    assert TransformationResult(None, False, None)


# Generated at 2022-06-14 02:39:47.970285
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    cr = CompilationResult(10, 0.1, (3, 7), ['stdlib'])
    assert len(cr.dependencies) == 1
    assert cr.time == 0.1
    assert isinstance(cr.dependencies[0], str)

# Generated at 2022-06-14 02:39:52.073521
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    TransformationResult(ast.parse('1'), True, ['a', 'b'])

# Result of target-finder transformation
TargetFinderResult = NamedTuple('TargetFinderResult',
                                [('tree', ast.AST),
                                 ('target', CompilationTarget),
                                 ('tree_changed', bool)])


# Generated at 2022-06-14 02:39:55.823552
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    ast_tree = ast.mod()

    tr = TransformationResult(ast_tree, False, [])

    assert tr.tree == ast_tree
    assert not tr.tree_changed
    assert len(tr.dependencies) == 0

# Generated at 2022-06-14 02:40:00.332113
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    assert TransformationResult(tree=None, tree_changed=True,
                                dependencies=['a.py'])

# Result of transformers execution
ExecutionResult = NamedTuple('ExecutionResult',
                             [('time', float),
                              ('input', Path),
                              ('inputs_changed', bool)])


# Generated at 2022-06-14 02:40:03.417677
# Unit test for constructor of class InputOutput
def test_InputOutput():
    in_ = Path('/in')
    out = Path('/out')
    p = InputOutput(input=in_, output=out)
    assert p.input == in_
    assert p.output == out

# Generated at 2022-06-14 02:40:09.069104
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    cr = CompilationResult(3, 0.3, (3, 6), ['a', 'b'])

    assert cr.files == 3
    assert cr.time == 0.3
    assert cr.target == (3, 6)
    assert cr.dependencies == ['a', 'b']


# Generated at 2022-06-14 02:40:10.430467
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    assert TransformationResult(ast.Module([]), False, [])


# Generated at 2022-06-14 02:40:14.942314
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    compilation_result = CompilationResult(1, 2.0, (3, 4), [])
    assert compilation_result.files == 1
    assert compilation_result.time == 2.0
    assert compilation_result.target == (3, 4)
    assert compilation_result.dependencies == []


# Generated at 2022-06-14 02:40:19.139747
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree = ast.parse('')

    tr = TransformationResult(tree, True, ['s', 'a'])

    assert tr.tree == tree
    assert tr.tree_changed == True
    assert tr.dependencies == ['s', 'a']


# Generated at 2022-06-14 02:40:23.832257
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    # default constructor
    CompilationResult(files=1, time=0.1, target=(3, 0), dependencies=[])


# Generated at 2022-06-14 02:40:27.229973
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input_output = InputOutput(Path('input.py'), Path('output.py'))
    assert input_output.input == Path('input.py')
    assert input_output.output == Path('output.py')


# Generated at 2022-06-14 02:40:31.257524
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    result = CompilationResult(0, 0.0, (0, 0), [])
    assert isinstance(result.files, int)
    assert isinstance(result.time, float)
    assert isinstance(result.target, CompilationTarget)
    assert isinstance(result.dependencies, List[str])



# Generated at 2022-06-14 02:40:33.731514
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input_output = InputOutput(Path('input'), Path('output'))
    assert input_output.input == Path('input')
    assert input_output.output == Path('output')

# Test of constructor of class TransformationResult

# Generated at 2022-06-14 02:40:40.637012
# Unit test for constructor of class InputOutput
def test_InputOutput():
    # type: () -> None
    """
    Unit test for constructor of class InputOutput
    """
    temp = tempfile.TemporaryDirectory()
    p = Path(temp.name)
    o = p / 'output'
    o.touch()
    i = p / 'input'
    i.touch()
    io = InputOutput(input=i, output=o)
    assert io.input == i
    assert io.output == o



# Generated at 2022-06-14 02:40:50.266608
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input_ = (Path('test.py'),)
    output = (Path('test.py.out'),)
    # Check that constructor works
    InputOutput(*(input_ + output))
    # Check that constructor doesn't work if output is missing
    with pytest.raises(TypeError):
        InputOutput(*input_)
    # Check that constructor doesn't work if more than 1 inputs are given
    with pytest.raises(TypeError):
        InputOutput(*(input_ + input_))
    # Check that constructor doesn't work if more than 1 outputs are given
    with pytest.raises(TypeError):
        InputOutput(*(input_ + output + output))

# Generated at 2022-06-14 02:40:55.636897
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    # type: () -> None
    r = CompilationResult(files=1, time=0.1, target=(3, 7), dependencies=[])
    assert r.files == 1
    assert r.time == 0.1
    assert r.target == (3, 7)
    assert r.dependencies == []

# Generated at 2022-06-14 02:41:01.250372
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    target = CompilationTarget(3, 7)
    result = CompilationResult(files=0,
                               time=0.0,
                               target=target,
                               dependencies=[])
    assert result.files == 0
    assert result.time == 0.0
    assert result.target == target
    assert result.dependencies == []


# Generated at 2022-06-14 02:41:04.071311
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    result = CompilationResult(files=1, time=2,
                               target=(3, 4),
                               dependencies=['5', '6'])
    assert result.files == 1
    assert result.time == 2
    assert result.target == (3, 4)
    assert result.dependencies == ['5', '6']


# Generated at 2022-06-14 02:41:05.426239
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    CompilationResult(1, 2.0, (3, 4), ['a', 'b'])

# Generated at 2022-06-14 02:41:12.762623
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    # Parse an example
    with open('example.py') as f:
        tree = ast.parse(f.read())
        none = TransformationResult(tree, False, [])

    none.tree_changed == False

# Generated at 2022-06-14 02:41:14.457976
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    assert CompilationResult(files=1, time=2.1, target=(3, 4), dependencies=['a'])


# Generated at 2022-06-14 02:41:17.786053
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    time = timeit.timeit()
    CompilationResult(files=1, time=time, target=(3, 8),
                      dependencies=['foo', 'bar'])


# Generated at 2022-06-14 02:41:26.464993
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    _ = TransformationResult(
        tree=ast.parse('a', 'example'),
        tree_changed=True,
        dependencies=['commands'])

    _ = TransformationResult(
        tree=ast.parse('a', 'example'),
        tree_changed=False,
        dependencies=[])


CommandInfo = NamedTuple('CommandInfo',
                          [('command_name', str),
                           ('options', List[str]),
                           ('input', InputOutput),
                           ('command_string', str)])

# Generated at 2022-06-14 02:41:30.484210
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    """Verify that we can instantiate TransformationResult class"""
    # pylint: disable=unused-argument,unsubscriptable-object
    tree = ast.parse("a = 1")
    TransformationResult(tree, True, ["a.py"])

# Generated at 2022-06-14 02:41:32.930455
# Unit test for constructor of class InputOutput
def test_InputOutput():
    InputOutput(input=Path('input'),
                output=Path('output'))


# Generated at 2022-06-14 02:41:34.067936
# Unit test for constructor of class TransformationResult

# Generated at 2022-06-14 02:41:41.140333
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree = ast.parse("x = 1")
    res = TransformationResult(tree, True, ['one.py', 'two.py'])
    assert res.tree == tree
    assert res.tree_changed == True
    assert res.dependencies == ['one.py', 'two.py']


# Result of specializers transformation
SpecializationResult = NamedTuple('SpecializationResult',
                                  [('tree', ast.AST),
                                   ('tree_changed', bool),
                                   ('interval', ast.AST)])

# Generated at 2022-06-14 02:41:44.513766
# Unit test for constructor of class InputOutput
def test_InputOutput():
    inp = Path('input')
    out = Path('output')
    input_output = InputOutput(inp, out)
    assert input_output.input == inp
    assert input_output.output == out


# Generated at 2022-06-14 02:41:52.289609
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    assert TransformationResult(ast.Module(), True, []) == TransformationResult(
            ast.Module(), True, [])
    assert TransformationResult(ast.Module(), True, ['a']) != TransformationResult(
            ast.Module(), True, ['a'])
    assert TransformationResult(ast.Module(), True, ['a']) != TransformationResult(
            ast.Module(), True, ['b'])
    assert TransformationResult(ast.Module(), True, ['a']) != TransformationResult(
            ast.Module([]), True, ['a'])
    assert TransformationResult(ast.Module(), True, ['a']) != TransformationResult(
            ast.Module(), False, ['a'])
    assert TransformationResult(ast.Module(), True, ['a']) != TransformationResult(
            ast.Module(), True, ['a', 'b'])

# Generated at 2022-06-14 02:42:03.763939
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    result = CompilationResult(42, 1., (3, 6), ['foo.py', 'bar.py'])
    assert isinstance(result, CompilationResult)
    assert result.files == 42
    assert result.time == 1.
    assert result.target == (3, 6)
    assert result.dependencies == ['foo.py', 'bar.py']


# Generated at 2022-06-14 02:42:11.876805
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    result = TransformationResult(None, False, [])
    assert 0 == len(result.dependencies)
    assert False == result.tree_changed


# Command line arguments
CommandLineArguments = NamedTuple('CommandLineArguments',
                                  [('input_path', Path),
                                   ('output_path', Path),
                                   ('target', CompilationTarget),
                                   ('debug', bool),
                                   ('verbose', bool),
                                   ('disable_module_transformation', bool)])


# Generated at 2022-06-14 02:42:21.038395
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    res0 = TransformationResult(None, False, [])
    res1 = TransformationResult(None, True, [])
    res2 = TransformationResult(None, False, ['Foo', 'Bar'])
    res3 = TransformationResult(None, True, ['Foo', 'Bar'])
    assert res0.tree is None
    assert res0.tree_changed is False
    assert res0.dependencies == []
    assert res1.tree is None
    assert res1.tree_changed is True
    assert res1.dependencies == []
    assert res2.tree is None
    assert res2.tree_changed is False
    assert res2.dependencies == ['Foo', 'Bar']
    assert res3.tree is None
    assert res3.tree_changed is True
    assert res3.dependencies == ['Foo', 'Bar']

# Generated at 2022-06-14 02:42:24.278754
# Unit test for constructor of class InputOutput
def test_InputOutput():
    inpout = InputOutput('input', 'output')
    assert inpout.input == 'input'
    assert inpout.output == 'output'


# Generated at 2022-06-14 02:42:27.444720
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    result = CompilationResult(files=10, time=20.0,
                               target=(7, 10), dependencies=['a'])
    assert result.files == 10
    assert result.time == 20.0
    assert result.target == (7, 10)
    assert result.dependencies == ['a']


# Generated at 2022-06-14 02:42:35.448021
# Unit test for constructor of class InputOutput
def test_InputOutput():
    x = InputOutput(Path(''), Path(''))
    assert isinstance(x.input, Path)
    assert isinstance(x.output, Path)

    x = InputOutput('', '')
    assert isinstance(x.input, Path)
    assert isinstance(x.output, Path)

    x = InputOutput(input='', output='')
    assert isinstance(x.input, Path)
    assert isinstance(x.output, Path)


# Generated at 2022-06-14 02:42:41.838768
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    ast_node = ast.Module(body=[])
    tree = TransformationResult(tree=ast_node, tree_changed=False,
                                dependencies=[])
    assert isinstance(tree, TransformationResult)
    assert tree.tree == ast_node
    assert tree.tree_changed == False
    assert tree.dependencies == []

# Generated at 2022-06-14 02:42:46.279841
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    files = 42
    time = 31.0
    target = (3, 7)
    dependencies = []

    result = CompilationResult(files, time, target, dependencies)
    assert isinstance(result, CompilationResult)
    assert result.files == files
    assert result.time == time
    assert result.target == target
    assert result.dependencies is dependencies



# Generated at 2022-06-14 02:42:47.696636
# Unit test for constructor of class InputOutput
def test_InputOutput():
    InputOutput(input=Path('/tmp/input'), output=Path('/tmp/output'))


# Generated at 2022-06-14 02:42:49.073118
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    assert CompilationResult(10, 0.3, (3, 6), [])


# Generated at 2022-06-14 02:43:16.188171
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    import astor
    import random

    def get_random_ast():
        return ast.parse(str(random.random())).body[0]

    def test_eq(a, b):
        assert astor.to_source(a) == astor.to_source(b)

    # The same tree
    a, b = get_random_ast(), get_random_ast()
    test_eq(a, b)

    # The same tree with different change status
    res1 = TransformationResult(tree=a, tree_changed=False, dependencies=[])
    res2 = TransformationResult(tree=a, tree_changed=True, dependencies=[])
    assert res1 != res2

    # The same tree with different dependencies

# Generated at 2022-06-14 02:43:21.915484
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    assert TransformationResult(tree=None, tree_changed=False, dependencies=None).tree is None
    assert not TransformationResult(tree=None, tree_changed=False, dependencies=None).tree_changed
    assert TransformationResult(tree=None, tree_changed=False, dependencies=None).dependencies is None

# Generated at 2022-06-14 02:43:26.572502
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree = ast.parse('')  # type: ignore
    deps = []

    result = TransformationResult(tree=tree,
                                  tree_changed=True,
                                  dependencies=deps)

    assert result.tree == tree
    assert result.tree_changed == True
    assert result.dependencies == deps

# Generated at 2022-06-14 02:43:30.593888
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree = ast.Module([])
    tr = TransformationResult(tree=tree, tree_changed=True, dependencies=[])

    assert isinstance(tr, TransformationResult)
    assert isinstance(tr.tree, ast.Module)
    assert isinstance(tr.tree_changed, bool)
    assert isinstance(tr.dependencies, list)

# Generated at 2022-06-14 02:43:33.011352
# Unit test for constructor of class InputOutput
def test_InputOutput():
    assert InputOutput(Path('a'), Path('b')) == InputOutput('a', 'b')



# Generated at 2022-06-14 02:43:37.109604
# Unit test for constructor of class InputOutput
def test_InputOutput():
    sample_input = 'input'
    sample_output = 'output'
    test_data = InputOutput(input=sample_input, output=sample_output)
    assert sample_input == test_data.input
    assert sample_output == test_data.output

# Generated at 2022-06-14 02:43:40.902433
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input_output = InputOutput(Path('data/input.py'),
                               Path('data/output.py'))
    assert input_output.input == Path('data/input.py')
    assert input_output.output == Path('data/output.py')

# Generated at 2022-06-14 02:43:44.313479
# Unit test for constructor of class InputOutput
def test_InputOutput():
    assert InputOutput(input=Path('test_InputOutput.py'),
                       output=Path('test_InputOutput.pyc')) \
        == InputOutput(input='test_InputOutput.py',
                       output='test_InputOutput.pyc')

# Generated at 2022-06-14 02:43:49.039075
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    a = CompilationResult(files=1, time=3.0, target=(3, 5),
                          dependencies=['a', 'b'])
    assert(a.files == 1 and a.time == 3.0 and a.target == (3, 5) and
           a.dependencies == ['a', 'b'])


# Generated at 2022-06-14 02:43:50.850282
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    try:
        TransformationResult(tree=None, tree_changed=False, dependencies=None)
    except TypeError:
        assert False

# Generated at 2022-06-14 02:44:40.427918
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    any_tree = ast.parse('a = 0')
    any_dependencies = ['a']
    TransformationResult(any_tree, False, any_dependencies)

# Generated at 2022-06-14 02:44:44.780410
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree = ast.parse('2 + 3')
    tree_changed = True
    dependencies = ['sys', 'os']
    tr = TransformationResult(tree, tree_changed, dependencies)
    assert tr.tree == tree
    assert tr.tree_changed == tree_changed
    assert tr.dependencies == dependencies

# Generated at 2022-06-14 02:44:48.359264
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    # type: () -> None
    t = TransformationResult(tree=None, tree_changed=False, dependencies=None)
    assert t.tree is None
    assert t.tree_changed ==  False
    assert t.dependencies is None


# Generated at 2022-06-14 02:44:51.149149
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    # check that we can create CompilationResult object
    CompilationResult(files=1, time=1.0, target=(3, 5), dependencies=['a', 'b'])

# Generated at 2022-06-14 02:44:53.917991
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input_path = Path('foo.py')
    output_path = Path('foo.py')
    assert InputOutput(input_path, output_path) == InputOutput(input_path, output_path)

# Generated at 2022-06-14 02:44:56.345372
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    assert(CompilationResult(0, 0.0, (3, 4), []) ==
           CompilationResult(files=0, time=0.0, target=(3, 4), dependencies=[]))


# Generated at 2022-06-14 02:45:00.533239
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input = Path('input.py')
    output = Path('output.py')
    in_out = InputOutput(input, output)
    assert in_out.input == input
    assert in_out.output == output

# Generated at 2022-06-14 02:45:02.214982
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    CompilationResult(files=1, time=0.1,
                      target=(3, 5), dependencies=['a', 'b'])

# Generated at 2022-06-14 02:45:06.299397
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree = ast.parse('x=1')
    dependencies = []
    t = TransformationResult(tree, True, dependencies)
    assert t.tree == tree
    assert t.tree_changed == True
    assert t.dependencies == dependencies

# Name of python package
PackageName = NamedTuple('PackageName', [('name', str)])

# Name of python module
ModuleName = NamedTuple('ModuleName', [('name', str)])

# Generated at 2022-06-14 02:45:09.509215
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    assert TransformationResult(
        tree=object(),
        tree_changed=False,
        dependencies=[]) == \
        TransformationResult(
            tree=object(),
            tree_changed=False,
            dependencies=[])

# Generated at 2022-06-14 02:45:59.726087
# Unit test for constructor of class InputOutput
def test_InputOutput():
    i = Path('/tmp/input')
    o = Path('/tmp/output')
    x = InputOutput(input = i, output = o)
    assert x.input == i
    assert x.output == o
    x = InputOutput(i, o)
    assert x.input == i
    assert x.output == o


# Generated at 2022-06-14 02:46:02.880122
# Unit test for constructor of class InputOutput
def test_InputOutput():
    assert InputOutput(input=Path('a'), output=Path('b'))


# Generated at 2022-06-14 02:46:09.025260
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    name = CompilationResult(
        files=1,
        time=0.0,
        target=(2, 7),
        dependencies=["foo/bar.py"])
    assert name.files == 1
    assert name.time == 0.0
    assert name.target == (2, 7)
    assert name.dependencies == ["foo/bar.py"]

# Generated at 2022-06-14 02:46:14.232818
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    from typing import Union
    tr = TransformationResult(tree=ast.parse("foo"),
                              tree_changed=True,
                              dependencies=['foo', 'bar'])
    assert tr.tree_changed is True
    assert isinstance(tr.dependencies, list)
    assert isinstance(tr.tree, ast.AST)

# Generated at 2022-06-14 02:46:20.967837
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    test_files = 1
    test_time = 0.5
    test_target = (3, 7)
    test_dependencies = ['a']
    res = CompilationResult(files=test_files,
                            time=test_time,
                            target=test_target,
                            dependencies=test_dependencies)
    assert res.files == 1
    assert res.time == 0.5
    assert res.target == (3, 7)
    assert res.dependencies == ['a']


# Generated at 2022-06-14 02:46:23.730595
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input = Path('/input/path')
    output = Path('/output/path')
    io = InputOutput(input=input, output=output)
    assert io.input == input
    assert io.output == output


# Generated at 2022-06-14 02:46:25.291774
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    assert TransformationResult(None, True, None) != None

# Generated at 2022-06-14 02:46:31.536358
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    class MyTuple(NamedTuple):
        a: int
        b: int

    m = MyTuple(4, 5)
    assert m.a == 4
    assert m.b == 5
    assert m.__class__.__name__ == 'MyTuple'

# Transform using transformer

# Generated at 2022-06-14 02:46:40.884917
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    success = lambda: TransformationResult(ast.parse("1 + 1"),
                                           True,
                                           ["a", "b"])
    fail = lambda: TransformationResult("foo", "bar", "1 + 1")

    tests = [("Correct", success),
             ("Incorrect", fail)]

    for test_name, f in tests:
        try:
            f()
        except:
            logger.error("Test {} failed".format(test_name))
            raise
        else:
            logger.info("Test {} succeeded".format(test_name))

# Generated at 2022-06-14 02:46:44.828772
# Unit test for constructor of class InputOutput
def test_InputOutput():
    test_tuple = InputOutput(Path('a'), Path('b'))
    assert test_tuple.input == Path('a')
    assert test_tuple.output == Path('b')


# Generated at 2022-06-14 02:48:25.659864
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    to_test = TransformationResult(ast.AST(), True, [])
    assert to_test.tree is not None
    assert to_test.tree_changed
    assert to_test.dependencies == []

# Generated at 2022-06-14 02:48:27.504007
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    CompilationResult(files=1, time=1.0,
                      target=(3, 4), dependencies=['a', 'b'])

# Generated at 2022-06-14 02:48:34.689928
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    c = CompilationResult(files=0, time=0, target=(3, 6), dependencies=['__builtin__'])
    assert isinstance(c.files, int)
    assert isinstance(c.time, float)
    assert isinstance(c.target, tuple)
    assert len(c.target) == 2
    assert all(isinstance(x, int) for x in c.target)
    assert isinstance(c.dependencies, list)


# Generated at 2022-06-14 02:48:38.487516
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input = Path('in.py')
    output = Path('out.py')

    i_o = InputOutput(input, output)
    assert i_o.input == input
    assert i_o.output == output

# Generated at 2022-06-14 02:48:41.401922
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    t = ast.parse('import sys\nimport os')
    result = TransformationResult(tree=t, tree_changed=True,
                                  dependencies=['sys', 'os'])
    assert isinstance(result, TransformationResult)

# Generated at 2022-06-14 02:48:49.697038
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    assert CompilationResult(5, 1.5, (2, 7), ["a", "b", "c"]) == CompilationResult(5, 1.5, (2, 7), ["a", "b", "c"])
    assert CompilationResult(5, 1.5, (2, 7), ["a", "b", "c"]) != CompilationResult(5, 1.5, (2, 7), ["a", "b", "d"])
    assert CompilationResult(5, 1.5, (2, 7), ["a", "b", "c"]) != CompilationResult(5, 1.6, (2, 7), ["a", "b", "c"])

# Generated at 2022-06-14 02:48:55.738278
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    # pylint: disable=invalid-name
    tr = TransformationResult(ast.Expression(body=ast.Name('a', ast.Load())),
                              True, ['foo_module.txt'])
    assert isinstance(tr.tree, ast.AST)
    assert isinstance(tr.tree_changed, bool)
    assert isinstance(tr.dependencies, list)
    assert tr.dependencies == ['foo_module.txt']

# Generated at 2022-06-14 02:49:06.740270
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    ast_ = ast.parse("# Comment\npass")
    trr = TransformationResult(tree=ast_, tree_changed=True, dependencies=[])
    assert isinstance(trr.tree, ast.AST)
    assert trr.tree_changed is True
    assert isinstance(trr.dependencies, List)
    trr = TransformationResult(tree=ast_, tree_changed=False, dependencies=[])
    assert isinstance(trr.tree, ast.AST)
    assert trr.tree_changed is False
    assert isinstance(trr.dependencies, List)