

# Generated at 2022-06-14 02:39:03.574377
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    t = TransformationResult
    assert t.tree.__name__ == 'AST'
    assert t.tree_changed.__name__ == 'bool'
    assert t.dependencies.__name__ == 'List'

# Generated at 2022-06-14 02:39:08.363464
# Unit test for constructor of class InputOutput
def test_InputOutput():
    assert InputOutput(Path('foo'), Path('bar')).input == Path('foo')
    assert InputOutput(Path('foo'), Path('bar')).output == Path('bar')
    assert str(InputOutput(Path('foo'), Path('bar'))) == \
        "InputOutput(input=PosixPath('foo'), output=PosixPath('bar'))"


# Generated at 2022-06-14 02:39:13.019429
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    test_tree = ast.parse('', '<string>')
    test_tree_changed = True
    test_dependencies = ['a', 'b', 'c']
    test_result = TransformationResult(test_tree, test_tree_changed,
                                       test_dependencies)
    assert test_result.tree == test_tree
    assert test_result.tree_changed == test_tree_changed
    assert test_result.dependencies == test_dependencies

# Generated at 2022-06-14 02:39:15.357170
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    CompilationResult(files=0, time=0.0, target=(3, 8), dependencies=[])



# Generated at 2022-06-14 02:39:20.784210
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    cr = CompilationResult(files=1, time=2.0, target=(3, 4), dependencies=[])
    assert cr.files == 1
    assert cr.time == 2.0
    assert cr.target == (3, 4)
    assert cr.dependencies == []
    assert str(cr) == 'files: 1, time: 2.0, target: (3, 4), deps: []'


# Generated at 2022-06-14 02:39:22.981444
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    CompilationResult(1, 2, (3, 4), ['a'])

# Generated at 2022-06-14 02:39:24.789283
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tr = TransformationResult(tree=None,
                              tree_changed=False,
                              dependencies=[])

# Generated at 2022-06-14 02:39:26.163413
# Unit test for constructor of class InputOutput
def test_InputOutput():
    assert InputOutput(input=Path('.'), output=Path('.'))


# Generated at 2022-06-14 02:39:28.691081
# Unit test for constructor of class InputOutput
def test_InputOutput():
    a = InputOutput('in', 'out')
    assert isinstance(a.input, Path)
    assert isinstance(a.output, Path)



# Generated at 2022-06-14 02:39:32.828141
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    files = 2
    time = 1.23
    target = (3, 5)
    dependencies = ['foo', 'bar/baz']
    result = CompilationResult(files, time, target, dependencies)
    assert result.files == files
    assert result.time == time
    assert result.target == target
    assert result.dependencies == dependencies


# Generated at 2022-06-14 02:39:38.466056
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input_path = Path('/a/./b/file.py')
    output_path = Path('/some/path.py')
    input_output = InputOutput(input_path, output_path)
    assert input_output.input == input_path
    assert input_output.output == output_path

# Generated at 2022-06-14 02:39:41.052558
# Unit test for constructor of class InputOutput
def test_InputOutput():
    # Constructor accepts both string and path objects
    path1 = InputOutput(Path('in'), Path('out'))
    path2 = InputOutput('in', 'out')
    assert path1 == path2


# Generated at 2022-06-14 02:39:43.987906
# Unit test for constructor of class InputOutput
def test_InputOutput():
    path1 = Path('1.py')
    path2 = Path('2.py')

    assert InputOutput(path1, path2) is InputOutput(path1, path2)
    assert InputOutput(path1, path2) != InputOutput(path2, path1)

# Generated at 2022-06-14 02:39:47.456305
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tr = TransformationResult(ast.parse('{}'), True, ['foo', 'bar'])
    assert tr.tree
    assert tr.tree_changed
    assert tr.dependencies == ['foo', 'bar']

# Generated at 2022-06-14 02:39:50.941846
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree = ast.parse('x = 1')
    result = TransformationResult(tree=tree, tree_changed=True, dependencies=['foo.txt'])
    assert result.tree is tree
    assert result.tree_changed is True
    assert result.dependencies == ['foo.txt']


# Generated at 2022-06-14 02:39:52.762380
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    _ = CompilationResult(files=5, time=3.3, target=(3, 7), dependencies=['foo', 'bar'])

