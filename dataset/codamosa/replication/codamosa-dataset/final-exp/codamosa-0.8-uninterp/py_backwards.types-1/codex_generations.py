

# Generated at 2022-06-14 02:39:10.600747
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    # type: () -> None
    obj = TransformationResult(tree=None, tree_changed=False, dependencies=[])
    assert obj.tree == None
    assert obj.tree_changed == False
    assert obj.dependencies == []

    obj = TransformationResult(tree=None, tree_changed=True, dependencies=[])
    assert obj.tree == None
    assert obj.tree_changed == True
    assert obj.dependencies == []

    obj = TransformationResult(tree=None,
                               tree_changed=False,
                               dependencies=['/usr/lib/foo.py', '/etc/bar.py'])
    assert obj.tree == None
    assert obj.tree_changed == False
    assert obj.dependencies == ['/usr/lib/foo.py', '/etc/bar.py']


# Compilation source and target

# Generated at 2022-06-14 02:39:13.113497
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    ast_tree = ast.parse('__import__("os")')
    dependencies = ['os']
    tr = TransformationResult(tree=ast_tree,
                              tree_changed=True,
                              dependencies=dependencies)
    assert tr.tree == ast_tree
    assert tr.tree_changed == True
    assert tr.dependencies == dependencies

# Generated at 2022-06-14 02:39:19.333654
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input = Path('/input')
    output = Path('/output')

    # Only input
    assert InputOutput(input, None) == InputOutput(input=input, output=None)

    # Only output
    assert InputOutput(None, output) == InputOutput(input=None, output=output)

    # Both
    assert InputOutput(input, output) == InputOutput(input=input, output=output)

# Generated at 2022-06-14 02:39:25.882323
# Unit test for constructor of class TransformationResult
def test_TransformationResult():  # type: () -> None
    result = TransformationResult(tree=None, tree_changed=None,
                                  dependencies=None)

    assert isinstance(result, TransformationResult)
    assert isinstance(result.tree, ast.AST)
    assert isinstance(result.tree_changed, bool)
    assert isinstance(result.dependencies, list)

# Result of transformers transformation
TransformationResult = NamedTuple('TransformationResult',
                                  [('tree', ast.AST),
                                   ('tree_changed', bool),
                                   ('dependencies', List[str])])

# Generated at 2022-06-14 02:39:29.916627
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree = ast.parse("print('foo')")
    assert tree is not None
    res = TransformationResult(tree, True, [])
    assert isinstance(res, TransformationResult)
    assert res.tree is not None
    assert res.tree_changed is True
    assert res.dependencies == []


# Generated at 2022-06-14 02:39:39.822588
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    class Test1:
        def __init__(self):
            self.tree = ast.parse('print("Hello, world!")')
            self.tree_changed = True
            self.dependencies = ['/home/user/test1.py']
        def __eq__(self, other):
            return Test1.__eq__(self, other)
        def __ne__(self, other):
            return Test1.__ne__(self, other)
        def __hash__(self):
            return Test1.__hash__(self)
    class Test2:
        def __init__(self):
            self.tree = ast.parse('print("Hello, world!")')
            self.tree_changed = True
            self.dependencies = ['/home/user/test1.py']
    assert Test1() == Test2

# Generated at 2022-06-14 02:39:42.352159
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    result = TransformationResult(tree=None, tree_changed=False, dependencies=[])

    assert result.tree is None
    assert result.tree_changed is False
    assert result.dependencies == []


# Generated at 2022-06-14 02:39:43.875216
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    CompilationResult(files=1, time=2.0, target=(10, 20), dependencies=["a", "b"])


# Generated at 2022-06-14 02:39:49.342021
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    compilation_result = CompilationResult(files=2, time=10, target=(3, 4),
                                           dependencies=['dep1', 'dep2'])
    assert compilation_result.files == 2
    assert compilation_result.time == 10
    assert compilation_result.target == (3, 4)
    assert compilation_result.dependencies == ['dep1', 'dep2']

# Generated at 2022-06-14 02:39:52.232901
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input_ = Path('input')
    output = Path('output')

    a = InputOutput(input_, output)

    assert isinstance(a, InputOutput)
    assert a.input == input_
    assert a.output == output

