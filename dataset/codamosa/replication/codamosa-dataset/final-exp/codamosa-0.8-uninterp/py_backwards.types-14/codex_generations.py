

# Generated at 2022-06-14 02:38:58.502428
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    r = TransformationResult(ast.parse('pass'), True, ['dep1', 'dep2'])
    assert r.tree
    assert r.tree_changed is True
    assert r.dependencies == ['dep1', 'dep2']

# Generated at 2022-06-14 02:39:03.508514
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    c = CompilationResult(5, 1.0, (3, 7), [])
    assert c.files == 5
    assert c.time == 1.0
    assert c.target == (3, 7)
    assert c.dependencies == []


# Generated at 2022-06-14 02:39:07.177880
# Unit test for constructor of class InputOutput
def test_InputOutput():
    # type: () -> None
    input_output = InputOutput(input=Path('input'),
                               output=Path('output'))

    assert input_output.input == Path('input')
    assert input_output.output == Path('output')



# Generated at 2022-06-14 02:39:12.129597
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    # Nothing special to test here
    TransformationResult(tree=1, tree_changed=False, dependencies=[])


# Result of compilation
CompilationJobResult = NamedTuple('CompilationJobResult',
                                  [('input', Path),
                                   ('output', Path),
                                   ('compilation_result', CompilationResult),
                                   ('transformation_result', TransformationResult),
                                   ('errors', List[str])])

# Generated at 2022-06-14 02:39:15.540968
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input_output = InputOutput('README.md', 'README.md')
    assert input_output.input.name == 'README.md'
    assert input_output.output.name == 'README.md'

# Generated at 2022-06-14 02:39:20.865917
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    c = CompilationResult(0, 0.0, (3, 5), [])
    assert c.files == 0
    assert c.time == 0.0
    assert c.target == (3, 5)
    assert c.dependencies == []


# Generated at 2022-06-14 02:39:25.398041
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    a = ast.parse('pass')
    b = [('/a/foo.py', ['/bar.py'])]
    x = TransformationResult(a, True, b)
    assert type(x.tree) is ast.Module and x.tree_changed and x == x

# Generated at 2022-06-14 02:39:28.478417
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    compilation_result = CompilationResult(0, 0.0, (0, 0), [])
    assert compilation_result.files == 0
    assert compilation_result.time == 0.0
    assert compilation_result.target == (0, 0)
    assert compilation_result.dependencies == []



# Generated at 2022-06-14 02:39:32.907399
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    import logging
    import sys
    import time

    result = CompilationResult(0, time.time(), sys.version_info[:2], [])
    logging.info(result)
    assert result.files == 0
    assert result.time >= 0
    assert result.target == sys.version_info[:2]
    assert result.dependencies == []


# Unit tests for constructor of class InputOutput

# Generated at 2022-06-14 02:39:40.928842
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    _compilation_result = CompilationResult(
        files=1,
        time=1.0,
        target=(3, 7),
        dependencies=['file1.py', 'file2.py'])

    assert isinstance(_compilation_result, CompilationResult)
    assert _compilation_result.files == 1
    assert _compilation_result.time == 1.0
    assert _compilation_result.target == (3, 7)
    assert _compilation_result.dependencies[0] == 'file1.py'
    assert _compilation_result.dependencies[1] == 'file2.py'


# Generated at 2022-06-14 02:39:44.564624
# Unit test for constructor of class InputOutput
def test_InputOutput():
    path1 = 'path1'
    path2 = 'path2'
    input_output = InputOutput(path1, path2)
    assert input_output.input == path1
    assert input_output.output == path2


# Generated at 2022-06-14 02:39:46.013171
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    TransformationResult(ast.Module(), False, [])

# Generated at 2022-06-14 02:39:52.652571
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree = ast.parse("pass")
    tree_changed = True
    dependencies = ["a", "b"]
    res = TransformationResult(tree, tree_changed, dependencies)
    assert(res.tree == tree)
    assert(res.tree_changed == tree_changed)
    assert(res.dependencies == dependencies)

# Limitiation of compilation
CompilationLimit = NamedTuple("CompilationLimit",
                              [("time", float),
                               ("file_size", int)])

