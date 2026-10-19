

# Generated at 2022-06-14 02:39:00.955384
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    result = CompilationResult(files = 1, time = 0.0, target = (3, 6), dependencies = [])
    assert result.files == 1
    assert result.time == 0.0
    assert result.target == (3, 6)
    assert result.dependencies == []



# Generated at 2022-06-14 02:39:03.671632
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input = Path('test')
    output = Path('test2')
    pair = InputOutput(input, output)
    assert pair.input == input
    assert pair.output == output

# Generated at 2022-06-14 02:39:05.404405
# Unit test for constructor of class InputOutput
def test_InputOutput():
    assert InputOutput(Path('i'), Path('o')) == InputOutput('i', 'o')

# Generated at 2022-06-14 02:39:07.113037
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    assert TransformationResult(
        ast.Module([]), True, []).tree_changed == True

# Generated at 2022-06-14 02:39:08.667127
# Unit test for constructor of class InputOutput
def test_InputOutput():
    test = InputOutput('input', 'output')
    assert test.input == 'input'
    assert test.output == 'output'


# Generated at 2022-06-14 02:39:13.019342
# Unit test for constructor of class InputOutput
def test_InputOutput():
    p = Path('a.b')
    a = p
    assert InputOutput(p, p)
    assert InputOutput(p, p) == InputOutput(a, a)
    assert InputOutput(p, p) != (p, p)
    assert InputOutput(p, p).input == p
    assert InputOutput(p, p).output == p
    assert InputOutput(p, p).input == a
    assert InputOutput(p, p).output == a


# Generated at 2022-06-14 02:39:17.280007
# Unit test for constructor of class InputOutput
def test_InputOutput():
    assert InputOutput(Path('/a'), Path('/b')) == InputOutput(Path('/a'), Path('/b'))
    assert InputOutput(Path('/a'), Path('/b')) != InputOutput(Path('/b'), Path('/a'))

# Generated at 2022-06-14 02:39:21.479619
# Unit test for constructor of class InputOutput
def test_InputOutput():
    # GIVEN input/output pair
    input = Path('a.py')
    output = Path('a.pyc')
    # WHEN creating instance
    instance = InputOutput(input, output)
    # THEN values are correct
    assert instance.input == input
    assert instance.output == output


# Generated at 2022-06-14 02:39:28.295526
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    # pylint: disable=too-many-function-args
    tree = ast.parse('1 + 2')
    a = TransformationResult(tree, True, ['dependency-a'])
    b = TransformationResult(tree, False, ['dependency-b'])
    c = TransformationResult(tree, False, ['dependency-c'])
    assert a.tree != b.tree
    assert a != b
    assert b == c
    assert b != 'some string'


# Generated at 2022-06-14 02:39:31.445873
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree = ast.parse('x = 5')
    result = TransformationResult(tree, False, [])
    assert result.tree == tree
    assert result.tree_changed == False
    assert result.dependencies == []


# Generated at 2022-06-14 02:39:36.074801
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    result = TransformationResult(ast.Module([], []), False, [])
    assert isinstance(result.tree, ast.AST)
    assert result.tree_changed == False
    assert isinstance(result.dependencies, List)

# Generated at 2022-06-14 02:39:39.855183
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    result = CompilationResult(1, 1.1, (3, 1), ['a', 'b'])
    assert result.files == 1
    assert result.time == 1.1
    assert result.target == (3, 1)
    assert result.dependencies == ['a', 'b']


# Generated at 2022-06-14 02:39:46.954040
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    ast_tree = ast.Module(body=[ast.Expr(value=ast.Num(n=1))])
    result = TransformationResult(tree=ast_tree,
                                  tree_changed=True,
                                  dependencies=[])

    assert result.tree == ast_tree
    assert result.tree_changed == True
    assert result.dependencies == []

# Compilation pipeline
CompilePipeline = NamedTuple('CompilePipeline',
                             [('transformation', TransformationResult),
                              ('compilation', CompilationResult)])

# Compilation with errors
CompileWithErrors = NamedTuple('CompileWithErrors',
                               [('pipeline', CompilePipeline),
                                ('errors', str)])