# Generated at 2022-06-14 02:40:00.709642
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    res = CompilationResult(files=5,
                            time=1.0,
                            target=(3, 7),
                            dependencies=['/a/b/c/d.py'])
    assert res.files == 5
    assert res.time == 1.0
    assert res.target == (3, 7)
    assert res.dependencies == ['/a/b/c/d.py']


# Generated at 2022-06-14 02:40:04.559625
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    r = CompilationResult(files=1, time=1.0, target=(3,6), dependencies=[])
    assert r.files == 1
    assert r.time == 1.0
    assert r.target == (3, 6)
    assert r.dependencies == []

# Generated at 2022-06-14 02:40:07.485098
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input = Path("A.py")
    output = Path("B.py")
    io = InputOutput(input, output)
    assert io.input == input
    assert io.output == output


# Generated at 2022-06-14 02:40:13.286328
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    result = CompilationResult(files=3,
                               time=1.1,
                               target=(3, 5),
                               dependencies=['idx.py'])
    assert result
    # pylint: disable=unsubscriptable-object
    assert result[0] == 3
    assert result.files == 3
    # pylint: enable=unsubscriptable-object


# Generated at 2022-06-14 02:40:24.710813
# Unit test for constructor of class InputOutput
def test_InputOutput():
    assert InputOutput(Path('a/b/c.py'), Path('d/e/f.py')) == \
           InputOutput(Path('a/b/c.py'), Path('d/e/f.py'))
    assert InputOutput(Path('a/b/c.py'), Path('d/e/f.py')) != \
           InputOutput(Path('a/b/c.py'), Path('d/e/f1.py'))
    assert InputOutput(Path('a/b/c.py'), Path('d/e/f.py')) != \
           InputOutput(Path('a/b/c1.py'), Path('d/e/f.py'))
    assert InputOutput(Path('a/b/c.py'), Path('d/e/f.py')) != \
           InputOutput

# Generated at 2022-06-14 02:40:28.857558
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    class A:
        pass

    foo = A()
    foo.x = 5
    res = TransformationResult(foo, True, ["a", "b"])
    assert type(res.tree) == A
    assert res.tree_changed == True
    assert res.dependencies == ["a", "b"]

# Generated at 2022-06-14 02:40:31.666316
# Unit test for constructor of class InputOutput
def test_InputOutput():
    path1 = Path('a')
    path2 = Path('b')
    io = InputOutput(path1, path2)
    assert io.input == path1
    assert io.output == path2


# Generated at 2022-06-14 02:40:33.329979
# Unit test for constructor of class InputOutput
def test_InputOutput():
    assert InputOutput(input=Path('input'), output=Path('output')) == InputOutput(input='input', output='output')

# Generated at 2022-06-14 02:40:37.146676
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input = Path('input')
    output = Path('output')
    input_output = InputOutput(input, output)
    assert input_output.input == input
    assert inpu

# Generated at 2022-06-14 02:40:41.174157
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    r = CompilationResult(files=1, time=1.0, target=(3, 6), dependencies=[])
    assert r.files == 1
    assert r.time == 1.0
    assert r.target == (3, 6)
    assert r.dependencies == []


# Generated at 2022-06-14 02:40:49.467487
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    result = TransformationResult(tree=ast.parse('None'),
                                  tree_changed=True,
                                  dependencies=['foo', 'bar'])
    assert result.tree_changed
    assert result.dependencies == ['foo', 'bar']

# Generated at 2022-06-14 02:40:55.553302
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    t = ast.parse('pass')
    assert TransformationResult(tree=t, tree_changed=False, dependencies=[])
    assert TransformationResult(tree=t, tree_changed=False, dependencies=['a'])
    assert TransformationResult(tree=t, tree_changed=True, dependencies=['a'])
    assert TransformationResult(tree=t, tree_changed=True, dependencies=[])

# Generated at 2022-06-14 02:40:59.626545
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input = 'input'
    output = 'output'
    result = InputOutput(input=Path(input), output=Path(output))
    assert result.input is Path(input)
    assert result.output is Path(output)


