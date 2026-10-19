

# Generated at 2022-06-14 02:39:02.197098
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    compilation_result = CompilationResult(files=0, time=0.1,
                                           target=(3, 4),
                                           dependencies=[])
    assert compilation_result.files == 0
    assert compilation_result.time == 0.1
    assert compilation_result.target == (3, 4)
    assert compilation_result.dependencies == []


# Generated at 2022-06-14 02:39:08.748705
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    transformation_result = TransformationResult(ast.Num(1), False, ['a', 'b'])

    assert isinstance(transformation_result.tree, ast.Num)
    assert transformation_result.tree_changed == False
    assert transformation_result.dependencies == ['a', 'b']


# Generated at 2022-06-14 02:39:11.947552
# Unit test for constructor of class InputOutput
def test_InputOutput():
    inp = Path('file_in.py')
    outp = Path('file_out.py')
    iop = InputOutput(inp, outp)
    assert iop.input == inp
    assert iop.output == outp
    assert iop == (inp, outp)


# Generated at 2022-06-14 02:39:18.345488
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree = ast.parse('pass')
    trans_result = TransformationResult(tree, False, [])
    assert trans_result.tree == tree
    assert trans_result.tree_changed == False
    assert trans_result.dependencies == []

    trans_result = TransformationResult(tree, True, [])
    assert trans_result.tree == tree
    assert trans_result.tree_changed == True
    assert trans_result.dependencies == []

# Generated at 2022-06-14 02:39:21.701970
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    res = CompilationResult(0, 0.0, (3, 6), [])
    assert res.files == 0
    assert res.time == 0.0
    assert res.target == (3, 6)
    assert res.dependencies == []


# Generated at 2022-06-14 02:39:23.733009
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    assert TransformationResult

__all__ = ['test_TransformationResult']

# Generated at 2022-06-14 02:39:27.496271
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    result = CompilationResult(1, 0, (3, 7), ['a.py'])
    assert result.files == 1
    assert result.time == 0
    assert result.target == (3, 7)
    assert result.dependencies == ['a.py']


# Generated at 2022-06-14 02:39:30.616957
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input = Path("/tmp/a.py")
    output = Path("/tmp/b.py")
    inout = InputOutput(input, output)
    assert inout.input == input
    assert inout.output == output

# Generated at 2022-06-14 02:39:38.797221
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree = ast.parse('pass')
    TransformationResult(tree=tree, tree_changed=True, dependencies=[])

# Result of compilation of a single file
FileCompilationResult = NamedTuple('FileCompilationResult',
                                   [('tree', ast.AST),
                                    ('time', float),
                                    ('target', CompilationTarget),
                                    ('dependencies', List[str])])

# Result of compilation of a multiple files
CompilationResultMulti = NamedTuple('CompilationResultMulti',
                                    [('files', int),
                                     ('time', float),
                                     ('result', List[FileCompilationResult])])

# Generated at 2022-06-14 02:39:41.054628
# Unit test for constructor of class InputOutput
def test_InputOutput():
    inp = Path("hi")
    out = Path("bye")
    pair = InputOutput(inp, out)
    assert pair.input == inp
    assert pair.output == out

# Generated at 2022-06-14 02:39:48.741822
# Unit test for constructor of class InputOutput
def test_InputOutput():
    assert InputOutput(Path('foo.in'), Path('foo.out')) == InputOutput('foo.in', 'foo.out')
    assert InputOutput(Path('foo.in'), Path('foo.out')).input == 'foo.in'
    assert InputOutput(Path('foo.in'), Path('foo.out')).output == 'foo.out'
    assert str(InputOutput('foo.in', 'foo.out')) == 'foo.in -> foo.out'

# Generated at 2022-06-14 02:39:51.324832
# Unit test for constructor of class InputOutput
def test_InputOutput():
    from pathlib import Path
    x = InputOutput(Path('a'), Path('b'))
    assert x.input == Path('a')
    assert x.output == Path('b')


# Generated at 2022-06-14 02:39:53.358845
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    res = TransformationResult(None, False, [])

    assert res.tree is None
    assert res.tree_changed is False
    assert res.dependencies == []

# Generated at 2022-06-14 02:39:58.609600
# Unit test for constructor of class InputOutput
def test_InputOutput():
    assert InputOutput(Path('/some/input/file.py'), Path('/some/output/file.py')).input == Path('/some/input/file.py')
    assert InputOutput(Path('/some/input/file.py'), Path('/some/output/file.py')).output == Path('/some/output/file.py')