# Generated at 2022-06-14 02:39:49.281631
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input_obj = Path('tmp')
    output_obj = Path('out')
    io = InputOutput(input_obj, output_obj)
    assert io.input == input_obj
    assert io.output == output_obj
    assert io.input != io.output


# Generated at 2022-06-14 02:39:52.155195
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    r = TransformationResult([1, 2, 3], True, ['a', 'b'])
    assert r.tree == [1, 2, 3]
    assert r.tree_changed is True
    assert r.dependencies == ['a', 'b']

# Generated at 2022-06-14 02:39:58.169775
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    compilation_result = CompilationResult(files=10, time=10.0, target=(3, 6), dependencies=['a', 'b', 'c'])
    assert compilation_result.files == 10
    assert compilation_result.time == 10.0
    assert compilation_result.target == (3, 6)
    assert compilation_result.dependencies == ['a', 'b', 'c']


# Generated at 2022-06-14 02:40:03.565183
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input = Path('/home/stdlib/stdlib.py')
    output = Path('/home/stdlib/stdlib.pyc')
    iop = InputOutput(input=input, output=output)
    assert iop.input == input
    assert iop.output == output
    assert iop.dependencies == []
    assert not iop.tree_changed

# Generated at 2022-06-14 02:40:06.163111
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input = Path('a.py')
    output = Path('b.py')
    io = InputOutput(input, output)
    assert io.input == input
    assert io.output == output

# Generated at 2022-06-14 02:40:09.833964
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    result = CompilationResult(files=1,
                               time=0.0,
                               target=(3, 7),
                               dependencies=[''])
    assert '(' in repr(result)
    assert str(result) == '1 files in 0.0 s, target: python3.7'


# Generated at 2022-06-14 02:40:13.978348
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    # Given
    tree_changed = True
    dependencies = ['foo']

    # When
    transformation_result = TransformationResult(None, tree_changed, dependencies)

    # Then
    assert transformation_result.tree_changed == tree_changed
    assert transformation_result.dependencies == dependencies

# Generated at 2022-06-14 02:40:19.012946
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    files = 2
    time = 0.5
    target = (3, 5)
    dependencies = ['a.py', 'b.py']
    result = CompilationResult(files, time, target, dependencies)
    assert result.files == files
    assert result.time == time
    assert result.target == target
    assert result.dependencies == dependencies


# Generated at 2022-06-14 02:40:25.532049
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    # Create instance TransformationResult
    obj = TransformationResult(tree=ast.parse('pass').body[0],
                               tree_changed=True,
                               dependencies=['foo', 'bar'])

    # Check if instance attributes were correctly set
    assert obj.tree == ast.parse('pass').body[0]
    assert obj.tree_changed == True
    assert obj.dependencies == ['foo', 'bar']

# Testcase of class TransformationResult

# Generated at 2022-06-14 02:40:34.282472
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    assert (CompilationResult(files=100, time=2.0, target=(3, 5),
                              dependencies=['foo', 'bar']).files == 100)
    assert (CompilationResult(files=100, time=2.0, target=(3, 5),
                              dependencies=['foo', 'bar']).time == 2.0)
    assert (CompilationResult(files=100, time=2.0, target=(3, 5),
                              dependencies=['foo', 'bar']).target ==
            (3, 5))
    assert (CompilationResult(files=100, time=2.0, target=(3, 5),
                              dependencies=['foo', 'bar']).dependencies ==
            ['foo', 'bar'])


# Generated at 2022-06-14 02:40:37.640781
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree = ast.AST()
    tr = TransformationResult(tree, True, [])
    assert tr.tree_changed is True
    assert tr.dependencies == []
    assert tr.tree == tree

# Generated at 2022-06-14 02:40:39.693653
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    CompilationResult(1, 0.5, (3, 6), [])


# Generated at 2022-06-14 02:40:45.579925
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    transformation_result = TransformationResult(tree=ast.parse("foo = 'bar'"),
                                                 tree_changed=False,
                                                 dependencies=['file://tmp.py'])
    assert transformation_result.tree is not None
    assert transformation_result.tree_changed is False
    assert len(transformation_result.dependencies) == 1


