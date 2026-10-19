

# Generated at 2024-06-01 15:19:59.670549
# Unit test for method visit_Constant of class Resolver
def test_Resolver_visit_Constant():    resolver = Resolver(root="test", alias={})

# Generated at 2024-06-01 15:20:03.069780
# Unit test for method load_docstring of class Parser
def test_Parser_load_docstring():    parser = Parser()

# Generated at 2024-06-01 15:20:09.307716
# Unit test for method is_public of class Parser
def test_Parser_is_public():    parser = Parser()

# Generated at 2024-06-01 15:20:11.766494
# Unit test for method visit_Constant of class Resolver
def test_Resolver_visit_Constant():    resolver = Resolver(root="test", alias={})

# Generated at 2024-06-01 15:20:14.809313
# Unit test for method visit_Attribute of class Resolver
def test_Resolver_visit_Attribute():    resolver = Resolver(root="", alias={})
    
    # Test case 1: Attribute with typing prefix

# Generated at 2024-06-01 15:20:19.051251
# Unit test for method class_api of class Parser
def test_Parser_class_api():    parser = Parser()

# Generated at 2024-06-01 15:20:21.675415
# Unit test for method func_api of class Parser
def test_Parser_func_api():    parser = Parser()

# Generated at 2024-06-01 15:20:24.758071
# Unit test for method visit_Subscript of class Resolver
def test_Resolver_visit_Subscript():    # Test case 1: PEP604 - Union
    node = Subscript(value=Name(id='Union', ctx=Load()), slice=Tuple(elts=[Name(id='int', ctx=Load()), Name(id='str', ctx=Load())], ctx=Load()), ctx=Load())
    resolver = Resolver(root='', alias={'Union': 'typing.Union'})
    result = resolver.visit_Subscript(node)
    assert isinstance(result, BinOp)
    assert isinstance(result.left, Name) and result.left.id == 'int'
    assert isinstance(result.op, BitOr)
    assert isinstance(result.right, Name) and result.right.id == 'str'

    # Test case 2: PEP604 - Optional
    node = Subscript(value=Name(id='Optional', ctx=Load()), slice=Name(id='int', ctx=Load()), ctx=Load())
    resolver = Resolver(root='', alias={'Optional': 'typing.Optional'})
    result = resolver

# Generated at 2024-06-01 15:20:28.087782
# Unit test for method visit_Constant of class Resolver
def test_Resolver_visit_Constant():    resolver = Resolver(root="root", alias={"root.SomeAlias": "SomeActualValue"})
    
    # Test with a non-string constant

# Generated at 2024-06-01 15:20:31.755808
# Unit test for function doctest

# Generated at 2024-06-01 15:22:00.491832
# Unit test for function walk_body
def test_walk_body():    from ast import parse, If, Try, Expr, Constant

    # Test case 1: Simple body with no If or Try

# Generated at 2024-06-01 15:22:04.528006
# Unit test for method visit_Name of class Resolver
def test_Resolver_visit_Name():    # Test case 1: Name is self_ty
    resolver = Resolver(root="root", alias={}, self_ty="self")
    node = Name(id="self", ctx=Load())
    result = resolver.visit_Name(node)
    assert isinstance(result, Name)
    assert result.id == "Self"

    # Test case 2: Name is in alias and not in its own alias value
    resolver = Resolver(root="root", alias={"root.name": "alias_value"})
    node = Name(id="name", ctx=Load())
    result = resolver.visit_Name(node)
    assert isinstance(result, Expr)
    assert unparse(result) == "alias_value"

    # Test case 3: Name is in alias and in its own alias value
    resolver = Resolver(root="root", alias={"root.name": "root.name"})
    node = Name(id="name", ctx=Load())
    result = resolver.visit_Name(node)

# Generated at 2024-06-01 15:22:07.880825
# Unit test for method compile of class Parser
def test_Parser_compile():    parser = Parser()

# Generated at 2024-06-01 15:22:10.787029
# Unit test for method visit_Subscript of class Resolver
def test_Resolver_visit_Subscript():    from ast import Subscript, Name, Load, Tuple, Constant, BinOp, BitOr

# Generated at 2024-06-01 15:22:14.716756
# Unit test for function const_type
def test_const_type():    assert const_type(Constant(value=42)) == "int"

# Generated at 2024-06-01 15:22:17.915069
# Unit test for method func_ann of class Parser
def test_Parser_func_ann():    parser = Parser()

# Generated at 2024-06-01 15:22:21.618993
# Unit test for method func_api of class Parser
def test_Parser_func_api():    parser = Parser()

# Generated at 2024-06-01 15:22:24.921222
# Unit test for function walk_body
def test_walk_body():    from ast import parse, If, Try, Expr, Constant

    # Test case 1: Simple body with no If or Try

# Generated at 2024-06-01 15:22:28.094138
# Unit test for method func_api of class Parser
def test_Parser_func_api():    parser = Parser()

# Generated at 2024-06-01 15:22:32.527030
# Unit test for function table
def test_table():    assert table('a', 'b', items=[['c', 'd'], ['e', 'f']]) == (
        "| a | b |\n"
        "|:---:|:---:|\n"
        "| c | d |\n"
        "| e | f |\n\n"
    )

# Generated at 2024-06-01 15:23:47.687710
# Unit test for method func_api of class Parser
def test_Parser_func_api():    parser = Parser()

# Generated at 2024-06-01 15:23:50.084558
# Unit test for method visit_Attribute of class Resolver
def test_Resolver_visit_Attribute():    resolver = Resolver(root="", alias={})

# Generated at 2024-06-01 15:23:53.752276
# Unit test for method globals of class Parser
def test_Parser_globals():    parser = Parser()

# Generated at 2024-06-01 15:23:57.055493
# Unit test for method class_api of class Parser
def test_Parser_class_api():    parser = Parser()

# Generated at 2024-06-01 15:24:00.350806
# Unit test for method func_ann of class Parser
def test_Parser_func_ann():    parser = Parser()

# Generated at 2024-06-01 15:24:03.053161
# Unit test for method load_docstring of class Parser
def test_Parser_load_docstring():    parser = Parser()

# Generated at 2024-06-01 15:24:05.819974
# Unit test for method load_docstring of class Parser
def test_Parser_load_docstring():    parser = Parser()

# Generated at 2024-06-01 15:24:09.043568
# Unit test for method compile of class Parser
def test_Parser_compile():    parser = Parser()

# Generated at 2024-06-01 15:24:12.337536
# Unit test for method compile of class Parser
def test_Parser_compile():    parser = Parser()

# Generated at 2024-06-01 15:24:15.041332
# Unit test for method func_api of class Parser
def test_Parser_func_api():    parser = Parser()