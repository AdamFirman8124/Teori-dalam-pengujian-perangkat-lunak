

# Generated at 2022-06-14 02:38:57.884023
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree = ast.parse('')
    tree_changed = False
    dependencies = []
    TransformationResult(tree, tree_changed, dependencies)

# Generated at 2022-06-14 02:39:06.836877
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    t = TransformationResult(ast.parse('a = 2'), True, [])
    assert t[0] == ast.parse('a = 2')
    assert t[1] == True
    assert t[2] == []

    t = TransformationResult(ast.parse('a = 2'), True, ['a', 'b'])
    assert t[0] == ast.parse('a = 2')
    assert t[1] == True
    assert t[2] == ['a', 'b']

    t = TransformationResult(ast.parse('a = 2'), False, [])
    assert t[0] == ast.parse('a = 2')
    assert t[1] == False
    assert t[2] == []

# Generated at 2022-06-14 02:39:07.830166
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    pass

# Generated at 2022-06-14 02:39:10.824078
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input = Path('path/to/input')
    output = Path('path/to/output')
    input_output = InputOutput(input=input, output=output)
    assert input_output.input == input
    assert input_output.output == output

# Generated at 2022-06-14 02:39:14.094989
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    assert TransformationResult(None, None, None)


Transformer = NamedTuple('Transformer', [('name', str),
                                         ('func', callable),
                                         ('dependencies', List)])


# Fake class for typing

# Generated at 2022-06-14 02:39:15.225956
# Unit test for constructor of class TransformationResult

# Generated at 2022-06-14 02:39:21.022308
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    cresult = CompilationResult(1, 1.0, (3, 5), [])
    if cresult.files != 1:
        raise AssertionError()
    if cresult.time != 1.0:
        raise AssertionError()
    if cresult.target != (3, 5):
        raise AssertionError()
    if cresult.dependencies != []:
        raise AssertionError()


# Generated at 2022-06-14 02:39:23.833889
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    assert CompilationResult(files=1, time=1.0, target=(3, 6), dependencies=['foo'])


# Generated at 2022-06-14 02:39:28.009458
# Unit test for constructor of class InputOutput
def test_InputOutput():
    test_input = Path('test_input')
    test_output = Path('test_output')
    test_pair = InputOutput(input=test_input, output=test_output)
    assert test_pair.input == test_input
    assert test_pair.output == test_output


# Generated at 2022-06-14 02:39:30.957215
# Unit test for constructor of class CompilationResult
def test_CompilationResult():

    result = CompilationResult(files=1, time=2, target=(3, 4),
                               dependencies=['x'])
    assert result.files == 1
    assert result.time == 2
    assert result.target == (3, 4)
    assert result.dependencies == ['x']



# Generated at 2022-06-14 02:39:36.027464
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    cr = CompilationResult(1, 2.0, (3, 4), [])
    assert cr.files == 1
    assert cr.time == 2.0
    assert cr.target == (3, 4)
    assert cr.dependencies == []



# Generated at 2022-06-14 02:39:36.993647
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    TransformationResult(None, False, [])

# Generated at 2022-06-14 02:39:45.122875
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    
    # Initialization
    cr = CompilationResult(2, 3.14, (3, 4), ["foo", "bar"])
    cr_correct = CompilationResult(2, 3.14, (3, 4), ["foo", "bar"])
    
    # Equalities
    assert cr == cr_correct
    assert cr.time == 3.14

    # Inequalities
    cr_incorrect = CompilationResult(2, 3.14, (3, 5), ["foo", "bar"])
    assert cr != cr_incorrect

    # Less than
    assert cr < cr_incorrect

    # Less than or equal
    assert cr <= cr_incorrect
    assert cr <= cr_correct

    # Greater than
    assert cr_incorrect > cr

    # Greater than or equal
    assert cr_incorrect >= cr
   

# Generated at 2022-06-14 02:39:46.724497
# Unit test for constructor of class InputOutput
def test_InputOutput():
    InputOutput(Path('a'),
                Path('b'))