# Generated at 2022-06-14 02:40:01.579769
# Unit test for constructor of class InputOutput
def test_InputOutput():
    i = Path('foo')
    o = Path('bar')
    inout = InputOutput(i, o)
    assert inout.input == i
    assert inout.output == o

# Generated at 2022-06-14 02:40:05.843402
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input_path = Path('/path/', 'input.py')
    output_path = Path('/path/', 'output.py')
    input_output = InputOutput(input_path, output_path)
    assert input_output.input == input_path
    assert input_output.output == output_path

# Generated at 2022-06-14 02:40:08.333631
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    _ = CompilationResult(files=1,
                          time=0.0,
                          target=(0, 0),
                          dependencies=[])



# Generated at 2022-06-14 02:40:15.523962
# Unit test for constructor of class InputOutput
def test_InputOutput():
    assert InputOutput(Path('input'), Path('output')) == \
           InputOutput(Path('input'), Path('output'))
    assert InputOutput(Path('input'), Path('output')) != \
           InputOutput(Path('input1'), Path('output'))
    assert InputOutput(Path('input'), Path('output')) != \
           InputOutput(Path('input'), Path('output1'))
    assert InputOutput(Path('input'), Path('output')) != \
           InputOutput(Path('input1'), Path('output1'))


# Generated at 2022-06-14 02:40:16.829316
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    TransformationResult(ast.parse('a'), True, ['a.py'])

# Generated at 2022-06-14 02:40:26.021301
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree = ast.parse('print("Hello World!")')
    result = TransformationResult(tree, True, [])

    assert result.tree == tree
    assert result.tree_changed == True
    assert result.dependencies == []
    assert str(result) == 'TransformationResult(tree=Module(' \
                          'body=[Expr(value=Call(' \
                          'func=Name(id=\'print\', ctx=Load()), ' \
                          'args=[Str(s=\'Hello World!\')], keywords=[]))]), ' \
                          'tree_changed=True, dependencies=[])'

# Generated at 2022-06-14 02:40:32.803426
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    assert TransformationResult(ast.parse('a = 1'),
                                False,
                                []).tree == ast.parse('a = 1')

    assert TransformationResult(ast.parse('a = 1'),
                                True,
                                []).tree_changed is True

    assert TransformationResult(ast.parse('a = 1'),
                                False,
                                [__file__]).dependencies == [__file__]


# Generated at 2022-06-14 02:40:40.831882
# Unit test for constructor of class InputOutput
def test_InputOutput():
    path1 = Path('/home/user/hi.py')
    path2 = Path('/home/user/bye.py')
    input1 = InputOutput(path1, path2)
    input2 = InputOutput(path1, path2)
    assert(input1 == input2)
    input3 = InputOutput(path1, path1)
    assert(input1 != input3)
    input4 = InputOutput(path2, path1)
    assert(input1 != input4)

# Generated at 2022-06-14 02:40:50.428279
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    assert TransformationResult(ast.parse("a = 0\n"),
                                False,
                                []).tree == ast.parse("a = 0\n")
    assert TransformationResult(ast.parse("a = 0\n"),
                                True,
                                []).tree_changed
    assert TransformationResult(ast.parse("a = 0\n"),
                                True,
                                []).dependencies == []

# Fixture for test transformer
TransformationFixture = NamedTuple('TransformationFixture',
                                   [('target', CompilationTarget),
                                    ('input', InputOutput),
                                    ('output', ast.AST)])

# Generated at 2022-06-14 02:40:55.422522
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    from .. import base
    tree = ast.parse("")
    value = TransformationResult(tree, True, [])
    assert value.tree == tree
    assert value.tree_changed == True
    assert value.dependencies == []
    base.test_object(value)

# Generated at 2022-06-14 02:40:59.925816
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input = Path('foo/bar')
    output = Path('baz/qux')

    i = InputOutput(input, output)

    assert i.input == input
    assert i.output == output
    assert i.input != output
    assert i.output != input


# Generated at 2022-06-14 02:41:02.728606
# Unit test for constructor of class InputOutput
def test_InputOutput():
    def foo(i, o):
        return InputOutput(i, o)
    assert foo('abc', 'def') == InputOutput(Path('abc'), Path('def'))


# Generated at 2022-06-14 02:41:11.224499
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    assert CompilationResult(files=0,
                             time=1.0,
                             target=(3, 4),
                             dependencies=[])
    assert CompilationResult(files=1,
                             time=0.5,
                             target=(2, 7),
                             dependencies=['a', 'b'])
    assert CompilationResult(files=1,
                             time=0.5,
                             target=(2, 7),
                             dependencies=['a', 'b'])
    assert CompilationResult(files=1,
                             time=0.5,
                             target=(2, 7),
                             dependencies=['a', 'b'])


