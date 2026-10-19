

# Generated at 2022-06-14 02:39:01.067982
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree = ast.parse('')
    TransformationResult(tree,
                         True,
                         ['import pytest', 'import coverage'])

# Generated at 2022-06-14 02:39:02.983338
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    CompilationResult(1, 2.0, (3, 4), ['test'])


# Generated at 2022-06-14 02:39:06.639796
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tr = TransformationResult(tree=None, tree_changed=True, dependencies=[])
    assert  (None, True, []) == tr


__all__ = ['TransformationResult',
           'InputOutput',
           'CompilationResult',
           'CompilationTarget']

# Generated at 2022-06-14 02:39:14.531702
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    with pytest.raises(TypeError):
        CompilationResult(1, 1, (3, 7))
    with pytest.raises(TypeError):
        CompilationResult('1', 1, (3, 7))
    with pytest.raises(TypeError):
        CompilationResult(1.1, 1, (3, 7))
    with pytest.raises(TypeError):
        CompilationResult(1, 1.1, (3, 7))
    with pytest.raises(TypeError):
        CompilationResult(1, 1, 1)
    with pytest.raises(TypeError):
        CompilationResult(1, 1, 1.1)
    with pytest.raises(TypeError):
        CompilationResult(1, 1, (3, 7), 1)

# Generated at 2022-06-14 02:39:18.943837
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    t = TransformationResult(tree=ast.parse('True'),
                             tree_changed=True,
                             dependencies=['first', 'second'])
    # Check that we have all fields
    assert t.tree
    assert t.tree_changed
    assert t.dependencies == ['first', 'second']

# Generated at 2022-06-14 02:39:20.252029
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    assert CompilationResult(0, 0, (3, 0), [])


# Generated at 2022-06-14 02:39:26.848484
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    r = CompilationResult(files=42,
                          time=3.14,
                          target=(3, 7),
                          dependencies=['a', 'b', 'c'])
    assert r.files == 42
    assert r.time == 3.14
    assert r.target == (3, 7)
    assert r.dependencies == ['a', 'b', 'c']


# Generated at 2022-06-14 02:39:31.537527
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    class TestNode(ast.AST):
        pass

    test_node = TestNode()
    res = TransformationResult(tree=test_node,
                               tree_changed=True,
                               dependencies=["a", "b"])
    assert res.tree is test_node
    assert res.tree_changed is True
    assert res.dependencies == ["a", "b"]



# Generated at 2022-06-14 02:39:33.735334
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input = Path('hello')
    output = Path('goodbye')
    io = InputOutput(input, output)
    assert io.input == input and io.output == output

# Generated at 2022-06-14 02:39:39.941014
# Unit test for constructor of class InputOutput
def test_InputOutput():
    path = Path('/home/agr/file.py')
    input = Path('/home/agr/input.txt')
    output = Path('/home/agr/output.txt')
    pair = InputOutput(input, output)

    assert pair.input == input
    assert pair.output == output
    assert str(pair) == "InputOutput(input: '/home/agr/input.txt', output: '/home/agr/output.txt')"

# Generated at 2022-06-14 02:39:45.920704
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tr = TransformationResult(None, None, None)
    assert tr.tree is None
    assert tr.tree_changed is None
    tr = TransformationResult(0, 0, 0)
    assert tr.tree == 0
    assert tr.tree_changed == 0

# Generated at 2022-06-14 02:39:51.324134
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    compilation_result = CompilationResult(files=6,
                                           time=3.14,
                                           target=(3, 7),
                                           dependencies=['foo', 'bar'])
    assert(compilation_result.files == 6)
    assert(compilation_result.time == 3.14)
    assert(compilation_result.target == (3, 7))
    assert(compilation_result.dependencies == ['foo', 'bar'])

# Generated at 2022-06-14 02:39:53.083284
# Unit test for constructor of class InputOutput
def test_InputOutput():
    assert InputOutput(input=Path('input'), output=Path('output')) == \
        InputOutput(input=Path('input'), output=Path('output'))

# Generated at 2022-06-14 02:39:58.684373
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    result = CompilationResult(files=42,
                               time=12.3,
                               target=(3, 5),
                               dependencies=['a', 'b'])
    assert result.files == 42
    assert result.time == 12.3
    assert result.target == (3, 5)
    assert result.dependencies == ['a', 'b']