# Compilation limit with no limit
limit = CompilationLimit(float("inf"), int("inf"))

# Generated at 2022-06-14 02:39:53.594350
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    assert TransformationResult(None, None, None) is not None

# Generated at 2022-06-14 02:39:54.578438
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    assert TransformationResult(None, True, [])

# Generated at 2022-06-14 02:39:58.629081
# Unit test for constructor of class InputOutput
def test_InputOutput():
    inp = Path("input")
    out = Path("output")
    input_output_pair = InputOutput(inp, out)
    assert input_output_pair.input == inp
    assert input_output_pair.output == out

# Generated at 2022-06-14 02:40:01.176184
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    r = TransformationResult(
        tree = ast.parse(text = 'pass'),
        tree_changed = False,
        dependencies = []
    )

# Generated at 2022-06-14 02:40:04.812284
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree = ast.parse('a = 5')  # type: ast.AST
    result = TransformationResult(tree, True, ['1', '2'])
    assert result.tree == ast.parse('a = 5')  # type: ast.AST
    assert result.tree_changed is True
    assert result.dependencies == ['1', '2']

# Generated at 2022-06-14 02:40:08.793084
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree = ast.parse('print(1)')
    tree_changed = False
    dependencies = ['a', 'b']
    res = TransformationResult(tree, tree_changed, dependencies)

    assert res.tree == tree
    assert res.tree_changed == tree_changed
    assert res.dependencies == dependencies

# Generated at 2022-06-14 02:40:16.091347
# Unit test for constructor of class InputOutput
def test_InputOutput():
    p1 = 'tests/data/module.py'
    p2 = 'tests/data/module.pyi'
    i = InputOutput(input=Path(p1),
                    output=Path(p2))
    assert i.input == Path(p1)
    assert i.input is not Path(p1)
    assert i.output == Path(p2)
    assert i.output is not Path(p2)
    assert i.input.read_text() == p1
    assert i.output.read_text() == ''

# Generated at 2022-06-14 02:40:19.445508
# Unit test for constructor of class InputOutput
def test_InputOutput():
    assert InputOutput(Path('1.py'), Path('1.pyc'))
    assert InputOutput(Path('1.py'), Path('1.pyc')).__slots__ == ('input', 'output')



# Generated at 2022-06-14 02:40:22.011199
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree: ast.AST = ast.AST()
    dependencies: List[str] = []
    TransformationResult(tree, False, dependencies)

# Generated at 2022-06-14 02:40:27.379706
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    from typing import List
    from typed_ast import ast3 as ast

    node = ast.Module()

    res = TransformationResult(tree=node,
                               tree_changed=True,
                               dependencies=['a', 'b', 'c'])

    assert res.tree == node
    assert res.tree_changed is True
    assert res.dependencies == ['a', 'b', 'c']

# Generated at 2022-06-14 02:40:32.838570
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    compilation_result = CompilationResult(
        files=3,
        time=1.3,
        target=(3, 5),
        dependencies=['/path/to/dependency.py']
    )

    assert compilation_result.files == 3
    assert compilation_result.time == 1.3
    assert compilation_result.target == (3, 5)
    assert compilation_result.dependencies == ['/path/to/dependency.py']



# Generated at 2022-06-14 02:40:36.476558
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    "Unit test for constructor of class TransformationResult"
    assert TransformationResult(tree=None, tree_changed=False, dependencies=[])


# Generated at 2022-06-14 02:40:39.833849
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input = Path('/tmp/input.txt')
    output = Path('/tmp/output.txt')
    pair = InputOutput(input, output)
    assert pair.input == input
    assert pair.output == output

# Generated at 2022-06-14 02:40:44.799174
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    #pylint: disable=no-member

    assert TransformationResult(None, None, None)
    assert TransformationResult(None, None, []).dependencies == []
    assert TransformationResult(None, True, []).tree_changed
    assert not TransformationResult(None, False, []).tree_changed



# Generated at 2022-06-14 02:40:46.699299
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    result = CompilationResult(files=2, time=3.0, target=(3, 7),
                               dependencies=['a', 'b'])
    assert result.files == 2
    assert result.time == 3.0
    assert result.target == (3, 7)
    assert result.dependencies == ['a', 'b']


