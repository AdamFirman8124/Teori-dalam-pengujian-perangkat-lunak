

# Generated at 2022-06-14 02:39:05.495257
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    data = CompilationResult(files=1, time=123.4, target=(3, 8),
                             dependencies=['dep1'])
    assert data.files == 1
    assert data.time == 123.4
    assert data.target == (3, 8)
    assert data.dependencies == ['dep1']


# Generated at 2022-06-14 02:39:06.438620
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    CompilationResult(1, 2.0, (3, 4), ['a', 'b'])



# Generated at 2022-06-14 02:39:09.258236
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    result = TransformationResult(None, None, None)
    result.tree
    result.tree_changed
    result.dependencies
    result.tree = None
    result.tree_changed = None
    result.dependencies = None

# Generated at 2022-06-14 02:39:11.460027
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    node = ast.parse('x + y')
    result = TransformationResult(node, True, [])
    assert result.tree is node
    assert result.tree_changed is True
    assert result.dependencies == []

# Generated at 2022-06-14 02:39:16.591338
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input = Path('input')
    output = Path('output')
    assert InputOutput(input, output) == InputOutput(input, output)
    assert InputOutput(input, output).input == input
    assert InputOutput(input, output).output == output
    result = InputOutput(input, output)
    assert result.input == input
    assert result.output == output


# Generated at 2022-06-14 02:39:20.154307
# Unit test for constructor of class InputOutput
def test_InputOutput():
    i = Path('/etc/hosts')
    o = Path('/tmp/hosts')
    p = InputOutput(i, o)
    assert p.input.name == i.name



# Generated at 2022-06-14 02:39:24.646288
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input_path = Path('input')
    output_path = Path('output')
    result = InputOutput(input_path, output_path)
    assert result.input == input_path
    assert result.output == output_path



# Generated at 2022-06-14 02:39:26.477896
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    _ = CompilationResult(100, 100.0, (3, 5), ['a.py'])



# Generated at 2022-06-14 02:39:31.856548
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tr = TransformationResult(ast.parse(""), False, list())
    assert tr.tree_str() == "Module(body=[])"
    tr = TransformationResult(ast.parse("pass"), False, list())
    assert tr.tree_str() == "Module(body=[Pass()])"
    tr = TransformationResult(ast.parse("pass"), True, list())
    assert tr.tree_str() == "Module(body=[Pass()])"

# Generated at 2022-06-14 02:39:38.254137
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    # Create a compilation result
    compilation_result = CompilationResult(files=17, time=13.52,
                                           target=(3, 6),
                                           dependencies=["foo", "bar"])
    # assert the fields have the expected values
    assert compilation_result.files == 17
    assert compilation_result.time == 13.52
    assert compilation_result.target == (3, 6)
    assert compilation_result.dependencies == ["foo", "bar"]


# Generated at 2022-06-14 02:39:40.163409
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    assert TransformationResult(None, False, [])

# Generated at 2022-06-14 02:39:42.650350
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    assert TransformationResult(ast.Module(body=[], type_ignores=[]),
                                False,
                                []) == TransformationResult(ast.Module(body=[], type_ignores=[]),
                                                            False,
                                                            [])

# Generated at 2022-06-14 02:39:47.506195
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    cr = CompilationResult(files=10, time=0.1, target=(3, 7),
                           dependencies=['dep1', 'dep2'])
    assert cr.files == 10
    assert cr.time == 0.1
    assert cr.target == (3, 7)
    assert cr.dependencies == ['dep1', 'dep2']

# Generated at 2022-06-14 02:39:50.388535
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    out = CompilationResult(1, 2.0, (3, 4), ['A', 'B', 'C'])
    assert out.files == 1
    assert out.time == 2.0
    assert out.target == (3, 4)
    assert out.dependencies == ['A', 'B', 'C']


# Generated at 2022-06-14 02:39:52.869805
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    assert CompilationResult(1, 0.1, (3, 5), ['a', 'b']) == CompilationResult(
        1, 0.1, (3, 5), ['a', 'b'])


# Generated at 2022-06-14 02:39:56.521707
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input = Path('foo/bar')
    output = Path('foo/baz')
    test_cond = InputOutput(input, output)
    assert test_cond.input == input
    assert test_cond.output == output


