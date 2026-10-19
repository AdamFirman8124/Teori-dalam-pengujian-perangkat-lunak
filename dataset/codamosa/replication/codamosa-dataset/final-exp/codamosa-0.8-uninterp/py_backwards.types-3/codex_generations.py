

# Generated at 2022-06-14 02:38:59.846824
# Unit test for constructor of class InputOutput
def test_InputOutput():
    inp = 'input'
    out = 'output'
    input_output = InputOutput(inp, out)
    assert input_output.input == inp
    assert input_output.output == out


# Generated at 2022-06-14 02:39:05.833894
# Unit test for constructor of class InputOutput
def test_InputOutput():
    test_path = Path('test_path')
    io1 = InputOutput(test_path, test_path)
    io2 = InputOutput(test_path, test_path)
    assert io1 == io2
    assert io1.input == io2.input
    assert io1.output == io2.output
    assert io1.input is io2.input
    assert io1.output is io2.output


# Generated at 2022-06-14 02:39:09.297960
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree = ast.parse('print("Hello, World!")')
    tree_changed = True
    dependencies = ['a', 'z', 'some_file']

    tr = TransformationResult(tree, tree_changed, dependencies)

    assert isinstance(tr.tree, ast.AST)
    assert tr.tree_changed
    assert tr.dependencies == dependencies

# Generated at 2022-06-14 02:39:12.043565
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    result = CompilationResult(3, 1.0, (3, 7), ['dep1', 'dep2'])
    assert result.files == 3
    assert result.time == 1.0
    assert result.target == (3, 7)
    assert result.dependencies == ['dep1', 'dep2']


# Generated at 2022-06-14 02:39:14.665900
# Unit test for constructor of class InputOutput
def test_InputOutput():
    path_input = Path("input.txt")
    path_output = Path("output.txt")
    InputOutput(path_input, path_output)

# Generated at 2022-06-14 02:39:16.289598
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    assert CompilationResult(files=0, time=0.0, target=(3, 8))


# Generated at 2022-06-14 02:39:23.970927
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    e = ast.parse('1+1')
    r = TransformationResult(tree=e, tree_changed=True,
                             dependencies=['foo', 'bar'])
    assert isinstance(r.tree, ast.AST)
    assert r.tree_changed is True
    assert r.dependencies == ['foo', 'bar']

# Result of type checking
TypeCheckResult = NamedTuple('TypeCheckResult',
                             [('tree', ast.Module),
                              ('new_info', ast.symbol_table.SymbolTable)])

# Generated at 2022-06-14 02:39:26.938141
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    assert isinstance(TransformationResult(ast.Module(), False, []),
                      TransformationResult)
    assert not TransformationResult(ast.Module(), False, []) == \
        TransformationResult(ast.Module(), False, [])

# Generated at 2022-06-14 02:39:30.149426
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input_ = Path('./input')
    output = Path('./output')

    io_pair = InputOutput(input_, output)

    assert io_pair.input == input_
    assert io_pair.output == output


# Generated at 2022-06-14 02:39:33.533467
# Unit test for constructor of class InputOutput
def test_InputOutput():
    fname = 'a\nb'
    inp = Path(fname)
    assert inp == InputOutput(inp, inp).input
    assert inp == InputOutput(inp, inp).output


# Generated at 2022-06-14 02:39:36.984250
# Unit test for constructor of class InputOutput
def test_InputOutput():
    # Input/output pair
    InputOutput(input='foo.py', output='bar.py')

# Generated at 2022-06-14 02:39:42.939137
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    # pylint: disable=unused-variable
    tree = ast.parse('')
    TransformationResult(tree, True, [])
    TransformationResult(tree, True, ['foo.py'])
    TransformationResult(tree, False, [])
    TransformationResult(tree, False, ['foo.py'])


# Result of parsing file
ParsingResult = NamedTuple('ParsingResult',
                           [('tree', ast.AST),
                            ('filename', str),
                            ('parse_errors', List[str])])