# Generated at 2022-06-14 02:41:15.762563
# Unit test for constructor of class InputOutput
def test_InputOutput():
    i = InputOutput(input=Path("input_file"), output=Path("output_file"))
    assert i.input == Path("input_file")
    assert i.output == Path("output_file")


# Generated at 2022-06-14 02:41:19.585501
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    result_obj = CompilationResult(1, 10.0, (3, 6), [])
    assert result_obj.files == 1
    assert result_obj.time == 10.0
    assert result_obj.target == (3, 6)
    assert result_obj.dependencies == []


# Generated at 2022-06-14 02:41:25.294291
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input = Path("test/__init__.py")
    output = Path("test/__init__.pyc")
    iop = InputOutput(input, output)
    assert iop.input is input
    assert iop.output is output
    assert iop == (input, output)



# Generated at 2022-06-14 02:41:32.871543
# Unit test for constructor of class InputOutput
def test_InputOutput():
    res = InputOutput(Path('input'), Path('output'))
    assert res.input.name == 'input'
    assert res.output.name == 'output'

# Generated at 2022-06-14 02:41:34.906325
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    assert TransformationResult(tree=ast.parse(""),
                                tree_changed=True,
                                dependencies=[]) is not None

# Generated at 2022-06-14 02:41:38.250282
# Unit test for constructor of class InputOutput
def test_InputOutput():
    i = InputOutput(input='a', output='b')
    assert i.input == 'a', 'InputOutput initialization failed'
    assert i.output == 'b', 'InputOutput initialization failed'


# Generated at 2022-06-14 02:41:43.522422
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    result = CompilationResult(1, 1.0, (3, 5), [])
    assert result.files == 1
    assert result.time == 1.0
    assert result.target == (3, 5)
    assert result.dependencies == []


# Generated at 2022-06-14 02:41:46.478099
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input_file = Path('test.py')
    output_file = Path('test.pyc')
    io = InputOutput(input_file, output_file)
    assert io.input == input_file
    assert io.output == output_file

# Generated at 2022-06-14 02:41:48.578660
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input_ = Path('in')
    output = Path('out')
    io = InputOutput(input_, output)
    assert io.input == input_
    assert io.output == output

# Generated at 2022-06-14 02:41:50.110452
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    CompilationResult(1, 1.0, (1, 1), ['/usr/local/lib'])


# Generated at 2022-06-14 02:41:56.213439
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    try:
        cres = CompilationResult(1, 1.0, (3, 5), [])
    except Exception:
        pytest.fail("failed to construct CompilationResult")

    assert cres.files == 1
    assert cres.time == 1.0
    assert cres.target == (3, 5)
    assert cres.dependencies == []



# Generated at 2022-06-14 02:42:01.559529
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree = ast.parse('')

    r_1 = TransformationResult(tree, False, [])
    r_2 = TransformationResult(tree, True, [])
    r_3 = TransformationResult(tree, False, ['A', 'B'])

    assert r_1 == r_1
    assert r_1 != r_2
    assert r_1 != r_3

# Generated at 2022-06-14 02:42:02.701024
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    CompilationResult(0, 0.0, (0, 0), [])

# Generated at 2022-06-14 02:42:14.045147
# Unit test for constructor of class InputOutput
def test_InputOutput():
    i, o = InputOutput("input", "output")
    assert i == 'input'
    assert type(i) is Path
    assert o == 'output'
    assert type(o) is Path

# Generated at 2022-06-14 02:42:15.481824
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    CompilationResult(1, 1, (3, 5), ['a', 'b'])



# Generated at 2022-06-14 02:42:17.146492
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    CompilationResult(files=2, time=1.0, target=(3, 6), dependencies=["a", "b"])


# Generated at 2022-06-14 02:42:19.058412
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    CompilationResult(1, '1.0', (3, 8), [])



# Generated at 2022-06-14 02:42:28.420499
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    a = CompilationResult(files=2,
                          time=1.2345,
                          target=(3, 5),
                          dependencies=['a', 'b', 'c'])
    assert a.files == 2
    assert a.time == 1.2345
    assert a.target == (3, 5)
    assert a.dependencies == ['a', 'b', 'c']
    b = CompilationResult(files=3,
                          time=5.4321,
                          target=(2, 5),
                          dependencies=['d', 'e', 'f'])
    assert b.files == 3
    assert b.time == 5.4321
    assert b.target == (2, 5)
    assert b.dependencies == ['d', 'e', 'f']
    c = a + b