# Generated at 2022-06-14 02:40:50.622378
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree = ast.Expression(ast.Num(42))
    tr = TransformationResult(tree, True, ['module1', 'module2'])
    assert tr.tree == tree
    assert tr.tree_changed is True
    assert tr.dependencies == ['module1', 'module2']

# Generated at 2022-06-14 02:40:52.889636
# Unit test for constructor of class TransformationResult

# Generated at 2022-06-14 02:41:00.963234
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tr = TransformationResult(ast.parse('x = 1'), False, [])
    assert tr


# Special log messages
LogMessage = NamedTuple('LogMessage', [('message', str),
                                       ('file', Path),
                                       ('line', int),
                                       ('column', int),
                                       ('level', str)])


# Generated at 2022-06-14 02:41:03.207796
# Unit test for constructor of class InputOutput
def test_InputOutput():
    inp = Path('/tmp/inp')
    out = Path('/tmp/out')

    io = InputOutput(inp, out)

    assert io.input == inp
    assert io.output == out

# Generated at 2022-06-14 02:41:06.332838
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    assert TransformationResult(None, None, None).tree is None
    assert TransformationResult(None, None, None).tree_changed is None
    assert TransformationResult(None, None, None).dependencies is None

# TODO: create unit test for this class

# Generated at 2022-06-14 02:41:13.608026
# Unit test for constructor of class InputOutput
def test_InputOutput():
    i = InputOutput(Path('/tmp/input'), Path('/tmp/output'))
    assert i.input.name == 'input'
    assert i.output.name == 'output'
    assert str(i.input) == '/tmp/input'
    assert str(i.output) == '/tmp/output'


# Generated at 2022-06-14 02:41:17.677617
# Unit test for constructor of class InputOutput
def test_InputOutput():
    in_path = Path('/tmp/in.py')
    out_path = Path('/tmp/out.py')
    io = InputOutput(input=in_path, output=out_path)

    assert io.input == in_path
    assert io.output == out_path

# Generated at 2022-06-14 02:41:22.818863
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input_path = Path('.')
    output_path = Path('..')
    input_output = InputOutput(input_path, output_path)
    assert input_output.input == input_path
    assert input_output.output == output_path


# Generated at 2022-06-14 02:41:27.991395
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    r = TransformationResult(None, True, ['a', 'b'])
    assert r.tree is None
    assert r.tree_changed is True
    assert r.dependencies == ['a', 'b']

# Generated at 2022-06-14 02:41:31.410232
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input = Path('.')
    output = Path('.')
    io = InputOutput(input, output)

    assert io.input, input
    assert io.output, output

# Generated at 2022-06-14 02:41:36.439156
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    i = 5
    t = 0.1
    target = (3, 9)
    dep = ['a', 'b']
    res = CompilationResult(i, t, target, dep)
    assert res.files == i
    assert res.time == t
    assert res.target == target
    assert res.dependencies == dep



# Generated at 2022-06-14 02:41:40.861388
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree = ast.Module()
    tree_changed = False
    dependencies = []
    result = TransformationResult(ast.AST,
                                  tree_changed,
                                  dependencies)
    assert (result.tree == tree)
    assert (result.tree_changed == tree_changed)

# Generated at 2022-06-14 02:41:45.471506
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input_output = InputOutput(Path('input.py'), Path('output.py'))
    assert input_output.input == Path('input.py')


# Generated at 2022-06-14 02:41:48.832973
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    assert TransformationResult(ast.parse('pass'), True, []).tree_changed
    assert TransformationResult(ast.parse('pass'), False, []).tree_changed is False
    assert TransformationResult(ast.parse('pass'), True, ['f1']) \
           .dependencies == ['f1']


# Generated at 2022-06-14 02:41:51.841041
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    assert TransformationResult(ast.parse('pass'), True, []).tree_changed == True
    assert TransformationResult(ast.parse('pass'), False, []).tree_changed == False
    assert TransformationResult(ast.parse('pass'), True, ['a', 'b']).dependencies == ['a', 'b']