# Generated at 2022-06-14 02:40:00.987846
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    import astor
    node = ast.parse('pass')
    tr = TransformationResult(node, True, [])
    assert isinstance(tr.tree, ast.AST)
    assert tr.tree_changed == True
    assert tr.dependencies == []
    assert astor.to_source(tr.tree) == 'pass'
    assert isinstance(tr, TransformationResult)

# Generated at 2022-06-14 02:40:02.861021
# Unit test for constructor of class InputOutput
def test_InputOutput():
    assert InputOutput(input=Path("input"), output=Path("output")) \
        == InputOutput("input", "output")

# Generated at 2022-06-14 02:40:05.053352
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tr = TransformationResult(None, None, None)
    assert tr

# Key for saving the result of the compilation to Redis

# Generated at 2022-06-14 02:40:07.981634
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tr = TransformationResult(tree=ast.parse('print("Hello world!")'),
                              tree_changed=True,
                              dependencies=['a.py', 'b.py'])
    assert tr.tree_changed

# Generated at 2022-06-14 02:40:12.839960
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    assert TransformationResult(ast.Module([]),
                                True,
                                []) == (ast.Module([]),
                                        True,
                                        [])

# Generated at 2022-06-14 02:40:16.592779
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    cr = CompilationResult(files=0, time=0, target=(2, 7), dependencies=[])
    assert cr.files == 0
    assert cr.time == 0
    assert cr.target == (2, 7)
    assert cr.dependencies == []


# Generated at 2022-06-14 02:40:19.649664
# Unit test for constructor of class InputOutput
def test_InputOutput():
    io = InputOutput(Path('./in'), Path('./out'))
    assert io.input == './in'
    assert io.output == './out'


# Generated at 2022-06-14 02:40:23.105857
# Unit test for constructor of class InputOutput
def test_InputOutput():
    assert InputOutput(Path('a.py'), Path('b.py'))
    assert InputOutput(Path('a.py'), Path('b.py')).dependencies == []



# Generated at 2022-06-14 02:40:31.959426
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    import random
    import time

    # Get random target
    major = random.randint(0, 2)
    minor = random.randint(0, 5)
    target = CompilationTarget(major, minor)

    # Get random files
    files = random.randint(0, 10)

    # Get random time
    time_taken = random.uniform(0, 10)

    # Get random dependencies
    dependencies = ['', '', '']

    # Test object
    result = CompilationResult(files, time_taken, target, dependencies)

    # Test values
    assert result.files == files
    assert result.time == time_taken
    assert result.target == target
    assert result.dependencies == dependencies


# Generated at 2022-06-14 02:40:36.568584
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input = Path('1.py')
    output = Path('2.py')
    subject = InputOutput(input, output)
    assert subject.input == input
    assert subject.output == output

# Generated at 2022-06-14 02:40:43.367481
# Unit test for constructor of class CompilationResult
def test_CompilationResult(): # type: () -> None
    result = CompilationResult(files=100, time=0.5, target=(3, 5),
                               dependencies=['foo', 'bar'])
    fields = result._asdict()
    assert fields['files'] == 100
    assert fields['time'] == 0.5
    assert fields['target'] == (3, 5)
    assert fields['dependencies'] == ['foo', 'bar']



# Generated at 2022-06-14 02:40:52.427416
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    res1 = TransformationResult(ast.parse('pass'), True, [])
    res2 = TransformationResult(ast.parse('pass'), True, ['dep1', 'dep2'])
    assert res1 != res2
    res1.dependencies = [1, 2, 3]
    assert res1 != res2

# Result of running a test
TestResult = NamedTuple('TestResult',
                        [('files', int),
                         ('inputs', List[InputOutput]),
                         ('dependencies', List[str])])

# Result of running a program
ProgramResult = NamedTuple('ProgramResult',
                           [('files', int),
                            ('inputs', List[InputOutput]),
                            ('dependencies', List[str])])


# Generated at 2022-06-14 02:40:56.556302
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree = ast.parse('')
    tree_changed = True
    dependencies = []
    tr = TransformationResult(tree, tree_changed, dependencies)
    assert tr.tree == tree
    assert tr.tree_changed == tree_changed
    assert tr.dependencies == dependencies

# Generated at 2022-06-14 02:41:00.267098
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree = ast.AST()
    result = TransformationResult(tree, True, [])
    assert result.tree is tree
    assert result.tree_changed is True
    assert result.dependencies == []