# Generated at 2022-06-14 02:39:48.958027
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    t = ast.Stmt()
    dep = ['a', 'b']
    TransformationResult(t, False, dep)



# Generated at 2022-06-14 02:39:53.358539
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree = ast.parse('1')
    t = TransformationResult(tree, True, [])
    assert t.tree is tree
    assert t.tree_changed is True
    assert t.dependencies  == []

# Result of assert removing
AssertResult = NamedTuple('AssertResult',
                          [('tree', ast.AST),
                           ('assertions_count', int)])


# Generated at 2022-06-14 02:39:55.822518
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    CompilationResult(files=1,
                      time=2.5,
                      target=(3, 4),
                      dependencies=['foo'])



# Generated at 2022-06-14 02:40:01.478620
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    compilation_result = CompilationResult(files=1,
                                           time=2.0,
                                           target=(3, 4),
                                           dependencies=[])
    assert compilation_result.files == 1
    assert compilation_result.time == 2.0
    assert compilation_result.target == (3, 4)
    assert compilation_result.dependencies == []


# Generated at 2022-06-14 02:40:10.744010
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree = ast.Module(
        name='test',
    )
    tr = TransformationResult(tree_changed=True,
                              tree=tree,
                              dependencies=['a', 'b'])
    assert tr.tree_changed == True
    assert tr.tree == tree
    assert tr.dependencies == ['a', 'b']

# Target python version
Target = Tuple[int, int]

# Information about compilation
Result = NamedTuple('Result',
                    [('files', int),
                     ('time', float),
                     ('target', Target),
                     ('dependencies', List[str])])

# Input/output pair
IoPair = NamedTuple('IoPair', [('input', Path),
                               ('output', Path)])

# Result of transformers transformation

# Generated at 2022-06-14 02:40:15.892401
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    result = CompilationResult(
        files=10,
        time=5.5,
        target=(3, 4),
        dependencies=['a', 'b', 'c']
    )
    assert result.files == 10
    assert result.time == 5.5
    assert result.target == (3, 4)
    assert result.dependencies == ['a', 'b', 'c']

# Generated at 2022-06-14 02:40:25.028426
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    from typed_ast.ast3 import expr
    from typing import List
    import typing
    import types

    assert isinstance(TransformationResult.__new__(TransformationResult,
                                                   tree=expr.Name(id='foo',
                                                                  ctx=expr.Load()),
                                                   tree_changed=False,
                                                   dependencies=['foo.py']),
                      TransformationResult)
    assert isinstance(TransformationResult.__new__(TransformationResult,
                                                   tree=expr.Name(id='foo',
                                                                  ctx=expr.Load()),
                                                   tree_changed=True,
                                                   dependencies=['foo.py']),
                      TransformationResult)

# Generated at 2022-06-14 02:40:27.273536
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    assert CompilationResult(files=1, time=0.5, target=(3, 7), dependencies=['a', 'b'])


# Generated at 2022-06-14 02:40:29.583008
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    CompilationResult(files=1, time=1.0, target=(3, 7), dependencies=['a', 'b'])


# Generated at 2022-06-14 02:40:32.375304
# Unit test for constructor of class InputOutput
def test_InputOutput():
    p1 = Path('a.in')
    p2 = Path('a.out')
    input_output = InputOutput(p1, p2)
    assert(input_output.input == p1)
    assert(input_output.output == p2)

# Generated at 2022-06-14 02:40:38.284464
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    assert TransformationResult(None, None, None) is not None

# Source file
SourceFile = NamedTuple('SourceFile', [('code', str),
                                       ('path', Path),
                                       ('filename', str),
                                       ('module_name', str)])


# Generated at 2022-06-14 02:40:42.040784
# Unit test for constructor of class InputOutput
def test_InputOutput():
    in_path = 'in'/'pass'
    out_path = 'out'/'pass'
    in_out = InputOutput(in_path, out_path)
    assert in_out.input == in_path
    assert in_out.output == out_path