# Generated at 2022-06-14 02:41:01.346718
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    TransformationResult(ast.parse('a = 1'), True, [])

# Generated at 2022-06-14 02:41:09.179333
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    assert CompilationResult(42, 1337.0, (3, 5), ['spam', 'eggs']).files == 42
    assert CompilationResult(42, 1337.0, (3, 5), ['spam', 'eggs']).time == 1337.0
    assert CompilationResult(42, 1337.0, (3, 5), ['spam', 'eggs']).target == (3, 5)
    assert CompilationResult(42, 1337.0, (3, 5), ['spam', 'eggs']).dependencies == ['spam', 'eggs']


# Generated at 2022-06-14 02:41:15.052526
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input_path = '.'
    output_path = '.'
    input_output = InputOutput(input_path, output_path)

    assert isinstance(input_output, InputOutput)
    assert input_output.input == '.'
    assert input_output.output == '.'

# Generated at 2022-06-14 02:41:18.295011
# Unit test for constructor of class InputOutput
def test_InputOutput():
    inp = Path('foo.py')
    out = Path('bar.py')
    io = InputOutput(inp, out)
    assert io.input == inp
    assert io.output == out


# Generated at 2022-06-14 02:41:21.872754
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input = Path('a')
    output = Path('b')
    InputOutput(input, output)



# Generated at 2022-06-14 02:41:25.842558
# Unit test for constructor of class InputOutput
def test_InputOutput():
    i = Path('tests/unit/good/single_if_statement.py')
    o = Path('tests/unit/good/single_if_statement.py.cil')
    pair = InputOutput(i, o)
    assert pair.input == i
    assert pair.output == o

# Generated at 2022-06-14 02:41:30.383676
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input_output = InputOutput(Path('input'), Path('output'))
    assert input_output.input == Path('input')
    assert input_output.output == Path('output')
    assert str(input_output) == "input -> output"

# Generated at 2022-06-14 02:41:42.084097
# Unit test for constructor of class InputOutput
def test_InputOutput():
    # Arrange
    input = Path('input')
    output = Path('output')

    # Act
    result = InputOutput(input, output)

    # Assert
    assert result.input == input
    assert result.output == output

# Generated at 2022-06-14 02:41:44.357831
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    assert TransformationResult.__annotations__['tree'] == ast.AST
    assert TransformationResult.__annotations__['tree_changed'] == bool
    assert TransformationResult.__annotations__['dependencies'] == List[str]

# Generated at 2022-06-14 02:41:45.739295
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    assert TransformationResult(None, False, None)

# Handler for out of tree files

# Generated at 2022-06-14 02:41:47.904165
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    t = ast.AST(body=[])
    assert TransformationResult(tree=t,
                                tree_changed=True,
                                dependencies=["mod1.py"]).warn()

# Generated at 2022-06-14 02:41:55.186047
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    res = CompilationResult(files=1,
                            time=0.1,
                            target=(2, 7),
                            dependencies=['foo'])
    assert res.files == 1
    assert res.time == 0.1
    assert res.target == (2, 7)
    assert res.dependencies == ['foo']
    res2 = CompilationResult(*res)
    assert res2 is not res
    assert res2 == res


# Generated at 2022-06-14 02:41:59.132773
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree = ast.parse('a = 2')
    res = TransformationResult(tree, True, ['a.py'])
    assert type(res.tree) is ast.Module
    assert res.tree_changed
    assert res.dependencies == ['a.py']

# Generated at 2022-06-14 02:42:02.542935
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    # GIVEN
    tree = ast.AST()
    tree_changed = False
    dependencies = []
    # WHEN
    result = TransformationResult(tree, tree_changed, dependencies)
    # THEN
    assert result.tree == tree
    assert result.tree_changed == tree_changed
    assert result.dependencies == dependencies

# Generated at 2022-06-14 02:42:05.082621
# Unit test for constructor of class InputOutput
def test_InputOutput():
    io = InputOutput(Path('a'), Path('b'))
    assert io.input == Path('a')
    assert io.output == Path('b')