# Generated at 2022-06-14 02:41:09.201703
# Unit test for constructor of class InputOutput
def test_InputOutput():
    # Given
    input_file = Path('/tmp/input.txt')
    output_file = Path('/tmp/output.txt')
    pair = InputOutput(input_file, output_file)

    # When
    actual_input = pair.input
    actual_output = pair.output

    # Then
    assert actual_input == input_file
    assert actual_output == output_file



# Generated at 2022-06-14 02:41:12.832441
# Unit test for constructor of class InputOutput
def test_InputOutput():
    test_input = Path('/test/input')
    test_output = Path('/test/output')
    test_obj = InputOutput(test_input, test_output)
    assert test_obj.input == test_input
    assert test_obj.output == test_output

# Generated at 2022-06-14 02:41:16.995747
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    c = CompilationResult(files=0, time=0, target=(3, 7), dependencies=[])
    assert c.files == 0
    assert c.time == 0
    assert c.target == (3, 7)
    assert c.dependencies == []


# Generated at 2022-06-14 02:41:19.802703
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    r = CompilationResult(1, 0.1, (2, 7), [])
    assert r.files == 1
    assert r.time == 0.1
    assert r.target == (2, 7)
    assert r.dependencies == []


# Generated at 2022-06-14 02:41:26.070153
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    cr = CompilationResult(files=2,
                           time=0.1,
                           target=(6, 1),
                           dependencies=['a', 'b'])
    assert cr.files == 2
    assert cr.time == 0.1
    assert cr.target == (6, 1)
    assert cr.dependencies == ['a', 'b']


# Generated at 2022-06-14 02:41:31.897816
# Unit test for constructor of class InputOutput
def test_InputOutput():
    # Arrange
    input_name = 'foobar'
    # Act
    input_output = InputOutput(Path(input_name), Path(input_name))
    # Assert
    assert input_name == input_output.input.name
    assert input_name == input_output.output.name

# Generated at 2022-06-14 02:41:36.072417
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input_file = "input_file"
    output_file = "output_file"
    io = InputOutput(input=input_file, output=output_file)

    assert io.input == input_file
    assert io.output == output_file



# Generated at 2022-06-14 02:41:39.349782
# Unit test for constructor of class InputOutput
def test_InputOutput():
    i = Path('input')
    o = Path('output')
    input_output = InputOutput(input=i, output=o)
    assert input_output.input == i
    assert input_output.output == o

# Generated at 2022-06-14 02:41:41.897162
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    assert CompilationResult(1, 1.0, (3, 6), [])

# Generated at 2022-06-14 02:41:43.682068
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    CompilationResult(files=2, time=3, target=(3, 7), dependencies=["a", "b"])

# Generated at 2022-06-14 02:41:54.370118
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    with pytest.raises(TypeError):
        TransformationResult(None, True, [])
    with pytest.raises(TypeError):
        TransformationResult(ast.Name('a', ast.Store()), True, [])
    with pytest.raises(TypeError):
        TransformationResult(ast.Name('a', ast.Store()),
                             'True', [])
    with pytest.raises(TypeError):
        TransformationResult(ast.Name('a', ast.Store()),
                             True, None)
    with pytest.raises(TypeError):
        TransformationResult(ast.Name('a', ast.Store()),
                             True, [None])
    with pytest.raises(TypeError):
        TransformationResult(ast.Name('a', ast.Store()),
                             True, [None, 1])

# Generated at 2022-06-14 02:41:58.708641
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input_path = Path('path/to/input.py')
    output_path = Path('path/to/output.py')
    io = InputOutput(input_path, output_path)
    assert io.input == input_path
    assert io.output == output_path

# Generated at 2022-06-14 02:42:02.836698
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    res = CompilationResult(100, 12345.67, (3, 8), ['dep1', 'dep2'])
    assert res.files == 100
    assert res.time == 12345.67
    assert res.target == (3, 8)
    assert res.dependencies == ['dep1', 'dep2']


# Generated at 2022-06-14 02:42:10.514524
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    t1 = ast.parse('x')
    t2 = ast.parse('y')
    assert type(TransformationResult(t1, True, [])) == TransformationResult
    assert type(TransformationResult(t2, False, [])) == TransformationResult


# Input/output pair with dependencies
InputOutputDependencies = NamedTuple('InputOutputDependencies',
                                     [('input_output', InputOutput),
                                      ('dependencies', List[str])])


