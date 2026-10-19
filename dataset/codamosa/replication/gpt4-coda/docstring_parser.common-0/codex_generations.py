

# Generated at 2024-03-18 05:17:23.120637
# Unit test for constructor of class Docstring
def test_Docstring():    # Create an instance of Docstring
    docstring = Docstring()

    # Check initial values of the instance
    assert docstring.short_description is None
    assert docstring.long_description is None
    assert docstring.blank_after_short_description is False
    assert docstring.blank_after_long_description is False
    assert isinstance(docstring.meta, list)
    assert len(docstring.meta) == 0

    # Check properties
    assert isinstance(docstring.params, list)
    assert len(docstring.params) == 0
    assert isinstance(docstring.raises, list)
    assert len(docstring.raises) == 0
    assert docstring.returns is None
    assert docstring.deprecation is None

    print("test_Docstring passed.")


# Generated at 2024-03-18 05:17:25.249058
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():    args = ["deprecated"]

# Generated at 2024-03-18 05:17:28.012401
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():    args = ["type", "description"]

# Generated at 2024-03-18 05:17:31.133541
# Unit test for constructor of class Docstring
def test_Docstring():    docstring = Docstring()

# Generated at 2024-03-18 05:17:34.744502
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():    args = ["returns"]

# Generated at 2024-03-18 05:17:36.156799
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():    args = ["param", "arg1"]

# Generated at 2024-03-18 05:17:42.567117
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():    # Test initialization with all arguments
    deprecated_all_args = DocstringDeprecated(
        args=["deprecated"],
        description="This feature is deprecated.",
        version="1.2.3"
    )
    assert deprecated_all_args.args == ["deprecated"]
    assert deprecated_all_args.description == "This feature is deprecated."
    assert deprecated_all_args.version == "1.2.3"

    # Test initialization with only required arguments
    deprecated_required_args = DocstringDeprecated(
        args=["deprecated"],
        description=None,
        version=None
    )
    assert deprecated_required_args.args == ["deprecated"]
    assert deprecated_required_args.description is None
    assert deprecated_required_args.version is None

    # Test initialization with no arguments, should raise TypeError
    try:
        invalid_deprecated = DocstringDeprecated()
    except TypeError as e:
        assert str(e) == "__init__() missing 2 required positional arguments: 'args' and 'description'"

# Generated at 2024-03-18 05:17:45.461229
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():    # Arrange
    args = ["deprecated"]
    description = "This feature will be removed in future versions."
    version = "2.0"

    # Act
    deprecated_meta = DocstringDeprecated(args, description, version)

    # Assert
    assert deprecated_meta.args == args
    assert deprecated_meta.description == description
    assert deprecated_meta.version == version

# Generated at 2024-03-18 05:17:49.360172
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():    args = ["returns"]

# Generated at 2024-03-18 05:17:56.485611
# Unit test for constructor of class DocstringParam
def test_DocstringParam():    # Test initialization of DocstringParam with all arguments
    param = DocstringParam(
        args=["param", "arg_name"],
        description="description of the parameter",
        arg_name="arg_name",
        type_name="str",
        is_optional=True,
        default="'default_value'"
    )
    assert param.args == ["param", "arg_name"]
    assert param.description == "description of the parameter"
    assert param.arg_name == "arg_name"
    assert param.type_name == "str"
    assert param.is_optional is True
    assert param.default == "'default_value'"

    # Test initialization of DocstringParam with minimal arguments
    param_minimal = DocstringParam(
        args=["param"],
        description=None,
        arg_name="arg_name",
        type_name=None,
        is_optional=None,
        default=None
    )
    assert param_minimal.args == ["param"]
    assert param_minimal.description is None
    assert param

# Generated at 2024-03-18 05:18:02.195717
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():    args = ["type_name"]

# Generated at 2024-03-18 05:18:04.956919
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():    args = ["type", "description"]

# Generated at 2024-03-18 05:18:06.976934
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():    args = ["param", "arg1"]

# Generated at 2024-03-18 05:18:08.455350
# Unit test for constructor of class ParseError

# Generated at 2024-03-18 05:18:10.309474
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():    args = ["deprecated"]

# Generated at 2024-03-18 05:18:12.984559
# Unit test for constructor of class Docstring
def test_Docstring():    docstring = Docstring()

# Generated at 2024-03-18 05:18:15.608568
# Unit test for constructor of class Docstring
def test_Docstring():    docstring = Docstring()