# Generated at 2022-06-14 02:40:01.076923
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree = ast.Module()
    res = TransformationResult(tree, True, [])
    assert res.tree == tree
    assert res.tree_changed == True
    assert res.dependencies == []
    res = TransformationResult(tree, False, [])
    assert res.tree == tree
    assert res.tree_changed == False
    assert res.dependencies == []
    res = TransformationResult(tree, True, ['a'])
    assert res.tree == tree
    assert res.tree_changed == True
    assert res.dependencies == ['a']


# Generated at 2022-06-14 02:40:03.320446
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    res = CompilationResult(files=1, time=0.0,
                            target=(3, 6),
                            dependencies=[])

# Generated at 2022-06-14 02:40:07.094161
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input_path = Path('.') / 'foo.py'
    output_path = Path('.') / 'foo_out.py'
    io = InputOutput(input_path, output_path)
    assert io.input == input_path
    assert io.output == output_path

# Generated at 2022-06-14 02:40:14.858812
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    T = TransformationResult
    transformer_name = 'test-transformer'

    # Positive test
    node = ast.parse('1')
    tree_changed = True
    dependencies = []
    T(node, tree_changed, dependencies)

    # Negative test (unhashable type)
    _ = lambda: T(node, tree_changed, [node])
    assert_raises(TypeError, _)

    # Negative test (not tree)
    _ = lambda: T('1', tree_changed, dependencies)
    assert_raises(TypeError, _)

# Generated at 2022-06-14 02:40:23.177499
# Unit test for constructor of class CompilationResult
def test_CompilationResult():

    # If no files were produced, then the target and time are None
    cr = CompilationResult(0, 10.0, (3, 7), None)
    assert cr.files == 0
    assert cr.target is None
    assert cr.time is None
    assert cr.dependencies is None

    # If zero time was taken, then the target is None
    cr = CompilationResult(2, 0.0, (3, 7), None)
    assert cr.files == 2
    assert cr.target is None
    assert cr.time == 0.0
    assert cr.dependencies is None

    # If all values are set, then they should be equal to the input
    cr = CompilationResult(2, 10.0, (3, 7), ['a.py', 'b.py'])
    assert cr.files == 2

# Generated at 2022-06-14 02:40:30.155563
# Unit test for constructor of class TransformationResult
def test_TransformationResult():  # type: () -> None
    from ast import parse
    from tests import helpers
    body = parse("pass").body
    result = TransformationResult(body, False, ["path_to_dependency"])
    assert result.tree is body
    assert result.tree_changed is False
    assert result.dependencies == ["path_to_dependency"]
    helpers.assert_raises_typeerror(result, "dependencies", "hello")
    helpers.assert_raises_typeerror(result, "dependencies", [1])



# Generated at 2022-06-14 02:40:32.556268
# Unit test for constructor of class InputOutput
def test_InputOutput():
    class A(NamedTuple):
        a: Path
        b: Path

    assert InputOutput(Path("a"), Path("b")) == A(Path("a"), Path("b"))



# Generated at 2022-06-14 02:40:39.115243
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree = ast.parse('x=5')
    tree_changed = True
    dependencies = ['a.py', 'b.py']
    r = TransformationResult(tree, tree_changed, dependencies)
    assert(r.tree == tree)
    assert(r.tree_changed == tree_changed)
    assert(r.dependencies == dependencies)

# Generated at 2022-06-14 02:40:44.063811
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree = ast.parse('pass')
    tr = TransformationResult(tree, False, ['x.py'])
    assert repr(tr) == "TransformationResult(tree=<_ast.Module object at 0x7f849e5a5128>, tree_changed=False, dependencies=['x.py'])"

# Generated at 2022-06-14 02:40:44.903675
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    node = ast.parse('pass')
    tr = TransformationResult(node, False, [])
    assert tr.tree == node



# Generated at 2022-06-14 02:40:49.543114
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    result = CompilationResult(100, 32.5, (2, 7), [])
    assert result.files == 100
    assert result.time == 32.5
    assert result.target == (2, 7)
    assert result.dependencies == []


# Generated at 2022-06-14 02:40:59.269796
# Unit test for constructor of class InputOutput
def test_InputOutput():
    assert InputOutput(input = Path('input.txt'),
                       output = Path('output.txt'))
    try:
        InputOutput(input = Path('input.txt'),
                    output = None)
        assert False
    except ValueError:
        assert True

    try:
        InputOutput(input = Path('input.txt'),
                    output = 'output.txt')
        assert False
    except TypeError:
        assert True

    try:
        InputOutput(input = None,
                    output = Path('output.txt'))
        assert False
    except ValueError:
        assert True

    try:
        InputOutput(input = 'input.txt',
                    output = Path('output.txt'))
        assert False
    except TypeError:
        assert True