# Generated at 2022-06-14 02:40:05.652410
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    import typed_ast.ast3 as ast
    from .parsing import parse_file
    file_path = Path('ast_transformer/data/helloworld.py')
    initial_tree = parse_file(file_path)
    res = TransformationResult(initial_tree, True, ['ast_transformer/data/__init__.py'])

    assert res.tree is initial_tree
    assert res.tree_changed is True
    assert res.dependencies == ['ast_transformer/data/__init__.py']

# Generated at 2022-06-14 02:40:09.723826
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    import astor
    t = astor.code_to_ast('class A: pass')
    tr = TransformationResult(t, True, [])
    assert tr.tree_changed == True and tr.dependencies == []
    tr = TransformationResult(t, False, [])
    assert tr.tree_changed == False and tr.dependencies == []

# Generated at 2022-06-14 02:40:13.180011
# Unit test for constructor of class InputOutput
def test_InputOutput():
    assert InputOutput(Path('a'), Path('b')) == InputOutput(input=Path('a'),
                                                            output=Path('b'))

# Generated at 2022-06-14 02:40:16.869295
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    cr = CompilationResult(files=1, time=1.0, target=(3, 8), dependencies=[])
    assert cr.files == 1
    assert cr.time == 1.0
    assert cr.target == (3, 8)
    assert cr.dependencies == []


# Generated at 2022-06-14 02:40:21.177187
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree = ast.parse('pass')
    tr = TransformationResult(tree, True, ['/a'])
    assert tr.tree is tree
    assert tr.tree_changed is True
    assert tr.dependencies == ['/a']

# Generated at 2022-06-14 02:40:23.428891
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    CompilationResult(0, 0.0, (3, 7), [''])


# Generated at 2022-06-14 02:40:31.165910
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    class MockAST(ast.AST):
        pass
        
    tree = MockAST()
    result = TransformationResult(tree, True, [])
    assert result.tree == tree
    assert result.tree_changed == True
    assert result.dependencies == []


# Generated at 2022-06-14 02:40:33.524882
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input = "input"
    output = "output"
    io = InputOutput(input, output)

    assert io.input == input
    assert io.output == output

# Generated at 2022-06-14 02:40:39.834474
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    compilation_result = CompilationResult(files=0,
                                           time=0.0,
                                           target=(3, 4),
                                           dependencies=[])
    assert compilation_result.files == 0
    assert compilation_result.time == 0.0
    assert compilation_result.target == (3, 4)
    assert compilation_result.dependencies == []


# Generated at 2022-06-14 02:40:42.030665
# Unit test for constructor of class InputOutput
def test_InputOutput():
    inp = Path('/input')
    out = Path('/output')
    InputOutput(inp, out)


# Generated at 2022-06-14 02:40:46.588285
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    class Test(ast.AST):
        pass
    tree = Test()
    dependencies = []
    result = TransformationResult(tree, True, dependencies)
    assert result.tree is tree
    assert result.tree_changed
    assert result.dependencies is dependencies

# Generated at 2022-06-14 02:40:50.224381
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    cr = CompilationResult(12, 3.14, (3, 5), [])
    assert cr.files == 12
    assert cr.time == 3.14
    assert cr.target == (3, 5)
    assert cr.dependencies == []

# Generated at 2022-06-14 02:41:00.566300
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    result_1 = CompilationResult(files=1,
                                 time=2.0,
                                 target=(3, 4),
                                 dependencies=['a',
                                               'b',
                                               'c'])
    assert result_1.files == 1
    assert result_1.time == 2.0
    assert result_1.target[0] == 3
    assert result_1.target[1] == 4
    assert result_1.dependencies[0] == 'a'
    assert result_1.dependencies[1] == 'b'
    assert result_1.dependencies[2] == 'c'


# Generated at 2022-06-14 02:41:05.714332
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    unit = CompilationResult(files=10, time=5, target=(3, 5),
                             dependencies=['foo.py', 'bar.py'])
    assert unit.files == 10
    assert unit.time == 5
    assert unit.target == (3, 5)
    assert unit.dependencies == ['foo.py', 'bar.py']


# Generated at 2022-06-14 02:41:10.837454
# Unit test for constructor of class TransformationResult
def test_TransformationResult():

    # Empty dependencies
    result: TransformationResult = TransformationResult(ast.parse('pass'),
                                                         False,
                                                         [])

    assert result.tree_changed is False
    assert result.dependencies == []