# Generated at 2022-06-14 02:41:56.167254
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tr = TransformationResult(ast.AST(), False, ['path'])
    assert type(tr) is TransformationResult
    assert tr.tree is not None
    assert tr.tree_changed == False
    assert tr.dependencies == ['path']

# Generated at 2022-06-14 02:41:58.231966
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    assert TransformationResult(tree=None,
                                tree_changed=False,
                                dependencies=None) is not None

# Generated at 2022-06-14 02:42:09.137696
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    assert CompilationResult(files=1, time=2.0, target=(3, 4), dependencies=['a']) == CompilationResult(files=1, time=2.0, target=(3, 4), dependencies=['a'])
    assert CompilationResult(files=1, time=2.0, target=(3, 4), dependencies=['a']) != CompilationResult(files=1, time=2.0, target=(3, 5), dependencies=['a'])
    assert CompilationResult(files=1, time=2.0, target=(3, 4), dependencies=['a']) != CompilationResult(files=1, time=2.0, target=(3, 4), dependencies=['b'])
    assert CompilationResult(files=1, time=2.0, target=(3, 4), dependencies=['a']) != Compilation

# Generated at 2022-06-14 02:42:11.353575
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    from tempfile import mkstemp
    from os import remove
    from os.path import basename

    _, input_path = mkstemp(suffix='.py')

# Generated at 2022-06-14 02:42:14.044805
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input = Path('foo.py')
    output = Path('bar.py')
    input_output = InputOutput(input, output)
    assert input_output.input == input
    assert input_output.output == output

# Generated at 2022-06-14 02:42:15.783815
# Unit test for constructor of class InputOutput
def test_InputOutput():
    i = Path.cwd()
    o = Path.home()
    _ = InputOutput(input=i, output=o)

# Generated at 2022-06-14 02:42:22.140939
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    ast_tree = ast.parse('a = 1\n')
    ast_tree_changed = True
    ast_dependencies = []
    transform_result = TransformationResult(
        tree=ast_tree,
        tree_changed=ast_tree_changed,
        dependencies=ast_dependencies
    )
    assert transform_result.tree == ast_tree
    assert transform_result.tree_changed == ast_tree_changed
    assert transform_result.dependencies == ast_dependencies

# Generated at 2022-06-14 02:42:28.112215
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    ast_tree = ast.parse('1 + 2')
    result = TransformationResult(tree=ast_tree,
                                  tree_changed=True,
                                  dependencies=['f1.py', 'f2.py'])
    assert result.tree == ast_tree
    assert result.tree_changed == True
    assert result.dependencies == ['f1.py', 'f2.py']

# Generated at 2022-06-14 02:42:30.006234
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    TransformationResult(ast.parse('x = 1'), False, [])


# Generated at 2022-06-14 02:42:36.417489
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree = ast.parse('a = 1')
    result = TransformationResult(tree, False, [])
    assert isinstance(result.tree, ast.AST)
    assert isinstance(result.tree_changed, bool)
    assert isinstance(result.dependencies, list)
    assert result.tree == tree
    assert result.tree_changed == False
    assert result.dependencies == []

# Generated at 2022-06-14 02:42:46.313886
# Unit test for constructor of class TransformationResult
def test_TransformationResult():  # type: () -> None
    import sys
    import time

    assert TransformationResult(tree=None, tree_changed=False, dependencies=[]).tree is None
    assert TransformationResult(tree=None, tree_changed=False, dependencies=[]).tree_changed is False
    assert TransformationResult(tree=None, tree_changed=False, dependencies=[]).dependencies == []

    dummy_tree = ast.Module([ast.Import(names=[ast.alias(name="", asname=None)])])
    assert TransformationResult(tree=dummy_tree, tree_changed=False, dependencies=[]).tree is dummy_tree
    assert TransformationResult(tree=dummy_tree, tree_changed=False, dependencies=[]).tree_changed is False
    assert TransformationResult(tree=dummy_tree, tree_changed=False, dependencies=[]).dependencies == []

# Generated at 2022-06-14 02:42:49.765839
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    result = CompilationResult(files=1,
                               time=0.0,
                               target=(3, 5),
                               dependencies=[])
    assert result.files == 1
    assert result.time == 0.0
    assert result.target == (3, 5)
    assert result.dependencies == []