# Generated at 2022-06-14 02:40:48.499607
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    # tuple of empty tree and empty deps
    tr = TransformationResult(ast.Module([]),
                              True,
                              [])

# Generated at 2022-06-14 02:40:50.185235
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    CompilationResult(1, 1.0, (1, 1), [])


# Generated at 2022-06-14 02:40:55.885372
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input_output = InputOutput(input=Path('a/b.c'), output=Path('b.c'))
    assert isinstance(input_output.input, Path)
    assert isinstance(input_output.output, Path)
    assert input_output.input.is_file()
    assert input_output.output.is_file()

# Generated at 2022-06-14 02:40:57.044601
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    TransformationResult(ast.AST(), False, [])

# Generated at 2022-06-14 02:41:03.774824
# Unit test for constructor of class InputOutput
def test_InputOutput():
    i1 = InputOutput("foo", "bar")
    assert i1.input == "foo"
    assert i1.output == "bar"

    i2 = InputOutput(Path("foo"), Path("bar"))
    assert i2.input == Path("foo")
    assert i2.output == Path("bar")

# Generated at 2022-06-14 02:41:07.634470
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    t = CompilationResult(files=10, time=1, target=(3, 6), dependencies=[])
    assert t.files == 10
    assert t.time == 1
    assert t.target == (3, 6)
    assert t.dependencies == []


# Generated at 2022-06-14 02:41:13.007385
# Unit test for constructor of class InputOutput
def test_InputOutput():
    a = Path('a')
    b = Path('b')
    assert InputOutput(a, b) == InputOutput(a, b)
    assert InputOutput(a, b) != InputOutput(b, a)


# Generated at 2022-06-14 02:41:18.811371
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    cr = CompilationResult(files=2, time=3.4, target=(3, 4), dependencies=[])
    assert type(cr.files) is int
    assert type(cr.time) is float
    assert type(cr.target) is CompilationTarget
    assert type(cr.target[0]) is int
    assert type(cr.target[1]) is int
    assert type(cr.dependencies) is List[str]


# Generated at 2022-06-14 02:41:23.599239
# Unit test for constructor of class InputOutput
def test_InputOutput():
    assert InputOutput("", Path("")) == InputOutput("", "")
    assert InputOutput("", "") == InputOutput(Path(""), "")
    assert InputOutput("", "") == InputOutput(Path(""), Path(""))

# Generated at 2022-06-14 02:41:26.196952
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    transformationResult = TransformationResult(None, False, None)
    assert transformationResult.tree is None
    assert transformationResult.tree_changed is False
    assert transformationResult.dependencies is None


# Environment variables

# Generated at 2022-06-14 02:41:30.434543
# Unit test for constructor of class InputOutput
def test_InputOutput():
    InputOutput_ = InputOutput(Path('./a.py'), Path('./b.py'))
    assert InputOutput_.input == Path('./a.py')
    assert InputOutput_.output == Path('./b.py')

# Generated at 2022-06-14 02:41:33.828282
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    # This test requires the mypy hint
    assert(CompilationResult(5, 3.5, (3, 5), ['a', 'b']) != None)


# Generated at 2022-06-14 02:41:38.093252
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input_path = Path('foo.in')
    output_path = Path('foo.out')
    io = InputOutput(input_path, output_path)
    assert io.input == input_path
    assert io.output == output_path


# Generated at 2022-06-14 02:41:41.884896
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input_output = InputOutput(Path('../a.py'), Path('../a.v.py'))
    assert input_output.input == Path('../a.py')
    assert input_output.output == Path('../a.v.py')


# Generated at 2022-06-14 02:41:53.102522
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    p = Path("#1.py").resolve()
    t = ast.parse("import foo, bar")
    TransformationResult(t, True, ["foo", "bar"])
    TransformationResult(t, False, [])

TransformationResult.__doc__ = """
Result of a transformation.
"""

TransformationResult.tree.__doc__ = """
Abstract syntax tree (AST) of transformed code.
"""

TransformationResult.tree_changed.__doc__ = """
Flag whether AST tree was changed by transformation.
"""

TransformationResult.dependencies.__doc__ = """
List of dependencies added by the transformation.
"""