# Generated at 2024-03-18 05:18:18.877605
# Unit test for constructor of class DocstringParam
def test_DocstringParam():    arg_name = "test_arg"

# Generated at 2024-03-18 05:18:20.034342
# Unit test for constructor of class ParseError

# Generated at 2024-03-18 05:18:24.556316
# Unit test for constructor of class DocstringParam
def test_DocstringParam():    arg_name = "test_arg"

# Generated at 2024-03-18 05:18:30.697746
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():    args = ["raises", "ValueError"]

# Generated at 2024-03-18 05:18:32.456683
# Unit test for constructor of class ParseError

# Generated at 2024-03-18 05:18:34.528555
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():    args = ["param", "arg1"]

# Generated at 2024-03-18 05:18:42.645845
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():    # Test case for DocstringReturns with all arguments provided
    args = ["returns"]
    description = "A description of the return value."
    type_name = "int"
    is_generator = False
    return_name = "result"
    docstring_returns = DocstringReturns(args, description, type_name, is_generator, return_name)
    assert docstring_returns.args == args
    assert docstring_returns.description == description
    assert docstring_returns.type_name == type_name
    assert docstring_returns.is_generator == is_generator
    assert docstring_returns.return_name == return_name

    # Test case for DocstringReturns with minimal arguments provided
    args = ["yields"]
    description = None
    type_name = None
    is_generator = True
    docstring_returns_minimal = DocstringReturns(args, description, type_name, is_generator)
    assert docstring_returns_minimal.args == args
    assert docstring_returns_minimal

# Generated at 2024-03-18 05:18:44.739163
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():    args = ["param", "arg1"]

# Generated at 2024-03-18 05:18:46.945858
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():    args = ["deprecated"]

# Generated at 2024-03-18 05:18:51.424161
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():    args = ["deprecated"]

# Generated at 2024-03-18 05:19:00.801033
# Unit test for constructor of class Docstring
def test_Docstring():    # Create an instance of Docstring
    docstring = Docstring()

    # Check initial values of the instance
    assert docstring.short_description is None
    assert docstring.long_description is None
    assert docstring.blank_after_short_description is False
    assert docstring.blank_after_long_description is False
    assert isinstance(docstring.meta, list)
    assert len(docstring.meta) == 0

    # Check properties
    assert isinstance(docstring.params, list)
    assert len(docstring.params) == 0
    assert isinstance(docstring.raises, list)
    assert len(docstring.raises) == 0
    assert docstring.returns is None
    assert docstring.deprecation is None

    # Add meta information and check if it is reflected in properties
    param_meta = DocstringParam(['param'], 'description', 'arg_name', 'type_name', False, 'default')
    docstring.meta.append(param_meta)
   

# Generated at 2024-03-18 05:19:05.349443
# Unit test for constructor of class DocstringParam
def test_DocstringParam():    arg_name = "test_arg"

# Generated at 2024-03-18 05:19:08.400361
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():    args = ["exception"]

# Generated at 2024-03-18 05:19:20.655323
# Unit test for constructor of class Docstring
def test_Docstring():    # Create an instance of Docstring
    docstring = Docstring()

    # Check initial values of the instance
    assert docstring.short_description is None
    assert docstring.long_description is None
    assert docstring.blank_after_short_description is False
    assert docstring.blank_after_long_description is False
    assert isinstance(docstring.meta, list)
    assert len(docstring.meta) == 0

    # Check properties
    assert isinstance(docstring.params, list)
    assert len(docstring.params) == 0
    assert isinstance(docstring.raises, list)
    assert len(docstring.raises) == 0
    assert docstring.returns is None
    assert docstring.deprecation is None

    # Add some meta information

# Generated at 2024-03-18 05:19:23.920572
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():    args = ["deprecated"]

# Generated at 2024-03-18 05:19:29.585539
# Unit test for constructor of class DocstringParam
def test_DocstringParam():    # Test case for DocstringParam with all arguments provided
    param = DocstringParam(
        args=['param', 'arg_name', 'type_name'],
        description='description of the parameter',
        arg_name='arg_name',
        type_name='type_name',
        is_optional=True,
        default='None'
    )
    assert param.args == ['param', 'arg_name', 'type_name']
    assert param.description == 'description of the parameter'
    assert param.arg_name == 'arg_name'
    assert param.type_name == 'type_name'
    assert param.is_optional is True
    assert param.default == 'None'

    # Test case for DocstringParam with minimal arguments provided
    param_minimal = DocstringParam(
        args=['param', 'arg_name'],
        description=None,
        arg_name='arg_name',
        type_name=None,
        is_optional=None,
        default=None
    )

