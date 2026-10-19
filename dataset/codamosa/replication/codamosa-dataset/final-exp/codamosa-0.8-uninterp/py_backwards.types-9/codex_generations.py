

# Generated at 2022-06-14 02:39:00.209259
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    class MockTree:
        pass

    res = TransformationResult(MockTree(), True, ['first.dep', 'second.dep'])
    assert res.tree is MockTree
    assert res.tree_changed is True
    assert res.dependencies == ['first.dep', 'second.dep']

# Generated at 2022-06-14 02:39:07.699361
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    # pylint: disable=redefined-outer-name
    path1 = '/usr/bin/env/python'
    path2 = '/usr/lib/python/2.7/abc.py'
    tree = ast.AST()
    tree_changed = True
    dependencies = [path1, path2]
    result = TransformationResult(tree=tree, tree_changed=True,
                                  dependencies=[path1, path2])
    assert isinstance(result, TransformationResult)
    assert result.tree == tree
    assert result.tree_changed == tree_changed
    assert result.dependencies == dependencies

# Generated at 2022-06-14 02:39:11.049628
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input_path = Path(__file__)
    output_path = Path(__file__ + '.pyc')
    assert InputOutput(input_path, output_path).input == input_path
    assert InputOutput(input_path, output_path).output == output_path


# Generated at 2022-06-14 02:39:15.357361
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree = ast.parse('a = 1')
    TransformationResult(tree, True, [])
    TransformationResult(tree, False, [])
    TransformationResult(tree, True, ['b', 'c'])
    TransformationResult(tree, False, ['d', 'e'])
    TransformationResult(tree, True, [])

# Generated at 2022-06-14 02:39:18.572749
# Unit test for constructor of class InputOutput
def test_InputOutput():
    i = InputOutput(Path('input.txt'), Path('output.txt'))
    assert i.input == Path('input.txt')
    assert i.output == Path('output.txt')


# Generated at 2022-06-14 02:39:20.983726
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input_output = InputOutput(Path('foo'), Path('bar'))
    assert input_output.input == Path('foo')
    assert input_output.output == Path('bar')


# Generated at 2022-06-14 02:39:23.782070
# Unit test for constructor of class InputOutput
def test_InputOutput():
    assert InputOutput(Path('input'), Path('output')) == InputOutput(Path('input'), Path('output'))


# Generated at 2022-06-14 02:39:26.799893
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input = Path("input")
    output = Path("output")
    input_output = InputOutput(input, output)
    assert input_output.input == input
    assert input_output.output == output


# Generated at 2022-06-14 02:39:30.701665
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input_output = InputOutput(input=Path('foo.py'),
                               output=Path('foo.pyi'))
    assert input_output.input == Path('foo.py')
    assert input_output.output == Path('foo.pyi')

# Test equality of objects of class InputOutput

# Generated at 2022-06-14 02:39:31.252372
# Unit test for constructor of class InputOutput
def test_InputOutput():
    pass

# Generated at 2022-06-14 02:39:36.201004
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tr = TransformationResult(
        tree=ast.parse('a = b + c'),
        tree_changed=False,
        dependencies=[]
    )
    assert tr.tree is not None
    assert not tr.tree_changed
    assert not tr.dependencies

# Generated at 2022-06-14 02:39:37.885625
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    CompilationResult(2, 3.0, (3, 5), ['dep1'])


# Generated at 2022-06-14 02:39:40.206149
# Unit test for constructor of class InputOutput
def test_InputOutput():
    inp = Path('inp')
    out = Path('out')
    io = InputOutput(inp, out)
    assert io.input == inp
    assert io.output == out

# Generated at 2022-06-14 02:39:43.495902
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    cr = CompilationResult(1, 1.0, (3, 5), ["pip", "setuptools"])
    assert cr.files == 1
    assert cr.time == 1.0
    assert cr.target == (3, 5)
    assert cr.dependencies == ["pip", "setuptools"]