# Generated at 2022-06-14 02:41:17.040294
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    r = CompilationResult(0, 0.0, (3, 6), None)
    assert r.files == 0
    assert r.time == 0.0
    assert r.target == (3, 6)
    assert r.dependencies is None


# Generated at 2022-06-14 02:41:29.932083
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree = ast.parse('')
    tree_changed = False
    dependencies = []
    TransformationResult(tree, tree_changed, dependencies)

# Test that a default value will be used if not specified

# Generated at 2022-06-14 02:41:35.121392
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    x = CompilationResult(files=1, time=2, target=(3, 4), dependencies=['a', 'b'])

    assert x.files == 1
    assert x.time == 2
    assert x.target == (3, 4)
    assert x.dependencies == ['a', 'b']



# Generated at 2022-06-14 02:41:41.230260
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input = Path("/path/to/input.py")
    output = Path("/path/to/output.py")
    with pytest.raises(TypeError):
        InputOutput(input, "wrong type")
    with pytest.raises(TypeError):
        InputOutput("wrong type", output)
    assert InputOutput(input, output).input == input
    assert InputOutput(input, output).output == output



# Generated at 2022-06-14 02:41:48.921294
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    '''Tests if CompilationResult has expected structure'''

    # Creation with minimal arguments
    minim = CompilationResult(1, 1.0, (3, 7), ['dep1.py'])
    assert minim.files == 1
    assert minim.time == 1.0
    assert minim.target == (3, 7)
    assert minim.dependencies == ['dep1.py']

    # Creation with all arguments
    maxim = CompilationResult(1, 1.0, (3, 7), ['dep1.py'])
    assert maxim.files == 1
    assert maxim.time == 1.0
    assert maxim.target == (3, 7)
    assert maxim.dependencies == ['dep1.py']


# Generated at 2022-06-14 02:41:51.670474
# Unit test for constructor of class InputOutput
def test_InputOutput():
    import pytest
    dummy1 = Path("dummy1")
    dummy2 = Path("dummy2")
    dummy_input_output = InputOutput(dummy1, dummy2)
    assert dummy_input_output.input == dummy1
    assert dummy_input_output.output == dummy2

# Generated at 2022-06-14 02:41:59.968741
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    assert CompilationResult(files=1, time=0.1, target=(3, 6), dependencies=[]).files == 1
    assert CompilationResult(files=1, time=0.1, target=(3, 6), dependencies=[]).time == 0.1
    assert CompilationResult(files=1, time=0.1, target=(3, 6), dependencies=[]).target == (3, 6)
    assert CompilationResult(files=1, time=0.1, target=(3, 6), dependencies=[]).dependencies == []


# Generated at 2022-06-14 02:42:02.906194
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    files = 1
    time = 0.1
    target = (3, 4)
    dependencies = []
    result = CompilationResult(files, time, target, dependencies)
    assert result.files == files
    assert result.time == time
    assert result.target == target
    assert result.dependencies == dependencies


# Generated at 2022-06-14 02:42:04.955622
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    assert (TransformationResult(tree=None,
                                 tree_changed=None,
                                 dependencies=None) is not None)

# Generated at 2022-06-14 02:42:07.448698
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input = Path('somefile.py')
    output = Path('otherfile.py')
    input_output = InputOutput(input, output)
    assert input_output.input == input
    assert input_output.output == output


# Generated at 2022-06-14 02:42:09.080066
# Unit test for constructor of class InputOutput
def test_InputOutput():
    assert InputOutput(Path('1'), Path('1')) == InputOutput(input=Path('1'), output=Path('1'))

# Generated at 2022-06-14 02:42:22.466698
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input_ = Path('/input/file')
    output = Path('/output/file')
    io = InputOutput(input_, output)
    assert io.input == input_
    assert io.output == output



# Generated at 2022-06-14 02:42:26.219291
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree = ast.parse('x = 1')
    tree_changed = False
    dependencies = []
    result = TransformationResult(tree, tree_changed, dependencies)
    assert result.tree == tree
    assert result.tree_changed == tree_changed
    assert result.dependencies == dependencies


# Generated at 2022-06-14 02:42:30.768767
# Unit test for constructor of class InputOutput
def test_InputOutput():
    p1 = Path('file1.py')
    p2 = Path('file2.py')
    in_out = InputOutput(input=p1, output=p2)
    assert in_out.input == p1
    assert in_out.output == p2