# Generated at 2022-06-14 02:42:07.830417
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    assert CompilationResult(1, 1.5, (3, 7), []) == \
        CompilationResult(1, 1.5, (3, 7), [])



# Generated at 2022-06-14 02:42:10.707548
# Unit test for constructor of class InputOutput
def test_InputOutput():
    assert InputOutput(1, 2) == InputOutput(Path('1'), Path('2'))


# Generated at 2022-06-14 02:42:29.051906
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    # type: () -> None
    result = TransformationResult(ast.parse('x = 1'), True, ['foo.py'])
    assert isinstance(result, TransformationResult)
    assert isinstance(result.tree, ast.AST)
    assert result.tree_changed
    assert isinstance(result.dependencies, List)
    assert len(result.dependencies) == 1
    assert result.dependencies[0] == 'foo.py'
    # check equality
    assert result == TransformationResult(ast.parse('x = 1'), True, ['foo.py'])
    assert result != TransformationResult(ast.parse('x = 2'), True, ['foo.py'])
    assert result != TransformationResult(ast.parse('x = 1'), False, ['foo.py'])

# Generated at 2022-06-14 02:42:33.679206
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    t = ast.Num(n=100)
    result = TransformationResult(t, False, ['abc', 'def'])
    assert result.tree is t
    assert result.tree_changed is False
    assert result.dependencies == ['abc', 'def']

# Generated at 2022-06-14 02:42:42.889715
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree = ast.parse('x = 1')
    result = TransformationResult(tree, True, ['foo', 'bar'])

    assert result.tree is tree
    assert result.tree_changed
    assert result.dependencies == ['foo', 'bar']

# Result of source to source compilation
SourceCompilationResult = NamedTuple('SourceCompilationResult',
                                     [('result', CompilationResult),
                                      ('compiled_file', Path),
                                      ('source_path', Path)])


# Generated at 2022-06-14 02:42:49.423480
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    ast_tree = ast.parse('print(1)')
    result = TransformationResult(ast_tree, True, ['foo.py', 'bar.py'])
    assert result.tree is ast_tree
    assert result.tree_changed is True
    assert result.dependencies == ['foo.py', 'bar.py']
    assert repr(result) == 'TransformationResult(tree=Module(body=[Expr(value=Call(func=Name(id=\'print\', ctx=Load()), args=[Num(n=1)], keywords=[]))]), tree_changed=True, dependencies=[\'foo.py\', \'bar.py\'])'

# Generated at 2022-06-14 02:42:55.957899
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    import ast
    import random
    true_or_false = random.randint(0, 1)
    tree = ast.parse('print("Hello world")')
    deps = ['spam.py', 'eggs.py']
    r = TransformationResult(tree, true_or_false, deps)
    assert type(r) == TransformationResult
    assert r.tree == tree
    assert r.tree_changed == true_or_false
    assert r.dependencies == deps

# Generated at 2022-06-14 02:42:58.191251
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    CompilationResult(files=0,
                      time=0,
                      target=(0, 0),
                      dependencies=[])



# Generated at 2022-06-14 02:43:00.864915
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree = ast.parse('pass')
    res = TransformationResult(tree, True, ['test'])
    assert res.tree is tree
    assert res.tree_changed
    assert res.dependencies == ['test']

# Generated at 2022-06-14 02:43:04.704685
# Unit test for constructor of class InputOutput
def test_InputOutput():
    i = Path('in.py')
    o = Path('out.py')
    a = InputOutput(i, o)
    expected = InputOutput(i, o)
    assert a == expected


# Generated at 2022-06-14 02:43:08.493906
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input = Path('input/path/')
    output = Path('output/path/')
    input_output = InputOutput(input, output)
    assert input_output.input == input
    assert input_output.output == output


# Generated at 2022-06-14 02:43:12.794424
# Unit test for constructor of class InputOutput
def test_InputOutput():
    inp_path = Path("/home/x")
    out_path = Path("/home/y")
    inputoutput = InputOutput(inp_path, out_path)

    assert inputoutput.input == inp_path
    assert inputoutput.output == out_path