# Generated at 2022-06-14 02:41:04.971194
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    files = 1
    time = 0.0
    target = (3, 7)
    dependencies = ['dep1', 'dep2']
    res = CompilationResult(files=files, time=time,
                            target=target,
                            dependencies=dependencies)
    assert res.files == files
    assert res.time == time
    assert res.target == target
    assert res.dependencies == dependencies


# Generated at 2022-06-14 02:41:14.431301
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    # pylint: disable=missing-init

    def check(obj):
        if obj.tree_changed:
            assert obj.tree is not None
            assert len(obj.dependencies) >= 0
        else:
            assert obj.tree is None
            assert len(obj.dependencies) == 0

    check(TransformationResult(tree=None,
                               tree_changed=False,
                               dependencies=[]))

    check(TransformationResult(tree=None,
                               tree_changed=True,
                               dependencies=['a', 'b']))

    check(TransformationResult(tree=ast.parse('pass'),
                               tree_changed=False,
                               dependencies=['a', 'b']))


# Generated at 2022-06-14 02:41:28.580934
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    t = ast.parse('x = 1')
    assert t.body[0].value.n == 1
    r = TransformationResult(t, False, [])
    assert r.tree is t
    assert r.tree.body[0].value.n == 1
    t.body[0].value.n = 2
    assert r.tree.body[0].value.n == 2
    r.tree.body[0].value.n = 42
    assert t.body[0].value.n == 42

# Settings for compilation

# Generated at 2022-06-14 02:41:40.097432
# Unit test for constructor of class InputOutput
def test_InputOutput():
    test_path1 = Path('/tmp/test/paths/1')
    test_path2 = Path('/tmp/test/paths/2')
    io1 = InputOutput(test_path1, test_path2)
    io2 = InputOutput(test_path2, test_path1)
    io3 = InputOutput(test_path1, test_path1)
    io4 = InputOutput(test_path2, test_path2)
    assert io1 != io2
    assert io1 != io3
    assert io1 != io4
    assert io2 != io3
    assert io2 != io4
    assert not io1 == io2
    assert not io1 == io3
    assert not io1 == io4
    assert not io2 == io3
    assert not io2 == io4
    assert io1

# Generated at 2022-06-14 02:41:42.571921
# Unit test for constructor of class InputOutput
def test_InputOutput():
    assert InputOutput(Path('input'), Path('output')) == InputOutput('input', 'output')

# Generated at 2022-06-14 02:41:44.942481
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tr = TransformationResult(ast.parse('1+1'), True, ['abc'])
    assert tr.tree != None
    assert tr.tree_changed == True
    assert tr.dependencies == ['abc']



# Generated at 2022-06-14 02:41:48.016175
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input = "build/plugin.py"
    output = "build/python2_target/plugin.py"
    input_output = InputOutput(input, output)
    assert input_output.input == input
    assert input_output.output == output


# Generated at 2022-06-14 02:41:55.008756
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    result = CompilationResult(files=3,
                               time=1.0,
                               target=(3, 5),
                               dependencies=['a', 'b'])
    assert result.files == 3
    assert result.time == 1.0
    assert result.target[0] == 3
    assert result.target[1] == 5
    assert result.dependencies == ['a', 'b']


# Generated at 2022-06-14 02:41:59.293485
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    result = CompilationResult(files=2, time=12.0, target=(3, 5), dependencies=[])
    assert result.files == 2
    assert result.time == 12.0
    assert result.target == (3, 5)
    assert result.dependencies == []


# Generated at 2022-06-14 02:42:04.502422
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    res = TransformationResult(ast.AST(body=[]), True, [])
    assert isinstance(res, TransformationResult)
    assert isinstance(res.tree, ast.AST)
    assert isinstance(res.tree_changed, bool)
    assert isinstance(res.dependencies, list)


# Result of transformers transformation
TransformersResult = NamedTuple('TransformersResult',
                                [('source', str),
                                 ('source_changed', bool),
                                 ('dependencies', List[str])])


# Generated at 2022-06-14 02:42:09.388629
# Unit test for constructor of class InputOutput
def test_InputOutput():
    assert InputOutput(input = Path('a'), output = Path('b')) == InputOutput(input = Path('a'), output = Path('b'))
    assert InputOutput(input = Path('a'), output = Path('b')) != InputOutput(input = Path('a1'), output = Path('b'))