# Generated at 2022-06-14 02:39:47.455767
# Unit test for constructor of class InputOutput
def test_InputOutput():
    i = InputOutput('a/a.py', 'a/b.py')
    assert i.input == 'a/a.py'
    assert i.output == 'a/b.py'
    with pytest.raises(TypeError):
        InputOutput(1, 1)


# Generated at 2022-06-14 02:39:49.057502
# Unit test for constructor of class InputOutput
def test_InputOutput():
    assert InputOutput(input=Path('input.txt'),
                       output=Path('output.txt'))


# Generated at 2022-06-14 02:39:51.955550
# Unit test for constructor of class InputOutput
def test_InputOutput():
    inp = Path('/a/b/c/x')
    outp = Path('/d/e/f/g')
    io = InputOutput(inp, outp)
    assert io.input == inp
    assert io.output == outp


# Generated at 2022-06-14 02:39:58.892317
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    result = CompilationResult(1, 13, (3, 5), ['foo.py'])
    assert isinstance(result, NamedTuple)
    assert str(result) == 'CompilationResult(files=1, time=13, target=(3, 5), dependencies=[\'foo.py\'])'
    assert result.files == 1
    assert result.time == 13
    assert result.target == (3, 5)
    assert result.dependencies == ['foo.py']


# Generated at 2022-06-14 02:40:01.022946
# Unit test for constructor of class InputOutput
def test_InputOutput():
    assert InputOutput(Path('a'), Path('b')) == \
        ('a', 'b')



# Generated at 2022-06-14 02:40:02.555530
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    result = TransformationResult(tree=None,
                                  tree_changed=True,
                                  dependencies=[])
    assert result.tree is None
    assert result.tree_changed is True
    assert result.dependencies == []

# Generated at 2022-06-14 02:40:06.656219
# Unit test for constructor of class InputOutput
def test_InputOutput():
    # type: () -> None
    inp = Path('input.py')
    outp = Path('output.py')
    pair = InputOutput(inp, outp)
    assert pair.input == inp
    assert pair.output == outp


# Generated at 2022-06-14 02:40:09.610412
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree = ast.parse('pass')

    result = TransformationResult(tree, True, ['dependency1'])

    assert result.tree is tree
    assert result.tree_changed is True
    assert result.dependencies == ['dependency1']

# Generated at 2022-06-14 02:40:17.765059
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    compilation_result = CompilationResult(files=10,
                                           time=15.0,
                                           target=(3, 7),
                                           dependencies=['foo.py', 'bar.py'])
    assert compilation_result.files == 10
    assert compilation_result.time == 15.0
    assert compilation_result.target == (3, 7)
    assert compilation_result.dependencies == ['foo.py', 'bar.py']


# Generated at 2022-06-14 02:40:21.808027
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    assert CompilationResult.files == 'files'
    assert CompilationResult.time == 'time'
    assert CompilationResult.target == 'target'
    assert CompilationResult.dependencies == 'dependencies'


# Generated at 2022-06-14 02:40:26.877395
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    r = CompilationResult(files=10, time=5, target=(2, 5),
                          dependencies=['dep1', 'dep2'])
    assert r.files == 10
    assert r.time == 5
    assert r.target == (2, 5)
    assert r.dependencies == ['dep1', 'dep2']


# Generated at 2022-06-14 02:40:34.612922
# Unit test for constructor of class InputOutput
def test_InputOutput():
    # test creation with pathlib.Path
    input_output1 = InputOutput(input=Path('input.py'),
                                output=Path('output.py'))
    input_output2 = InputOutput(input='input.py',
                                output='output.py')
    input_output3 = InputOutput(input=Path('input.py'),
                                output='output.py')
    input_output4 = InputOutput(input='input.py',
                                output=Path('output.py'))
    assert input_output1 == input_output2
    assert input_output1 == input_output3
    assert input_output1 == input_output4


# Generated at 2022-06-14 02:40:43.367002
# Unit test for constructor of class InputOutput
def test_InputOutput():
    path1 = Path('/tmp/foo')
    path2 = Path('/tmp/bar')
    io = InputOutput(path1, path2)
    assert io.input == path1
    assert io.output == path2
    # Constructor should raise TypeError if any element is not a Path
    with raises(TypeError):
        InputOutput('/tmp/foo', '/tmp/bar')
    with raises(TypeError):
        InputOutput(path1, '/tmp/bar')
    with raises(TypeError):
        InputOutput('/tmp/foo', path2)