# Generated at 2022-06-14 02:42:36.193282
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tr = TransformationResult(ast.If(ast.NameConstant(True),
                                     [ast.Pass(), ast.Pass()],
                                     [ast.Pass()]),
                              True,
                              ["Module"])
    assert tr.tree.test.value == True
    assert tr.dependencies[0] == "Module"

# Generated at 2022-06-14 02:42:38.852793
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    # type: () -> None
    CompilationResult(1, 1.0, (1, 2), [])


# Generated at 2022-06-14 02:42:43.907358
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    res = CompilationResult(files=1, time=2.0,
                            target=(3, 4), dependencies=[])
    assert res.files == 1
    assert res.time == 2.0
    assert res.target == (3, 4)
    assert res.dependencies == []


# Generated at 2022-06-14 02:42:46.443802
# Unit test for constructor of class InputOutput
def test_InputOutput():
    path1 = Path('/')
    path2 = Path('.')
    input_output = InputOutput(path1, path2)
    assert input_output.input == path1
    assert input_output.output == path2

# Generated at 2022-06-14 02:42:49.600871
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    t = ast.parse("pass")
    TransformationResult(tree=t, tree_changed=True, dependencies=['foo'])
    TransformationResult(tree=t, tree_changed=False, dependencies=['foo'])
    TransformationResult(tree=t, tree_changed=True, dependencies=[])
    TransformationResult(tree=t, tree_changed=False, dependencies=[])

# Generated at 2022-06-14 02:42:56.271785
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    '''
    Test for constructor of the class CompilationResult
    '''
    # Create instance
    test_instance = CompilationResult(2, 3.0, (2, 7), ['a', 'b'])

    # Check fields
    assert test_instance.files == 2
    assert test_instance.time == 3.0
    assert test_instance.target == (2, 7)
    assert test_instance.dependencies == ['a', 'b']


# Generated at 2022-06-14 02:42:58.481333
# Unit test for constructor of class CompilationResult
def test_CompilationResult(): # pylint: disable=redefined-outer-name
    assert CompilationResult(0, 0, CompilationTarget(3, 0), [])


# Generated at 2022-06-14 02:43:23.697867
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    # pylint: disable=invalid-name
    c = CompilationResult(2, 3.14, (2, 7), ['foo', 'bar'])
    assert c.files == 2
    assert c.time == 3.14
    assert c.target == (2, 7)
    assert c.dependencies == ['foo', 'bar']


# Generated at 2022-06-14 02:43:27.349906
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input_ = Path('/input')
    output = Path('/output')
    io = InputOutput(input_, output)
    assert io.input == input_
    assert io.output == output

# Generated at 2022-06-14 02:43:31.004725
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    result = CompilationResult(files=1, time=0.5,
                               target=(3, 6), dependencies=[])
    assert result.files == 1
    assert result.time == 0.5
    assert result.target == (3, 6)
    assert result.dependencies == []


# Generated at 2022-06-14 02:43:33.427029
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    # Should not have any problems
    TransformationResult(ast.parse('pass'), True, list())



# Generated at 2022-06-14 02:43:34.887043
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    CompilationResult(1, 2.0, (3, 4), ['a', 'b'])


# Generated at 2022-06-14 02:43:39.758610
# Unit test for constructor of class InputOutput
def test_InputOutput():
    in_path = Path("foo/bar")
    out_path = Path("/tmp/foo/baz")
    inout = InputOutput(input=in_path, output=out_path)
    assert inout.input == in_path
    assert inout.output == out_path


# Generated at 2022-06-14 02:43:42.909041
# Unit test for constructor of class InputOutput
def test_InputOutput():
    inp = Path('tasks/programs/hello.py')
    out = inp.with_name(inp.stem)
    assert InputOutput(input=inp, output=out)


# Generated at 2022-06-14 02:43:45.305312
# Unit test for constructor of class InputOutput
def test_InputOutput():
    assert InputOutput(Path('input'), Path('output'))


# Generated at 2022-06-14 02:43:48.343985
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input = Path('input')
    output = Path('output')
    io = InputOutput(input, output)
    assert io.input == input
    assert io.output == output



# Generated at 2022-06-14 02:43:51.637156
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    d = CompilationResult(10, 5.0, (2, 3), ['foo', 'bar'])
    assert d.files == 10
    assert d.time == 5.0
    assert d.target == (2, 3)
    assert d.dependencies == ['foo', 'bar']