# Generated at 2022-06-14 02:43:34.064928
# Unit test for constructor of class InputOutput
def test_InputOutput():
    a = InputOutput(Path('.'), Path('..'))
    assert isinstance(a.output, Path)
    assert isinstance(a.input, Path)

# Generated at 2022-06-14 02:43:36.040768
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    CompilationResult(files=0, time=0.0, target=(3, 7), dependencies=[])


# Generated at 2022-06-14 02:43:42.068883
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input_output = InputOutput(Path(__file__), Path(__file__))
    assert isinstance(input_output.input, Path)
    assert isinstance(input_output.output, Path)
    assert input_output.input == Path(__file__)
    assert input_output.output == Path(__file__)
    assert input_output.input == input_output.output


# Generated at 2022-06-14 02:43:47.278497
# Unit test for constructor of class InputOutput
def test_InputOutput():
    assert InputOutput('input', 'output') == InputOutput(Path('input'),
                                                         Path('output'))
    assert InputOutput(Path('input'), Path('output')) == InputOutput('input',
                                                                     'output')
    assert str(InputOutput(Path('input'), Path('output'))) == \
           (Path('input').absolute().as_posix() + ' -> ' +
            Path('output').absolute().as_posix())


# Generated at 2022-06-14 02:43:50.559409
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input_ = Path('myfile.py')
    output = Path('myfile.pyi')
    in_out = InputOutput(input_, output)
    assert in_out.input == input_
    assert in_out.output == output


# Generated at 2022-06-14 02:43:55.971038
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input = Path('/home/user/files')
    output = Path('/home/user/files_compiled')
    assert InputOutput(input, output)
    assert InputOutput(input, output).input.samefile(input)
    assert InputOutput(input, output).output.samefile(output)

# Generated at 2022-06-14 02:44:01.325423
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    result = CompilationResult(files=1, time=2.0, target=(3, 4), dependencies=['d1', 'd2'])
    assert result.files == 1
    assert result.time == 2.0
    assert result.target == (3, 4)
    assert result.dependencies == ['d1', 'd2']



# Generated at 2022-06-14 02:44:03.045500
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tr = TransformationResult(tree=ast.parse(''),
                              tree_changed=False,
                              dependencies=[])


# Generated at 2022-06-14 02:44:08.750163
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    result = CompilationResult(files=1,
                               time=1,
                               target=(3, 5),
                               dependencies=["a", "b"])
    assert result.files == 1
    assert result.time == 1
    assert result.target == (3, 5)
    assert result.dependencies == ['a', 'b']

# Generated at 2022-06-14 02:44:13.588611
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    result = TransformationResult(ast.parse('1'), True, ['a', 'b'])
    assert result.tree == ast.parse('1')
    assert result.tree_changed is True
    assert result.dependencies == ['a', 'b']



# Generated at 2022-06-14 02:45:05.401334
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    c = CompilationResult(1, 5.0, (3, 5), [])
    assert c.files == 1
    assert c.time == 5.0
    assert c.target == (3, 5)
    assert c.dependencies == []


# Generated at 2022-06-14 02:45:08.165048
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    CompilationResult(1, 2.0, (3, 4), ["a", "b", "c"])

# Generated at 2022-06-14 02:45:09.327291
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    assert CompilationResult(123, 42, (3, 7), [])


# Generated at 2022-06-14 02:45:11.207897
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    CompilationResult(10, 1.0, (3, 7), [])


# Generated at 2022-06-14 02:45:16.581791
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    a = CompilationResult(1, 0.1, (3, 6), [])
    b = CompilationResult(2, 0.2, (3, 5), [])

    assert a.files == 1
    assert a.time == 0.1
    assert a.target == (3, 6)
    assert a.dependencies == []

    assert b.files == 2
    assert b.time == 0.2
    assert b.target == (3, 5)
    assert b.dependencies == []


# Generated at 2022-06-14 02:45:22.086908
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    c = CompilationResult(1, 2.5, (3, 4),
                          ["x.py", "y.py", "z.py"])
    assert c.files == 1
    assert c.time == 2.5
    assert c.target == (3, 4)
    assert c.dependencies == ["x.py", "y.py", "z.py"]