# Generated at 2022-06-14 02:42:31.933067
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    CompilationResult(files=10,
                      time=2.25,
                      target=(3, 7),
                      dependencies=['a', 'b'])


# Generated at 2022-06-14 02:42:34.733719
# Unit test for constructor of class CompilationResult
def test_CompilationResult():  # noqa
    CompilationResult(files=1, time=2, target=(2, 7), dependencies=['1.py'])

# Generated at 2022-06-14 02:42:45.313758
# Unit test for constructor of class TransformationResult
def test_TransformationResult():  # pylint: disable=W0613
    """Test constructor of TransformationResult
    """
    # pylint: disable=W0106
    '''Test constructor of TransformationResult'''
    assert TransformationResult(None, False, []).tree is None
    assert TransformationResult(None, False, []).tree_changed is False
    assert TransformationResult(None, False, []).dependencies == []
    assert TransformationResult(None, True, []).tree_changed is True
    assert TransformationResult(None, False, ['a', 'b']).dependencies == ['a', 'b']

# Result of class extractor
ClassExtractorResult = NamedTuple('ClassExtractorResult',
                                  [('name', str),
                                   ('bases', List[str]),
                                   ('methods', List[Tuple[str, ast.AST]])])


# Generated at 2022-06-14 02:42:48.604415
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input_ = Path('foo.py')
    output = Path('bar.py')

    actual = InputOutput(input=input_, output=output)
    assert str(actual.input) == 'foo.py'
    assert str(actual.output) == 'bar.py'



# Generated at 2022-06-14 02:42:49.938251
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    assert TransformationResult(ast.AST([]), False, ['a', 'b', 'c'])

# Generated at 2022-06-14 02:43:09.538717
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    # pylint: disable=unused-variable
    res = TransformationResult(None, None, None)

# Generated at 2022-06-14 02:43:10.593607
# Unit test for constructor of class InputOutput
def test_InputOutput():
    assert InputOutput(input="a/b/c", output="d/e/f") \
        == InputOutput(input=Path("a/b/c"), output=Path("d/e/f"))


# Generated at 2022-06-14 02:43:12.798449
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    CompilationResult(files=0,
                      time=0.0,
                      target=(0, 0),
                      dependencies=[])


# Generated at 2022-06-14 02:43:15.189996
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    CompilationResult(files=1, time=0.0, target=(3, 7), dependencies=[])


# Generated at 2022-06-14 02:43:18.222131
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    TransformationResult(ast.parse('1'),
                         True,
                         ['file1.py', 'file2.py'])

# Generated at 2022-06-14 02:43:22.461115
# Unit test for constructor of class InputOutput
def test_InputOutput():
    i = InputOutput(Path('./main.py'), Path('./main.py'))
    assert i.input.name == 'main.py'
    assert i.output.name == 'main.py'

# Generated at 2022-06-14 02:43:26.627613
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    result = CompilationResult(3, 0.5, (3, 5), [])
    assert result.files == 3
    assert result.time == 0.5
    assert result.target == (3, 5)
    assert result.dependencies == []


# Generated at 2022-06-14 02:43:28.263768
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    CompilationResult(files=1, time=1.0, target=(3, 5), dependencies=["a"])

# Generated at 2022-06-14 02:43:31.143180
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree = ast.Module()
    t = TransformationResult(tree, True, ['a', 'b'])
    assert t.tree == tree
    assert t.tree_changed == True
    assert t.dependencies == ['a', 'b']

# Generated at 2022-06-14 02:43:36.094148
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tr = TransformationResult(ast.parse(''), True, ['a', 'b'])
    assert tr.tree is not None
    assert tr.tree_changed is True
    assert tr.dependencies == ['a', 'b']


# Mock of class CompilationResult

# Generated at 2022-06-14 02:44:22.736701
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    c = CompilationResult(files=23,
                          time=12.3,
                          target=(3, 4),
                          dependencies=['a', 'b', 'c'])
    assert c.files == 23
    assert c.time == 12.3
    assert c.target == (3, 4)
    asser

# Generated at 2022-06-14 02:44:25.377469
# Unit test for constructor of class InputOutput
def test_InputOutput():
    path1 = Path('.')
    path2 = Path('..')
    in_out = InputOutput(path1, path2)
    assert in_out.input == path1
    assert in_out.output == path2


# Generated at 2022-06-14 02:44:29.305209
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    result = CompilationResult(0, 0.0, (0, 0), [])
    assert result.files == 0
    assert result.time == 0.0
    assert result.target == (0, 0)
    assert result.dependencies == []