# Generated at 2022-06-14 02:40:52.874279
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    """
    Test constructor of class CompilationResult.
    In py.test fixtures should be preferred, but here we need to make sure that
    even if NamedTuple constructor does not work, we will be still able to find
    a bug.
    """
    assert CompilationResult(0, 0.0, (3, 7), []) == \
        CompilationResult(*(0, 0.0, (3, 7), []))
    assert CompilationResult(0, 0.0, (3, 7), []) != \
        CompilationResult(*(1, 0.0, (3, 7), []))
    assert CompilationResult(0, 0.0, (3, 7), []) != \
        CompilationResult(*(0, 1.0, (3, 7), []))

# Generated at 2022-06-14 02:40:58.861726
# Unit test for constructor of class InputOutput
def test_InputOutput():
    # GIVEN
    # A tuple
    values = (Path('a.py'), Path('a.pyc'))

    # WHEN
    # Creating InputOutput from the tuple
    obj = InputOutput(*values)

    # THEN
    # It should have the same values
    assert obj.input == values[0]
    assert obj.output == values[1]


# Generated at 2022-06-14 02:41:04.064641
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    result = CompilationResult(files=0, time=0.0, target=(0, 0), dependencies=[])
    assert result.files == 0
    assert result.time == 0.0
    assert result.target == (0, 0)
    assert result.dependencies == []


# Generated at 2022-06-14 02:41:05.461993
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    # type: () -> None
    TransformationResult(tree=None, tree_changed=False, dependencies=None)

# Generated at 2022-06-14 02:41:10.360513
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    compilation_target = (3, 7)
    compilation_result = CompilationResult(2, 3.0, compilation_target, ['a', 'b'])
    assert compilation_result.files == 2
    assert compilation_result.time == 3.0
    assert compilation_result.target == compilation_target
    assert compilation_result.dependencies == ['a', 'b']


# Generated at 2022-06-14 02:41:18.173527
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    assert TransformationResult(None, True, []).tree is None
    assert TransformationResult(None, True, []).tree_changed is True
    assert TransformationResult(None, True, []).dependencies == []
    assert TransformationResult(None, False, ["a", "c", "b"]).dependencies == ["a", "b", "c"]


# Generated at 2022-06-14 02:41:25.033388
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    # Create tree, which will be transformed
    tree = ast.parse('')
    # Create TransformationResult
    t = TransformationResult(tree, False, ['first', 'second'])
    # Test created TransformationResult
    assert t.tree == tree
    assert t.tree_changed == False
    assert t.dependencies == ['first', 'second']

# Generated at 2022-06-14 02:41:28.418410
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    CompilationResult(1, 2.0, (3, 4), ['a', 'b'])



# Generated at 2022-06-14 02:41:32.142846
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input_output = InputOutput(Path('input'), Path('output'))
    assert input_output.input == Path('input')
    assert input_output.output == Path('output')


# Generated at 2022-06-14 02:41:35.868810
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    cr = CompilationResult(1, 1, (1,1), [])
    assert cr.files == 1
    assert cr.time == 1
    assert cr.target == (1,1)
    assert cr.dependencies == []


# Generated at 2022-06-14 02:41:37.466540
# Unit test for constructor of class InputOutput
def test_InputOutput():
    assert InputOutput(Path('input.py'), Path('output.py'))

# Generated at 2022-06-14 02:41:39.523528
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    result = CompilationResult(files=1, time=0.0, target=(3, 6), dependencies=[])
    assert result.files == 1
    assert result.time == 0.0
    assert result.target == (3, 6)
    assert result.dependencies == []


# Generated at 2022-06-14 02:41:42.941445
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input = Path('test_input')
    output = Path('test_output')
    i_o = InputOutput(input, output)
    assert i_o.input == input
    assert i_o.output == output


