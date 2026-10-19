

# Generated at 2022-06-14 02:39:05.648196
# Unit test for constructor of class InputOutput
def test_InputOutput():
    # pylint: disable=no-value-for-parameter
    input_output = InputOutput(Path('/home/user/transpyle/data.dat'),
                               Path('/home/user/transpyle/data.pyc'))

    assert type(input_output.input) is Path
    assert type(input_output.output) is Path



# Generated at 2022-06-14 02:39:10.863363
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    result = CompilationResult(12, 0.42,
                               CompilationTarget(3, 6),
                               ['foo.py', 'bar.py'])
    assert result.files == 12
    assert result.time == 0.42
    assert result.target == (3, 6)
    assert result.dependencies == ['foo.py', 'bar.py']


# Generated at 2022-06-14 02:39:14.147531
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    res = CompilationResult(1, 1.0, (2, 2), {})
    assert repr(res) == "CompilationResult(files=1, time=1.0, target=(2, 2), dependencies={})"


# Generated at 2022-06-14 02:39:22.921350
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input = Path('./input')
    output = Path('./output')
    pair = InputOutput(input, output)
    assert pair.input == input
    assert pair.output == output

# Description of a single Python transformer
TransformerDescription = NamedTuple('TransformerDescription',
                                    [('name', str),
                                     ('transformer', Callable[[ast.AST], TransformationResult]),
                                     ('source_path', Path)])

# Description of a single Python target
TargetDescription = NamedTuple('TargetDescription',
                               [('target', CompilationTarget),
                                ('directory', Path),
                                ('transforms', List[TransformerDescription])])

if __name__ == "__main__":
    test_InputOutput()

# Generated at 2022-06-14 02:39:28.285640
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    result = CompilationResult(files=5,
                               time=42.0,
                               target=(3, 6),
                               dependencies=['a', 'b', 'c'])
    assert result.files == 5
    assert result.time == 42.0
    assert result.target == (3, 6)
    assert result.dependencies == ['a', 'b', 'c']


# Generated at 2022-06-14 02:39:30.301878
# Unit test for constructor of class InputOutput
def test_InputOutput():
    io = InputOutput(input = '/input/path', output = '/output/path')
    assert io.input == Path('/input/path')
    assert io.output == Path('/output/path')



# Generated at 2022-06-14 02:39:37.781329
# Unit test for constructor of class InputOutput
def test_InputOutput():
    try:
        InputOutput('a', 'b')
    except TypeError:
        pass
    else:
        assert False, "InputOutput should be constructed with Paths"
    assert InputOutput(Path('a'), Path('b')) == InputOutput(Path('a'),
                                                            Path('b'))
    assert InputOutput(Path('a'), Path('b')) != InputOutput(Path('b'),
                                                            Path('b'))
    assert InputOutput(Path('a'), Path('b')) != (Path('a'), Path('b'))


# Generated at 2022-06-14 02:39:40.586276
# Unit test for constructor of class TransformationResult
def test_TransformationResult():  # type: () -> None
    tr = TransformationResult(tree=None,
                              tree_changed=False,
                              dependencies=[])
    assert tr.tree is None
    assert tr.tree_changed is False
    assert tr.dependencies == []

# Generated at 2022-06-14 02:39:43.611381
# Unit test for constructor of class InputOutput
def test_InputOutput():
    in_path = Path('foo.py')
    out_path = Path('bar.py')
    res = InputOutput(in_path, out_path)
    assert res.input == in_path
    assert res.output == out_path


# Generated at 2022-06-14 02:39:48.742083
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tr = TransformationResult(tree={'a': 20},
                              tree_changed=True,
                              dependencies=['hello', 'world'])

    assert isinstance(tr, TransformationResult)
    assert tr.tree == {'a': 20}
    assert tr.tree_changed is True
    assert tr.dependencies == ['hello', 'world']

# Generated at 2022-06-14 02:39:54.165370
# Unit test for constructor of class InputOutput
def test_InputOutput():
    i1 = InputOutput(input=Path('in1'), output=Path('out1'))
    assert i1 == InputOutput(input=Path('in1'), output=Path('out1'))
    assert i1.input == Path('in1')
    assert i1.output == Path('out1')


