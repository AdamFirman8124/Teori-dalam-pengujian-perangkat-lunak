

# Generated at 2022-06-14 02:39:02.750831
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    compilation_result = CompilationResult(2, 3.0, (3, 4), ['test_dep_1', 'test_dep_2'])
    assert compilation_result.files == 2
    assert round(compilation_result.time, 1) == 3.0
    assert compilation_result.target == (3, 4)
    assert compilation_result.dependencies == ['test_dep_1', 'test_dep_2']



# Generated at 2022-06-14 02:39:04.945360
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    CompilationResult(files=1, time=0.1, target=(3, 7), dependencies=['a', 'b'])


# Generated at 2022-06-14 02:39:09.612884
# Unit test for constructor of class InputOutput
def test_InputOutput():
    assert InputOutput(Path('path/to/input.py'),
                       Path('path/to/output.py')).input == \
                       Path('path/to/input.py')
    assert InputOutput(Path('path/to/input.py'),
                       Path('path/to/output.py')).output == \
                       Path('path/to/output.py')

# Generated at 2022-06-14 02:39:12.828622
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    cr = CompilationResult(1, 1.0, (3, 7), [])
    assert cr.files == 1
    assert cr.time == 1.0
    assert cr.target == (3, 7)
    assert cr.dependencies == []


# Generated at 2022-06-14 02:39:18.572780
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    compilation_result = CompilationResult(files=1, time=0.1,
                                           target=(3, 4),
                                           dependencies=[])

    assert compilation_result.files == 1
    assert compilation_result.time == 0.1
    assert compilation_result.target == (3, 4)
    assert compilation_result.dependencies == []


# Generated at 2022-06-14 02:39:22.778668
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    result = TransformationResult(
        ast.AST(),
        True,
        ['a', 'b'])

    assert result.tree is not None
    assert result.tree_changed == True
    assert type(result.dependencies) == list
    assert len(result.dependencies) == 2
    assert result.dependencies[0] == 'a'



# Generated at 2022-06-14 02:39:23.782127
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    assert TransformationResult(ast.AST(), False, [])

# Generated at 2022-06-14 02:39:27.960621
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    r = CompilationResult(files = 0, time = 0.0, target = (3, 4),
                          dependencies = [])
    assert r.files == 0
    assert r.time == 0.0
    assert r.target == (3, 4)
    assert r.dependencies == []


# Generated at 2022-06-14 02:39:30.701095
# Unit test for constructor of class InputOutput
def test_InputOutput():
    assert InputOutput(Path('/tmp/foo'), Path('/tmp/bar')) == \
            InputOutput(input=Path('/tmp/foo'), output=Path('/tmp/bar'))


# Generated at 2022-06-14 02:39:35.104429
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    r = CompilationResult(files=1, time=2, target=(3, 4), dependencies=[])
    assert r.files == 1
    assert r.time == 2
    assert r.target == (3, 4)
    assert r.dependencies == []


# Generated at 2022-06-14 02:39:40.678558
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    foo = CompilationResult(0, 'a', (1, 2), [])
    assert foo.files == 0
    assert foo.time == 'a'
    assert foo.target == (1, 2)
    assert foo.dependencies == []

# class CompilationResult

# Generated at 2022-06-14 02:39:42.580103
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    assert CompilationResult(files=0,
                             time=100.0,
                             target=(2, 7),
                             dependencies=['a.py'])



# Generated at 2022-06-14 02:39:45.968427
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree = ast.parse('a = 3')
    result = TransformationResult(tree, True, [])
    assert result.tree == tree
    assert result.tree_changed
    assert not result.dependencies

# Generated at 2022-06-14 02:39:48.610901
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input_output = InputOutput('input', 'output')
    assert input_output.input == Path('input')
    assert input_output.output == Path('output')