# Generated at 2022-06-14 02:40:49.422486
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    p = ast.parse('a = 3')
    result = TransformationResult(p, True, ['foo', 'bar'])
    assert result.tree_changed
    assert len(result.dependencies) == 2

# Result of transformer
TransformationResult = NamedTuple('TransformationResult',
                                  [('code', str),
                                   ('tree_changed', bool),
                                   ('dependencies', List[str])])


# Generated at 2022-06-14 02:40:53.679808
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    # type: () -> None
    tree = ast.parse("a + b")
    assert TransformationResult(tree, False, []).tree_changed
    assert not TransformationResult(tree, False, []).dependencies

# Generated at 2022-06-14 02:40:55.956832
# Unit test for constructor of class InputOutput
def test_InputOutput():
    inp = Path('foo')
    out = Path('bar')
    InputOutput(inp, out)

# Generated at 2022-06-14 02:41:00.171806
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    result = TransformationResult(tree=None, tree_changed=False, dependencies=['a'])
    assert(result.tree is None)
    assert(result.tree_changed is False)


# This class is for converting between typed_ast and ast.

# Generated at 2022-06-14 02:41:06.719674
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    assert CompilationResult(100, 3.14, (3, 4), ["dep1", "dep2"])


# Generated at 2022-06-14 02:41:19.016804
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    res = CompilationResult(files=1, time=0.5, target=(2, 7), dependencies=[])
    assert isinstance(res, CompilationResult)
    assert res.files == 1
    assert res.time == 0.5
    assert res.target == (2, 7)
    assert res.dependencies == []

    with pytest.raises(TypeError):
        CompilationResult(files='!', time=0.5, target=(2, 7), dependencies=[])
    with pytest.raises(TypeError):
        CompilationResult(files=1, time='!', target=(2, 7), dependencies=[])
    with pytest.raises(TypeError):
        CompilationResult(files=1, time=0.5, target='!', dependencies=[])
    with pytest.raises(TypeError):
        Comp

# Generated at 2022-06-14 02:41:23.767086
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input = Path('input')
    output = Path('output')
    iop = InputOutput(input, output)
    assert iop.input == input
    assert iop.output == output


# Generated at 2022-06-14 02:41:29.721897
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    result = CompilationResult(1, 2.0, (3, 4), ['test'])
    assert result.files == 1
    assert result.time == 2.0
    assert result.target == (3, 4)
    assert result.dependencies == ['test']


# Generated at 2022-06-14 02:41:35.342405
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    result = CompilationResult(files=1,
                               time=1.0,
                               target=(2, 7),
                               dependencies=["a", "b"])
    assert result.files == 1
    assert result.time == 1.0
    assert result.target == (2, 7)
    assert result.dependencies == ["a", "b"]

# Generated at 2022-06-14 02:41:39.450068
# Unit test for constructor of class InputOutput
def test_InputOutput():
    # Arrange
    input = InputOutput('input', 'output')

    # Assert
    assert str(input.input) == 'input'
    assert str(input.output) == 'output'
    assert input.input == Path('input')
    assert input.output == Path('output')

# Generated at 2022-06-14 02:41:43.235229
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    c = CompilationResult(1, 2.0, (3, 4), [])
    assert c.files == 1
    assert c.time == 2.0
    assert c.target == (3, 4)
    assert c.dependencies == []



# Generated at 2022-06-14 02:41:44.982531
# Unit test for constructor of class InputOutput
def test_InputOutput():
    assert InputOutput(Path('a'), Path('b')) == InputOutput(Path('a'),
                                                            Path('b'))

# Generated at 2022-06-14 02:41:46.861920
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    assert not TransformationResult(tree=None,
                                    tree_changed=True,
                                    dependencies=['a', 'b'])

# Generated at 2022-06-14 02:41:53.799442
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree1 = ast.parse('x = 100')
    result1 = TransformationResult(tree1, False, [])
    assert result1.tree == tree1
    assert result1.tree_changed == False
    assert result1.dependencies == []
    tree2 = ast.parse('x = 23')
    result2 = TransformationResult(tree2, True, ['foo', 'bar'])
    assert result2.tree == tree2
    assert result2.tree_changed == True
    assert result2.dependencies == ['foo', 'bar']