# Generated at 2022-06-14 02:44:31.965304
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    cr = CompilationResult(0, 0.0, (3, 4), [])
    assert cr.files == 0
    assert cr.time == 0.0
    assert cr.target == (3, 4)
    cr.files = 1
    cr.time = 1.0
    cr.target = (3, 5)


# Generated at 2022-06-14 02:44:33.817474
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    assert TransformationResult(tree=None, tree_changed=False, dependencies=[])

# Generated at 2022-06-14 02:44:36.730722
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input = Path('input')
    output = Path('output')
    obj = InputOutput(input, output)
    assert obj.input == input
    assert obj.output == output

# Generated at 2022-06-14 02:44:41.943895
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input = Path('a.py')
    output = Path('a.mpy')
    i_o = InputOutput(input, output)
    assert i_o.input == input
    assert i_o.output == output


# Generated at 2022-06-14 02:44:45.606530
# Unit test for constructor of class InputOutput
def test_InputOutput():
    path_input = Path('input')
    path_output = Path('output')
    input_output = InputOutput(path_input, path_output)
    assert input_output.input == path_input
    assert input_output.output == path_output



# Generated at 2022-06-14 02:44:49.193150
# Unit test for constructor of class InputOutput
def test_InputOutput():
    try:
        input = Path('a.py')
        output = Path('a.js')
        inout = InputOutput(input, output)
    except Exception as e:
        assert(False, e)


# Generated at 2022-06-14 02:44:52.391928
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input_ = Path("/foo")
    output_ = Path("/bar")
    io = InputOutput(input_, output_)
    assert io.input == input_
    assert io.output == output_

# Generated at 2022-06-14 02:46:28.642671
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    cr = CompilationResult(3, 1.2, (3, 7), ['foo', 'bar'])
    assert isinstance(cr, CompilationResult)
    assert cr.files == 3
    assert cr.time == 1.2
    assert cr.target == (3, 7)
    assert cr.dependencies == ['foo', 'bar']


# Generated at 2022-06-14 02:46:30.856033
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    target = (0, 0)
    compilatation_result = CompilationResult(0, 0, target, [])
    assert compilatation_result.target == target

# Generated at 2022-06-14 02:46:32.853859
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    TransformationResult(tree=None, tree_changed=True, dependencies=[])

# Generated at 2022-06-14 02:46:38.974868
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    result = CompilationResult(files=3, time=13.0, target=(3, 7), dependencies=['/a/b'])
    assert result.files == 3
    assert result.time == 13.0
    assert result.target == (3, 7)
    assert result.dependencies == ['/a/b']


# Generated at 2022-06-14 02:46:41.698884
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    c = CompilationResult(files=1, time=2.0, target=(3, 4), dependencies=[])
    assert c.files == 1
    assert c.time == 2.0
    assert c.target == (3, 4)
    assert c.dependencies == []


# Generated at 2022-06-14 02:46:45.986048
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    result = CompilationResult(files=2, time=2.0, target=(3, 5), dependencies=[])
    assert result.files == 2
    assert result.time == 2.0
    assert result.target == (3, 5)
    assert result.dependencies == []


# Generated at 2022-06-14 02:46:52.566305
# Unit test for constructor of class InputOutput
def test_InputOutput():
    path_name = 'test_path'
    input_output = InputOutput(path_name, path_name)
    assert input_output.input == Path(path_name)
    assert input_output.output == Path(path_name)

if __name__ == '__main__':
    import sys
    import os
    sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
    test_InputOutput()

# Generated at 2022-06-14 02:46:56.214360
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input_path = Path('/tmp/path/to/input')
    output_path = Path('/tmp/path/to/output')
    io = InputOutput(input_path, output_path)

    assert io.input == input_path
    assert io.output == output_path

# Generated at 2022-06-14 02:47:00.201082
# Unit test for constructor of class InputOutput
def test_InputOutput():
    assert InputOutput(
        input=Path('a'),
        output=Path('b')
    ) == InputOutput(input=Path('a'),
                     output=Path('b'))
    assert InputOutput(
        input=Path('a'),
        output=Path('b')
    ) != InputOutput(input=Path('a'),
                     output=Path('c'))

# Generated at 2022-06-14 02:47:04.320282
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    result = CompilationResult(0, 0.0, (3, 6), ['a', 'b', 'c'])
    assert result.files == 0
    assert result.time == 0.0
    assert result.target == (3, 6)
    assert result.dependencies == ['a', 'b', 'c']
