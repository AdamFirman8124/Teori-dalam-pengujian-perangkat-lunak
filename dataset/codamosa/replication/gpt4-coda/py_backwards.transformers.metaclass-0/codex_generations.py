

# Generated at 2024-03-18 06:30:25.210480
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():    transformer = MetaclassTransformer()

    # Create a class definition with a metaclass

# Generated at 2024-03-18 06:30:30.723621
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():    # Arrange
    transformer = MetaclassTransformer()
    metaclass_name = ast.Name(id='Meta', ctx=ast.Load())
    class_node = ast.ClassDef(
        name='A',
        bases=[],
        keywords=[ast.keyword(arg='metaclass', value=metaclass_name)],
        body=[],
        decorator_list=[]
    )
    expected_bases = class_bases.get_body(metaclass=metaclass_name, bases=ast.List(elts=[]))

    # Act
    transformed_node = transformer.visit_ClassDef(class_node)

    # Assert
    assert transformed_node.keywords == []
    assert transformed_node.bases == expected_bases
    assert transformer._tree_changed is True

# Generated at 2024-03-18 06:30:36.692910
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():    # Arrange
    transformer = MetaclassTransformer()
    metaclass_name = ast.Name(id='Meta', ctx=ast.Load())
    class_node = ast.ClassDef(
        name='A',
        bases=[],
        keywords=[ast.keyword(arg='metaclass', value=metaclass_name)],
        body=[],
        decorator_list=[]
    )
    expected_bases = class_bases.get_body(metaclass=metaclass_name, bases=ast.List(elts=[]))

    # Act
    transformed_node = transformer.visit_ClassDef(class_node)

    # Assert
    assert transformed_node.keywords == []
    assert transformed_node.bases == expected_bases
    assert transformer._tree_changed is True

# Generated at 2024-03-18 06:30:46.501529
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():    # Arrange
    transformer = MetaclassTransformer()
    metaclass_name = ast.Name(id='Meta', ctx=ast.Load())
    class_node = ast.ClassDef(
        name='A',
        bases=[],
        keywords=[ast.keyword(arg='metaclass', value=metaclass_name)],
        body=[],
        decorator_list=[]
    )

    # Act
    transformed_node = transformer.visit_ClassDef(class_node)

    # Assert
    assert len(transformed_node.bases) == 1
    assert isinstance(transformed_node.bases[0], ast.Call)
    assert transformed_node.bases[0].func.id == '_py_backwards_six_withmetaclass'
    assert transformed_node.bases[0].args[0] is metaclass_name
    assert transformed_node.keywords == []

# Generated at 2024-03-18 06:30:53.053367
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():    transformer = MetaclassTransformer()

    # Create a class definition with a metaclass

# Generated at 2024-03-18 06:30:59.233690
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():    transformer = MetaclassTransformer()

    # Create a class definition with a metaclass

# Generated at 2024-03-18 06:31:04.324780
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():    transformer = MetaclassTransformer()

    # Create a class definition with a metaclass

# Generated at 2024-03-18 06:31:09.790948
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():    transformer = MetaclassTransformer()

    # Create a class definition with a metaclass

# Generated at 2024-03-18 06:31:17.756092
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():    transformer = MetaclassTransformer()

    # Create a class definition with a metaclass

# Generated at 2024-03-18 06:31:24.041122
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():    transformer = MetaclassTransformer()

    # Create a module node with no body

# Generated at 2024-03-18 06:31:32.431546
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():    transformer = MetaclassTransformer()

    # Create a class definition with a metaclass

# Generated at 2024-03-18 06:31:38.096533
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():    transformer = MetaclassTransformer()

    # Create a class definition with a metaclass

# Generated at 2024-03-18 06:31:44.141934
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():    transformer = MetaclassTransformer()

    # Create a class definition with a metaclass

# Generated at 2024-03-18 06:31:49.724491
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():    transformer = MetaclassTransformer()

    # Create a module node with no body

# Generated at 2024-03-18 06:31:56.353581
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():    transformer = MetaclassTransformer()

    # Create a module node with no body

# Generated at 2024-03-18 06:32:04.091801
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():    transformer = MetaclassTransformer()

    # Create a class definition with a metaclass

# Generated at 2024-03-18 06:32:19.178532
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():    # Arrange
    transformer = MetaclassTransformer()
    module_node = ast.Module(body=[])

    # Act
    transformed_module = transformer.visit_Module(module_node)

    # Assert
    assert len(transformed_module.body) == 1
    assert isinstance(transformed_module.body[0], ast.ImportFrom)
    assert transformed_module.body[0].module == 'six'
    assert transformed_module.body[0].names[0].name == 'with_metaclass'
    assert transformed_module.body[0].names[0].asname == '_py_backwards_six_withmetaclass'

# Generated at 2024-03-18 06:32:26.945470
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():    transformer = MetaclassTransformer()

    # Create a class definition with a metaclass

# Generated at 2024-03-18 06:32:32.524051
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():    transformer = MetaclassTransformer()

    # Create a class definition with a metaclass