# Result of transformer for one file
TransformationFileResult = \
    NamedTuple('TransformationFileResult', [('io', InputOutput),
                                            ('result', TransformationResult)])

# Result of transformer

# Generated at 2022-06-14 02:42:09.180097
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree = ast.parse("pass")
    res = TransformationResult(tree, False, [])
    assert res.tree == tree
    assert res.tree_changed == False
    assert res.dependencies == []

# Result of file cache
FileCacheResult = NamedTuple('FileCacheResult',
                             [('success', bool),
                              ('hash', str),
                              ('tree', ast.AST),
                              ('dependencies', List[str])])


# Generated at 2022-06-14 02:42:14.006174
# Unit test for constructor of class InputOutput
def test_InputOutput():
    def test_input_output(input_: str, output_: str):
        input_output = InputOutput(Path(input_), Path(output_))
        assert str(input_output.input) == input_
        assert str(input_output.output) == output_

    test_input_output(input_='input', output_='output')

# Generated at 2022-06-14 02:42:18.678734
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    params = (1, 10.0, (3, 7), ['file1', 'file2'])
    cr = CompilationResult(*params)
    assert isinstance(cr, CompilationResult)
    assert cr.files == params[0]
    assert cr.time == params[1]
    assert cr.target == params[2]
    assert cr.dependencies == params[3]


# Generated at 2022-06-14 02:42:21.364895
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    assert CompilationResult(1, 1.0, (3, 7), ['foo']) == CompilationResult(1, 1.0, (3, 7), ['foo'])


# Generated at 2022-06-14 02:42:23.833965
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    assert TransformationResult(tree=None, tree_changed=False, dependencies=[])


# Generated at 2022-06-14 02:42:25.695403
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input_ = Path('/tmp/input.py')
    output = Path('/tmp/output.py')
    io = InputOutput(input_, output)
    assert io.input == input_
    assert io.output == output

# Generated at 2022-06-14 02:42:30.707904
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    result = CompilationResult(1, 0.5, (3, 7), ['./foo'])
    assert result.files == 1
    assert result.time == 0.5
    assert result.target == (3, 7)
    assert result.dependencies == ['./foo']


# Generated at 2022-06-14 02:42:36.286105
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    # Arrange
    ast_tree = ast.parse('print(42)')
    dependencies = ['foo', 'bar']

    # Act
    res = TransformationResult(ast_tree, True, dependencies)

    # Assert
    assert res.tree == ast_tree
    assert res.tree_changed == True
    assert res.dependencies == dependencies

# Generated at 2022-06-14 02:42:41.699594
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input = Path('foo/bar/file.py')
    output = input.parent / 'file.fixed.py'
    io = InputOutput(input, output)
    assert io.input == input
    assert io.output == output


# Generated at 2022-06-14 02:42:43.037891
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    CompilationResult(1, 1.0, (3, 7), ['a', 'b'])

# Generated at 2022-06-14 02:43:06.028161
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    cr = CompilationResult(1, 2.0, (3, 4), [])
    assert cr.files == 1
    assert cr.time == 2.0
    assert cr.target == (3, 4)
    assert cr.dependencies == []



# Generated at 2022-06-14 02:43:09.635415
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    c = CompilationResult(1, 2.0, (3, 4), [])
    assert c.files == 1
    assert c.time == 2.0
    assert c.target == (3, 4)
    assert c.dependencies == []

# Generated at 2022-06-14 02:43:13.079462
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    t = ast.parse('class Foo: pass')
    r = TransformationResult(tree=t, tree_changed=False, dependencies=[])
    assert r.tree == t
    assert not r.tree_changed
    assert r.dependencies == []