CompilationResult.__doc__ = """
Result of compilation.
"""

CompilationResult.files.__doc__ = """
Number of source files in compilation.
"""


# Generated at 2022-06-14 02:41:59.638318
# Unit test for constructor of class TransformationResult
def test_TransformationResult():  # type: () -> None
    tr = TransformationResult(tree = ast.Module(body = []), tree_changed = True, dependencies = [])
    assert isinstance(tr.tree, ast.AST)
    assert tr.tree_changed
    assert tr.dependencies == []


# Result of transformers transformation
BuildResult = NamedTuple('BuildResult',
                         [('code', bytes),
                          ('code_changed', bool)])


# Generated at 2022-06-14 02:42:02.928089
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    comp_res = CompilationResult(1, 1.2, (3, 4), ["ab"])

    assert comp_res.files == 1
    assert comp_res.time == 1.2
    assert comp_res.target == (3, 4)
    assert comp_res.dependencies == ["ab"]


# Generated at 2022-06-14 02:42:05.543555
# Unit test for constructor of class InputOutput
def test_InputOutput():
    assert InputOutput(Path('input'), Path('output')) == \
           InputOutput(input=Path('input'), output=Path('output'))

# Generated at 2022-06-14 02:42:08.135167
# Unit test for constructor of class InputOutput
def test_InputOutput():
    assert InputOutput(input="foo", output="bar").input == "foo"
    assert InputOutput(input="foo", output="bar").output == "bar"


# Generated at 2022-06-14 02:42:13.576333
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    # Setup
    transformation_result: TransformationResult = \
        TransformationResult(ast.parse('pass'), False, [])

    # Test
    assert transformation_result.tree is not None
    assert isinstance(transformation_result.tree, ast.AST)
    assert not transformation_result.tree_changed
    assert len(transformation_result.dependencies) == 0

# Generated at 2022-06-14 02:42:16.290824
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input_output = InputOutput(input=Path('in'), output=Path('out'))
    assert input_output.input == Path('in')
    assert input_output.output == Path('out')
    print(input_output)


# Generated at 2022-06-14 02:42:18.802477
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    _ = CompilationResult(files=1, time=2.0, target=(3, 4),
                          dependencies=['a.py', 'b.py'])

# Generated at 2022-06-14 02:42:26.073972
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    res1 = CompilationResult(None, None, None, None)
    res2 = CompilationResult(files=5, time=5.0, target=(3, 6),
                             dependencies=['foo', 'bar'])

    assert res1 == CompilationResult(None, None, None, None)
    assert res1 != res2

    assert res2.files == 5
    assert res2.time == 5.0
    assert res2.target == (3, 6)
    assert res2.dependencies == ['foo', 'bar']



# Generated at 2022-06-14 02:42:31.125414
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input_output = InputOutput('foo.input', 'bar.output')

    assert isinstance(input_output.input, Path)
    assert input_output.input == 'foo.input'

    assert isinstance(input_output.output, Path)
    assert input_output.output == 'bar.output'


# Generated at 2022-06-14 02:42:41.837828
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    assert isinstance(TransformationResult(None, False, None), TransformationResult)

# Generated at 2022-06-14 02:42:43.611582
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    CompilationResult(1, 1.0, (3, 5), ['a', 'b'])

# Generated at 2022-06-14 02:42:48.000446
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input = Path('test.py')
    output = Path('test.pyc')
    io = InputOutput(input, output)
    assert io.input == input
    assert io.output == output
    assert io.input != output
    assert io.output != input
    assert io.input.name == 'test.py'
    assert io.output.name == 'test.pyc'


# Generated at 2022-06-14 02:42:49.724870
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    CompilationResult(files=3,
                      time=2.0,
                      target=(3, 5),
                      dependencies=['some_file.py'])

# Generated at 2022-06-14 02:42:52.360819
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    assert TransformationResult(None, False, None).tree is None
    assert not TransformationResult(None, False, None).tree_changed
    assert TransformationResult(None, False, None).dependencies is None

# Generated at 2022-06-14 02:42:55.164147
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input_output = InputOutput(input='input', output='output')
    assert input_output.input == Path('input')
    assert input_output.output == Path('output')