# Generated at 2022-06-14 02:42:13.110272
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree = ast.Module([])
    tree_changed = True
    dependencies = ['a', 'b']
    TransformationResult(tree, tree_changed, dependencies)



# Generated at 2022-06-14 02:42:16.151127
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    CompilationResult._make((1, 1.1, (3, 5), 'foo'))

    assert CompilationResult(1, 1.1, (3, 5), 'foo') == CompilationResult._make((1, 1.1, (3, 5), 'foo'))


# Generated at 2022-06-14 02:42:24.154650
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    # Test empty constructor
    cr = CompilationResult()
    assert cr.files == 0
    assert cr.time == 0.0
    assert cr.target == (0, 0)
    assert cr.dependencies == []
    # Test nonempty constructor
    cr = CompilationResult(42, 42.42, (3, 6), ["spam", "egg", "ham"])
    assert cr.files == 42
    assert cr.time == 42.42
    assert cr.target == (3, 6)
    assert cr.dependencies == ["spam", "egg", "ham"]


# Generated at 2022-06-14 02:42:25.958036
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    result = TransformationResult(ast.parse(''), False, [])
    assert result.tree_changed == False
    assert len(result.dependencies) == 0

# Generated at 2022-06-14 02:42:30.530133
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    TransformationResult(ast.parse('1'),
                         True,
                         ['a', 'b'])
    TransformationResult(ast.parse('1'),
                         False,
                         ['a', 'b'])
    TransformationResult(ast.parse('1'),
                         True,
                         [])

# Generated at 2022-06-14 02:42:33.672411
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree = ast.parse('a = 1')
    result = TransformationResult(tree, False, [])
    assert result.tree_changed == False
    assert result.dependencies == []

# Generated at 2022-06-14 02:42:45.589454
# Unit test for constructor of class InputOutput
def test_InputOutput():
    # Check if InputOutput can be constructed.
    # This test also verifies that mypy doesn't break.
    IO = InputOutput(input=Path('abc'), output=Path('abc'))  # type: ignore
    assert IO.input == Path('abc')
    assert IO.output == Path('abc')


# Generated at 2022-06-14 02:42:48.532377
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    ComRes = CompilationResult(files=1, time=1, target=(1, 1), dependencies=[])
    assert ComRes.files == 1 and ComRes.time == 1 and ComRes.target == (1, 1) and ComRes.dependencies == []


# Generated at 2022-06-14 02:42:50.194476
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tr = TransformationResult(ast.AST(), False, ["a"])
    tr = TransformationResult(ast.AST(), True, ["b"])

# Generated at 2022-06-14 02:42:55.567374
# Unit test for constructor of class TransformationResult
def test_TransformationResult():  # type: () -> None
    ast_tree = ast.parse("print(123)")
    assert type(ast_tree) == ast.Module

    tr = TransformationResult(ast_tree, True, [])

    assert type(tr) == TransformationResult
    assert type(tr.tree) == ast.Module
    assert tr.tree_changed == True
    assert tr.dependencies == []

# Generated at 2022-06-14 02:43:00.390906
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    # type: () -> None
    cr = CompilationResult(0, 0.0, (0, 0), [])
    assert cr.files == 0
    assert cr.time == 0.0
    assert cr.target == (0, 0)
    assert cr.dependencies == []
    assert cr == CompilationResult(0, 0.0, (0, 0), [])


# Generated at 2022-06-14 02:43:04.450670
# Unit test for constructor of class InputOutput
def test_InputOutput():
    p = Path('a')
    q = Path('b')
    io = InputOutput(p, q)
    assert io.input == p
    assert io.output == q


# Generated at 2022-06-14 02:43:09.942706
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree = ast.parse('a = 1')
    tree_changed = True
    dependencies = ['a', 'b']

    # Expected result
    result = TransformationResult(tree, tree_changed, dependencies)

    # Check
    assert result.tree == tree
    assert result.tree_changed == tree_changed
    assert result.dependencies == dependencies