# Generated at 2022-06-14 02:39:57.490298
# Unit test for constructor of class InputOutput
def test_InputOutput():
    i = Path('foo')
    o = Path('bar')
    io = InputOutput(i, o)
    assert io.input == i
    assert io.output == o


# Generated at 2022-06-14 02:40:01.531510
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree = ast.Module([ast.Expr(ast.Num(1))])
    result = TransformationResult(tree, False, [])
    assert result.tree == tree
    assert result.tree_changed == False
    assert result.dependencies == []

# Generated at 2022-06-14 02:40:06.511889
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    assert TransformationResult(0, False, []) == (0, False, [])
    assert TransformationResult(0, False, []) != (0, True, [])

# Result of transformers compilation
CompilationResult = NamedTuple('CompilationResult',
                               [('tree', ast.AST),
                                ('output', Path),
                                ('dependencies', List[str])])

# Generated at 2022-06-14 02:40:09.494070
# Unit test for constructor of class InputOutput
def test_InputOutput():
    path = Path('/path/to/file.py')
    input_output = InputOutput(path, path)
    assert isinstance(input_output.input, Path)
    assert isinstance(input_output.output, Path)



# Generated at 2022-06-14 02:40:12.396996
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    assert CompilationResult(files=0, time=0.0,
                             target=(0, 0),
                             dependencies=[])

# Generated at 2022-06-14 02:40:18.326831
# Unit test for constructor of class InputOutput
def test_InputOutput():
    # pylint: disable=unused-variable
    input_ = Path('/path/to/input')
    output = Path('/path/to/output')
    pair = InputOutput(input_, output)
    assert pair.input == input_
    assert pair.output == output


# Generated at 2022-06-14 02:40:27.688599
# Unit test for constructor of class InputOutput
def test_InputOutput():
    # Check initial value
    assert InputOutput(Path(), Path()).input == Path('.')

    # Check usage of constructor with None
    assert InputOutput(None, None).input == Path('.')

    # Check usage of constructor with empty string
    assert InputOutput('', '').input == Path('.')

    # Check usage of constructor with not empty string
    assert InputOutput('in', 'out').input == Path('in')

    # Check usage of constructor with path
    assert InputOutput(Path(), Path()).input == Path('.')

    # Check usage of constructor with other path
    assert InputOutput(Path('in'), Path('out')).input == Path('in')

# Generated at 2022-06-14 02:40:32.716586
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    t = ast.parse('x = 1')
    r = TransformationResult(tree=t, tree_changed=True, dependencies=[])
    assert r.tree == t
    assert r.tree_changed == True
    assert r.dependencies == []

# Compilation results for single file
FileResult = NamedTuple('FileResult',
                        [('file', Path),
                         ('result', CompilationResult)])


# Generated at 2022-06-14 02:40:36.013935
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    CompilationResult(5, 12.5, (3, 8), [])


# Generated at 2022-06-14 02:40:41.294888
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input_output = InputOutput(input=Path('a'), output=Path('b'))
    assert input_output.input == Path('a')
    assert input_output.output == Path('b')

# Test implementation of __eq__
# Test implementation of __ne__
# Test implementation of __hash__

# Generated at 2022-06-14 02:40:44.657546
# Unit test for constructor of class InputOutput
def test_InputOutput():
    x = InputOutput(Path.cwd(), Path.home())
    assert x.input == Path.cwd()
    assert x.output == Path.home()


# Generated at 2022-06-14 02:40:50.923844
# Unit test for constructor of class InputOutput
def test_InputOutput():
    p1 = Path('/')
    p2 = Path('bash.txt')
    io = InputOutput(p1, p2)
    assert io.input == p1
    assert io.output == p2
    assert io.input.parent == Path('/')
    assert io.output.parent == Path('.')
    assert io.input.name == ''
    assert io.output.name == 'bash.txt'



# Generated at 2022-06-14 02:40:58.194810
# Unit test for constructor of class TransformationResult
def test_TransformationResult(): # type: () -> None
    from collections import namedtuple
    from typed_ast import ast3 as ast
    from mypy_boto3_builder.transformer_class import TransformationResult
    Tr = TransformationResult(
        tree=ast.parse('import "os"'),
        tree_changed=False,
        dependencies=['os'])
    assert Tr.tree_changed == False