# Generated at 2022-06-14 02:39:52.195927
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    cr = CompilationResult(files=1, time=1, target=(3, 8), dependencies=['a', 'b'])
    assert cr.files == 1
    assert cr.time == 1
    assert cr.target == (3, 8)
    assert cr.dependencies == ['a', 'b']


# Generated at 2022-06-14 02:39:53.955499
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    _ = CompilationResult(0, 0, (0, 0), [''])



# Generated at 2022-06-14 02:40:03.171205
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    assert not TransformationResult(ast.parse('1'), False, [])
    assert TransformationResult(ast.parse('1'), False, []) != TransformationResult(ast.parse('1'), True, [])
    assert TransformationResult(ast.parse('1'), False, []) != TransformationResult(ast.parse('1'), False, ['t.py'])
    assert TransformationResult(ast.parse('_'), True, []) != TransformationResult(ast.parse('1'), True, [])

# This is a restricted version of Cython Lib/site-packages/Cython/Build/Dependencies.py._p_cythonize_dependencies
# returning just a set of dependencies.

# Generated at 2022-06-14 02:40:04.609434
# Unit test for constructor of class InputOutput
def test_InputOutput():
    assert InputOutput(Path(__file__), Path(__file__))


# Generated at 2022-06-14 02:40:12.667840
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    from datetime import datetime
    from time import time

    dt = datetime.now()
    nanotime = time()
    result = CompilationResult(files=5, time=nanotime, target=(3, 6), dependencies=[])
    assert isinstance(result, CompilationResult)
    assert result.files == 5
    assert result.time == nanotime
    assert result.target == (3, 6)
    assert isinstance(result.dependencies, list)
    assert isinstance(str(result), str)
    assert isinstance(repr(result), str)
    assert len(result) == 4
    assert result[0] == 5
    assert result[1] == nanotime
    assert result[2] == (3, 6)
    assert result[3] == []


# Generated at 2022-06-14 02:40:14.564472
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    CompilationResult(files=10, time=100.0, target=(3, 8), dependencies=[])


# Generated at 2022-06-14 02:40:25.930990
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    target = (3, 8)
    tree = ast.parse("print('Hello')")
    result = CompilationResult(files=1,
                               time=3.14,
                               target=target,
                               dependencies=['foo.py', 'bar.py'])
    assert result.files == 1
    assert result.time == 3.14
    assert result.target == target
    assert result.dependencies == ['foo.py', 'bar.py']


# Generated at 2022-06-14 02:40:28.839893
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input_ = Path('input')
    output_ = Path('output')
    io = InputOutput(input_, output_)
    assert io.input == input_
    assert io.output == output_

# Generated at 2022-06-14 02:40:33.328273
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input = Path('./a')
    output = Path('./b')
    assert InputOutput(input, output) == InputOutput(input, output)
    assert InputOutput(input, output) != InputOutput(output, input)
    assert InputOutput(input, output) != InputOutput(input, input)
    assert InputOutput(input, output) != InputOutput(output, output)


# Generated at 2022-06-14 02:40:39.406274
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    result = CompilationResult(files=10,
                               time=20,
                               target=(3, 6),
                               dependencies=['a', 'b'])

    assert result.files == 10
    assert result.time == 20
    assert result.target == (3, 6)
    assert result.dependencies == ['a', 'b']


# Generated at 2022-06-14 02:40:43.056680
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    a = CompilationResult(0, 42, (1, 0), [])
    b = CompilationResult(0, 42, (1, 0), [])
    assert a == b


# Generated at 2022-06-14 02:40:44.944245
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    CompilationResult(1, 1.0, (3, 4), ['a', 'b'])


# Generated at 2022-06-14 02:40:46.992035
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    CompilationResult(1, 2.0, (3, 4), ["dep1", "dep2"])


# Generated at 2022-06-14 02:40:51.545289
# Unit test for constructor of class CompilationResult
def test_CompilationResult():  # type: () -> None
    assert CompilationResult(files=1,
                             time=1.0,
                             target=(3, 5),
                             dependencies=['1']) == CompilationResult(files=1,
                                                                        time=1.0,
                                                                        target=(3, 5),
                                                                        dependencies=['1'])