# Generated at 2022-06-14 02:43:18.214303
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree = ast.parse("""pass""")
    assert TransformationResult(tree, False, []).tree is tree
    assert TransformationResult(tree, True, []).tree is tree
    assert TransformationResult(tree, False, []).tree_changed is False
    assert TransformationResult(tree, True, []).tree_changed is True
    assert TransformationResult(tree, False, []).dependencies == []
    assert TransformationResult(tree, True, []).dependencies == []
    assert TransformationResult(tree, False, ['a']).dependencies == ['a']
    assert TransformationResult(tree, True, ['a']).dependencies == ['a']

# Generated at 2022-06-14 02:43:18.922254
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    pass

# Generated at 2022-06-14 02:43:25.130585
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    compilation_result = CompilationResult(
        files=3, time=4.4, target=(3, 4), dependencies=[])
    assert compilation_result.files == 3
    assert compilation_result.time == 4.4
    assert compilation_result.target == (3, 4)
    assert compilation_result.dependencies == []


# Generated at 2022-06-14 02:43:35.719497
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    CompilationResult(0, 0.0, (3, 6), [])



# Generated at 2022-06-14 02:43:39.758034
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree = ast.parse('pass')
    trans_res = TransformationResult(tree, True, [])
    assert trans_res.tree == tree
    assert trans_res.tree_changed == True
    assert trans_res.dependencies == []

# Generated at 2022-06-14 02:43:48.626749
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    t = ast.Module()
    d = []
    n = ast.Name()
    n.id = "foo"
    assert TransformationResult(tree=t, tree_changed=False, dependencies=d) == \
        TransformationResult(tree=t, tree_changed=False, dependencies=d)
    assert TransformationResult(tree=n, tree_changed=True, dependencies=d) == \
        TransformationResult(tree=n, tree_changed=True, dependencies=d)
    assert TransformationResult(tree=n, tree_changed=True, dependencies=d) != \
        TransformationResult(tree=t, tree_changed=True, dependencies=d)
    assert TransformationResult(tree=n, tree_changed=False, dependencies=d) != \
        TransformationResult(tree=n, tree_changed=True, dependencies=d)

# Generated at 2022-06-14 02:43:50.145792
# Unit test for constructor of class InputOutput
def test_InputOutput():
    assert InputOutput(input="1", output="2") == ("1", "2")


# Generated at 2022-06-14 02:43:51.222495
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    CompilationResult(1, 1, (3, 6), [])



# Generated at 2022-06-14 02:43:55.226658
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input_output = InputOutput(Path('./file.py'), Path('./file.pyc'))
    assert input_output.input.name == 'file.py'
    assert input_output.output.name == 'file.pyc'

# Generated at 2022-06-14 02:43:59.431009
# Unit test for constructor of class InputOutput
def test_InputOutput():
    data = InputOutput(input=Path('a.txt'), output=Path('b.txt'))

    assert(data.input == Path('a.txt'))
    assert(data.output == Path('b.txt'))



# Generated at 2022-06-14 02:44:04.252795
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input_path = Path('input')
    output_path = Path('output')
    input_output = InputOutput(input_path, output_path)
    assert input_path == input_output.input
    assert output_path == input_output.output
    assert isinstance(repr(input_output), str)
    assert isinstance(str(input_output), str)


# Generated at 2022-06-14 02:44:12.359290
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    assert TransformationResult(tree=None,
                                tree_changed=False,
                                dependencies=[]).tree is None
    assert TransformationResult(tree=None,
                                tree_changed=False,
                                dependencies=['a']).dependencies == ['a']
    assert TransformationResult(tree=ast.Module(body=[]),
                                tree_changed=True,
                                dependencies=[]).tree_changed

if __name__ == "__main__":
    test_TransformationResult()

# Generated at 2022-06-14 02:44:15.485539
# Unit test for constructor of class InputOutput
def test_InputOutput():
    i = InputOutput(Path('foo.py'), Path('bar.py'))
    assert i.input == Path('foo.py')
    assert i.output == Path('bar.py')


# Generated at 2022-06-14 02:44:50.850385
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    t = ast.parse('')
    t_d = ast.parse('import random')
    r1 = TransformationResult(tree=t, tree_changed=False, dependencies=[])
    r2 = TransformationResult(tree=t_d, tree_changed=True, dependencies=['random'])
    assert r1.tree == t
    assert not r1.tree_changed
    assert r1.dependencies == []
    assert r2.tree == t_d
    assert r2.tree_changed
    assert r2.dependencies == ['random']


__all__ = ['CompilationResult', 'InputOutput',
           'TransformationResult', 'test_TransformationResult']