TransformationResult.__module__ = 'mypy_boto3_builder.type_definitions'

# Generated at 2022-06-14 02:41:05.590420
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    test_vars = {'tree': ast.parse('x = 1'),
                 'tree_changed': True,
                 'dependencies': []}
    res = TransformationResult(**test_vars)
    assert res.tree == test_vars['tree']
    assert res.tree_changed == test_vars['tree_changed']
    assert res.dependencies == test_vars['dependencies']



# Generated at 2022-06-14 02:41:09.364615
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    t = TransformationResult(None, False, [])
    assert t.tree is None
    assert not t.tree_changed
    assert t.dependencies == []

# Generated at 2022-06-14 02:41:17.224050
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    try:
        TransformationResult(ast.AST(), True, [])
    except TypeError as e:
        print("Error while constructing TransformationResult:\n\t" + str(e))

# Result of grepper transformation
GrepResult = NamedTuple('GrepResult', [('output', Path)])

# Result of Generator transformation
GeneratorResult = NamedTuple('GeneratorResult', [('output', Path)])

# Result of template transformation
TemplateResult = NamedTuple('TemplateResult', [('output', Path)])

# Result of Compiler transformation
CompilerResult = NamedTuple('CompilerResult', [('output', Path)])

# Result of a transformation
Transformation = NamedTuple('Transformation',
                            [('input', InputOutput),
                             ('result', TransformationResult)])

# Result of a grepper
Gre

# Generated at 2022-06-14 02:41:22.241454
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tr = TransformationResult(ast.parse('s = 1'),
                              True,
                              ['a', 'b'])
    assert tr.tree_changed == True
    assert tr.dependencies == ['a', 'b']

# Result of a single test run
TestResult = NamedTuple('TestResult',
                        [('name', str),
                         ('result', bool),
                         ('output', str),
                         ('error', str),
                         ('time', float)])


# Generated at 2022-06-14 02:41:26.982186
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    # Arrange
    files = 1
    time = 1.0
    target = (2, 3)
    dependencies = ['a.py']

    # Act
    result = CompilationResult(files, time, target, dependencies)

    # Assert
    assert result.files == files
    assert result.time == time
    assert result.target == target
    assert result.dependencies == dependencies


# Generated at 2022-06-14 02:41:29.172037
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    assert CompilationResult(1, 2.0, (3, 4), ["a.py"])


# Generated at 2022-06-14 02:41:39.696101
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tr = TransformationResult(tree=ast.parse('x=42'),
                              tree_changed=False,
                              dependencies=[])
    assert tr.tree_changed == False
    assert tr.dependencies == []
    assert ast.dump(tr.tree) == "Module(body=[Assign(targets=[Name(id='x', ctx=Store())],value=Constant(value=42))])"


# Generated at 2022-06-14 02:41:42.492226
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    CompilationResult(1, 2.3, (3, 4), [])


# Generated at 2022-06-14 02:41:44.169333
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    CompilationResult(files=2,
                      time=5.5,
                      target=(3, 4),
                      dependencies=["d1", "d2"])

# Generated at 2022-06-14 02:41:47.522890
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    a = CompilationResult(files=1, time=2.0, target=(3, 4), dependencies=[])
    assert a.files == 1
    assert a.time == 2.0
    assert a.dependencies == []
    assert a.target == (3, 4)


# Generated at 2022-06-14 02:41:48.613190
# Unit test for constructor of class InputOutput
def test_InputOutput():
    InputOutput(input=Path('.'), output=Path('.'))


# Generated at 2022-06-14 02:41:51.641612
# Unit test for constructor of class TransformationResult
def test_TransformationResult():  # noqa: D103
    t = ast.parse("x = 1")
    tr = TransformationResult(tree=t,
                              tree_changed=False,
                              dependencies=[])
    assert tr.tree == t
    assert not tr.tree_changed
    assert len(tr.dependencies) == 0