# Generated at 2024-03-18 05:19:31.082435
# Unit test for constructor of class ParseError

# Generated at 2024-03-18 05:19:36.322500
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():    args = ["returns"]

# Generated at 2024-03-18 05:19:40.847661
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():    args = ["returns"]

# Generated at 2024-03-18 05:19:43.783046
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():    args = ["deprecated"]

# Generated at 2024-03-18 05:19:45.001844
# Unit test for constructor of class ParseError

# Generated at 2024-03-18 05:19:50.237707
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():    args = ["returns"]

# Generated at 2024-03-18 05:19:52.381242
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():    args = ["param", "arg1"]

# Generated at 2024-03-18 05:20:00.813675
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():    args = ["deprecated"]

# Generated at 2024-03-18 05:20:03.450123
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():    args = ["exception"]

# Generated at 2024-03-18 05:20:06.289439
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():    args = ["deprecated"]

# Generated at 2024-03-18 05:20:08.546134
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():    args = ["exception"]

# Generated at 2024-03-18 05:20:10.565287
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():    args = ["param", "arg1"]

# Generated at 2024-03-18 05:20:17.984204
# Unit test for constructor of class DocstringParam
def test_DocstringParam():    # Arrange
    args = ["param", "arg_name", "type_name", "is_optional", "default"]
    description = "This is a test parameter."
    arg_name = "test_arg"
    type_name = "str"
    is_optional = True
    default = "None"

    # Act
    param = DocstringParam(args, description, arg_name, type_name, is_optional, default)

    # Assert
    assert param.args == args
    assert param.description == description
    assert param.arg_name == arg_name
    assert param.type_name == type_name
    assert param.is_optional == is_optional
    assert param.default == default

# Generated at 2024-03-18 05:20:21.398461
# Unit test for constructor of class Docstring
def test_Docstring():    docstring = Docstring()

# Generated at 2024-03-18 05:20:24.176232
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():    args = ["deprecated"]

# Generated at 2024-03-18 05:20:31.916660
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():    # Test case for DocstringReturns with all arguments provided
    args = ["returns"]
    description = "A description of the return value."
    type_name = "int"
    is_generator = False
    return_name = "result"

    docstring_returns = DocstringReturns(args, description, type_name, is_generator, return_name)

    assert docstring_returns.args == args
    assert docstring_returns.description == description
    assert docstring_returns.type_name == type_name
    assert docstring_returns.is_generator == is_generator
    assert docstring_returns.return_name == return_name

    # Test case for DocstringReturns with minimal arguments provided
    args = ["yields"]
    description = None
    type_name = None
    is_generator = True

    docstring_returns_minimal = DocstringReturns(args, description, type_name, is_generator)

    assert docstring_returns_minimal.args == args
    assert docstring_returns_minimal

# Generated at 2024-03-18 05:20:37.950051
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():    args = ["returns"]

# Generated at 2024-03-18 05:20:50.760919
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():    args = ["param", "arg1"]

# Generated at 2024-03-18 05:20:53.381636
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():    args = ["ValueError"]

# Generated at 2024-03-18 05:21:03.290091
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():    args = ["deprecated"]

# Generated at 2024-03-18 05:21:05.553277
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():    args = ["exception"]

# Generated at 2024-03-18 05:21:10.095377
# Unit test for constructor of class DocstringParam
def test_DocstringParam():    # Arrange
    args = ["param", "arg_name", "type_name", "is_optional", "default"]
    description = "This is a test parameter."
    arg_name = "test_arg"
    type_name = "str"
    is_optional = True
    default = "None"

    # Act
    param = DocstringParam(args, description, arg_name, type_name, is_optional, default)

    # Assert
    assert param.args == args
    assert param.description == description
    assert param.arg_name == arg_name
    assert param.type_name == type_name
    assert param.is_optional == is_optional
    assert param.default == default

# Generated at 2024-03-18 05:21:11.368335
# Unit test for constructor of class ParseError

# Generated at 2024-03-18 05:21:13.065290
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():    args = ["param", "arg1"]