# Generated at 2022-06-14 02:44:58.606584
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    import astor
    assert TransformationResult is not None, "unable to create transformation result"
    assert 'tree' in dir(TransformationResult)
    assert 'tree_changed' in dir(TransformationResult)
    assert 'dependencies' in dir(TransformationResult)

    tree = ast.parse("x = 1")
    assert isinstance(tree, ast.Module)
    tr = TransformationResult(tree, True, ['foo', 'bar'])
    assert tr.tree_changed == True
    assert len(tr.dependencies) == 2
    assert tr.dependencies[0] == 'foo'
    assert tr.dependencies[1] == 'bar'
    assert astor.codegen.to_source(tr.tree) == "x = 1"

# Generated at 2022-06-14 02:45:03.260769
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input = Path("main.py")
    output = Path("target.py")
    iop = InputOutput(input, output)
    assert iop.input == input
    assert iop.output == output

# Generated at 2022-06-14 02:45:05.750594
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input = Path('/home/test/input')
    output = Path('/home/test/output')
    io = InputOutput(input, output)
    assert io.input == input
    assert io.output == output


# Generated at 2022-06-14 02:45:09.252443
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input = Path('input')
    output = Path('output')
    io = InputOutput(input, output)
    assert io.input == input
    assert io.output == output


# Generated at 2022-06-14 02:45:12.306506
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    CompilationResult(1, 1.0, (3, 7), ['foo', 'bar'])


# Generated at 2022-06-14 02:45:16.205775
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    cr = CompilationResult(files=2, time=10.0, target=(3, 7), dependencies=['foo', 'bar'])
    assert cr.files == 2
    assert cr.time == 10.0
    assert cr.target == (3, 7)
    assert cr.dependencies == ['foo', 'bar']


# Generated at 2022-06-14 02:45:22.678906
# Unit test for constructor of class InputOutput
def test_InputOutput():
    inp = Path('foo.txt')
    outp = Path('bar.txt')
    in_out = InputOutput(inp, outp)
    assert in_out.input == inp
    assert in_out.output == outp
    in_out.input = Path('quuz.txt')
    in_out.output = Path('baz.txt')
    assert in_out.input == Path('quuz.txt')
    assert in_out.output == Path('baz.txt')


# Generated at 2022-06-14 02:45:27.240167
# Unit test for constructor of class TransformationResult
def test_TransformationResult(): # pylint: disable=invalid-name
    a = TransformationResult(ast.parse('a'), False, ['a', 'b'])
    assert type(a.tree) == ast.Module
    assert a.tree_changed == False
    assert a.dependencies == ['a', 'b']

# Compiler error

# Generated at 2022-06-14 02:45:32.229711
# Unit test for constructor of class InputOutput
def test_InputOutput():
    i1 = Path("/a/b/c")
    o1 = Path("/a/b/c")
    io1 = InputOutput(i1, o1)
    assert io1.input is i1
    assert io1.output is o1


# Generated at 2022-06-14 02:46:19.782421
# Unit test for constructor of class InputOutput
def test_InputOutput():
    i = Path('in')
    o = Path('out')
    assert InputOutput(i, o).input == i
    assert InputOutput(i, o).output == o


# Generated at 2022-06-14 02:46:24.748002
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tr1 = TransformationResult(ast.Module(body=[]), True, ['d1', 'd2'])
    tr2 = TransformationResult(ast.Module(body=[]), False, [])
    tr3 = TransformationResult(ast.Module(body=[]), True, [])
    assert tr1 is not None
    assert tr2 is not None
    assert tr3 is not None
    assert tr1.tree_changed
    assert not tr2.tree_changed
    assert tr3.tree_changed

# Generated at 2022-06-14 02:46:29.307835
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    cr = CompilationResult(files=0, time=0.0, target=(3, 7), dependencies=[])
    assert cr.files == 0
    assert cr.time == 0.0
    assert cr.target == (3, 7)
    assert cr.dependencies == []


# Result of rewriter transformation
RewritingResult = NamedTuple('RewritingResult',
                             [('source', str),
                              ('source_changed', bool),
                              ('dependencies', List[str])])


# Generated at 2022-06-14 02:46:34.776227
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    assert TransformationResult(None, False, []) != None # noqa