# Generated at 2022-06-14 02:43:01.702866
# Unit test for constructor of class InputOutput
def test_InputOutput():
    inp = InputOutput(Path("input"), Path("output"))
    assert inp.input == Path("input")
    assert inp.input.name == "input"
    assert inp.output == Path("output")
    assert inp.output.name == "output"

    inp = InputOutput("input", "output")
    assert inp.input == Path("input")
    assert inp.input.name == "input"
    assert inp.output == Path("output")
    assert inp.output.name == "output"

# Generated at 2022-06-14 02:43:09.403835
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree = ast.parse('a + b')
    result = TransformationResult(tree, True, ['a'])
    assert result.tree is tree
    assert result.tree_changed is True
    assert result.dependencies == ['a']


# Result of transformer.visit(tree)
TransformationResult2 = NamedTuple('TransformationResult2',
                                   [('node', ast.Node),
                                    ('node_changed', bool),
                                    ('dependencies', List[str])])


# Generated at 2022-06-14 02:43:14.473201
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input_string = 'path/to/file'
    output_string = 'path/to/otherfile'
    input_path = Path(input_string)
    output_path = Path(output_string)
    input_output = InputOutput(input=input_path, output=output_path)
    assert input_output.input == input_path
    assert input_output.output == output_path


# Generated at 2022-06-14 02:43:20.970377
# Unit test for constructor of class InputOutput
def test_InputOutput():
    d = {'input': Path('foo'), 'output': Path('bar')}
    inout = InputOutput(**d)
    for key, value in d.items():
        assert getattr(inout, key) == value
InputOutput.namedtuple_test = test_InputOutput

# Generated at 2022-06-14 02:43:43.370605
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    root = ast.parse('x = 1')
    result = TransformationResult(root, False, [])
    assert result.tree == root
    assert result.tree_changed == False
    assert result.dependencies == []

# An AST node is hidden, if it has a single line comment with
# 'HIDDEN' immediately before it


# Generated at 2022-06-14 02:43:47.066748
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tr = TransformationResult(ast.parse("print('hello')"), True, [])
    tr = TransformationResult(ast.parse("print('hello')"), False, [])

# Generated at 2022-06-14 02:43:50.383341
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    expect = TransformationResult(tree=ast.parse(""),
                                  tree_changed=True,
                                  dependencies=[])
    got = TransformationResult(tree=ast.parse(""),
                               tree_changed=True,
                               dependencies=[])
    assert expect == got

# Generated at 2022-06-14 02:43:55.592603
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    from collections import namedtuple
    from typing import NamedTuple, List, Tuple
    from typed_ast import ast3 as ast

    from typed_ast import ast3 as ast
    from typed_ast.ast3 import Module, FunctionDef, arguments, Name, \
        arguments, Name, List, Call, Load, Return, Attribute
    from typed_ast.typeshed_ast import parse
    import astor

    ast.parse('def f(x: List[int]) -> int: return x[0]')

import os

# List of directories where the footer is to be added

# Generated at 2022-06-14 02:43:59.834121
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree = ast.parse("a = b")
    trans = TransformationResult(tree, True, ["tensorflow"])
    assert trans.tree == tree
    assert trans.tree_changed == True
    assert trans.dependencies == ['tensorflow']

# Generated at 2022-06-14 02:44:07.184792
# Unit test for constructor of class InputOutput
def test_InputOutput():
    assert InputOutput(input='D:\\', output='D:\\a.txt') == \
           InputOutput(Path('D:\\'), Path('D:\\a.txt'))
    assert InputOutput(input='D:\\', output='D:\\a.txt') != \
           InputOutput(Path('D:\\'), Path('D:\\a.txt'))
    assert InputOutput(input='D:\\', output='D:\\a.txt') != \
           InputOutput(Path('D:\\'), Path('D:\\b.txt'))
    assert InputOutput(input='D:\\b.txt', output='D:\\a.txt') != \
           InputOutput(Path('D:\\a.txt'), Path('D:\\b.txt'))