# Generated at 2022-06-14 02:42:12.450456
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input_output = InputOutput('input', 'output')
    assert str(input_output.input) == 'input'
    assert str(input_output.output) == 'output'

# Generated at 2022-06-14 02:42:24.493919
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    assert CompilationResult(files=1, time=2, target=(3, 4),
                             dependencies=['/foo', '/bar'])


# Generated at 2022-06-14 02:42:26.256661
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree = ast.parse('a = 5')
    TransformationResult(tree=tree, tree_changed=True, dependencies=["a", "b", "c"])

# Generated at 2022-06-14 02:42:30.826404
# Unit test for constructor of class InputOutput
def test_InputOutput():
    # Arrange
    input = Path('input.txt')
    output = Path('output.txt')

    # Act
    io = InputOutput(input, output)

    # Assert
    assert io.input == input
    assert io.output == output



# Generated at 2022-06-14 02:42:37.654177
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    files = 20
    time = 1.5
    target = (3, 7)
    dependencies = ['some', 'libs']

    result = CompilationResult(files=files, time=time,
                               target=target, dependencies=dependencies)

    assert result.files == files
    assert result.time == time
    assert result.target == target
    assert result.dependencies == dependencies



# Generated at 2022-06-14 02:42:45.266741
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    cr = CompilationResult(
        files=0,
        time=100.1,
        target=(3, 4),
        dependencies=[
            "dependency_1",
            "dependency_2",
        ],
    )
    assert cr.files == 0
    assert cr.time == 100.1
    assert cr.target == (3, 4)
    assert cr.dependencies == [
        "dependency_1",
        "dependency_2",
    ]


# Generated at 2022-06-14 02:42:49.664930
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    assert TransformationResult(None, False, []).tree is None
    assert TransformationResult(None, False, []).tree_changed == False
    assert TransformationResult(None, False, []).dependencies == []
    assert TransformationResult(ast.parse(""), False, []).tree is not None
    assert TransformationResult(ast.parse(""), False, []).tree_changed == False
    assert TransformationResult(ast.parse(""), False, []).dependencies == []


# Generated at 2022-06-14 02:42:52.686539
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    compilation_result = CompilationResult(files=1,
                                           time=0.7,
                                           target=(3, 6),
                                           dependencies=['d1', 'd2'])


# Generated at 2022-06-14 02:42:56.575811
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    t = ast.parse('a')
    assert TransformationResult(t, True, []) == TransformationResult(t, True, [])
    assert TransformationResult(t, False, ['a']) != TransformationResult(t, True, ['a'])

# Generated at 2022-06-14 02:42:59.487770
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    # pylint: disable=unused-variable
    # pylint: disable=unused-argument
    TransformationResult(tree=None,
                         tree_changed=False,
                         dependencies=None)

# Generated at 2022-06-14 02:43:02.392197
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree = object()
    tree_changed = object()
    dependencies = object()
    tr = TransformationResult(tree, tree_changed, dependencies)
    assert tr.tree is tree
    assert tr.tree_changed is tree_changed
    assert tr.dependencies is dependencies



# Generated at 2022-06-14 02:43:29.458494
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    version = (3, 7)
    result = TransformationResult(ast.parse('1'), True, ['a', 'b'])
    assert isinstance(result, TransformationResult)
    assert isinstance(result.tree, ast.AST)
    assert isinstance(result.tree_changed, bool)
    assert isinstance(result.dependencies, list)
    assert len(result.dependencies) == 2
    assert isinstance(result.dependencies[0], str)

# Result of compilation of single file
FileCompilationResult = NamedTuple('FileCompilationResult',
                                   [('tree', ast.AST),
                                    ('outfile', Path),
                                    ('target', CompilationTarget),
                                    ('time', float),
                                    ('success', bool),
                                    ('dependencies', List[str])])


# Generated at 2022-06-14 02:43:31.250522
# Unit test for constructor of class InputOutput
def test_InputOutput():
    dirname = Path.cwd() / 'test'
    assert InputOutput(dirname / 'test.txt', dirname / 'test.txt')

# Generated at 2022-06-14 02:43:35.352091
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input_output = InputOutput(Path("a"), Path("b"))
    assert input_output.input == Path("a")
    assert input_output.output == Path("b")



# Generated at 2022-06-14 02:43:36.964849
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    assert CompilationResult(0, 0, (3, 5), [])