# Generated at 2022-06-14 02:42:55.463010
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    result = CompilationResult(files=1,
                               time=2,
                               target=(3, 4),
                               dependencies=['dependency1', 'dependency2'])

    assert result[0] == 1
    assert result[1] == 2
    assert result[2] == (3, 4)
    assert result[3] == ['dependency1', 'dependency2']


# Generated at 2022-06-14 02:43:00.632886
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    cre = CompilationResult(files=1,
                            time=10.0,
                            target=(3, 7),
                            dependencies=['a', 'b', 'c'])
    assert cre.files == 1
    assert cre.time == 10.0
    assert cre.target == (3, 7)
    assert cre.dependencies == ['a', 'b', 'c']


# Generated at 2022-06-14 02:43:05.121976
# Unit test for constructor of class TransformationResult
def test_TransformationResult():  # type: () -> None
    t = ast.parse("x = 1")
    res = TransformationResult(t, True, ["dep1"])
    assert res.tree == t
    assert res.tree_changed
    assert res.dependencies == ["dep1"]

# Generated at 2022-06-14 02:43:08.492601
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input_ = Path('input')
    output = Path('output')
    pair = InputOutput(input_, output)

    assert(pair.input == input_)
    assert(pair.output == output)

# Generated at 2022-06-14 02:43:11.588017
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input = Path('/tmp/file.py')
    output = Path('/tmp/file.pyc')
    pair = InputOutput(input, output)
    assert pair.input == input
    assert pair.output == output

# Generated at 2022-06-14 02:43:21.096459
# Unit test for constructor of class InputOutput
def test_InputOutput():
    i = 'a'
    o = 'b'
    obj = InputOutput(i, o)
    assert(obj.input == i)
    assert(obj.output == o)

# Generated at 2022-06-14 02:43:23.450436
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree = ast.parse('pass')
    tr = TransformationResult(tree, True, [])
    assert tr.tree_changed

# Generated at 2022-06-14 02:43:27.111458
# Unit test for constructor of class InputOutput
def test_InputOutput():
    path = Path('.')
    input_output = InputOutput(input=path,
                               output=path)
    assert input_output.input == path
    assert input_output.output == path

# Generated at 2022-06-14 02:43:28.822558
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    # pylint: disable=unused-variable
    TransformationResult(tree=None, tree_changed=False, dependencies=[])

# Generated at 2022-06-14 02:43:32.170863
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    t = ast.Name(id='foobar', ctx=ast.Load())
    tr = TransformationResult(tree=t, tree_changed=False, dependencies=[])

    assert tr.tree == t
    assert tr.tree_changed == False
    assert tr.dependencies == []


# Helper function to convert input/output pair to string

# Generated at 2022-06-14 02:43:37.064583
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    cr = CompilationResult(10, 0.3, (3, 5), ["foo"])
    assert cr.files == 10
    assert cr.time == 0.3
    assert cr.target == (3, 5)
    assert cr.dependencies == ["foo"]


# Generated at 2022-06-14 02:43:42.114973
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input_output = InputOutput(Path('input'), Path('output'))
    assert isinstance(input_output, InputOutput)
    assert isinstance(input_output.input, Path)
    assert isinstance(input_output.output, Path)
    assert input_output.input == Path('input')
    assert input_output.output == Path('output')

# Generated at 2022-06-14 02:43:47.514722
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    ret = CompilationResult(4, 13.4, (3, 6), ['a', 'b'])
    assert ret.files == 4
    assert ret.time == 13.4
    assert ret.target == (3, 6)
    assert ret.dependencies == ['a', 'b']



# Generated at 2022-06-14 02:43:49.161166
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    t = ast.parse("3")
    TransformationResult(t, True, ["a", "b"])

# Generated at 2022-06-14 02:43:50.024228
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    pass


# Generated at 2022-06-14 02:44:01.969336
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    cr = CompilationResult(files=123, time=2.1, target=(2, 7),
                           dependencies=['abc', 'def'])
    assert(cr.files == 123)
    assert(cr.time == 2.1)
    assert(cr.target == (2, 7))
    assert(cr.dependencies == ['abc', 'def'])