# Generated at 2022-06-14 02:44:13.343022
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree_changed = True
    tree = ast.parse("x = y + z")
    dependencies = ['a', 'b']
    result = TransformationResult(tree, tree_changed, dependencies)
    assert isinstance(result, TransformationResult)
    assert result.tree_changed == tree_changed
    assert result.tree == tree
    assert result.dependencies == dependencies

# Generated at 2022-06-14 02:44:21.564728
# Unit test for constructor of class InputOutput
def test_InputOutput():
    # Success
    _ = InputOutput(Path('a'), Path('b'))

    # Failure
    try:
        _ = InputOutput(Path('a'), 'b')
        assert False
    except TypeError:
        pass

    try:
        _ = InputOutput('a', Path('b'))
        assert False
    except TypeError:
        pass

    try:
        _ = InputOutput(Path('a'))
        assert False
    except TypeError:
        pass

    try:
        _ = InputOutput(Path('a'), Path('b'), Path('c'))
        assert False
    except TypeError:
        pass

# Generated at 2022-06-14 02:44:24.446463
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    assert len(TransformationResult(None, False, [])) == 3
    result = TransformationResult(None, False, [])
    assert result.tree is None
    assert not result.tree_changed
    assert result.dependencies == []

# Generated at 2022-06-14 02:44:29.036128
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input_ = Path('foo/bar.py')
    output = Path('foo/output.py')
    io = InputOutput(input_, output)
    assert io.input == input_
    assert io.output == output



# Generated at 2022-06-14 02:45:19.809063
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    input_ = ast.parse("pass")
    dependencies = ["sys", "typing", "typed_ast"]
    result = TransformationResult(input_, True, dependencies)
    assert(result.tree == input_)
    assert(result.tree_changed)
    assert(result.dependencies == dependencies)

# Generated at 2022-06-14 02:45:22.353813
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    assert TransformationResult(None, False, []).tree is None
    assert TransformationResult(None, False, []).tree_changed is False
    assert TransformationResult(None, False, []).dependencies == []

# Generated at 2022-06-14 02:45:27.544097
# Unit test for constructor of class InputOutput
def test_InputOutput():
    # Try to create with invalid arguments
    with pytest.raises(TypeError):
        i = InputOutput(1, 2)
    # Try to create with valid arguments
    i = InputOutput(Path('a'), Path('b'))
    # Check that attributes are correct
    assert i[0] == Path('a')
    assert i[1] == Path('b')


# Generated at 2022-06-14 02:45:39.344034
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    result = TransformationResult(tree=ast.parse('None'),
                                  tree_changed=False,
                                  dependencies=[])
    assert result.tree is not None
    assert result.tree_changed == False
    assert result.dependencies == []

# Transformation result returned by transformers
TransformerResult = TransformationResult

# Input/output pair
SourceTarget = NamedTuple('SourceTarget', [('source', Path),
                                           ('target', Path)])

# Result of transformers transformation
TransformationResult = NamedTuple('TransformationResult',
                                  [('tree', ast.AST),
                                   ('tree_changed', bool),
                                   ('dependencies', List[str])])

# Input/output pair
InputOutput = NamedTuple('InputOutput', [('input', Path),
                                         ('output', Path)])

# Generated at 2022-06-14 02:45:43.458460
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    cr = CompilationResult(files=1, time=2.0, target=(3, 5),
                           dependencies=['test_dep'])

    assert cr.files == 1
    assert cr.time == 2.0
    assert cr.target == (3, 5)
    assert cr.dependencies == ['test_dep']


# Generated at 2022-06-14 02:45:59.085408
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree = ast.parse('pass')
    assert TransformationResult(tree, True, []).tree_changed == True
    assert TransformationResult(tree, False, []).tree_changed == False
    assert TransformationResult(tree, False, []).dependencies == []
    assert TransformationResult(tree, True, ['mymodule']).dependencies == ['mymodule']

    # Test assignment of non-list types for dependencies
    with pytest.raises(TypeError):
        TransformationResult(tree, False, 'mymodule')
    with pytest.raises(TypeError):
        TransformationResult(tree, False, 0)
    with pytest.raises(TypeError):
        TransformationResult(tree, False, 1.0)
    with pytest.raises(TypeError):
        TransformationResult(tree, False, False)