# Generated at 2022-06-14 02:41:47.483620
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    result = CompilationResult(files=1, time=2.0,
                               target=(3, 4), dependencies=['wow', 'test'])
    assert isinstance(result, CompilationResult)
    (files, time, target, dependencies) = result
    assert files == 1
    assert time == 2.0
    assert target == (3, 4)
    assert dependencies == ['wow', 'test']

# Generated at 2022-06-14 02:41:53.838434
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree = ast.parse('x = 1')
    res = TransformationResult(tree, True, [])
    assert res.tree == tree and res.tree_changed and len(res.dependencies) == 0
    res = TransformationResult(tree, False, [])
    assert res.tree == tree and not res.tree_changed and len(res.dependencies) == 0

# Test TransformationResult

# Generated at 2022-06-14 02:42:05.229986
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    trans_res = TransformationResult(ast.AST(), True, ['a', 'b'])
    assert trans_res.tree                # type: ignore
    assert trans_res.tree_changed        # type: ignore
    assert trans_res.dependencies == ['a', 'b']


# Return value of transformation of SINGLE file
SingleFileResult = NamedTuple('SingleFileResult',
                              [('path', Path),
                               ('original_size', int),
                               ('new_size', int),
                               ('time', float),
                               ('output', Path)])

# Overall result of transformation.
# Is a list of SingleFileResult
CompilationResult = List[SingleFileResult]

# Type of a transformer.
# A transformer is a function that is called with an AST and returns a new AST
# or None if no changes made.

# Generated at 2022-06-14 02:42:07.554261
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    data = [('tree', ast.AST), ('tree_changed', bool), ('dependencies', List[str])]
    asser

# Generated at 2022-06-14 02:42:11.275522
# Unit test for constructor of class InputOutput
def test_InputOutput():
    io = InputOutput(Path("a"), Path("b"))
    assert io.input == Path("a")
    assert io.output == Path("b")


# Generated at 2022-06-14 02:42:15.213788
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    c_res = CompilationResult(files=23, time=0.5, target=(3, 6), dependencies=[])
    assert c_res.files == 23
    assert c_res.time == 0.5
    assert c_res.target == (3, 6)
    assert c_res.dependencies == []


# Generated at 2022-06-14 02:42:19.288753
# Unit test for constructor of class InputOutput
def test_InputOutput():
    # type: () -> None
    i = InputOutput(Path('in'), Path('out'))
    assert i.input == Path('in')
    assert i.output == Path('out')
    assert str(i) == "InputOutput(input=PosixPath('in'), output=PosixPath('out'))"


# Generated at 2022-06-14 02:42:23.573641
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree = ast.parse('a = 1')
    r = TransformationResult(tree, True, [])
    assert len(r) == 3
    assert r.tree == tree
    assert r.tree_changed == True
    assert r.dependencies == []

# Generated at 2022-06-14 02:42:26.400032
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree = ast.parse('pass')
    trans_res = TransformationResult(tree, False, [])
    assert trans_res.tree is tree
    assert not trans_res.tree_changed
    assert trans_res.dependencies == []

# Generated at 2022-06-14 02:42:39.702531
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    from mypy.util import get_prefix_dirs
    from pytype.pyi import split_prefix_dirs
    import random
    import string

    # Get random prefix dir
    prefix_dirs = sorted(get_prefix_dirs())
    prefix_dirs = [d for d in prefix_dirs if not d.startswith('/tmp')]
    prefix_dirs = split_prefix_dirs(prefix_dirs)
    random_index = random.randint(0, len(prefix_dirs) - 1)
    prefix_dir = prefix_dirs[random_index]

    # Get random module name
    random_size = random.randint(1, 20)

# Generated at 2022-06-14 02:42:44.707520
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    res = CompilationResult(files=1, time=0.1, target=(3, 7),
                            dependencies=['foo', 'bar'])
    assert res.files == 1
    assert res.time == 0.1
    assert res.target == (3, 7)
    assert res.dependencies == ['foo', 'bar']