# Generated at 2022-06-14 02:39:46.578657
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    # pylint: disable=invalid-name
    a = TransformationResult(tree=None, tree_changed=True, dependencies=None)
    assert a.tree_changed is True

# Generated at 2022-06-14 02:39:51.498568
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    assert (isinstance(TransformationResult(ast.AST(), False, ['foo', 'bar']),
                        TransformationResult))
    assert (TransformationResult(ast.AST(), False, ['foo', 'bar']).dependencies ==
            ['foo', 'bar'])

__all__ = [
    'CompilationTarget',
    'CompilationResult',
    'InputOutput',
    'TransformationResult'
]

# Generated at 2022-06-14 02:39:56.373861
# Unit test for constructor of class InputOutput
def test_InputOutput():
    path_in = 'data/input.py'
    path_out = 'data/output.py'

    input_output = InputOutput(path_in, path_out)
    assert input_output.input.name == 'input.py'
    assert input_output.output.name == 'output.py'

# Generated at 2022-06-14 02:40:00.817437
# Unit test for constructor of class InputOutput
def test_InputOutput():
    """ Unit test for InputOutput constructor. """
    input_path = Path('foo')
    output_path = Path('bar')
    pair = InputOutput(input=input_path, output=output_path)
    assert pair.input == input_path
    assert pair.output == output_path

# Generated at 2022-06-14 02:40:04.267607
# Unit test for constructor of class TransformationResult
def test_TransformationResult(): # type: () -> None
    tree = ast.Module([])
    tree_changed = False
    dependencies = []
    res = TransformationResult(tree, tree_changed, dependencies)
    assert res.tree_changed == tree_changed
    assert res.dependencies == dependencies

# Generated at 2022-06-14 02:40:05.650117
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    CompilationResult(1, 0.0, (3, 5), [])

# Generated at 2022-06-14 02:40:10.060613
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    t = TransformationResult(tree=None, tree_changed=True, dependencies=[])
    assert t.tree_changed
    assert not t.dependencies

# Generated at 2022-06-14 02:40:14.266435
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree = ast.parse("print('hello')")
    assert TransformationResult(tree, True, ['a', 'b', 'c']) == \
           TransformationResult(tree=tree, tree_changed=True,
                                dependencies=['a', 'b', 'c'])

# Generated at 2022-06-14 02:40:19.138381
# Unit test for constructor of class InputOutput
def test_InputOutput():
    p = Path('test.py')
    io = InputOutput(input=p, output=p)
    assert io.input == p
    assert io.output == p
    assert io.input == io.output
    assert io.input == Path('test.py')
    assert io.output == Path('test.py')


# Generated at 2022-06-14 02:40:21.723866
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    # pylint: disable=C0103
    CompilationResult(3, 5.0, (3, 7), [])



# Generated at 2022-06-14 02:40:25.490425
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    a = ast.parse('x')
    r = TransformationResult(tree=a, tree_changed=True, dependencies=['a'])

    assert r.tree == a
    assert r.tree_changed == True
    assert r.dependencies == ['a']

# Generated at 2022-06-14 02:40:28.909925
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    assert CompilationResult._field_types == \
           OrderedDict([('files', int),
                        ('time', float),
                        ('target', Tuple[int, int]),
                        ('dependencies', List[str])])



# Generated at 2022-06-14 02:40:31.885987
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input_output = InputOutput(Path('a.txt'), Path('b.txt'))
    assert input_output.input == Path('a.txt')
    assert input_output.output == Path('b.txt')



# Generated at 2022-06-14 02:40:34.497446
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    t = TransformationResult(ast.parse('x = "test"'), True, [])
    assert isinstance(t.tree, ast.AST)
    assert isinstance(t.tree_changed, bool)
    assert isinstance(t.dependencies, list)

# Generated at 2022-06-14 02:40:38.031076
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    import astroid
    # tree argument is an ast node
    astroid.parse('')
    # tree_changed argument is a bool
    True
    # dependencies argument is a list of strings
    []