# Generated at 2022-06-14 02:45:24.248529
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    assert CompilationResult(files=1, time=2.0, target=(3, 4), dependencies=[])


# Generated at 2022-06-14 02:45:28.513108
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    var = CompilationResult(files=1,
                            time=2.0,
                            target=(3, 4),
                            dependencies=["foo", "bar"])

    assert var.files == 1
    assert var.time == 2.0
    assert var.target == (3, 4)
    assert var.dependencies == ["foo", "bar"]


# Generated at 2022-06-14 02:45:35.591636
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    cr = CompilationResult(files=10, time=0.5, target=(3, 6), dependencies=['foo', 'bar'])
    assert cr.files == 10
    assert cr.time == 0.5
    assert cr.target == (3, 6)
    assert cr.dependencies == ['foo', 'bar', 'baz']
    assert cr == cr.replace(dependencies=['foo', 'bar'])



# Generated at 2022-06-14 02:45:39.507592
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    # GIVEN
    target = (3, 7)
    result = CompilationResult(10, 2.0, target, [])

    # THEN
    assert result.files == 10
    assert result.time == 2.0
    assert result.target == target
    assert result.dependencies == []


# Generated at 2022-06-14 02:47:22.315025
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    c = CompilationResult(
        files=2,
        time=0.1,
        target=(3, 8),
        dependencies=['a', 'b', 'c'])

    assert c.files == 2
    assert c.time == 0.1
    assert c.target == (3, 8)
    assert c.dependencies == ['a', 'b', 'c']


# Generated at 2022-06-14 02:47:31.722327
# Unit test for constructor of class InputOutput
def test_InputOutput():
    assert InputOutput(Path('/foo/bar.txt'), Path('/baz')) == \
        InputOutput(Path('/foo/bar.txt'), Path('/baz'))
    assert InputOutput(Path('/foo/bar.txt'), Path('/baz')) != \
        InputOutput(Path('/foo/bar.txt'), Path('/qux'))
    assert InputOutput(Path('/foo/bar.txt'), Path('/baz')) != \
        InputOutput(Path('/foo/qux.txt'), Path('/baz'))

# Generated at 2022-06-14 02:47:33.293859
# Unit test for constructor of class InputOutput
def test_InputOutput():
    assert InputOutput(input=Path('input'), output=Path('output'))

# Generated at 2022-06-14 02:47:34.642273
# Unit test for constructor of class InputOutput
def test_InputOutput():
    assert InputOutput(Path('a.txt'), Path('b.txt'))

# Generated at 2022-06-14 02:47:37.651814
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    res = CompilationResult(1, 2, (3, 4), [])
    assert res.files == 1
    assert res.time == 2

    res.files = 9
    assert res.files == 9



# Generated at 2022-06-14 02:47:42.473895
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    test = CompilationResult(5, 1.0, (3, 7), ['dep1', 'dep2'])
    assert test.files == 5
    assert test.time == 1.0
    assert test.target == (3, 7)
    assert test.dependencies == ['dep1', 'dep2']



# Generated at 2022-06-14 02:47:44.738560
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    CompilationResult(files=0,
                      time=0.0,
                      target=(0, 0),
                      dependencies=['a.py', 'b.py'])


# Generated at 2022-06-14 02:47:48.063190
# Unit test for constructor of class InputOutput
def test_InputOutput():
    io = InputOutput(Path('a.py'), Path('b.py'))
    assert io.input == Path('a.py')
    assert io.output == Path('b.py')


# Generated at 2022-06-14 02:47:52.288361
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    compilation_result = CompilationResult(1, 4.2, (3, 4), ['a', 'b'])
    assert compilation_result.files == 1
    assert compilation_result.time == 4.2
    assert compilation_result.target == (3, 4)
    assert compilation_result.dependencies == ['a', 'b']


# Generated at 2022-06-14 02:47:55.779160
# Unit test for constructor of class InputOutput
def test_InputOutput():
    test = InputOutput(Path("/a/b"), Path("c/d"))
    assert test.input == Path("/a/b")
    assert test.output == Path("c/d")