# Generated at 2022-06-14 02:42:00.894023
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree = ast.parse('from typing import List\n'
                     'def f(x: List[int])->List[int]:\n'
                     '    return [2*n for n in x]\n')
    result = TransformationResult(
        ast.parse('from typing import List\n'
                  'def f(x: List[int])->List[int]:\n'
                  '    return [2*n for n in x]\n'),
        True,
        ['typing'])
    assert result.tree == tree
    assert result.tree_changed
    assert result.dependencies == ['typing']

# Generated at 2022-06-14 02:42:05.485701
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    assert TransformationResult(ast.parse('2+2'), False, []) == \
           TransformationResult(ast.parse('2+2'), False, [])
    assert TransformationResult(ast.parse('2+2'), True, ['foo']) == \
           TransformationResult(ast.parse('2+2'), True, ['foo'])
    assert TransformationResult(ast.parse('2+2'), False, ['bar']) == \
           TransformationResult(ast.parse('2+2'), False, ['bar'])
    assert TransformationResult(ast.parse('2+2'), True, ['foo', 'bar']) == \
           TransformationResult(ast.parse('2+2'), True, ['foo', 'bar'])

# Generated at 2022-06-14 02:42:07.828171
# Unit test for constructor of class InputOutput
def test_InputOutput():
    assert InputOutput(input=Path('input'), output=Path('output')) == InputOutput(Path('input'), Path('output'))


# Generated at 2022-06-14 02:42:13.048401
# Unit test for constructor of class InputOutput
def test_InputOutput():
    str_input = '/a/b/c/d/e'
    str_output = '/a/b/c/d/f'
    assert InputOutput(input=str_input, output=str_output) == \
        InputOutput(input=Path(str_input), output=Path(str_output))

# Generated at 2022-06-14 02:42:18.974446
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    assert TransformationResult(ast.Name(), True, [])

# Generated at 2022-06-14 02:42:22.684200
# Unit test for constructor of class InputOutput
def test_InputOutput():
    inp = Path('hello')
    out = Path('world')
    p = InputOutput(input=inp, output=out)
    assert p.input == inp
    assert p.output == ou

# Generated at 2022-06-14 02:42:26.676703
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    res = TransformationResult(ast.parse('pass'), True, [__file__])
    assert res.tree_changed
    assert 'TransformationResult(tree=Module' in repr(res)
    assert 'tree_changed=True,' in repr(res)
    assert 'dependencies=[' in repr(res)
    assert ']' in repr(res)

# Generated at 2022-06-14 02:42:31.756804
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    test_result = CompilationResult(files=1, time=1.0, target=(3, 5), dependencies=[])
    test_result.files
    test_result.time
    test_result.target
    test_result.dependencies



# Generated at 2022-06-14 02:42:35.863936
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input = Path('test/test_file.py')
    output = Path('test/test_file.pyc')
    io = InputOutput(input, output)
    assert io.input == input
    assert io.output == output



# Generated at 2022-06-14 02:42:39.017782
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input = Path('in')
    output = Path('out')
    pair = InputOutput(input, output)
    assert pair.input == input
    assert pair.output == output

# Generated at 2022-06-14 02:42:41.467816
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    t = CompilationResult(files=1, time=2.0, target=(3, 4), dependencies=[])
    assert t.files == 1
    assert t.time == 2.0
    assert t.target == (3, 4)
    assert t.dependencies == []


# Generated at 2022-06-14 02:42:47.017351
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    assert CompilationResult(files=1, time=2.3, target=(3, 4), dependencies=["1"])
    assert CompilationResult(files=0, time=3.3, target=(3, 4), dependencies=[])
    assert CompilationResult(files=0, time=2.3, target=(0, 0), dependencies=[""])
    assert CompilationResult(files=0, time=0.0, target=(0, 0), dependencies=[])


# Generated at 2022-06-14 02:42:48.315734
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    CompilationResult(files=0, time=0, target=(3, 8), dependencies=[])

# Generated at 2022-06-14 02:42:49.550821
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    CompilationResult(1, 2.0, (3, 4), ['abc', 'def'])


# Generated at 2022-06-14 02:43:01.238281
# Unit test for constructor of class CompilationResult
def test_CompilationResult():  # type: ignore
    CompilationResult(1, 2, (3, 4), ['a', 'b'])