# Generated at 2022-06-14 02:40:45.579925
# Unit test for constructor of class InputOutput
def test_InputOutput():
    assert InputOutput(Path('a.in'), Path('a.out')) == \
        InputOutput(input=Path('a.in'), output=Path('a.out'))
    assert InputOutput(Path('a.in'), Path('a.out')) != \
        InputOutput(Path('a.in'), Path('b.out'))
    assert InputOutput(Path('a.in'), Path('a.out')) != \
        InputOutput(Path('b.in'), Path('a.out'))


# Generated at 2022-06-14 02:40:54.222627
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    r = TransformationResult(tree=None,
                             tree_changed=False,
                             dependencies=[])
    assert r.tree is None
    assert r.tree_changed is False
    assert r.dependencies == []

# Generated at 2022-06-14 02:40:59.675880
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    result = TransformationResult(ast.parse('def f(x): return x + 1'),
                                  True,
                                  ['module.py', 'a.py'])
    assert(result.tree_changed is True)
    assert(result.dependencies == ['module.py', 'a.py'])

# Generated at 2022-06-14 02:41:01.767504
# Unit test for constructor of class InputOutput
def test_InputOutput():
    assert InputOutput(input=Path('i'), output=Path('o')) == InputOutput('i', 'o')

# Generated at 2022-06-14 02:41:05.168439
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    result = CompilationResult(10, 0.5, (3, 7), ['std'])
    assert result.files == 10 and result.time == 0.5 and result.target == (3, 7) and result.dependencies == ['std']


# Generated at 2022-06-14 02:41:09.024670
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree = ast.parse('pass')
    result = TransformationResult(tree, True, ['a'])
    assert isinstance(result.tree, ast.AST)
    assert result.tree_changed
    assert result.dependencies == ['a']

test_TransformationResult()

# Generated at 2022-06-14 02:41:16.617427
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    # type: () -> None

    tr = TransformationResult(tree=None, tree_changed=False,
                              dependencies=['test.py', 'test2.py'])
    assert tr.tree is None
    assert tr.tree_changed == False
    assert tr.dependencies == ['test.py', 'test2.py']
    return

# Generated at 2022-06-14 02:41:19.556470
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree = ast.parse('1 + 1')
    a = TransformationResult(tree, True, ['test_file.py'])
    assert a.tree == tree
    assert a.tree_changed == True
    assert a.dependencies == ['test_file.py']

# Generated at 2022-06-14 02:41:22.190711
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    CompilationResult(1, 1.0, (3, 5), [])

# Generated at 2022-06-14 02:41:31.445181
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    compilation_result = CompilationResult(files=1,
                                           time=2,
                                           target=[3, 4],
                                           dependencies=["a", "b", "c"])
    assert compilation_result.files == 1
    assert compilation_result.time == 2
    assert compilation_result.target == (3, 4)
    assert compilation_result.dependencies == ["a", "b", "c"]


# Generated at 2022-06-14 02:41:36.695992
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    a = TransformationResult(tree = ast.parse('pass'),
                             tree_changed = True,
                             dependencies = ['foo'])
    assert a.tree_changed == True
    assert a.dependencies == ['foo']

# Generated at 2022-06-14 02:41:48.472228
# Unit test for constructor of class InputOutput
def test_InputOutput():
    i = Path('/a/b.py')
    o = Path('/o/b.py')
    io = InputOutput(input=i, output=o)

    assert io.input == i
    assert io.output == o

# Generated at 2022-06-14 02:41:51.337941
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    cr = CompilationResult(files=3, time=3.3, target=(3, 4), dependencies=[])
    assert cr.files == 3
    assert cr.time == 3.3
    assert cr.target == (3, 4)
    assert cr.dependencies == []