# Generated at 2022-06-14 02:43:42.483080
# Unit test for constructor of class InputOutput
def test_InputOutput():
    """
    `InputOutput` constructor raises TypeError when input or output are not instaces of
    `pathlib.Path`.
    """
    with pytest.raises(TypeError):
        InputOutput(Path('a.py'), 'b.py')

    with pytest.raises(TypeError):
        InputOutput('a.py', Path('b.py'))

# Generated at 2022-06-14 02:43:49.079004
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    assert TransformationResult(ast.AST(), True, []) == \
           TransformationResult(ast.AST(), True, [])

# Result of runners run
ExecutionResult = NamedTuple('ExecutionResult',
                             [('command', str),
                              ('execution_time', float),
                              ('returncode', int),
                              ('stdout', str),
                              ('stderr', str)])


# Generated at 2022-06-14 02:43:51.670080
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input_ = Path('file_input')
    output = Path('file_output')

    i_output = InputOutput(input_, output)

    assert i_output.input == input_
    assert i_output.output == output



# Generated at 2022-06-14 02:43:59.267901
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    correct_values = CompilationResult(files=4,
                                       time=12.1,
                                       target=(3, 2),
                                       dependencies=['a', 'b'])
    assert isinstance(correct_values, CompilationResult)
    assert correct_values.files == 4
    assert correct_values.time == 12.1
    assert correct_values.target == (3, 2)
    assert correct_values.dependencies == ['a', 'b']


# Generated at 2022-06-14 02:44:06.948897
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    try:
        c = CompilationResult(files=1, time=1.0, target=(3, 4), dependencies=['one', 'two'])
    except Exception as e:
        raise TypeError('Unexpected exception raised: ' + str(e)) from e
    try:
        c = CompilationResult(files=None, time=0.0, target=(3, 4), dependencies=['one', 'two'])
        raise Exception('Exception was not raised')
    except TypeError as e:
        pass
    try:
        c = CompilationResult(files=1, time='string', target=(3, 4), dependencies=['one', 'two'])
        raise Exception('Exception was not raised')
    except TypeError as e:
        pass

# Generated at 2022-06-14 02:44:13.105784
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    class EmptyTransformer(ast.NodeTransformer):
        pass
    x = ast.parse('a')
    tt = EmptyTransformer().visit(x)
    t = TransformationResult(tt, False, [])
    assert t.tree_changed == False
    assert t.dependencies == []
    assert t.tree == tt

# Generated at 2022-06-14 02:45:06.920265
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    assert CompilationResult(files=18, time=1.0, target=(3, 6), dependencies=['foo', 'bar'])
    assert CompilationResult(files=1, time=1.0, target=(3, 7), dependencies=['foo', 'bar'])
    assert CompilationResult(files=19, time=1.0, target=(3, 8), dependencies=['foo', 'bar'])


# Generated at 2022-06-14 02:45:11.840677
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    result = CompilationResult(files=1, time=.5, target=(3, 5),
                               dependencies=['mod1', 'mod2'])
    assert result.files == 1
    assert result.time == .5
    assert result.target == (3, 5)
    assert result.dependencies == ['mod1', 'mod2']


# Generated at 2022-06-14 02:45:14.412264
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    files = 1
    time = 1.0
    target = (3, 6)
    dependencies = []
    compilation_result = CompilationResult(files, time, target, dependencies)


# Generated at 2022-06-14 02:45:21.147564
# Unit test for constructor of class TransformationResult
def test_TransformationResult():  # pragma: no cover
    import sys
    import os
    import inspect
    import ast
    from astmonkey import transformers

    # Simple AST from class Transformer
    tree = ast.parse(inspect.getsource(transformers.Transformer))
    # Transform this AST with no-op transformer
    res = TransformationResult(tree, False, [])
    # Check attributes of result
    assert res.tree is tree
    assert res.tree_changed == False
    assert res.dependencies == []

# Generated at 2022-06-14 02:45:22.463456
# Unit test for constructor of class InputOutput
def test_InputOutput():
    # pylint:disable=redefined-outer-name
    InputOutput('foo', 'bar')

# Generated at 2022-06-14 02:45:27.355183
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    input_tree = ast.parse("")
    output_tree = ast.parse("")
    construct = TransformationResult(input_tree, True, ["dep1", "dep2"])
    assert construct.tree == input_tree
    assert construct.tree_changed == True
    assert construct.dependencies == ["dep1", "dep2"]