# Generated at 2022-06-14 02:44:06.146011
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    assert TransformationResult(ast.Module(), False, []).tree_changed == False
    assert TransformationResult(ast.Module(), False, []).dependencies == []
    assert TransformationResult(ast.Module(), False, []).tree == ast.Module()

# Generated at 2022-06-14 02:44:10.243557
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input = Path('input.py')
    output = Path('output.py')

    assert InputOutput(input, output).input == input
    assert InputOutput(input, output).output == output


# Generated at 2022-06-14 02:44:14.499601
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    result = CompilationResult(files=0, time=0, target=(3, 5), dependencies=[])
    assert result.files == 0
    assert result.time == 0
    assert result.target == (3, 5)
    assert result.dependencies == []


# Generated at 2022-06-14 02:44:17.571830
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    # Empty tuple
    CompilationResult()

    # Full tuple
    CompilationResult(files=1, time=0.1, target=(3, 6), dependencies=['a'])


# Generated at 2022-06-14 02:44:20.785344
# Unit test for constructor of class InputOutput
def test_InputOutput():
    """
    :return:
    """
    input_output = InputOutput(Path('file1'), Path('file2'))
    assert input_output.input == Path('file1')
    assert input_output.output == Path('file2')

# Generated at 2022-06-14 02:44:24.484067
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    assert TransformationResult(ast.parse('3 + 5'),
                                False,
                                [])
    assert TransformationResult(ast.parse('3 + 5'),
                                True,
                                [])
    assert TransformationResult(ast.parse('3 + 5'),
                                False,
                                ['x'])

# Generated at 2022-06-14 02:44:29.251394
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input_ = Path('/a/b/c/file.txt')
    output = Path('/a/b/c/file.py')
    result = InputOutput(input_, output)
    assert result.input == input_
    assert result.output == output


# Generated at 2022-06-14 02:44:33.013104
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    # type: () -> None
    """
    Unit test for constructor of class TransformationResult.
    """
    import pytest

    tree = ast.parse('a = 0')
    with pytest.raises(TypeError):
        TransformationResult('tree', 'tree_changed', 'dependencies')
        TransformationResult('tree', 'tree_changed', ['dependencies'])
        TransformationResult(tree, 'tree_changed', ['dependencies'])
        TransformationResult(tree, False, 'dependencies')


# Generated at 2022-06-14 02:44:34.108741
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    assert CompilationResult(9, 0, (3, 8), [])


# Generated at 2022-06-14 02:44:50.203916
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    result = TransformationResult(
        tree=ast.AST(),
        tree_changed=False,
        dependencies=['foo', 'bar']
    )
    assert result.tree
    assert not result.tree_changed
    assert result.dependencies == ['foo', 'bar']



# Generated at 2022-06-14 02:44:54.703753
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    res = CompilationResult(files=0, time=0.0, target=(3, 6),
                            dependencies=['a.py'])
    assert res.files == 0
    assert res.time == 0.0
    assert res.target == (3, 6)
    assert res.dependencies == ['a.py']

# Generated at 2022-06-14 02:44:58.862458
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input = Path('a')
    output = Path('b')
    result = InputOutput(input, output)
    assert result.input == input
    assert result.output == output

# Generated at 2022-06-14 02:45:04.084470
# Unit test for constructor of class InputOutput
def test_InputOutput():
    inp = Path("inp")
    oup = Path("oup")
    iop = InputOutput(inp, oup)
    assert iop.input == inp
    assert iop.output == oup

# Generated at 2022-06-14 02:45:08.470315
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    result = TransformationResult(tree=None, tree_changed=False,
                                  dependencies=[])
    assert result.tree is None
    assert not result.tree_changed
    assert result.dependencies == []

# Generated at 2022-06-14 02:45:13.601356
# Unit test for constructor of class InputOutput
def test_InputOutput():
    path1 = Path('/')
    path2 = Path('/')
    assert path1 is path2
    pair = InputOutput(path1, path2)
    assert pair.input is path1
    assert pair.output is path2