# Generated at 2024-03-18 06:32:37.061612
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():    # Arrange
    source_ast = ast.parse("class A: pass")
    transformer = MetaclassTransformer()

    # Act
    transformed_ast = transformer.visit_Module(source_ast)

    # Assert
    assert len(transformed_ast.body) == 2
    assert isinstance(transformed_ast.body[0], ast.ImportFrom)
    assert transformed_ast.body[0].module == 'six'
    assert transformed_ast.body[0].names[0].name == 'with_metaclass'
    assert isinstance(transformed_ast.body[1], ast.ClassDef)
    assert transformed_ast.body[1].name == 'A'

# Generated at 2024-03-18 06:32:48.585706
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():    transformer = MetaclassTransformer()

    # Create a class definition with a metaclass

# Generated at 2024-03-18 06:32:53.656092
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():    transformer = MetaclassTransformer()

    # Create a module node with no body

# Generated at 2024-03-18 06:32:59.048391
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():    # Arrange
    transformer = MetaclassTransformer()
    metaclass_name = ast.Name(id='Meta', ctx=ast.Load())
    class_node = ast.ClassDef(
        name='A',
        bases=[],
        keywords=[ast.keyword(arg='metaclass', value=metaclass_name)],
        body=[],
        decorator_list=[]
    )
    expected_bases = class_bases.get_body(metaclass=metaclass_name, bases=ast.List(elts=[]))

    # Act
    transformed_node = transformer.visit_ClassDef(class_node)

    # Assert
    assert transformed_node.keywords == []
    assert transformed_node.bases == expected_bases
    assert transformer._tree_changed is True

# Generated at 2024-03-18 06:33:05.143350
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():    transformer = MetaclassTransformer()

    # Create a class definition with a metaclass

# Generated at 2024-03-18 06:33:10.560641
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():    transformer = MetaclassTransformer()

    # Create a module node with no body

# Generated at 2024-03-18 06:33:16.719924
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():    transformer = MetaclassTransformer()

    # Create a class definition with a metaclass

# Generated at 2024-03-18 06:33:20.775334
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():    transformer = MetaclassTransformer()

    # Create a module node with no body

# Generated at 2024-03-18 06:33:28.590713
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():    transformer = MetaclassTransformer()

    # Create a class definition with a metaclass

# Generated at 2024-03-18 06:33:36.878174
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():    transformer = MetaclassTransformer()

    # Create a class definition with a metaclass

# Generated at 2024-03-18 06:33:42.813464
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():    transformer = MetaclassTransformer()

    # Create a class definition with a metaclass

# Generated at 2024-03-18 06:33:58.856817
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():    # Arrange
    transformer = MetaclassTransformer()
    metaclass_name = ast.Name(id='Meta', ctx=ast.Load())
    class_node = ast.ClassDef(
        name='A',
        bases=[],
        keywords=[ast.keyword(arg='metaclass', value=metaclass_name)],
        body=[],
        decorator_list=[]
    )
    expected_bases = class_bases.get_body(metaclass=metaclass_name, bases=ast.List(elts=[]))

    # Act
    transformed_node = transformer.visit_ClassDef(class_node)

    # Assert
    assert transformed_node.keywords == []
    assert transformed_node.bases == expected_bases
    assert transformer._tree_changed is True

# Generated at 2024-03-18 06:34:06.716608
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():    transformer = MetaclassTransformer()

    # Create a class definition with a metaclass

# Generated at 2024-03-18 06:34:13.095431
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():    transformer = MetaclassTransformer()

    # Create a class definition with a metaclass

# Generated at 2024-03-18 06:34:18.841655
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():    transformer = MetaclassTransformer()

    # Create a class definition with a metaclass

# Generated at 2024-03-18 06:34:24.111276
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():    transformer = MetaclassTransformer()

    # Create a class definition with a metaclass

# Generated at 2024-03-18 06:34:29.746726
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():    transformer = MetaclassTransformer()

    # Create a class definition with a metaclass

# Generated at 2024-03-18 06:34:38.072551
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():    transformer = MetaclassTransformer()

    # Create a class definition with a metaclass

# Generated at 2024-03-18 06:34:43.101403
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():    transformer = MetaclassTransformer()

    # Create a class definition with a metaclass

# Generated at 2024-03-18 06:34:51.455978
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():    transformer = MetaclassTransformer()

    # Create a class definition with a metaclass

# Generated at 2024-03-18 06:35:00.224970
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():    transformer = MetaclassTransformer()

    # Create a class definition with a metaclass

# Generated at 2024-03-18 06:35:27.717935
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():    transformer = MetaclassTransformer()

    # Create a class definition with a metaclass

# Generated at 2024-03-18 06:35:34.933871
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():    transformer = MetaclassTransformer()

    # Create a class definition with a metaclass

# Generated at 2024-03-18 06:35:42.127916
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():    transformer = MetaclassTransformer()

    # Create a class definition with a metaclass

# Generated at 2024-03-18 06:35:47.492983
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():    transformer = MetaclassTransformer()

    # Create a class definition with a metaclass

# Generated at 2024-03-18 06:35:52.446846
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():    transformer = MetaclassTransformer()

    # Create a class definition with a metaclass