# Generated at 2022-06-14 02:43:03.696329
# Unit test for constructor of class InputOutput
def test_InputOutput():
    _ = InputOutput(Path('a.txt'), Path('b.txt'))


# Generated at 2022-06-14 02:43:07.019595
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    try:
        CompilationResult()
    except Exception as e:
        assert type(e) == TypeError
    CompilationResult(0, 0, (0, 0), [])


# Generated at 2022-06-14 02:43:08.552386
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    TransformationResult(tree=None, tree_changed=False, dependencies=[])

# Generated at 2022-06-14 02:43:11.636239
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    cr = CompilationResult(1, 2, (2, 3), [])
    assert cr.files == 1
    assert cr.target == (2, 3)
    assert cr.dependencies == []



# Generated at 2022-06-14 02:43:15.740221
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    cr = CompilationResult(files=10, time=5.0,
                           target=(1, 2),
                           dependencies=['d1', 'd2'])
    assert cr.files == 10
    assert cr.time == 5.0
    assert cr.target == (1, 2)
    assert cr.dependencies == ['d1', 'd2']


# Generated at 2022-06-14 02:43:27.804766
# Unit test for constructor of class InputOutput
def test_InputOutput():
    assert InputOutput(Path("1.py"), Path("1.pyc")) == \
        InputOutput("1.py", "1.pyc")
    assert InputOutput(Path("1.py"), Path("1.pyc")) == \
        InputOutput("1.py", "1.pyc")
    assert InputOutput(Path("1.py"), Path("1.pyc")) == \
        InputOutput("1.py", Path("1.pyc"))
    assert InputOutput("1.py", "1.pyc") == \
        InputOutput("1.py", "1.pyc")
    assert InputOutput("1.py", "1.pyc") != \
        InputOutput("2.py", "2.pyc")

# Generated at 2022-06-14 02:43:32.048096
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    files = 10
    time = 10.0
    target = (3, 7)
    deps = ['a', 'b', 'c']
    cr = CompilationResult(files, time, target, deps)
    assert(cr.files == files)
    assert(cr.time == time)
    assert(cr.target == target)
    assert(cr.dependencies == deps)


# Generated at 2022-06-14 02:43:37.015780
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    c = TransformationResult(
        tree=ast.parse('1'),
        tree_changed=False,
        dependencies=['a', 'b'])
    assert c.tree is not None
    assert c.tree_changed is False
    assert c.dependencies == ['a', 'b']

# Generated at 2022-06-14 02:43:40.112747
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    result = TransformationResult(ast.Module([]), True, [])
    assert isinstance(result.tree, ast.AST)
    assert isinstance(result.tree_changed, bool)
    assert isinstance(result.dependencies, list)

# Generated at 2022-06-14 02:44:09.261109
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    compilationResult = CompilationResult(0, 0.1, (2, 7), ['a.py'])
    assert compilationResult.files == 0
    assert compilationResult.time == 0.1
    assert compilationResult.target == (2, 7)
    assert compilationResult.dependencies == ['a.py']


# Generated at 2022-06-14 02:44:13.296134
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input = Path("/in")
    output = Path("/out")
    io = InputOutput(input, output)
    assert io.input == input
    assert io.output == output


# Generated at 2022-06-14 02:44:17.564504
# Unit test for constructor of class InputOutput
def test_InputOutput():
    in_out = InputOutput(input=Path('/foo/bar/baz'),
                         output=Path('/foo/bar/fum'))
    assert in_out.input == Path('/foo/bar/baz')
    assert in_out.output == Path('/foo/bar/fum')


# Generated at 2022-06-14 02:44:21.495357
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    # Perform compilation result construction
    comp = CompilationResult(files=3, time=0.02, target=(3, 5), dependencies=['file1', 'file2'])
    # Perform assertions
    assert comp.files == 3
    assert comp.time == 0.02
    assert comp.target == (3, 5)
    assert comp.dependencies == ['file1', 'file2']


# Generated at 2022-06-14 02:44:24.965594
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    # type: () -> None

    result = CompilationResult(files=1, time=1.0, target=(3, 7), dependencies=[])
    assert result.files == 1
    assert result.time == 1.0
    assert result.target == (3, 7)
    assert result.dependencies == []