# Generated at 2022-06-14 02:45:16.785663
# Unit test for constructor of class TransformationResult
def test_TransformationResult():  # type: () -> None
    tree = ast.parse('pass')
    result = TransformationResult(tree, True, [])
    assert result.tree_changed == True
    assert result.dependencies == []
    assert result.tree == ast.parse('pass')

# Generated at 2022-06-14 02:45:21.018791
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    input = CompilationResult(files=1, time=0.1, target=(2, 7), dependencies=[])
    assert input.files == 1
    assert input.time == 0.1
    assert input.target == (2, 7)
    assert input.dependencies == []


# Generated at 2022-06-14 02:45:23.188912
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input = Path('/tmp/input')
    output = Path('/tmp/output')
    input_output = InputOutput(input, output)
    assert input_output.input == input
    assert input_output.output == output


# Generated at 2022-06-14 02:45:24.944117
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree = ast.parse('x=1')
    result = TransformationResult(tree, False, [])
    assert result is not None

# Generated at 2022-06-14 02:45:57.058885
# Unit test for constructor of class InputOutput
def test_InputOutput():
    assert InputOutput(Path('input'), Path('output')) == \
        InputOutput(Path('input'), Path('output'))
    assert InputOutput(Path('input'), Path('output')) != \
        InputOutput(Path('input'), Path('output2'))
    assert InputOutput(Path('input'), Path('output')) != \
        InputOutput(Path('input2'), Path('output'))


# Generated at 2022-06-14 02:46:01.546463
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    # Given
    dependencies = ['abc', 'xyz']
    input = "a = 1\n"
    tree = ast.parse(input, '<test>', 'exec')

    # When
    result = TransformationResult(tree=tree, tree_changed=True,
                                  dependencies=dependencies)

    # Then
    assert result.tree == tree
    assert result.tree_changed == True
    assert result.dependencies == dependencies

# Generated at 2022-06-14 02:46:09.349557
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    c = CompilationResult(files=1, time=1.0,
                          target=(3, 5),
                          dependencies=['/path/to/file'])
    assert c.files == 1
    assert c.time == 1.0
    assert c.target == (3, 5)
    assert c.dependencies[0] == '/path/to/file'

# Addition of two CompilationResult objects

# Generated at 2022-06-14 02:46:13.552096
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input_path = Path('input')
    output_path = Path('output')
    iop = InputOutput(input_path, output_path)
    assert iop.input == input_path
    assert iop.output == output_path


# Generated at 2022-06-14 02:46:20.395716
# Unit test for constructor of class InputOutput
def test_InputOutput():
    assert InputOutput(Path('foo'), Path('bar')) == InputOutput(Path('foo'), Path('bar'))
    assert InputOutput(Path('foo'), Path('bar')) != InputOutput(Path('foo'), Path('foo'))
    assert InputOutput(Path('foo'), Path('bar')) != InputOutput(Path('bar'), Path('bar'))
    assert InputOutput(Path('foo'), Path('bar')) != InputOutput(Path('bar'), Path('foo'))

# Generated at 2022-06-14 02:46:24.714050
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    dummy_deps = ['a.py', 'b.py']
    dummy_tree = ast.parse('1+1')
    result = TransformationResult(tree=dummy_tree, tree_changed=False, dependencies=dummy_deps)
    assert(result.tree is dummy_tree)
    assert(result.tree_changed is False)
    assert(result.dependencies is dummy_deps)

# Generated at 2022-06-14 02:46:34.450378
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input = Path("input.py")
    output = Path("output.py")
    assert InputOutput(input, output) == (InputOutput(input, output))
    assert InputOutput(input, output) != (InputOutput(input, input))
    assert InputOutput(input, output) != (InputOutput(output, output))
    assert InputOutput(input, output) != (InputOutput(output, input))
    assert InputOutput(input, output) != (CompilationResult(1, 1.0, (3, 7), ['']))

# Generated at 2022-06-14 02:46:35.888638
# Unit test for constructor of class InputOutput
def test_InputOutput():
    import pytest
    with pytest.raises(TypeError):
        InputOutput('', '')