# Generated at 2022-06-14 02:41:57.789222
# Unit test for constructor of class InputOutput
def test_InputOutput():
    class C(object):
        pass
    c = C()
    c.input = Path('foo')
    c.output = Path('bar')
    c.dependencies = ['baz']
    io = InputOutput(c.input, c.output)
    assert io.input == c.input
    assert io.output == c.output
    assert io.dependencies == c.dependencies


# Generated at 2022-06-14 02:42:03.205253
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    a = CompilationResult(files=1, time=0.0, target=(3, 7),
                          dependencies=['a', 'b', 'c'])
    assert a.files == 1
    assert a.time == 0.0
    assert a.target[0] == 3
    assert a.target[1] == 7
    assert a.dependencies == ['a', 'b', 'c']

# Generated at 2022-06-14 02:42:05.867788
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    CompilationResult(files=3, time=23.3, target=(3, 5),
                      dependencies=['a', 'b'])

# Generated at 2022-06-14 02:42:07.829330
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    '''TransformationResult shall be initialized successfully.'''
    assert TransformationResult(ast.AST(), True, [])

# Generated at 2022-06-14 02:42:10.861741
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    result = CompilationResult(files=1, time=1.5, target=(3, 6),
                               dependencies=[])
    assert result.files == 1
    assert result.time == 1.5
    assert result.target == (3, 6)
    assert result.dependencies == []


# Generated at 2022-06-14 02:42:14.609313
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    result = CompilationResult(1, 2.3, (3, 4), ['a', 'b'])
    assert result.files == 1
    assert result.time == 2.3
    assert result.target == (3, 4)
    assert result.dependencies == ['a', 'b']


# Generated at 2022-06-14 02:42:19.335499
# Unit test for constructor of class InputOutput
def test_InputOutput():
    inp = Path('/input/path')
    out = Path('/output/path')
    InputOutput(inp, out)
    inp = '/input/path'
    out = '/output/path'
    InputOutput(inp, out)
    inp = 'input-path'
    out = 'output-path'
    InputOutput(inp, out)


# Generated at 2022-06-14 02:42:21.308630
# Unit test for constructor of class InputOutput
def test_InputOutput():
    assert InputOutput(input='a', output='b') == (('a', 'b'))


# Generated at 2022-06-14 02:42:45.050627
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input_out_pairs = [('test.py', 'test.pyc'),
                       ('file.py', 'file.pyc'),
                       ('/usr/bin/python', '/usr/bin/pythonc'),
                       ('/usr/bin/python3', '/usr/bin/python3c'),
                       ]

    for input_, output in input_out_pairs:
        yield check_input_output, input_, output



# Generated at 2022-06-14 02:42:48.930120
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    compile_result = CompilationResult(files=1, time=2.0, target=(3, 4),
                                       dependencies=['a', 'b'])

    assert compile_result.files == 1
    assert compile_result.time == 2.0
    assert compile_result.target == (3, 4)
    assert compile_result.dependencies == ['a', 'b']


# Generated at 2022-06-14 02:42:52.401083
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input_path = Path('/home/input.py')
    output_path = Path('/home/output.py')
    io = InputOutput(input_path, output_path)
    assert io.input == input_path
    assert io.output == output_path


# Generated at 2022-06-14 02:42:55.218112
# Unit test for constructor of class InputOutput
def test_InputOutput():
    io = InputOutput(Path('input'), Path('output'))
    assert io.input == Path('input')
    assert io.output == Path('output')


# Generated at 2022-06-14 02:43:03.628538
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    # Check that can not construct with wrong arguments
    with pytest.raises(TypeError):
        CompilationResult('a', 'b', 'c', 'd')
    with pytest.raises(TypeError):
        CompilationResult(1, 'b', 'c', 'd')
    with pytest.raises(TypeError):
        CompilationResult(1, 2.0, 'c', 'd')
    with pytest.raises(TypeError):
        CompilationResult(1, 2.0, (3, 4), 'd')
    with pytest.raises(TypeError):
        CompilationResult(1, 2.0, (3, 4), [])

    # Check normal case
    CompilationResult(1, 2.0, (3, 4), ['a'])