# Generated at 2022-06-14 02:42:46.583077
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    assert isinstance(TransformationResult(None, False, []),
                      TransformationResult)
    assert isinstance(TransformationResult(None, False, []),
                      TransformationResult)

# Generated at 2022-06-14 02:42:59.530423
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    CompilationResult(9, 12, (3, 7), [])
    CompilationResult(42, 3.14, (2, 4), ['a', 'b'])
    CompilationResult(0, 0.0, (1, 0), [])


# Generated at 2022-06-14 02:43:02.656051
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    t = ast.parse('print("hoi")')
    tr = TransformationResult(tree=t, tree_changed=True, dependencies=['a', 'b'])
    assert tr.tree is t
    assert tr.tree_changed is True
    assert tr.dependencies == ['a', 'b']

# Generated at 2022-06-14 02:43:08.591511
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    # Prepare mock
    mock_new_tree = mock.Mock(spec=ast.AST)
    mock_dependency_list = mock.Mock(spec=List[str])
    # Create object
    TransformationResult(mock_new_tree, True, mock_dependency_list)
    # Check
    assert mock_new_tree is not None
    assert mock_dependency_list is not None

# Generated at 2022-06-14 02:43:10.108044
# Unit test for constructor of class InputOutput
def test_InputOutput():
    assert InputOutput('input', 'output') == InputOutput(input='input', output='output')

# Generated at 2022-06-14 02:43:10.805146
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tr = TransformationResult(None, None, None)

# Generated at 2022-06-14 02:43:18.387508
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    from tree_sitter import Language, Parser
    from tree_sitter.compat import c_string_encoding

    c_code = b"""
        #include <stdio.h>

        int main(int argc, char *argv) {
            printf("Hello, World!\\n");
            return 0;
        }
    """


# Generated at 2022-06-14 02:43:21.470768
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input = Path('input/path')
    output = Path('output/path')
    InputOutput(input=input, output=output)

# Generated at 2022-06-14 02:43:26.680415
# Unit test for constructor of class TransformationResult
def test_TransformationResult():

    ast.parse('1 + 1\n')

    # test object
    tr = TransformationResult(ast.parse('1 + 1\n'), True, ['module'])

    # check type on attributes
    assert type(tr.tree) is ast.AST
    assert type(tr.tree_changed) is bool
    assert type(tr.dependencies) is list

# Generated at 2022-06-14 02:43:31.003968
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    result = CompilationResult(files=2, time=5.3,
                               target=(3, 7), dependencies=['D1', 'D2'])
    assert result.files == 2
    assert result.time == 5.3
    assert result.target == (3, 7)
    assert result.dependencies == ['D1', 'D2']


# Generated at 2022-06-14 02:43:33.012934
# Unit test for constructor of class TransformationResult

# Generated at 2022-06-14 02:43:57.370141
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input = Path('foo')
    output = Path('bar')
    input_output = InputOutput(input, output)
    assert input_output.input == input
    assert input_output.output == output


# Generated at 2022-06-14 02:44:02.313953
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    t = ast.Import(names=[ast.alias(name='foo', asname='bar')])
    result = TransformationResult(t, True, [])
    assert result  # check if namedtuple compiles


__all__ = (
    'CompilationResult',
    'CompilationTarget',
    'InputOutput',
    'TransformationResult',
)

# Generated at 2022-06-14 02:44:04.546274
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    result = TransformationResult(ast.AST(), True, [])
    assert result.tree_changed

# Generated at 2022-06-14 02:44:16.265933
# Unit test for constructor of class InputOutput
def test_InputOutput():
    assert InputOutput(input='a', output='b') == InputOutput(input='a', output='b')
    assert InputOutput(input='a', output='b') != InputOutput(input='a', output='c')
    assert InputOutput(input='a', output='b') != InputOutput(input='c', output='b')
    assert InputOutput(input='a', output='b') != InputOutput(input='c', output='d')
    assert InputOutput(input='a', output='b') < InputOutput(input='c', output='b')
    assert InputOutput(input='a', output='b') < InputOutput(input='a', output='c')
    assert InputOutput(input='a', output='b') < InputOutput(input='c', output='d')