# Generated at 2022-06-14 02:41:00.712275
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    # default values
    comp_result = CompilationResult(files=10, time=3.14, target=(3, 6),
                                    dependencies=[])
    assert comp_result.files == 10
    assert comp_result.time == 3.14
    assert comp_result.target == (3, 6)
    assert comp_result.dependencies == []

    # custom values
    comp_result = CompilationResult(files=11, time=3.15, target=(3, 4),
                                    dependencies=['new.py'])
    assert comp_result.files == 11
    assert comp_result.time == 3.15
    assert comp_result.target == (3, 4)
    assert comp_result.dependencies == ['new.py']


# Generated at 2022-06-14 02:41:04.290576
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    assert CompilationResult(1, 2.0, (0, 0), []) == CompilationResult(1, 2.0, (0, 0), [])


# Generated at 2022-06-14 02:41:17.370825
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    result = CompilationResult(1, 2.0, (3, 4), ['a', 'b'])

    assert result.files == 1
    assert result.time == 2.0
    assert result.target == (3, 4)
    assert result.dependencies == ['a', 'b']


# Generated at 2022-06-14 02:41:19.827686
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    assert TransformationResult(ast.AST(), True, [])
    assert TransformationResult(ast.AST(), True, []).tree_changed
    assert TransformationResult(ast.AST(), False, [])
    assert not TransformationResult(ast.AST(), False, []).tree_changed

# Generated at 2022-06-14 02:41:25.465302
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    result = CompilationResult(2, 3.0, (2, 1), ['dep1', 'dep2'])
    assert result.files == 2
    assert result.time == 3.0
    assert result.target == (2, 1)
    assert result.dependencies == ['dep1', 'dep2']


# Generated at 2022-06-14 02:41:37.955683
# Unit test for constructor of class CompilationResult
def test_CompilationResult(): # type: () -> None
    cr = CompilationResult(files=1,
                           time=2.0,
                           target=(3, 4),
                           dependencies=['a', 'b'])
    assert cr.files == 1
    assert cr.time == 2.0
    assert cr.target == (3, 4)
    assert cr.dependencies == ['a', 'b']
    assert repr(cr) == ("CompilationResult"
                        "(files=1, "
                        "time=2.0, "
                        "target=(3, 4), "
                        "dependencies=['a', 'b'])")


# Generated at 2022-06-14 02:41:40.580319
# Unit test for constructor of class InputOutput
def test_InputOutput():
    i = Path('/home/test/test.py')
    o = Path('/home/test/test_out.py')
    InputOutput(i, o)

# Generated at 2022-06-14 02:41:47.872644
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    source_tree = ast.parse('a=1')
    source_tree_changed = True
    source_dependencies = []
    res = TransformationResult(source_tree, source_tree_changed, source_dependencies)  # noqa
    assert res.tree is source_tree
    assert res.tree_changed is source_tree_changed
    assert res.dependencies is source_dependencies


# Result of transformation of one file
FileResult = NamedTuple('FileResult',
                        [('source_file', str),
                         ('target_file', str),
                         ('time', float),
                         ('tree_changed', bool)])



# Generated at 2022-06-14 02:41:50.353572
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree = ast.parse('a=0')
    res = TransformationResult(tree, True, ['a/b.py'])
    assert isinstance(res.tree, ast.AST)
    assert res.dependencies == ['a/b.py']

# Generated at 2022-06-14 02:41:52.350378
# Unit test for constructor of class InputOutput
def test_InputOutput():
    assert InputOutput(Path('/tmp/a'), Path('/tmp/b')) is not None