# Generated at 2022-06-14 02:44:19.490347
# Unit test for constructor of class InputOutput
def test_InputOutput():
    path_in = '/tmp/input.py'
    path_out = '/tmp/output.py'
    input_output = InputOutput(Path(path_in), Path(path_out))
    assert isinstance(input_output, InputOutput)
    assert input_output.input == Path(path_in)
    assert input_output.output == Path(path_out)

# Generated at 2022-06-14 02:44:22.314043
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input = Path('input.py')
    output = Path('output.py')
    test = InputOutput(input, output)

    assert test.input == input
    assert test.output == output


# Generated at 2022-06-14 02:44:27.708822
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    result = CompilationResult(files=42, time=2.3, target=(3, 7), dependencies=['a', 'b'])
    assert result.files == 42
    assert result.time == 2.3
    assert result.target == (3, 7)
    assert result.dependencies == ['a', 'b']



# Generated at 2022-06-14 02:44:28.759076
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    TransformationResult(ast.parse(""), True, [])

# Generated at 2022-06-14 02:44:33.452489
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input_path = Path(__file__)
    output_path = input_path + '.new'
    input_output = InputOutput(input=input_path, output=output_path)
    assert input_output.input == input_path
    assert input_output.output == output_path


# Generated at 2022-06-14 02:44:36.440405
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input, output = Path('foo'), Path('bar')
    assert input == InputOutput(input, output).input
    assert output == InputOutput(input, output).output


# Generated at 2022-06-14 02:44:40.504422
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input = Path('/input')
    output = Path('/output')
    pair = InputOutput(input, output)
    assert pair.input == input
    assert pair.output == output

# Generated at 2022-06-14 02:44:48.181000
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    target = (2, 7)
    cr = CompilationResult(0, 0.0, target, [])
    assert cr.files == 0
    assert cr.time == 0.0
    assert cr.target == target
    assert cr.dependencies == []

    target = (3, 4)
    cr = CompilationResult(1, 1.0, target, ['foo', 'bar'])
    assert cr.files == 1
    assert cr.time == 1.0
    assert cr.target == target
    assert cr.dependencies == ['foo', 'bar']



# Generated at 2022-06-14 02:44:52.051574
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    changed = True
    tree = "ast"
    deps = ["dep1"]
    result = TransformationResult(tree, changed, deps)
    assert result.tree, "ast"
    assert result.tree_changed, changed
    assert result.dependencies, deps

# Generated at 2022-06-14 02:44:57.817993
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    ast_tree = ast.parse('print("hello world")')
    result = TransformationResult(ast_tree, False, [])
    assert(isinstance(result.tree, ast.AST) and result.tree_changed == False
           and len(result.dependencies) == 0)



# Generated at 2022-06-14 02:45:28.546573
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    # Given
    files = 1
    time = 42.0
    target = (3, 5)
    dependencies = ["foo.py"]

    # When
    result = CompilationResult(files, time, target, dependencies)

    # Then
    assert result.files == files
    assert result.time == time
    assert result.target == target
    assert result.dependencies == dependencies


# Generated at 2022-06-14 02:45:32.689875
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input_ = Path('./input.py')
    output = Path('./output.py')
    io = InputOutput(input_, output)
    assert io.input == input_
    assert io.output == output


# Generated at 2022-06-14 02:45:37.212210
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input_output = InputOutput(Path('test.txt'), Path('test2.txt'))
    assert input_output.input.name == 'test.txt' and input_output.output.name == 'test2.txt'


# Generated at 2022-06-14 02:45:38.358365
# Unit test for constructor of class InputOutput
def test_InputOutput():
    inp = Path('/path/to/file')
    out = Path('/path/to/output')
    io = InputOutput(inp, out)
    assert io.input == inp
    assert io.output == out


# Generated at 2022-06-14 02:45:42.880287
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    res = CompilationResult(files=1, time=1.0,
                            target=(0, 0), dependencies=[''])
    assert res.files == 1
    assert res.time == 1.0
    assert res.target == (0, 0)
    assert res.dependencies == ['']


# Generated at 2022-06-14 02:45:49.656022
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    print("Test class TransformationResult")
    tree = ast.parse("foo = 1")
    tree_changed = True
    dependencies = ["./foo.py"]
    result = TransformationResult(tree, tree_changed, dependencies)
    assert result.tree == tree
    assert result.tree_changed == tree_changed
    assert result.dependencies == dependencies