# Generated at 2024-03-18 05:21:17.302184
# Unit test for constructor of class DocstringParam
def test_DocstringParam():    # Test initialization of DocstringParam
    args = ["param", "arg_name", "type_name", "is_optional", "default"]
    description = "This is a test parameter."
    arg_name = "test_arg"
    type_name = "str"
    is_optional = True
    default = "None"

    param = DocstringParam(args, description, arg_name, type_name, is_optional, default)

    assert param.args == args
    assert param.description == description
    assert param.arg_name == arg_name
    assert param.type_name == type_name
    assert param.is_optional == is_optional
    assert param.default == default


# Generated at 2024-03-18 05:21:19.764226
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():    args = ["deprecated"]

# Generated at 2024-03-18 05:21:22.031176
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():    args = ["raises", "exception"]

# Generated at 2024-03-18 05:21:46.211859
# Unit test for constructor of class ParseError

# Generated at 2024-03-18 05:21:49.323822
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():    args = ["type", "description"]

# Generated at 2024-03-18 05:21:50.543361
# Unit test for constructor of class ParseError

# Generated at 2024-03-18 05:21:56.828495
# Unit test for constructor of class Docstring
def test_Docstring():    # Create an instance of Docstring
    docstring = Docstring()

    # Check initial values of the instance
    assert docstring.short_description is None
    assert docstring.long_description is None
    assert docstring.blank_after_short_description is False
    assert docstring.blank_after_long_description is False
    assert isinstance(docstring.meta, list)
    assert len(docstring.meta) == 0

    # Check properties
    assert isinstance(docstring.params, list)
    assert len(docstring.params) == 0
    assert isinstance(docstring.raises, list)
    assert len(docstring.raises) == 0
    assert docstring.returns is None
    assert docstring.deprecation is None

    # Add some meta information and check if it is reflected in properties

# Generated at 2024-03-18 05:22:04.792665
# Unit test for constructor of class Docstring
def test_Docstring():    # Create an instance of Docstring
    docstring = Docstring()

    # Check initial values of the instance
    assert docstring.short_description is None
    assert docstring.long_description is None
    assert docstring.blank_after_short_description is False
    assert docstring.blank_after_long_description is False
    assert isinstance(docstring.meta, list)
    assert len(docstring.meta) == 0

    # Check properties
    assert isinstance(docstring.params, list)
    assert len(docstring.params) == 0
    assert isinstance(docstring.raises, list)
    assert len(docstring.raises) == 0
    assert docstring.returns is None
    assert docstring.deprecation is None

    # Add some meta information and check if it is reflected in properties

# Generated at 2024-03-18 05:22:10.657812
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():    args = ["returns"]

# Generated at 2024-03-18 05:22:13.923506
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():    args = ["deprecated"]

# Generated at 2024-03-18 05:22:15.746505
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():    args = ["param", "arg1"]

# Generated at 2024-03-18 05:22:17.903728
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():    args = ["deprecated"]

# Generated at 2024-03-18 05:22:24.288584
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():    args = ["exception"]

# Generated at 2024-03-18 05:23:10.572852
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():    args = ["param", "arg1"]

# Generated at 2024-03-18 05:23:15.644190
# Unit test for constructor of class DocstringParam
def test_DocstringParam():    arg_name = "test_arg"

# Generated at 2024-03-18 05:23:19.339677
# Unit test for constructor of class Docstring
def test_Docstring():    docstring = Docstring()

# Generated at 2024-03-18 05:23:29.732348
# Unit test for constructor of class Docstring
def test_Docstring():    # Create an instance of Docstring
    docstring = Docstring()

    # Check initial values of the instance
    assert docstring.short_description is None
    assert docstring.long_description is None
    assert docstring.blank_after_short_description is False
    assert docstring.blank_after_long_description is False
    assert isinstance(docstring.meta, list)
    assert len(docstring.meta) == 0

    # Check properties
    assert isinstance(docstring.params, list)
    assert len(docstring.params) == 0
    assert isinstance(docstring.raises, list)
    assert len(docstring.raises) == 0
    assert docstring.returns is None
    assert docstring.deprecation is None

    # Add some meta information and check if properties return the correct values