# Generated at 2022-06-14 02:44:23.066689
# Unit test for constructor of class InputOutput
def test_InputOutput():
    # pylint: disable=unused-variable

    # No inputs
    with pytest.raises(TypeError):
        InputOutput(output=None)

    # No outputs
    with pytest.raises(TypeError):
        InputOutput(input=None)

    # No inputs, no outputs
    with pytest.raises(TypeError):
        InputOutput()

    # All good
    io = InputOutput(input=None, output=None)
    assert io.input is None
    assert io.output is None

# Generated at 2022-06-14 02:44:26.188624
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    CompilationResult(files=1,
                      time=0.,
                      target=(3, 4),
                      dependencies=['a', 'b'])

# Generated at 2022-06-14 02:44:28.824999
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tr = TransformationResult(tree=None, tree_changed=False, dependencies=[])
    assert tr.tree is None
    assert tr.tree_changed is False
    assert tr.dependencies == []

# Generated at 2022-06-14 02:44:34.109332
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    data = CompilationResult(files=2,
                             time=3.0,
                             target=(3, 7),
                             dependencies=['foo', 'bar'])
    assert data.files == 2
    assert data.time == 3.0
    assert data.target == (3, 7)
    assert data.dependencies == ['foo', 'bar']


# Generated at 2022-06-14 02:44:37.179994
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input = Path('foo.txt')
    output = Path('bar.txt')
    result = InputOutput(input, output)
    assert result.input == input
    assert result.output == output


# Generated at 2022-06-14 02:44:39.241660
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    assert CompilationResult(0, 0, (3, 4), [])


# Generated at 2022-06-14 02:45:29.694829
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    dependencies = ['A', 'B', 'C']
    target = (2, 7)
    result = CompilationResult(files=1, time=0.1,
                               target=target,
                               dependencies=dependencies)
    assert result.files == 1
    assert result.time == 0.1
    assert result.target == target
    assert result.dependencies == dependencies
    assert result == CompilationResult(
        files=1, time=0.1, target=target, dependencies=dependencies)


# Generated at 2022-06-14 02:45:31.578885
# Unit test for constructor of class InputOutput
def test_InputOutput():
    path = Path('/')
    io = InputOutput(path, path)
    assert io.input == io.output

# Generated at 2022-06-14 02:45:38.309460
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    result = CompilationResult(1, 1.0, (2, 7), ["dep1", "dep2"])
    assert result.files == 1
    assert result.time == 1.0
    assert result.target == (2, 7)
    assert len(result.dependencies) == 2
    assert result.dependencies[0] == 'dep1'
    assert result.dependencies[1] == 'dep2'


# Generated at 2022-06-14 02:45:43.140699
# Unit test for constructor of class InputOutput
def test_InputOutput():
    # GIVEN
    input_path = Path('a.txt')
    output_path = Path('b.txt')

    # WHEN
    io_pair = InputOutput(input_path, output_path)

    # THEN
    assert io_pair.input == input_path
    assert io_pair.output == output_path


# Generated at 2022-06-14 02:45:48.094393
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input = Path('some/path/to/file.py')
    output = Path('some/other/path/to/file.py')
    example = InputOutput(input, output)

    assert example.input == input
    assert example.output == output

# Generated at 2022-06-14 02:45:52.352515
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input = 'test.ini'
    output = 'out.txt'
    input_output = InputOutput(Path(input), Path(output))

    # test if the attrs are correct
    assert input_output.input == Path(input)
    assert input_output.output == Path(output)


# Generated at 2022-06-14 02:45:55.177922
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    # noinspection PyArgumentList
    res = CompilationResult(5,
                            0.5,
                            (3, 6),
                            ['PyQt5', 'six'])
    assert res.files == 5
    assert res.time == 0.5
    assert res.target == (3, 6)
    assert res.dependencies == ['PyQt5', 'six']


# Generated at 2022-06-14 02:45:58.091260
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input = Path('input.txt')
    output = Path('output.txt')
    io = InputOutput(input=input, output=output)
    assert io.input == input
    assert io.output == output