# Generated at 2022-06-14 02:43:23.638041
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    assert TransformationResult(ast.parse("pass"), False, []) != \
           TransformationResult(ast.parse("pass"), False, [])
    assert TransformationResult(ast.parse("pass"), False, []) == \
           TransformationResult(ast.parse("pass"), False, [])
    assert TransformationResult(ast.parse("pass"), False, []) != \
           TransformationResult(ast.parse("pass"), True, [])
    assert TransformationResult(ast.parse("pass"), False, ["a"]) != \
           TransformationResult(ast.parse("pass"), False, ["b"])
    assert TransformationResult(ast.parse("pass"), True, []) != \
           TransformationResult(ast.parse("pass"), True, [])

# Generated at 2022-06-14 02:43:29.543570
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    """Unit test for constructor of class TransformationResult."""
    tree = ast.parse("x=1")
    tree_changed = True
    dependencies = ["abc", "def"]

    result = TransformationResult(tree, tree_changed, dependencies)
    assert result.tree.body[0].value.n == 1
    assert result.tree_changed == True
    assert result.dependencies == dependencies

# Generated at 2022-06-14 02:43:32.220468
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    result = CompilationResult(1, 2, (3, 4), ['a'])
    assert result.files == 1
    assert result.time == 2
    assert result.target == (3, 4)
    assert result.dependencies == ['a']


# Generated at 2022-06-14 02:43:36.142923
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input = Path("1.py")
    output = Path("2.py")

    pair = InputOutput(input, output)

    assert pair.input == input
    assert pair.output == output


# Generated at 2022-06-14 02:43:38.301201
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    assert TransformationResult(ast.parse("a=1"), False, []) == TransformationResult(ast.parse("a=1"), False, [])

# Generated at 2022-06-14 02:43:41.838856
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    f = ast.parse('1 + 1')
    t = TransformationResult(tree=f, tree_changed=False, dependencies=[])
    assert t.tree is f
    assert not t.tree_changed
    assert t.dependencies == []

# Generated at 2022-06-14 02:43:43.693657
# Unit test for constructor of class InputOutput
def test_InputOutput():
    assert InputOutput(input=Path('tmp/input'), output=Path('tmp/output'))


# Generated at 2022-06-14 02:44:35.462815
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree = ast.parse('test()', 'test', 'exec')
    dependencies = ['test']
    tr = TransformationResult(tree, True, dependencies)
    assert (tr.tree == tree) and (tr.tree_changed == True) and (tr.dependencies == dependencies)

# Generated at 2022-06-14 02:44:44.040409
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input_file = Path('/') / 'this' / 'is' / 'a' / 'test'
    output_file = Path('/') / 'this' / 'is' / 'another' / 'test'

    pair = InputOutput(input_file, output_file)

    assert pair.input == input_file
    assert pair.output == output_file


# Generated at 2022-06-14 02:44:48.225969
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    cr = CompilationResult(files=0, time=0.0, target=(2, 5), dependencies=[])
    assert cr.files == 0
    assert cr.time == 0.0
    assert cr.target == (2, 5)
    assert cr.dependencies == []


# Generated at 2022-06-14 02:44:51.386261
# Unit test for constructor of class InputOutput
def test_InputOutput():
    assert InputOutput(Path('a'), Path('b')) == InputOutput('a', 'b')
    assert InputOutput(Path('a'), Path('b')) != InputOutput('b', 'a')

# Generated at 2022-06-14 02:44:53.470206
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    assert isinstance(CompilationResult(1, 1.0, (3, 4), ['a']), CompilationResult)


# Generated at 2022-06-14 02:44:57.131387
# Unit test for constructor of class InputOutput
def test_InputOutput():
    in_ = Path.cwd() / 'spam'
    out = Path.cwd() / 'eggs'
    io = InputOutput(in_, out)
    assert io.input == in_
    assert io.output == out
    assert io.input != io.output
    assert io.input != io.output.cwd()


# Generated at 2022-06-14 02:45:02.318971
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    assert TransformationResult.__new__(TransformationResult,
                                        tree=ast.parse(''),
                                        tree_changed=True,
                                        dependencies=['a', 'b']) != \
           TransformationResult.__new__(TransformationResult,
                                        tree=ast.parse('pass'),
                                        tree_changed=True,
                                        dependencies=['a', 'b'])