# Generated at 2024-03-18 06:36:00.974705
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():    transformer = MetaclassTransformer()

    # Create a class definition with a metaclass

# Generated at 2024-03-18 06:36:08.685664
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():    transformer = MetaclassTransformer()

    # Create a class definition with a metaclass

# Generated at 2024-03-18 06:36:13.949933
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():    # Arrange
    transformer = MetaclassTransformer()
    class_def_node = ast.ClassDef(
        name='A',
        bases=[],
        keywords=[ast.keyword(arg='metaclass', value=ast.Name(id='B', ctx=ast.Load()))],
        body=[],
        decorator_list=[]
    )

    expected_class_def_node = ast.ClassDef(
        name='A',
        bases=[class_bases.get_body(metaclass=ast.Name(id='B', ctx=ast.Load()), bases=ast.List(elts=[]))],
        keywords=[],
        body=[],
        decorator_list=[]
    )

    # Act
    transformed_node = transformer.visit_ClassDef(class_def_node)

    # Assert
    assert transformed_node == expected_class_def_node
    assert transformer._tree_changed is True

# Generated at 2024-03-18 06:36:20.472796
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():    transformer = MetaclassTransformer()

    # Create a class definition with a metaclass

# Generated at 2024-03-18 06:36:27.525099
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():    transformer = MetaclassTransformer()

    # Create a class definition with a metaclass

# Generated at 2024-03-18 06:37:08.682377
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():    transformer = MetaclassTransformer()

    # Create a class definition with a metaclass

# Generated at 2024-03-18 06:37:14.941392
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():    transformer = MetaclassTransformer()

    # Create a class definition with a metaclass

# Generated at 2024-03-18 06:37:20.124973
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():    transformer = MetaclassTransformer()

    # Create a class definition with a metaclass

# Generated at 2024-03-18 06:37:28.520426
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():    transformer = MetaclassTransformer()

    # Create a class definition with a metaclass

# Generated at 2024-03-18 06:37:34.458409
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():    # Arrange
    transformer = MetaclassTransformer()
    class_node = ast.ClassDef(
        name='A',
        bases=[],
        keywords=[ast.keyword(arg='metaclass', value=ast.Name(id='B', ctx=ast.Load()))],
        body=[],
        decorator_list=[]
    )

    # Act
    transformed_node = transformer.visit_ClassDef(class_node)

    # Assert
    assert len(transformed_node.bases) == 1
    assert isinstance(transformed_node.bases[0], ast.Call)
    assert transformed_node.bases[0].func.id == '_py_backwards_six_withmetaclass'
    assert len(transformed_node.bases[0].args) == 2
    assert isinstance(transformed_node.bases[0].args[0], ast.Name)
    assert transformed_node.bases[0].args[0].id == 'B'

# Generated at 2024-03-18 06:37:40.407484
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():    transformer = MetaclassTransformer()

    # Create a class definition with a metaclass

# Generated at 2024-03-18 06:37:49.102854
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():    transformer = MetaclassTransformer()

    # Create a class definition with a metaclass

# Generated at 2024-03-18 06:37:55.372564
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():    transformer = MetaclassTransformer()

    # Create a class definition with a metaclass

# Generated at 2024-03-18 06:38:04.234171
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():    transformer = MetaclassTransformer()

    # Create a class definition with a metaclass

# Generated at 2024-03-18 06:38:10.832489
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():    transformer = MetaclassTransformer()

    # Create a class definition with a metaclass

# Generated at 2024-03-18 06:39:32.022391
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():    # Arrange
    transformer = MetaclassTransformer()
    class_def_node = ast.ClassDef(
        name='A',
        bases=[],
        keywords=[ast.keyword(arg='metaclass', value=ast.Name(id='B', ctx=ast.Load()))],
        body=[],
        decorator_list=[]
    )

    expected_class_def_node = ast.ClassDef(
        name='A',
        bases=[class_bases.get_body(metaclass=ast.Name(id='B', ctx=ast.Load()), bases=ast.List(elts=[]))],
        keywords=[],
        body=[],
        decorator_list=[]
    )

    # Act
    transformed_node = transformer.visit_ClassDef(class_def_node)

    # Assert
    assert transformed_node == expected_class_def_node
    assert transformer._tree_changed is True

# Generated at 2024-03-18 06:39:38.233327
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():    transformer = MetaclassTransformer()

    # Create a class definition with a metaclass

# Generated at 2024-03-18 06:39:46.788032
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():    transformer = MetaclassTransformer()

    # Create a class definition with a metaclass

# Generated at 2024-03-18 06:39:54.785076
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():    transformer = MetaclassTransformer()

    # Create a class definition with a metaclass

# Generated at 2024-03-18 06:40:03.162523
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():    transformer = MetaclassTransformer()

    # Create a class definition with a metaclass

# Generated at 2024-03-18 06:40:08.480421
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():    transformer = MetaclassTransformer()

    # Create a class definition with a metaclass

# Generated at 2024-03-18 06:40:14.194772
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():    transformer = MetaclassTransformer()

    # Create a class definition with a metaclass