# Generated at 2022-06-14 02:43:07.894778
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    from typed_ast import ast3
    assert TransformationResult(tree=ast3.AST(),
                                tree_changed=True,
                                dependencies=[]) \
        == TransformationResult(tree=ast3.AST(),
                                tree_changed=True,
                                dependencies=[])

# Generated at 2022-06-14 02:43:11.400203
# Unit test for constructor of class InputOutput
def test_InputOutput():
    input_ = Path("test_input")
    output = Path("test_output")
    input_output = InputOutput(input_, output)
    assert input_output.input == input_
    assert input_output.output == output


# Generated at 2022-06-14 02:43:15.045679
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    assert TransformationResult(None, False, [])

# Result of AST validation
ValidationResult = NamedTuple('ValidationResult',
                              [('filename', str),
                               ('success', bool),
                               ('errors', List[str]),
                               ('warnings', List[str])])


# Generated at 2022-06-14 02:43:23.697115
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    compilation_result = CompilationResult(files=1,
                                           time=1,
                                           target=(3, 5),
                                           dependencies=['a', 'b', 'c'])
    assert compilation_result.files == 1
    assert compilation_result.time == 1
    assert compilation_result.target == (3, 5)
    assert compilation_result.dependencies == ['a', 'b', 'c']


# Generated at 2022-06-14 02:43:28.263288
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    cr = CompilationResult(42, 0.1, (3, 4), ['foo', 'bar'])
    assert cr.files == 42
    assert cr.time == 0.1
    assert cr.target == (3,4)
    assert cr.dependencies == ['foo', 'bar']


# Generated at 2022-06-14 02:44:22.896776
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    result = TransformationResult(tree=ast.parse(""),
                                  tree_changed=False,
                                  dependencies=[])
    assert isinstance(result.tree, ast.AST)
    assert isinstance(result.tree_changed, bool)
    assert isinstance(result.dependencies, list)
    assert result.dependencies == []

    result = TransformationResult(tree=ast.parse(""),
                                  tree_changed=False,
                                  dependencies=["a"])
    assert isinstance(result.tree, ast.AST)
    assert isinstance(result.tree_changed, bool)
    assert isinstance(result.dependencies, list)
    assert result.dependencies == ["a"]



# Generated at 2022-06-14 02:44:29.866188
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    """
    >>> TransformationResult(tree=ast.AST(), tree_changed=True, dependencies=['test'])
    TransformationResult(tree=<_ast.Module object at 0x7f33e4883f98>, tree_changed=True, dependencies=['test'])
    """
    pass

# Result of way through transformer
WayThrough = NamedTuple('WayThrough', [('input_output', InputOutput),
                                       ('result', TransformationResult)])


# Generated at 2022-06-14 02:44:35.487949
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    assert TransformationResult(
        ast.parse('x + 1'),
        True,
        ['dep1', 'dep2']
    )

# Information about transformation
TransformationRegistryItem = NamedTuple('TransformationRegistryItem',
                                        [('priority', int),
                                         ('transformer',
                                          Callable[[ast.AST, str], TransformationResult])])


# Generated at 2022-06-14 02:44:42.581703
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    assert TransformationResult(ast.Str('test'), False, ['foo']).tree_changed == False
    assert TransformationResult(ast.Str('test'), False, ['foo']).tree == ast.Str('test')
    assert TransformationResult(ast.Str('test'), False, ['foo']).dependencies == ['foo']

# Generated at 2022-06-14 02:44:43.523899
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    assert TransformationResult(ast.AST(), True, [])

# Generated at 2022-06-14 02:44:47.317084
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    cr = CompilationResult(1, 100, (3, 8), None)
    assert cr.files == 1
    assert cr.time == 100
    assert cr.target == (3, 8)
    assert cr.dependencies is None