# Generated at 2022-06-14 02:44:28.825291
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input_output = InputOutput(Path('my_input'), Path('my_output'))
    assert input_output.input == Path('my_input')
    assert input_output.output == Path('my_output')

# Generated at 2022-06-14 02:44:37.527208
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree = ast.mod()
    tree_changed = False
    dependencies = []
    TransformationResult(tree=tree, tree_changed=tree_changed,
                         dependencies=dependencies)


# Type of AST transformer
Transformer = NamedTuple('Transformer', [('name', str),
                                         ('transform', Callable),
                                         ('enabled', bool),
                                         ('description', str)])

# Element of a configuration
ConfigItem = NamedTuple('ConfigItem', [('name', str),
                                       ('set', Callable),
                                       ('get', Callable),
                                       ('type', type),
                                       ('default', object),
                                       ('description', str)])

# Generated at 2022-06-14 02:44:40.820424
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input = Path('')
    output = Path('')
    input_output = InputOutput(input, output)
    assert input_output.input == input
    assert input_output.output == output

# Generated at 2022-06-14 02:44:45.148464
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree = None
    tree_changed = False
    dependencies = ["a", "b"]
    r = TransformationResult(tree, tree_changed, dependencies)
    assert isinstance(r, TransformationResult)
    assert r.tree is tree
    assert r.tree_changed is tree_changed
    assert r.dependencies is dependencies

# Generated at 2022-06-14 02:44:54.499206
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    assert CompilationResult(files=2, time=1.0, target=(3, 7), dependencies=['a.py'])
    assert CompilationResult(files=2, time=1.0, target=(3, 7), dependencies=['a.py']).files == 2
    assert CompilationResult(files=2, time=1.0, target=(3, 7), dependencies=['a.py']).time == 1.0
    assert CompilationResult(files=2, time=1.0, target=(3, 7), dependencies=['a.py']).target == (3, 7)
    assert CompilationResult(files=2, time=1.0, target=(3, 7), dependencies=['a.py']).dependencies == ['a.py']


# Generated at 2022-06-14 02:45:25.493945
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    compilation_result = CompilationResult(files=1,
                                           time=0.5,
                                           target=(3, 7),
                                           dependencies=['a'])
    assert compilation_result.files == 1
    assert compilation_result.time == 0.5
    assert compilation_result.target == (3, 7)
    assert compilation_result.dependencies == ['a']


# Generated at 2022-06-14 02:45:29.443319
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input_output = InputOutput(Path('input'), Path('output'))
    assert input_output.input == Path('input')
    assert input_output.output == Path('output')


# Generated at 2022-06-14 02:45:33.054423
# Unit test for constructor of class InputOutput
def test_InputOutput():
    path_in = 'path/in'
    path_out = 'path/out'
    
    assert InputOutput(input=path_in,output=path_out) == \
           path_in, path_out


# Generated at 2022-06-14 02:45:38.463859
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input_output = InputOutput(input=Path('./a.py'), output=Path('./a.py.transformed.py'))
    assert(input_output.input == Path('./a.py'))
    assert(input_output.output == Path('./a.py.transformed.py'))


# Generated at 2022-06-14 02:45:40.567129
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    CompilationResult(1, 2, (3, 4), [])


# Generated at 2022-06-14 02:45:41.796573
# Unit test for constructor of class InputOutput
def test_InputOutput():
    InputOutput(Path('/tmp/foo'), Path('/tmp/bar'))

# Generated at 2022-06-14 02:45:48.408742
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    res = CompilationResult(files=1, time=1.0, target=(3, 6),
                            dependencies=['a', 'b'])
    assert res.files == 1
    assert res.time == 1.0
    assert res.target == (3, 6)
    assert res.dependencies == ['a', 'b']


# Generated at 2022-06-14 02:45:51.278872
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    CompilationResult(files=1, time=1.2, target=(3, 4), dependencies=[])


# Generated at 2022-06-14 02:45:56.594796
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tr = TransformationResult(
        ast.parse('x+y'),
        False,
        ['module1', 'module2']
    )
    assert tr.tree_changed == False
    assert len(tr.dependencies) == 2

