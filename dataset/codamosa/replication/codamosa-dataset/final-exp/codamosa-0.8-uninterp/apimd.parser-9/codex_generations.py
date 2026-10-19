

# Generated at 2022-06-13 17:45:25.173501
# Unit test for method class_api of class Parser

# Generated at 2022-06-13 17:45:31.980334
# Unit test for method is_public of class Parser
def test_Parser_is_public():
    p = Parser(['xx'])
    p.imp['xx'] = {'xx', 'xx.xx'}
    p.imp['xx.xx'] = {'xx.xx'}
    p.root['xx'] = 'xx'
    p.root['xx.xx'] = 'xx.xx'
    p.root['xx.xx.xx'] = 'xx.xx'
    assert p.is_public('xx')
    assert p.is_public('xx.xx')
    assert p.is_public('xx.xx.xx')
    assert not p.is_public('xx.xx.yy')
    p.imp['xx'] = {'xx'}
    p.imp['xx.xx'] = {}
    assert p.is_public('xx.xx')

# Generated at 2022-06-13 17:45:36.120381
# Unit test for function table
def test_table():
    assert table('a', 'b', [['c', 'd'], ['e', 'f']]) == '''\
| a | b |
|:---:|:---:|
| c | d |
| e | f |

'''

# Generated at 2022-06-13 17:45:40.200308
# Unit test for method visit_Attribute of class Resolver
def test_Resolver_visit_Attribute():
    e = parse("typing.Optional[int]").body[0]
    assert Resolver("", {}).visit(e).__class__.__name__ == "BinOp"

# Generated at 2022-06-13 17:45:48.199057
# Unit test for method visit_Subscript of class Resolver
def test_Resolver_visit_Subscript():
    assert Resolver("a.b", {'a.b': 'a.c'}).visit_Subscript(Subscript(Name("a", Load()), Tuple(elts=[Name("b", Load()), Name("c", Load())], ctx=Load()), Load())).__class__ == BinOp
    assert Resolver("a.b", {'a.b': 'a.c'}).visit_Subscript(Subscript(Name("a", Load()), Name("b", Load()), Load())).__class__ == Name
    assert Resolver("a.b", {'a.b': 'a.c'}).visit_Subscript(Subscript(Name("a", Load()), Name("b", Load()), Load())).id == "b"

# Generated at 2022-06-13 17:45:57.875510
# Unit test for function walk_body
def test_walk_body():
    # base case
    def test(body: Sequence[str]) -> Sequence[str]:
        nums = list(range(len(body)))
        return [*(unparse(node) for node in walk_body(nums)), *body]
    assert test([]) == []
    # If
    assert test(['1', 'if True:', '  pass', '2', '3']) == [1, 2, 3]
    assert test(['1', 'if True:', '  pass', '2', 'else:', '  pass', '3']) == [1, 2, 3]
    # Try
    assert test(['1', 'try:', '  pass', '2', 'except:', '  pass', '3']) == [1, 2, 3]

# Generated at 2022-06-13 17:46:00.256320
# Unit test for function table
def test_table():
    assert table('a', 'b', [['c', 'd'], ['e', 'f']]) == \
"""| a | b |
|:---:|:---:|
| c | d |
| e | f |

"""



# Generated at 2022-06-13 17:46:03.881106
# Unit test for function is_public_family
def test_is_public_family():
    assert is_public_family('os.path')
    assert is_public_family('pathlib.Path')
    assert not is_public_family('os._Environ')
    assert not is_public_family('os.__parse')
    assert not is_public_family('os.')
    assert is_public_family('_io.TextIOBase')
    assert not is_public_family('_io._IOBase')



# Generated at 2022-06-13 17:46:08.335193
# Unit test for function const_type

# Generated at 2022-06-13 17:46:15.469543
# Unit test for method func_ann of class Parser
def test_Parser_func_ann():
    p, root = Parser(), "root"
    args = [arg(a, n) for a, n in (("*args", None), ("**kwargs", None))]
    args.append(arg("return", Name("str", Load())))
    assert list(p.func_ann(root, args, has_self=False, cls_method=False)) == \
        [None, None, "str"]
    assert list(p.func_ann(root, args, has_self=True, cls_method=False)) == \
        ["Self", "tuple[Any, ...]", "dict[Any, Any]", "str"]