# Result of parser, either successful with AST or with error
ParseResult = NamedTuple('ParseResult',
                         [('ast', ast.AST),
                          ('error', str)])

# Transformer result
TransformerResult = NamedTuple('TransformerResult',
                               [('name', str),
                                ('result', TransformationResult),
                                ('time', float)])

# Transformation configuration
TransformerConfig = NamedTuple('TransformerConfig',
                               [('disable', List[str]),
                                ('enable', List[str]),
                                ('verbose', bool),
                                ('disabled_unless_depends', List[str])])
TransformerConfig.__new__.__defaults__ = (None, None, False, None)

# Execution

# Generated at 2022-06-14 02:46:37.832831
# Unit test for constructor of class InputOutput
def test_InputOutput():
    inp = Path('foo.py')
    out = Path('bar.py')
    io = InputOutput(input=inp, output=out)
    assert io.input == inp
    assert io.output == out

# Generated at 2022-06-14 02:46:41.249887
# Unit test for constructor of class InputOutput
def test_InputOutput():
    abstract_input = Path('input')
    abstract_output = Path('output')
    input_output = InputOutput(abstract_input, abstract_output)
    assert input_output.input == abstract_input
    assert input_output.output == abstract_output

# Generated at 2022-06-14 02:46:44.863185
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input = Path("a")
    output = Path("b")
    assert InputOutput(input, output).input == input
    assert InputOutput(input, output).output == output

# Generated at 2022-06-14 02:46:48.115927
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    CompilationResult(files=42, time=3.14,
                      target=(3, 7), dependencies=['foo', 'bar'])

# Generated at 2022-06-14 02:46:54.280234
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    compilation_result = CompilationResult(files=3, time=2.4,
                                           target=(3, 7),
                                           dependencies=['shared/module.py', 'shared/module2.py'])

    assert compilation_result.files == 3
    assert compilation_result.time == 2.4
    assert compilation_result.target == (3, 7)
    assert compilation_result.dependencies == ['shared/module.py', 'shared/module2.py']

# Generated at 2022-06-14 02:46:57.615375
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    result = CompilationResult(1, 2, (3, 4), [5])
    assert result.files == 1
    assert result.time == 2
    assert result.target == (3, 4)
    assert result.dependencies == [5]


# Generated at 2022-06-14 02:48:37.016016
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    CompilationResult(files=1,
                      time=1e-3,
                      target=(3, 6),
                      dependencies=['foo', 'bar'])

# Generated at 2022-06-14 02:48:38.770171
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    comp_result = CompilationResult(files=15, time=10.0, target=(2, 7), dependencies=[])

# Generated at 2022-06-14 02:48:42.023945
# Unit test for constructor of class InputOutput
def test_InputOutput():
    path1 = Path('/tmp/foo')
    path2 = Path('/tmp/bar')
    file  = InputOutput(path1, path2)
    assert file.input == path1
    assert file.output == path2


# Generated at 2022-06-14 02:48:43.882864
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    CompilationResult(1, 2.0, (3, 4), ['a', 'b', 'c', 'd'])


# Generated at 2022-06-14 02:48:47.376852
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    c = CompilationResult(10, 1.0, (2, 7), ['foo.py'])
    assert c.files == 10
    assert c.time == 1.0
    assert c.target == (2, 7)
    assert c.dependencies == ['foo.py']


# Generated at 2022-06-14 02:48:55.468056
# Unit test for constructor of class InputOutput
def test_InputOutput():
    path_in = Path('some/path')
    path_out = Path('some/other/path')
    expected_cstr = 'InputOutput(input=%s, output=%s)' % (str(path_in), str(path_out))
    pair = InputOutput(input=path_in, output=path_out)
    assert pair.input == path_in, \
        'Incorrect input in constructor result: ' + pair.input
    assert pair.output == path_out, \
        'Incorrect output in constructor result: ' + pair.output
    assert str(pair) == expected_cstr, \
        'toString representation of pair is incorrect: ' + str(pair)


# Generated at 2022-06-14 02:48:59.340339
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    # type: () -> None
    assert CompilationResult(1, 1.0, (2, 7), ["a", "b", "c"])


# Generated at 2022-06-14 02:49:03.250578
# Unit test for constructor of class InputOutput
def test_InputOutput():
    i, o = Path('a'), Path('b')
    in_out = InputOutput(i, o)
    assert in_out.input == i
    assert in_out.output == o