# Generated at 2022-06-14 02:41:59.600804
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    result = CompilationResult(files=1,
                               time=2.0,
                               target=(3, 4),
                               dependencies=['some.py'])
    result.files
    result.time
    result.target
    result.dependencies

    assert result.files == 1
    assert result.time == 2.0
    assert result.target == (3, 4)
    assert result.dependencies == ['some.py']

# Generated at 2022-06-14 02:42:00.795953
# Unit test for constructor of class InputOutput
def test_InputOutput():
    assert InputOutput(1, 2) == (1, 2)


# Generated at 2022-06-14 02:42:21.167878
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    result = CompilationResult(5, 3.5, (2, 7), [])
    assert isinstance(result, CompilationResult)

# Generated at 2022-06-14 02:42:25.957437
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    result = CompilationResult(files=1,
                               time=0,
                               target=(3, 7),
                               dependencies=['foo', 'bar'])
    assert result.files == 1
    assert result.time == 0
    assert result.target == (3, 7)
    assert result.dependencies == ['foo', 'bar']

# Generated at 2022-06-14 02:42:29.081860
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree = ast.parse('x = 1')
    tree_changed = True
    dependencies = ['a', 'b']
    TransformationResult(tree, tree_changed, dependencies)

# Generated at 2022-06-14 02:42:42.055961
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    result = [None, None, None]
    result[0] = ast.FunctionDef(name='test', args=ast.arguments(args=[], defaults=[]), body=[], decorator_list=[],
                                returns=None)
    result[1] = True
    result[2] = ["a", "b", "c"]
    tr = TransformationResult(tree=result[0], tree_changed=result[1], dependencies=result[2])

    assert(tr.tree == result[0] == ast.FunctionDef(
        name='test', args=ast.arguments(args=[], defaults=[]), body=[], decorator_list=[], returns=None))

    assert(tr.tree_changed == result[1] == True)

    assert(tr.dependencies == result[2] == ["a", "b", "c"])

# Generated at 2022-06-14 02:42:46.358835
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    dependencies = ["a.py", "b.py", "c.py"]
    r = CompilationResult(files=5, time=0.5, target=(3, 5), dependencies=dependencies)
    assert r.files == 5
    assert r.time == 0.5
    assert r.target == (3, 5)
    assert r.dependencies == dependencies


# Generated at 2022-06-14 02:42:48.965854
# Unit test for constructor of class InputOutput
def test_InputOutput():
    example_input_output = InputOutput(input='/dev/null',
                                       output='/dev/null')
    assert example_input_output.input == '/dev/null'
    assert example_input_output.output == '/dev/null'

# Generated at 2022-06-14 02:42:54.977073
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    assert CompilationResult(1, 2.3, (3, 4), ['foo']).files == 1
    assert CompilationResult(1, 2.3, (3, 4), ['foo']).time == 2.3
    assert CompilationResult(1, 2.3, (3, 4), ['foo']).target == (3, 4)
    assert CompilationResult(1, 2.3, (3, 4), ['foo']).dependencies == ['foo']


# Generated at 2022-06-14 02:43:00.390868
# Unit test for constructor of class InputOutput
def test_InputOutput():
    path_input = Path('input')
    path_output = Path('output')
    x: InputOutput = InputOutput(path_input, path_output)
    assert x.input == path_input
    assert x.output == path_output
    x.input = Path('other')
    x.output = Path('other')
    assert x.input == Path('other')
    assert x.output == Path('other')

# Generated at 2022-06-14 02:43:07.145795
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    tree = ast.parse('print(42)')
    deps = ['foo', 'bar']
    res = CompilationResult(files=1, time=42.0, target=(3, 5),
                            dependencies=deps)

    assert res.files == 1
    assert res.time == 42.0
    assert res.target == (3, 5)
    assert res.dependencies == deps


# Generated at 2022-06-14 02:43:11.014230
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    cr = CompilationResult(files=1,
                           time=0.1,
                           target=(3, 0),
                           dependencies=['a'])

    assert cr.files == 1
    assert cr.time == 0.1
    assert cr.target == (3, 0)
    assert cr.dependencies == ['a']