# Generated at 2024-03-18 05:23:35.198163
# Unit test for constructor of class DocstringParam
def test_DocstringParam():    # Test case for DocstringParam constructor
    arg_name = "test_arg"
    type_name = "str"
    is_optional = True
    default = "None"
    description = "This is a test argument."

    param = DocstringParam(
        args=[],
        description=description,
        arg_name=arg_name,
        type_name=type_name,
        is_optional=is_optional,
        default=default,
    )

    assert param.arg_name == arg_name
    assert param.type_name == type_name
    assert param.is_optional == is_optional
    assert param.default == default
    assert param.description == description


# Generated at 2024-03-18 05:23:36.318931
# Unit test for constructor of class ParseError

# Generated at 2024-03-18 05:23:38.464175
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():    args = ["param", "arg1"]

# Generated at 2024-03-18 05:23:44.739245
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():    args = ["returns"]

# Generated at 2024-03-18 05:23:49.134793
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():    args = ["returns"]

# Generated at 2024-03-18 05:23:57.151304
# Unit test for constructor of class Docstring
def test_Docstring():    # Create an instance of Docstring
    docstring = Docstring()

    # Check initial values of the instance
    assert docstring.short_description is None
    assert docstring.long_description is None
    assert docstring.blank_after_short_description is False
    assert docstring.blank_after_long_description is False
    assert isinstance(docstring.meta, list)
    assert len(docstring.meta) == 0

    # Check properties
    assert isinstance(docstring.params, list)
    assert len(docstring.params) == 0
    assert isinstance(docstring.raises, list)
    assert len(docstring.raises) == 0
    assert docstring.returns is None
    assert docstring.deprecation is None

    # Add some meta information and check if it is reflected in properties
    param_meta = DocstringParam(['param'], 'description', 'arg_name', 'type_name', False, 'default')
    docstring.meta.append(param_meta)


# Generated at 2024-03-18 05:24:43.291439
# Unit test for constructor of class ParseError

# Generated at 2024-03-18 05:24:47.813193
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():    args = ["raises", "exception"]

# Generated at 2024-03-18 05:24:52.972027
# Unit test for constructor of class DocstringParam
def test_DocstringParam():    arg_name = "test_arg"

# Generated at 2024-03-18 05:24:54.685525
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():    args = ["param", "arg1"]

# Generated at 2024-03-18 05:24:57.032424
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():    args = ["param", "arg1"]

# Generated at 2024-03-18 05:24:58.248737
# Unit test for constructor of class ParseError

# Generated at 2024-03-18 05:25:00.160253
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():    args = ["deprecated"]

# Generated at 2024-03-18 05:25:03.374125
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():    args = ["type", "description"]

# Generated at 2024-03-18 05:25:10.504226
# Unit test for constructor of class Docstring
def test_Docstring():    # Create an instance of Docstring
    docstring = Docstring()

    # Check initial values of the instance
    assert docstring.short_description is None
    assert docstring.long_description is None
    assert docstring.blank_after_short_description is False
    assert docstring.blank_after_long_description is False
    assert isinstance(docstring.meta, list)
    assert len(docstring.meta) == 0

    # Check properties
    assert isinstance(docstring.params, list)
    assert len(docstring.params) == 0
    assert isinstance(docstring.raises, list)
    assert len(docstring.raises) == 0
    assert docstring.returns is None
    assert docstring.deprecation is None

    # Add some meta information and check again

# Generated at 2024-03-18 05:25:12.405840
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():    args = ["param", "arg1"]

# Generated at 2024-03-18 05:25:59.348326
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():    args = ["param", "arg1"]

# Generated at 2024-03-18 05:26:01.030113
# Unit test for constructor of class ParseError

# Generated at 2024-03-18 05:26:03.016117
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():    args = ["param", "arg1"]

# Generated at 2024-03-18 05:26:04.857062
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():    args = ["ValueError"]

# Generated at 2024-03-18 05:26:08.100789
# Unit test for constructor of class DocstringParam
def test_DocstringParam():    arg_name = "test_arg"

# Generated at 2024-03-18 05:26:09.276402
# Unit test for constructor of class ParseError

# Generated at 2024-03-18 05:26:11.207867
# Unit test for constructor of class ParseError

# Generated at 2024-03-18 05:26:13.345862
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():    args = ["param", "arg1"]

# Generated at 2024-03-18 05:26:14.796332
# Unit test for constructor of class ParseError

# Generated at 2024-03-18 05:26:17.622280
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():    args = ["deprecated"]

# Generated at 2024-03-18 05:27:06.545697
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():    args = ["returns"]

# Generated at 2024-03-18 05:27:08.861419
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():    args = ["deprecated"]