# Generated at 2022-06-14 02:45:33.142321
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    # type: () -> None
    target = CompilationTarget(3, 7)
    result = CompilationResult(42, 42, target, ['spam'])

    assert result.files == 42
    assert result.time == 42
    assert result.target == target
    assert result.dependencies == ['spam']


# Generated at 2022-06-14 02:45:34.850774
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    _ = TransformationResult(tree=None, tree_changed=True, dependencies=[])

# Generated at 2022-06-14 02:45:37.355205
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    CompilationResult(0, 0.0, (3, 6), [])

# Compile single file

# Generated at 2022-06-14 02:45:42.474393
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    cr = CompilationResult(1, 2, (3, 4), ['dependency'])
    assert cr.files == 1
    assert cr.time == 2
    assert cr.target == (3, 4)
    assert cr.dependencies == ['dependency']


# Generated at 2022-06-14 02:47:33.647774
# Unit test for constructor of class InputOutput
def test_InputOutput():
    io = InputOutput(Path('myfile.py'), Path('myfile.out'))
    assert io.input == Path('myfile.py')
    assert io.output == Path('myfile.out')
    assert io.input.exists()



# Generated at 2022-06-14 02:47:39.196765
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    compilation_result = CompilationResult(files=1,
                                           time=3.14,
                                           target=(3, 7),
                                           dependencies=['foo', 'bar'])
    assert compilation_result.files == 1
    assert compilation_result.time == 3.14
    assert compilation_result.target == (3, 7)
    assert compilation_result.dependencies == ['foo', 'bar']


# Generated at 2022-06-14 02:47:43.008753
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    res = CompilationResult(files=10, time=20, target=(3, 7), dependencies=[])
    assert res.files == 10
    assert res.time == 20
    assert res.target == (3, 7)
    assert res.dependencies == []


# Generated at 2022-06-14 02:47:47.160382
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    assert TransformationResult(ast.parse("x=1"), True, ["/a/b/c.py"])
    assert TransformationResult(ast.parse("x=1"), False, ["/a/b/c.py"])
    assert TransformationResult(ast.parse("x=1"), True, [])
    assert TransformationResult(ast.parse("x=1"), False, [])

# Generated at 2022-06-14 02:47:51.975220
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    test_instance = CompilationResult(1, 2.3, (3, 4), ['a', 'b'])
    assert test_instance.files == 1
    assert test_instance.time == 2.3
    assert test_instance.target == (3, 4)
    assert test_instance.dependencies == ['a', 'b']


# Generated at 2022-06-14 02:47:57.056244
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    """Unit test for constructor of class TransformationResult."""
    # pylint: disable=unnecessary-lambda
    # pylint: disable=invalid-name
    # pylint: disable=no-value-for-parameter
    TransformationResult([ast.Module([]), True, ['']])



# Generated at 2022-06-14 02:48:08.245691
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    assert CompilationResult(0, 0.0, (0, 0), []) == \
           CompilationResult(0, 0.0, (0, 0), [])
    assert CompilationResult(0, 0.0, (0, 0), []) != \
           CompilationResult(1, 0.0, (0, 0), [])
    assert CompilationResult(0, 0.0, (0, 0), []) != \
           CompilationResult(0, 1.0, (0, 0), [])
    assert CompilationResult(0, 0.0, (0, 0), []) != \
           CompilationResult(0, 0.0, (1, 0), [])

# Generated at 2022-06-14 02:48:10.661318
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    class A:
        tree = 'a'
        tree_changed = True
        dependencies = ['b', 'c']

    TransformationResult(A)

# Generated at 2022-06-14 02:48:22.505014
# Unit test for constructor of class InputOutput
def test_InputOutput():
    # Empty constructor
    empty = InputOutput()
    assert empty.input is None
    assert empty.output is None

    # Correct paths
    input_path = Path('test/test_path.py')
    output_path = Path('test/test_path.pyc')
    input_output = InputOutput(input_path, output_path)
    assert input_output.input == input_path
    assert input_output.output == output_path

    # Incorrect paths
    try:
        InputOutput(4, 'test/')
        assert False
    except TypeError:
        pass

    try:
        InputOutput('test', 4)
        assert False
    except TypeError:
        pass

# Generated at 2022-06-14 02:48:27.784268
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input_path = Path('/sample/path')
    output_path = Path('/other/path')
    input_output = InputOutput(input=input_path, output=output_path)
    assert input_output.input == input_path
    assert input_output.output == output_path
    input_output = InputOutput(input_path, output_path)
    assert input_output.input == input_path
    assert input_output.output == output_path