# Generated at 2022-06-14 02:45:56.918558
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    cr = CompilationResult(files=5, time=5.5, target=(1, 2), dependencies=['a', 'b'])
    assert cr.files == 5
    assert cr.time == 5.5
    assert cr.target == (1, 2)
    assert cr.dependencies == ['a', 'b']


# Generated at 2022-06-14 02:45:59.562540
# Unit test for constructor of class InputOutput
def test_InputOutput():
    assert InputOutput(Path('in'), Path('out')) == InputOutput(input=Path('in'), output=Path('out'))


# Generated at 2022-06-14 02:46:07.040736
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    result = CompilationResult(files=3,
                               time=16.1,
                               target=(3, 8),
                               dependencies=['test.py'])
    assert result.files == 3
    assert result.time == 16.1
    assert result.target == (3, 8)
    assert result.dependencies == ['test.py']


# Generated at 2022-06-14 02:46:16.022341
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree = ast.Module([])
    tree_changed = True
    dependencies = []
    result = TransformationResult(tree, tree_changed, dependencies)
    assert isinstance(result, TransformationResult)
    assert result.tree == tree
    assert result.tree_changed == tree_changed
    assert result.dependencies == dependencies

# Result of checkers check
CheckerResult = NamedTuple('CheckerResult',
                           [('tree', ast.AST),
                            ('tree_changed', bool),
                            ('errors', List[str])])


# Generated at 2022-06-14 02:47:10.199804
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tp = ast.parse('pass')
    res = TransformationResult(tp, True, ['dep1', 'dep2'])
    assert isinstance(res.tree, ast.Module)
    assert res.tree_changed == True
    assert res.dependencies == ['dep1', 'dep2']

# Generated at 2022-06-14 02:47:15.532428
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    compilation_result = CompilationResult(files=1, time=0.2,
                                           target=(3, 5),
                                           dependencies=['foo', 'bar'])
    assert compilation_result.files == 1
    assert compilation_result.time == 0.2
    assert compilation_result.target == (3, 5)
    assert compilation_result.dependencies == ['foo', 'bar']


# Generated at 2022-06-14 02:47:23.838592
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input1 = Path(".").absolute() / "test" / "test.py"
    output1 = Path(".").absolute() / "test" / "test.pyi"
    input2 = Path(".").absolute() / "test" / "test2.py"
    output2 = Path(".").absolute() / "test" / "test2.pyi"
    assert InputOutput(input1, output1) == InputOutput(input1, output1)
    assert not InputOutput(input1, output1) == InputOutput(input2, output2)
    assert not InputOutput(input1, output1) == InputOutput(input1, output2)
    assert not InputOutput(input1, output1) == InputOutput(input2, output1)

# Generated at 2022-06-14 02:47:28.336245
# Unit test for constructor of class InputOutput
def test_InputOutput():
    test_input = 'test_input'
    test_output = 'test_output'

    result = InputOutput(test_input, test_output)

    assert result.input == test_input
    assert result.output == test_output


# Generated at 2022-06-14 02:47:32.934367
# Unit test for constructor of class InputOutput
def test_InputOutput():
    test_input = Path('a.py')
    test_output = Path('b.py')
    test = InputOutput(test_input, test_output)
    assert test.input == test_input
    assert test.output == test_output


# Generated at 2022-06-14 02:47:35.459138
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    CompilationResult(
        files=1,
        time=2,
        target=(3, 4),
        dependencies=['file1', 'file2']
    )



# Generated at 2022-06-14 02:47:38.445625
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    class_ = TransformationResult(tree=None, tree_changed=True, dependencies=[])
    assert class_.tree is None
    assert class_.tree_changed is True
    assert class_.dependencies == []

# Generated at 2022-06-14 02:47:43.292087
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input_path = 'foo/bar'
    output_path = 'baz/qux'
    input_output = InputOutput(input_path, output_path)
    assert (input_output.input  # type: ignore
            == Path(input_path))
    assert (input_output.output  # type: ignore
            == Path(output_path))


# Generated at 2022-06-14 02:47:51.280004
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    dummy_tree = ast.parse('a = 1')
    dummy_tree_changed = True
    dummy_dependencies = ['A', 'B']
    t = TransformationResult(dummy_tree, dummy_tree_changed,
                             dummy_dependencies)
    assert t.tree == dummy_tree
    assert t.tree_changed == dummy_tree_changed
    assert t.dependencies == dummy_dependencies

# Class to hold and propagate the AST from one transformer to another.

# Generated at 2022-06-14 02:47:53.819698
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    assert TransformationResult(None, True, None)