# Generated at 2022-06-14 02:46:02.208196
# Unit test for constructor of class InputOutput
def test_InputOutput():
    with pytest.raises(TypeError):
        result = InputOutput()
    result = InputOutput(Path(), Path())
    assert len(result) == 2
    assert isinstance(result[0], Path)
    assert isinstance(result[1], Path)
    assert result[0] == Path()
    assert result[1] == Path()
    assert result.input == Path()
    assert result.output == Path()

# Generated at 2022-06-14 02:46:06.914271
# Unit test for constructor of class InputOutput
def test_InputOutput():
    source = '/some/source.py'
    target = '/other/target.pyc'
    input_output = InputOutput(input=Path(source), output=Path(target))
    assert input_output.input == Path(source)

# Generated at 2022-06-14 02:47:48.468161
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree = ast.parse("True")

    transformation_result = TransformationResult(tree, False, [])
    assert transformation_result.tree is tree
    assert transformation_result.tree_changed is False
    assert transformation_result.dependencies == []

# Generated at 2022-06-14 02:47:51.279080
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    CompilationResult(files=0, time=0,
                      target=(3, 7),
                      dependencies=['a', 'b', 'c'])


# Generated at 2022-06-14 02:47:57.154692
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    res = TransformationResult(None, False, [])
    assert res.tree is None
    assert not res.tree_changed
    assert res.dependencies == []

# Result of transformer execution
TransformResult = NamedTuple('TransformResult',
                             [('code', str),
                              ('dependencies', List[str])])


# Generated at 2022-06-14 02:48:03.972873
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    compiler = CompilationResult(files=1,
                                 time=0.018,
                                 target=(3, 4),
                                 dependencies=["path.py"])
    assert compiler.files == 1
    assert compiler.time == 0.018
    assert compiler.target == (3, 4)
    assert compiler.dependencies == ["path.py"]


# Generated at 2022-06-14 02:48:06.975250
# Unit test for constructor of class InputOutput
def test_InputOutput():
    """ Unit test for constructor of class InputOutput """
    input_output = InputOutput('a', ['b', 'c'])
    assert input_output.input == 'a'
    assert input_output.output == ['b', 'c']


# Generated at 2022-06-14 02:48:10.325077
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input = Path('x')
    output = Path('y')

    sut = InputOutput(input=input, output=output)

    assert sut.input == input
    assert sut.output == output

# Generated at 2022-06-14 02:48:15.019569
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    code = 'pass'
    tree = ast.parse(code)

    tr = TransformationResult(tree=tree, tree_changed=True, dependencies=[])

    assert(tr.tree_changed == True)
    assert(tr.dependencies == [])
    assert(tr.tree.body[0].value.s == 'pass')

# Generated at 2022-06-14 02:48:26.547168
# Unit test for constructor of class InputOutput
def test_InputOutput():
    assert InputOutput(Path('a'), Path('b')) == InputOutput(Path('a'), Path('b'))
    assert InputOutput(Path('b'), Path('b')) != InputOutput(Path('a'), Path('b'))
    assert InputOutput(Path('a'), Path('a')) != InputOutput(Path('a'), Path('b'))
    assert InputOutput(Path('b'), Path('a')) != InputOutput(Path('a'), Path('b'))
    assert InputOutput(Path('a'), Path('b')) != InputOutput(Path('b'), Path('a'))
    assert InputOutput(Path('b'), Path('a')) != InputOutput(Path('a'), Path('a'))
    assert InputOutput(Path('a'), Path('a')) != InputOutput(Path('b'), Path('b'))
    assert Input

# Generated at 2022-06-14 02:48:32.860516
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    files = 1
    time = 2.0
    target = (3, 4)
    dependencies = ['a', 'b', 'c']

    result = CompilationResult(files, time, target, dependencies)

    assert result.files == files
    assert result.time == time
    assert result.target == target
    assert result.dependencies == dependencies


# Generated at 2022-06-14 02:48:36.858971
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input_output = InputOutput(Path('a.py'), Path('b.py'))
    assert input_output.input == Path('a.py')
    assert input_output.output == Path('b.py')