# Generated at 2022-06-14 02:43:51.636872
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    from typing import List
    from typed_ast import ast3 as ast
    from .typed_ast_extensions import FunctionDef


# Generated at 2022-06-14 02:43:54.881709
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    # pylint: disable=unused-variable
    cr = CompilationResult(1000, 3.14, (3, 6),
                           ["foo.py", "bar.py"])


# Generated at 2022-06-14 02:43:56.515890
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    assert TransformationResult(tree=None, tree_changed=False, dependencies=[])


# Generated at 2022-06-14 02:44:02.917458
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    a = ast.parse('a + b', filename='a.py', mode='eval')
    r = TransformationResult(tree=a, tree_changed=True, dependencies=[])
    assert str(r) == 'TransformationResult(tree=Expression(body=BinOp(left=Name(id=\'a\', ctx=Load()), op=Add(), right=Name(id=\'b\', ctx=Load()))), tree_changed=True, dependencies=[])'

# Generated at 2022-06-14 02:44:05.311456
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    TransformationResult(
        ast.AST,
        True,
        ['a', 'b', 'c'])

# Generated at 2022-06-14 02:44:08.801990
# Unit test for constructor of class InputOutput
def test_InputOutput():
    i = Path('i')
    o = Path('o')
    io = InputOutput(i, o)
    assert io.input == i
    assert io.output == o


# Generated at 2022-06-14 02:44:11.278383
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tr = TransformationResult(tree=None,
                              tree_changed=False,
                              dependencies=[])

# Generated at 2022-06-14 02:44:19.551859
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input_ = Path("input")
    output = Path("output")
    io = InputOutput(input_, output)

    assert io.input == input_
    assert io.input == "input"
    assert io.output == output
    assert io.output == "output"

    with pytest.raises(AssertionError):
        InputOutput("input", "output")

    with pytest.raises(AssertionError):
        InputOutput(input_, "output")

    io = InputOutput(input_ = "input", output = "output")
    assert io.input == input_
    assert io.output == output

# Generated at 2022-06-14 02:44:23.028780
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    result = CompilationResult(0, 0.0, (3, 5), [])

    assert result.files == 0
    assert result.time == 0.0
    assert result.target == (3, 5)
    assert result.dependencies == []


# Generated at 2022-06-14 02:44:24.780664
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    from typed_ast.ast3 import Module
    assert TransformationResult(tree=Module([], []), tree_changed=True, dependencies=[])

# Generated at 2022-06-14 02:45:13.762314
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    CompilationResult(files=1, time=2, target=(3, 4), dependencies=[])


# Generated at 2022-06-14 02:45:16.949763
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    result = TransformationResult(ast.Module(), True, ['foo.py'])
    assert result.tree is not None
    assert result.tree_changed is True
    assert len(result.dependencies) == 1
    assert result.dependencies[0] == 'foo.py'


# Generated at 2022-06-14 02:45:17.732480
# Unit test for constructor of class InputOutput
def test_InputOutput():
    InputOutput(Path('a'), Path('b'))

# Generated at 2022-06-14 02:45:20.698419
# Unit test for constructor of class TransformationResult
def test_TransformationResult():  # type: () -> None
    assert TransformationResult(ast.parse("print('foo');"),
                                True,
                                [])

# Generated at 2022-06-14 02:45:24.592448
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    result = CompilationResult(1, 1.0, (3, 6), ['dependency'])

    assert result.files == 1
    assert result.time == 1.0
    assert result.target == (3, 6)
    assert result.dependencies == ['dependency']


# Generated at 2022-06-14 02:45:29.199678
# Unit test for constructor of class InputOutput
def test_InputOutput():
    i, o = Path('a'), Path('b')
    io = InputOutput(i, o)
    assert io.input == i
    assert io.output == o
    assert io == InputOutput(i, o)
    assert io != InputOutput(i, Path('c'))
    assert io != InputOutput(Path('c'), o)
    assert io != InputOutput(Path('c'), Path('d'))
    assert io != None