# Generated at 2022-06-14 02:45:04.394339
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    # type: () -> None
    CompilationResult(3, 5.1, (3, 5), [])



# Generated at 2022-06-14 02:45:06.981961
# Unit test for constructor of class TransformationResult

# Generated at 2022-06-14 02:45:16.432319
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    t = ast.parse('a')
    d = TransformationResult(t, True, [])
    assert d.tree == t
    assert d.tree_changed
    assert d.dependencies == []

# Module in filesystem
InputModule = NamedTuple('InputModule', [('path', Path),
                                         ('relative_path', str)])

# Module in system
SystemModule = NamedTuple('SystemModule', [('name', str),
                                           ('package', str),
                                           ('path', str),
                                           ('relative_path', str)])

# Module in memory
MemoryModule = NamedTuple('MemoryModule', [('name', str),
                                           ('package', str),
                                           ('source', str),
                                           ('relative_path', str)])

# Mapping from package names to modules in system

# Generated at 2022-06-14 02:46:58.518379
# Unit test for constructor of class InputOutput
def test_InputOutput():
    i = 'abc'
    o = 'def'
    p = Path('a/b/c')
    q = Path('d/e/f')
    assert InputOutput(i, o) == InputOutput(p, q)
    assert InputOutput(i, o) == InputOutput(i, q)
    assert InputOutput(i, o) == InputOutput(p, o)
    assert InputOutput(i, o) != InputOutput(p, p)
    assert InputOutput(i, o) != InputOutput(q, q)
    assert InputOutput(i, o) != InputOutput(q, p)
    assert InputOutput(i, o) != None
    assert InputOutput(i, o) != 1
    assert not (InputOutput(i, o) != InputOutput(i, o)) # noqa

# Generated at 2022-06-14 02:47:00.200916
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    CompilationResult(files=1, time=1.5, target=(3, 8), dependencies=["1", "2"])


# Generated at 2022-06-14 02:47:03.714934
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    assert TransformationResult(ast.parse("pass", "<string>", "exec"),
                                True,
                                []) == TransformationResult(
        tree=ast.parse("pass", "<string>", "exec"),
        tree_changed=True,
        dependencies=[])


# Generated at 2022-06-14 02:47:09.190667
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    t = ast.parse("def add(x, y): return x + y")
    r = TransformationResult(t, False, ["file.py"])
    assert r.tree == t
    assert r.tree_changed == False
    assert r.dependencies == ["file.py"]

    r = TransformationResult(t, True, ["file.py"])
    assert r.tree == t
    assert r.tree_changed == True
    assert r.dependencies == ["file.py"]

# Generated at 2022-06-14 02:47:14.188529
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    files = 1
    time = 2.0
    target = (3, 4)
    dependencies = ['1', '2']
    result = CompilationResult(files, time, target, dependencies)
    assert result.files == files
    assert result.time == time
    assert result.target == target
    assert result.dependencies == dependencies


# Generated at 2022-06-14 02:47:18.315053
# Unit test for constructor of class InputOutput
def test_InputOutput():
    test_input = 'test/input'
    test_output = 'test/output'
    io = InputOutput(test_input, test_output)
    assert io.input == test_input
    assert io.output == test_output

# Generated at 2022-06-14 02:47:19.883421
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    CompilationResult(10, 0.1, (0, 0), [])

# Generated at 2022-06-14 02:47:22.521149
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree = ast.parse('True and None')
    assert TransformationResult(tree, True, ['test']) is not None

# Generated at 2022-06-14 02:47:25.696729
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input = Path('.')
    output = Path('.')
    assert InputOutput(input, output).input == input
    assert InputOutput(input, output).output == output


# Generated at 2022-06-14 02:47:29.021511
# Unit test for constructor of class InputOutput
def test_InputOutput():
    inputOutput = InputOutput('test input', 'test output')
    assert inputOutput.input == 'test input'
    assert inputOutput.output == 'test output'