# Generated at 2022-06-14 02:46:00.365262
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    cr = CompilationResult(10,
                           0.5,
                           (3, 5),
                           ['a', 'b', 'c'])
    assert cr.files == 10
    assert cr.time == 0.5
    assert cr.target == (3, 5)
    assert cr.dependencies == ['a', 'b', 'c']


# Generated at 2022-06-14 02:46:58.633297
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tr = TransformationResult(ast.parse("x = 12"),
                              True,
                              ['sys', 'typing'])

    assert(tr.tree.body[0].value.n == 12)
    assert(tr.tree_changed)
    assert(tr.dependencies == ['sys', 'typing'])

# Generated at 2022-06-14 02:47:01.044928
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input_path = '/tmp/foo'
    output_path = '/tmp/bar'
    pair = InputOutput(input_path, output_path)
    assert pair.input == input_path
    assert pair.output == output_path

# Generated at 2022-06-14 02:47:06.686941
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    cr = CompilationResult(0, 0.1, (3, 6), [])
    assert cr.files == 0
    assert cr.time == 0.1
    assert cr.target == (3, 6)
    assert cr.dependencies == []
    cr = CompilationResult(10, 10, (2, 7), ['foo', 'bar'])
    assert cr.files == 10
    assert cr.time == 10
    assert cr.target == (2, 7)
    assert cr.dependencies == ['foo', 'bar']


# Generated at 2022-06-14 02:47:09.807621
# Unit test for constructor of class InputOutput
def test_InputOutput():
    name = "file.py"
    io = InputOutput(input=Path("input/" + name),
                     output=Path("output/" + name))
    assert io.input == "input/" + name
    assert io.output == "output/" + name


# Generated at 2022-06-14 02:47:12.313221
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    CompilationResult(files=1, time=1.0, target=(3, 6), dependencies=['a.py'])

# Generated at 2022-06-14 02:47:22.119593
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    c1 = CompilationResult(1, 1.0, (2, 3), [])
    assert c1.files == 1
    assert c1.time == 1.0
    assert c1.target == (2, 3)
    assert c1.dependencies == []

    c2 = CompilationResult(1, 1.0, (2, 3), [])
    assert c2 == c1
    assert not c2 != c1

    c3 = CompilationResult(2, 1.0, (2, 3), [])
    assert c3 != c1

    c4 = CompilationResult(1, 2.0, (2, 3), [])
    assert c4 != c1

    c5 = CompilationResult(1, 1.0, (3, 3), [])
    assert c5 != c1

    c6 = Comp

# Generated at 2022-06-14 02:47:32.984822
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    from ast import parse

    tree = parse(source="print(42)")
    result = TransformationResult(tree=tree,
                                  tree_changed=True,
                                  dependencies=['spam', 42])
    assert tree is result.tree
    assert result.tree_changed is True
    assert result.dependencies == ['spam', 42]

    tree_2 = parse(source="print(42)")
    result_2 = TransformationResult(tree=tree_2,
                                    tree_changed=False,
                                    dependencies=[])
    assert tree_2 is result_2.tree
    assert result_2.tree_changed is False
    assert result_2.dependencies == []

# Generated at 2022-06-14 02:47:36.649229
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree = ast.parse('def f(): pass')
    dependencies = ['module1', 'module2']
    res = TransformationResult(tree, True, dependencies)

    assert res.tree == tree
    assert res.tree_changed == True
    assert res.dependencies ==  dependencies

# Generated at 2022-06-14 02:47:40.063799
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    TransformationResult(ast.AST(), False, [])

__all__ = ['CompilationTarget', 'CompilationResult', 'InputOutput',
           'TransformationResult', 'test_TransformationResult']

# TODO: EAFP??
# TODO: ModuleResult - dependencies, time, files?

# Generated at 2022-06-14 02:47:45.751488
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    def f(): pass

    assert isinstance(TransformationResult(
        tree=ast.parse(''), tree_changed=False, dependencies=[]
    ), TransformationResult)


# Result of single file compilation
CompilationFileResult = NamedTuple('CompilationFileResult',
                                   [('input_output', InputOutput),
                                    ('result', CompilationResult),
                                    ('transformation_results', List[TransformationResult])])