# Generated at 2022-06-14 02:46:08.011808
# Unit test for constructor of class InputOutput
def test_InputOutput():
    path = Path('/content/file.py')
    assert InputOutput(path, path)
    assert InputOutput(path, path) == InputOutput(path, path)
    assert InputOutput(path, path) != InputOutput(path, path + '2')
    assert hash(InputOutput(path, path)) == hash(path)
    assert str(InputOutput(path, path)) == str(path)
    assert repr(InputOutput(path, path)) == repr(path)


# Generated at 2022-06-14 02:46:13.046786
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    t = ast.parse('pass')
    r = TransformationResult(tree=t, tree_changed=True, dependencies=['a', 'b'])
    assert r.tree == t
    assert r.tree_changed == True
    assert r.dependencies == ['a', 'b']

# Generated at 2022-06-14 02:46:15.518260
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input_data_path = Path('input.data')
    output_data_path = Path('output.data')
    io = InputOutput(input_data_path, output_data_path)
    assert io.input == input_data_path
    assert io.output == output_data_path

# Generated at 2022-06-14 02:46:18.186533
# Unit test for constructor of class InputOutput
def test_InputOutput():
    i = InputOutput('input', 'output')
    assert i.input == Path('input')
    assert i.output == Path('output')


# Generated at 2022-06-14 02:48:03.258848
# Unit test for constructor of class InputOutput
def test_InputOutput():
    t = InputOutput(Path('in'), Path('out'))
    assert(t.input == Path('in'))
    assert(t.output == Path('out'))

# Generated at 2022-06-14 02:48:05.643453
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    CompilationResult(files=1,
                      time=123.456,
                      target=(3, 4),
                      dependencies=['123', '456'])



# Generated at 2022-06-14 02:48:09.796598
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    compile_result = CompilationResult(files=1,
                                       time=0.1,
                                       target=(3, 6),
                                       dependencies=['__init__.py'])

    assert compile_result.files == 1
    assert compile_result.time == 0.1
    assert compile_result.target == (3, 6)
    assert compile_result.dependencies == ['__init__.py']


# Generated at 2022-06-14 02:48:16.174170
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    cr = CompilationResult(files=0,
                           time=0.0,
                           target=(0, 0),
                           dependencies=[])

    assert cr.files == 0
    assert cr.time == 0
    assert cr.target == (0, 0)
    assert cr.dependencies == []


# Generated at 2022-06-14 02:48:23.258511
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input_ = Path('input.py')
    output = Path('output.py')
    assert InputOutput(input_, output)\
        == InputOutput(input_, output)
    assert InputOutput(input_, output)\
        != InputOutput(input_, Path('outpout.py'))
    assert InputOutput(input_, output)\
        != InputOutput(Path('inpout.py'), output)



# Generated at 2022-06-14 02:48:25.481996
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input = Path("test_input")
    output = Path("test_output")
    io = InputOutput(input, output)
    assert io.input == input and io.output == output

# Generated at 2022-06-14 02:48:27.382034
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree = ast.AST()
    assert TransformationResult(tree, True, [])

# Test for constructor of class InputOutput

# Generated at 2022-06-14 02:48:33.451720
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree = ast.parse('print("Hello, world!")')
    tr = TransformationResult(tree, True, ['f1.py', 'f2.py'])
    assert(isinstance(tr.tree, ast.AST))
    assert(tr.tree_changed)
    assert(tr.dependencies == ['f1.py', 'f2.py'])



# Generated at 2022-06-14 02:48:39.054627
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    t = TransformationResult(tree=ast.parse('x=1'), tree_changed=False,
                             dependencies=[])
    assert isinstance(t.tree, ast.AST)
    assert isinstance(t.tree_changed, bool)
    assert isinstance(t.dependencies, list)
    assert not t.tree_changed
    assert len(t.dependencies) == 0


# Generated at 2022-06-14 02:48:42.295914
# Unit test for constructor of class InputOutput
def test_InputOutput():
    inp = 'inp'
    outp = 'outp'
    inout = InputOutput(input = inp, output = outp)
    assert inout.input == inp
    assert inout.output == outp