# Generated at 2022-06-14 02:44:49.329782
# Unit test for constructor of class InputOutput
def test_InputOutput():
    path = Path(__file__)
    io = InputOutput(path, path)
    assert io.input == path
    assert io.output == path

# Generated at 2022-06-14 02:44:53.223014
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    compilation_result = CompilationResult(3, 1.5, (3, 7), [])
    assert compilation_result.files == 3
    assert compilation_result.time == 1.5
    assert compilation_result.target == (3, 7)
    assert compilation_result.dependencies == []

# Generated at 2022-06-14 02:44:57.327097
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree = ast.Module(body=[])
    tr = TransformationResult(tree, True, [])
    assert tr.tree == tree
    assert tr.tree_changed
    assert tr.dependencies == []

# Generated at 2022-06-14 02:45:04.813008
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    cr = CompilationResult(files=1,
                           time=0.1,
                           target=(2, 7),
                           dependencies=['path/to/dependency'])
    assert cr.files == 1
    assert cr.time == 0.1
    assert cr.target == (2, 7)
    assert cr.dependencies == ['path/to/dependency']



# Generated at 2022-06-14 02:46:49.231817
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    t = TransformationResult(ast.AST(), True, ["foo", "bar"])
    assert isinstance(t.tree, ast.AST)
    assert t.tree_changed
    assert t.dependencies == ["foo", "bar"]

# Generated at 2022-06-14 02:46:54.197480
# Unit test for constructor of class TransformationResult
def test_TransformationResult():  # type: () -> None
    result = TransformationResult(tree=ast.parse('pass'),
                                  tree_changed=False,
                                  dependencies=['foo.py'])
    assert isinstance(result, TransformationResult)
    assert isinstance(result.tree, ast.AST)
    assert isinstance(result.tree_changed, bool)
    assert isinstance(result.dependencies, list)

# Generated at 2022-06-14 02:46:56.215185
# Unit test for constructor of class InputOutput
def test_InputOutput():
    assert InputOutput('input', 'output') == InputOutput(Path('input'),
                                                         Path('output'))


# Generated at 2022-06-14 02:46:57.114941
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    assert TransformationResult(ast.AST(), True, [])

# Generated at 2022-06-14 02:46:58.897871
# Unit test for constructor of class TransformationResult
def test_TransformationResult():
    tree = ast.parse('x = 1 + 5')
    assert TransformationResult(tree, True, ['x', 'y', 'z']).tree == tree

# Generated at 2022-06-14 02:47:00.766099
# Unit test for constructor of class InputOutput
def test_InputOutput():
    obj = InputOutput(Path("foo.py"), Path("foo.out"))
    assert obj.input == Path("foo.py")
    assert obj.output == Path("foo.out")

# Generated at 2022-06-14 02:47:02.417819
# Unit test for constructor of class InputOutput
def test_InputOutput():
    assert isinstance(InputOutput(Path('file.py'), Path('file.cpp')), InputOutput)



# Generated at 2022-06-14 02:47:05.085203
# Unit test for constructor of class InputOutput
def test_InputOutput():
    # not doing much, just making sure everything is there
    i = Path("/tmp/input")
    o = Path("/tmp/output")
    io = InputOutput(i, o)

    assert io.input == i
    assert io.output == o

# Generated at 2022-06-14 02:47:08.891317
# Unit test for constructor of class CompilationResult
def test_CompilationResult():
    result = CompilationResult(5, 2.5, (3, 5), [])
    assert result.files == 5
    assert result.time == 2.5
    assert result.target == (3, 5)
    assert result.dependencies == []


# Generated at 2022-06-14 02:47:13.239392
# Unit test for constructor of class InputOutput
def test_InputOutput():
    # type: () -> None
    path1 = Path('./input_path')
    path2 = Path('./output_path')
    pair = InputOutput(input=path1, output=path2)

    assert pair.input == path1
    assert pair.output == path2