# Generated at 2022-06-14 02:46:38.932486
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    CompilationResult(1, 1.0, (0, 0), [])


# Generated at 2022-06-14 02:46:41.908941
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree_changed = False
    dependencies = []

    tr1 = TransformationResult(ast.AST(), tree_changed, dependencies)
    tr2 = TransformationResult(ast.AST(), tree_changed, dependencies)

    assert tr1 == tr2
    assert tr1.tree_changed == tree_changed
    assert tr1.dependencies == dependencies

# Generated at 2022-06-14 02:47:38.949685
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input = Path('input')
    output = Path('output')
    assert InputOutput(input, output).input == input
    assert InputOutput(input, output).output == output

# Generated at 2022-06-14 02:47:44.441864
# Unit test for constructor of class CompilationResult
def test_CompilationResult():

    # Zero files
    CompilationResult(0, 1.0, (3, 6), ['file.py'])

    # Custom target
    CompilationResult(0, 1.0, (3, 7), [])

    # Empty dependencies
    CompilationResult(0, 1.0, (3, 7), [])

    # Custom dependencies
    CompilationResult(0, 1.0, (3, 7), ['file1.py', 'file2.py'])

# Generated at 2022-06-14 02:47:51.714378
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    # Type check
    CompilationResult(1, 1.0, (3,6), ['abc'])  # OK
    #CompilationResult(1, 1.0, (3,6), ['abc'], 1)  # TypeError
    #CompilationResult(1, 1.0, (3,6))  # TypeError
    #CompilationResult(1, 1)  # TypeError
    #CompilationResult(1)  # TypeError
    #CompilationResult()  # TypeError


# Generated at 2022-06-14 02:48:00.753563
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    # Instance that has zero values
    result_zero = CompilationResult(0, 0.0, (0, 0), [])
    # Instance that has non-zero values
    result_nonzero = CompilationResult(1, 0.1, (2, 3), ['a'])

    assert result_zero.files == 0
    assert result_zero.time == 0.0
    assert result_zero.target == (0, 0)
    assert len(result_zero.dependencies) == 0

    assert result_nonzero.files == 1
    assert result_nonzero.time == 0.1
    assert result_nonzero.target == (2, 3)
    assert len(result_nonzero.dependencies) == 1
    assert result_nonzero.dependencies[0] == 'a'


# Generated at 2022-06-14 02:48:06.201901
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    c = CompilationResult(1, 2.0, (3, 4), ['a', 'b', 'c'])
    assert c.files == 1
    assert c.time == 2.0
    assert c.target == (3, 4)
    assert c.dependencies == ['a', 'b', 'c']


# Generated at 2022-06-14 02:48:08.774529
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input = Path("path/to/input.py")
    output = Path("path/to/output.py")
    iop = InputOutput(input, output)
    assert isinstance(iop.input, Path)
    assert isinstance(iop.output, Path)
    assert iop.input == input
    assert iop.output == output

# Generated at 2022-06-14 02:48:13.519889
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    assert TransformationResult(ast.parse('pass'), False, []).tree_changed == False

# Result of evaluation of a target class
TargetResult = NamedTuple('TargetResult', [('result', CompilationResult),
                                           ('target', CompilationTarget),
                                           ('files', List[Path])])


# Generated at 2022-06-14 02:48:21.473576
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    # GIVEN: any AST and some change flag
    node = ast.parse('42')
    changed = True
    try:
        # WHEN: creating a TransformationResult instance
        TransformationResult(node, changed, [])
    except TypeError:
        # THEN: fail
        assert False, 'Failed to create TransformationResult object'
    except Exception:
        # THEN: fail
        assert False, 'Should not reach this point'

# Test for the constructor of class TransformationResult

# Generated at 2022-06-14 02:48:26.268465
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    result = CompilationResult(4, 3.14, (3, 6), ['py.typed', 'typed_ast.ast3'])
    assert result.files == 4
    assert result.time == 3.14
    assert result.target == (3, 6)
    assert result.dependencies == ['py.typed', 'typed_ast.ast3']

# Generated at 2022-06-14 02:48:27.814727
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    CompilationResult(files=10, time=0.01,
                      target=(3, 5), dependencies=[])