# Generated at 2022-06-14 02:45:32.462920
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input_output = InputOutput(Path('input'),
                               Path('output'))
    assert input_output.input == Path('input')
    assert input_output.output == Path('output')


# Generated at 2022-06-14 02:45:36.238080
# Unit test for constructor of class InputOutput
def test_InputOutput():
    assert InputOutput(None, None) == InputOutput(None, None)
    assert InputOutput(3, None) != InputOutput(None, None)
    assert InputOutput(None, None) != InputOutput(None, True)

# Generated at 2022-06-14 02:45:39.005367
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input_ = Path('input.py')
    output = Path('output.py')
    pair = InputOutput(input_, output)
    assert pair.input == input_
    assert pair.output == output



# Generated at 2022-06-14 02:45:42.813870
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input = Path('test.py')
    output = Path('test.pyc')
    obj = InputOutput(input, output)
    print(str(obj))
    print(str(obj.input))
    print(str(obj.output))


# Generated at 2022-06-14 02:47:29.107949
# Unit test for constructor of class InputOutput
def test_InputOutput():
    for p in (Path('/'), Path('')):
        for s in ('/path/to/input', 'path/to/input'):
            for t in ('/path/to/output', 'path/to/output'):
                InputOutput(p / s, p / t)


# Generated at 2022-06-14 02:47:33.249168
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input = Path('foo.py')
    output = Path('baz.py')
    io = InputOutput(input=input, output=output)
    assert io.input == input
    assert io.output == output



# Generated at 2022-06-14 02:47:41.685583
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    """Constructor of TransformationResult"""
    result = TransformationResult(ast.Module(), False, [])
    ok, s = check(result, TransformationResult)
    assert ok, s

# Result of tests
TestResult = NamedTuple('TestResult',
                        [('time', float),
                         ('status', str),
                         ('outcome', str),
                         ('input_path', Path),
                         ('output_path', Path),
                         ('exception', str),
                         ('lexical_analysis', str),
                         ('parse_tree', ast.AST),
                         ('compilation_result', CompilationResult),
                         ('transformation_result', TransformationResult),
                         ('source_code', str),
                         ('input_code', str)])


# Generated at 2022-06-14 02:47:43.996906
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    result = CompilationResult(2, 3.5, (3, 6), ['/home/user/py2py3/module.py'])
    assert result


# Generated at 2022-06-14 02:47:46.802594
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    assert CompilationResult(42, 3.14, (3, 7), ['foo', 'bar']) ==\
           CompilationResult(42, 3.14, (3, 7), ['foo', 'bar'])


# Generated at 2022-06-14 02:47:50.885960
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    t1 = ast.parse('i = 0')
    t2 = ast.parse('i = 0')
    TransformationResult(t1, True, [])
    TransformationResult(t2, False, [])

# Generated at 2022-06-14 02:47:55.664365
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree = ast.parse('x = 1')
    t = TransformationResult(tree, True, [])
    assert t.tree
    assert t.tree_changed is True
    assert t.dependencies == []


# Generated at 2022-06-14 02:47:59.681847
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    assert CompilationResult(3, 2.3, (3, 5), ['foo.py']).target == (3, 5)


# Generated at 2022-06-14 02:48:02.922752
# Unit test for constructor of class InputOutput
def test_InputOutput():
    try:
        InputOutput(Path('a'), Path('b'))
    except Exception as error:
        assert 0, str(error)


# Generated at 2022-06-14 02:48:06.082742
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree = ast.parse("1 + 2", "<test>", "eval")
    tr = TransformationResult(tree, False, [])
    assert tr.tree == tree
    assert tr.tree_changed is False
    assert tr.dependencies == []