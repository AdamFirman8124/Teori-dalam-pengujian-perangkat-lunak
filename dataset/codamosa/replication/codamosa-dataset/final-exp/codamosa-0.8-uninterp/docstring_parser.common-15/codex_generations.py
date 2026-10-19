

# Generated at 2022-06-13 19:30:56.299050
# Unit test for constructor of class ParseError
def test_ParseError():
    #[Syntax error]
    try:
        raise ParseError("error")
    except ParseError as error:
        print(error)

# Generated at 2022-06-13 19:30:57.812959
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    DocstringDeprecated(["a", "b"], "c", "d")


# Generated at 2022-06-13 19:30:59.411171
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    assert DocstringMeta([], '')

# Generated at 2022-06-13 19:31:03.192538
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    docstringMeta = DocstringMeta(["arg", "parm"], "description of the parameter.")

    assert docstringMeta.args == ["arg", "parm"]
    assert docstringMeta.description == "description of the parameter."

# Generated at 2022-06-13 19:31:14.694332
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
     #Example 1
     assert(str(DocstringReturns(args=["return", "returns"], description="A string", \
           type_name="str", is_generator=False).args) == "['return', 'returns']")
     assert(DocstringReturns(args=["return", "returns"], description="A string", \
           type_name="str", is_generator=False).description == "A string")
     assert(DocstringReturns(args=["return", "returns"], description="A string", \
           type_name="str", is_generator=False).type_name == "str")
     assert(DocstringReturns(args=["return", "returns"], description="A string", \
           type_name="str", is_generator=False).is_generator == False)

# Generated at 2022-06-13 19:31:15.082494
# Unit test for constructor of class ParseError
def test_ParseError():
    ParseError()

# Generated at 2022-06-13 19:31:18.411317
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    args = ['param', 'arg', 'argument', 'attribute', 'key', 'keyword']
    description = ' descrip'
    type_name = 'type'
    d = DocstringRaises(args, description, type_name)
    if d.args == args and d.description == description and d.type_name == type_name:
        pass

# Generated at 2022-06-13 19:31:30.903638
# Unit test for constructor of class Docstring
def test_Docstring():
    # Arrange
    docstring = Docstring()

    # Act
    short_description = docstring.__short_description
    long_description = docstring.__long_description
    blank_after_short_description = docstring.__blank_after_short_description
    blank_after_long_description = docstring.__blank_after_long_description
    params = docstring.__params
    raises = docstring.__raises
    returns = docstring.__returns
    deprecation = docstring.__deprecation

    # Assert
    assert short_description == None
    assert long_description == None
    assert blank_after_short_description == False
    assert blank_after_long_description == False
    assert params == []
    assert raises == []
    assert returns == None
    assert deprecation == None




# Generated at 2022-06-13 19:31:38.697548
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    args = ["param", "arg", "description"]
    arg_name = "arg"
    type_name = "type"
    is_optional = False
    default = None
    d = DocstringParam(args, "description", arg_name, type_name, is_optional, default)
    assert d.args == args
    assert d.description == "description"
    assert d.arg_name == "arg"
    assert d.type_name == "type"
    assert d.is_optional == False
    assert d.default == None


# Generated at 2022-06-13 19:31:39.882648
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    pass


# Generated at 2022-06-13 19:31:50.052481
# Unit test for constructor of class Docstring
def test_Docstring():
    doc = Docstring()
    assert doc.short_description is None
    assert doc.long_description is None
    assert doc.blank_after_short_description is False
    assert doc.blank_after_long_description is False
    assert doc.meta == []
    assert doc.params == []
    assert doc.raises == []
    assert doc.returns is None
    assert doc.deprecation is None


# Generated at 2022-06-13 19:31:54.078682
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    """Unit test for constructor of class DocstringMeta."""
    args = ["a"]
    description = "abc"
    item = DocstringMeta(args, description)
    assert item.args == ["a"]
    assert item.description == description



# Generated at 2022-06-13 19:32:03.007392
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    try:
        # Docstring param that is not a docstring param
        DocstringReturns(args=['test_arg'], description='test_desc', type_name='test_type', is_generator=False, return_name='test_name')
        assert False
    except Exception:
        assert True
    # Docstring param that is a docstring param
    DocstringReturns(args=['test_arg'], description='test_desc', type_name='test_type', is_generator=True)
    assert True


# Generated at 2022-06-13 19:32:07.920903
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    a = DocstringMeta(['a', 'b'], 'hello world')
    assert a.args == ['a', 'b']
    assert a.description == 'hello world'


# Generated at 2022-06-13 19:32:11.272409
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    docstring = DocstringDeprecated('args', 'description', 'version')
    assert docstring.args == ['args']
    assert docstring.description == 'description'
    assert docstring.version == 'version'

# Generated at 2022-06-13 19:32:19.843665
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    import pytest
    docstringParam = DocstringParam([":param", "arg", ":"], "description", "arg", None, False, None)
    assert docstringParam.args == [":param", "arg", ":"]
    assert docstringParam.description == "description"
    assert docstringParam.arg_name == "arg"
    assert docstringParam.type_name is None
    assert docstringParam.is_optional is False
    assert docstringParam.default is None
    with pytest.raises(TypeError):
        docstringParam = DocstringParam("description", "description", "arg", None, False, None)
    with pytest.raises(TypeError):
        docstringParam = DocstringParam(["description"], ";", "arg", None, False, None)


# Generated at 2022-06-13 19:32:23.356571
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    docstring_raises = DocstringRaises(["args"], "This is a type", "TypeName")
    assert docstring_raises.args == ["args"]
    assert docstring_raises.description == "This is a type"
    assert docstring_raises.type_name == "TypeName"


# Generated at 2022-06-13 19:32:29.132505
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    args = ["parameter"]
    description = "Some Description"
    arg_name = "arg"
    type_name = "str"
    is_optional = True
    default = "''"
    test_item = DocstringParam(args = args, description = description, arg_name = arg_name, type_name = type_name, is_optional = is_optional, default = default)
    assert test_item.args == args
    assert test_item.description == description
    assert test_item.arg_name == arg_name
    assert test_item.type_name == type_name
    assert test_item.is_optional == is_optional
    assert test_item.default == default
    

# Generated at 2022-06-13 19:32:33.008076
# Unit test for constructor of class Docstring
def test_Docstring():
    a = Docstring()
    assert a.short_description is None
    assert a.long_description is None
    assert a.blank_after_short_description == False
    assert a.blank_after_long_description == False
    assert a.meta == []


# Generated at 2022-06-13 19:32:43.577819
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    args = ['param', 'arg1', 'arg2']
    description = 'description of parameter'
    arg_name = 'parameter'
    type_name = 'type'
    is_optional = True
    default = 'None'
    test_docstring = DocstringParam(args, description, arg_name, type_name, is_optional, default)
    assert(test_docstring.args == args)
    assert(test_docstring.description == description)
    assert(test_docstring.arg_name == arg_name)
    assert(test_docstring.type_name == type_name)
    assert(test_docstring.is_optional == is_optional)
    assert(test_docstring.default == default)


# Generated at 2022-06-13 19:33:00.622028
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    kwargs = {
        "args" : ["teste"],
        "description" : "teste",
        "type_name" : "teste",
        "is_generator" : True,
        "return_name" : "teste",
    }
    d_ret = DocstringReturns(**kwargs)

    assert d_ret.args == ["teste"]
    assert d_ret.description == "teste"
    assert d_ret.type_name == "teste"
    assert d_ret.is_generator == True
    assert d_ret.return_name == "teste"



# Generated at 2022-06-13 19:33:04.165286
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    args=['1','2','3','4','5']
    description='6'
    version='7'
    dd=DocstringDeprecated(args,description,version)
    assert dd.args==args
    assert dd.description==description
    assert dd.version==version


# Generated at 2022-06-13 19:33:07.024520
# Unit test for constructor of class ParseError
def test_ParseError():
    try:
        raise ParseError("Incorrect position for a paragraph line.")
    except ParseError:
        pass


# Generated at 2022-06-13 19:33:11.538011
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    # Test that the function constructs a DocstringDeprecated object properly
    docstring = DocstringDeprecated(["deprecated"], "This function is deprecated", "1.0")
    assert docstring.args == ["deprecated"]
    assert docstring.description == "This function is deprecated"
    assert docstring.version == "1.0"

# Generated at 2022-06-13 19:33:15.969623
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    d=DocstringRaises(["raises", "exception"], "description", "Exception")
    assert d.description == "description"
    assert d.type_name == "Exception"
    assert d.args == ["raises", "exception"]


# Generated at 2022-06-13 19:33:18.771740
# Unit test for constructor of class ParseError
def test_ParseError():
    try:
        raise ParseError('Bad mojo')
    except ParseError as e:
        print(e)
        assert str(e) == 'Bad mojo'


# Generated at 2022-06-13 19:33:24.283383
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    newDocstringDeprecated = DocstringDeprecated(":deprecated", "1.0.0", "None")
    docstringDeprecated = newDocstringDeprecated.args
    assert docstringDeprecated == [":deprecated"]
    assert newDocstringDeprecated.version == "1.0.0"
    assert newDocstringDeprecated.description == "None"



# Generated at 2022-06-13 19:33:27.074632
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    a = DocstringParam(["arg"], "description", "arg_name", "type_name", True, "default")
    assert a.args == ["arg"]
    assert a.description == "description"
    assert a.arg_name == "arg_name"
    assert a.type_name == "type_name"
    assert a.is_optional == True
    assert a.default == "default"


# Generated at 2022-06-13 19:33:34.108309
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    docstring_deprecated = DocstringDeprecated(["doesn't matter"], "Description of deprecated item.", "1.2.3")
    print(docstring_deprecated)
    # assert docstring_deprecated.args == ["doesn't matter"]
    # assert docstring_deprecated.description == "Description of deprecated item."
    # assert docstring_deprecated.version == "1.2.3"
    assert docstring_deprecated.args == ["doesn't matter"]
    assert docstring_deprecated.description == "Description of deprecated item."
    assert docstring_deprecated.version == "1.2.3"


test_DocstringDeprecated()

# Generated at 2022-06-13 19:33:37.936938
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    assert DocstringMeta(["param"], "Description").args == ["param"]
    assert DocstringMeta(["param"], "Description").description == "Description"


# Generated at 2022-06-13 19:33:59.192799
# Unit test for constructor of class Docstring
def test_Docstring():
    docstring = Docstring()
    assert docstring.short_description is None
    assert docstring.long_description is None
    assert docstring.blank_after_short_description is False
    assert docstring.blank_after_long_description is False
    assert docstring.meta == []
    params = docstring.params
    assert isinstance(params, list)
    raises = docstring.raises
    assert isinstance(raises, list)
    returns = docstring.returns
    assert returns is None
    deprecation = docstring.deprecation
    assert deprecation is None


# Generated at 2022-06-13 19:34:09.975390
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    args1 = ['param', 'parameter','arg','arg','attribute','key', 'keyword']
    description1= "description"
    arg_name1= "arg"
    type_name1= "int"
    is_optional1= True
    default1= 3
    new_DocstringParam = DocstringParam(args1, description1, arg_name1, type_name1, is_optional1, default1)
    # Unit test the getter of args
    args_result = new_DocstringParam.args
    assert args_result == ['param', 'parameter','arg','arg','attribute','key', 'keyword']
    # Unit test the getter of description
    description_result = new_DocstringParam.description
    assert description_result == "description"
    # Unit test the getter of arg_name
    arg_

# Generated at 2022-06-13 19:34:16.846701
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    item = DocstringParam(args=[1,2,3], description="Just a test object", arg_name="Test", 
    type_name="Nah", is_optional=True, default=None)
    assert item.args == [1,2,3]
    assert item.description == "Just a test object"
    assert item.arg_name == "Test"
    assert item.type_name == "Nah"
    assert item.is_optional == True
    assert item.default == None


# Generated at 2022-06-13 19:34:21.018396
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
     doc = DocstringReturns(['hello', 'world'], 'test', 'str')
     assert doc.args == ['hello', 'world']
     assert doc.description == 'test'
     assert doc.type_name == 'str'


# Generated at 2022-06-13 19:34:24.617187
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    d = DocstringReturns([], 'description', 'type_name', True, 'return_name')
    assert d.description == 'description'
    assert d.type_name == 'type_name'
    assert d.is_generator == True
    assert d.return_name == 'return_name'


# Generated at 2022-06-13 19:34:32.719748
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    test_object = DocstringReturns(args=['arg1', 'arg2'], description="fdsa", type_name="string", is_generator=True)
    assert test_object.args == ['arg1', 'arg2']
    assert test_object.description == "fdsa"
    assert test_object.type_name == "string"
    assert test_object.is_generator == True
    assert test_object.return_name == None
    assert test_object.description == "fdsa"
    test_object.description = "fdsafdsf"
    assert test_object.description == "fdsafdsf"



# Generated at 2022-06-13 19:34:34.016107
# Unit test for constructor of class Docstring
def test_Docstring():
    obj = Docstring()
    assert isinstance(obj, Docstring)



# Generated at 2022-06-13 19:34:46.499952
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
	# Make a dummy description
	description = "A description"
	# Make a dummy type_name
	type_name = "A type"
	# Make a dummy list of arguments
	args = ["arg1", "arg2", "arg3"]
	# Make a dummy is_generator
	is_generator = False
	# Create a DocstringReturns object
	DocstringReturns(args, description, type_name, is_generator)
	# Create a DocstringReturns object
	DocstringReturns(args, description, type_name, is_generator, "name")
	# End unit test
	return 0

# Generated at 2022-06-13 19:34:52.003810
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    """Unit test for constructor of class DocstringRaises."""
    args = ["param", "name"]
    desc = "raises TypeError if value is not an int"
    type_name = "TypeError"
    exc = DocstringRaises(args, desc, type_name)
    assert exc.args == args
    assert exc.description == desc
    assert exc.type_name == type_name



# Generated at 2022-06-13 19:34:55.002731
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    DocstringRaises(["raises"], "description", "type_name")


# Generated at 2022-06-13 19:35:05.647151
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    assert DocstringMeta(['param', 'arg', 'arg_name', 'type_name'], 'description')


# Generated at 2022-06-13 19:35:07.628709
# Unit test for constructor of class ParseError
def test_ParseError():
    try:
        pass
    except ParseError:
        pass



# Generated at 2022-06-13 19:35:09.666076
# Unit test for constructor of class ParseError
def test_ParseError():
    try:
        raise ParseError
    except ParseError:
        assert True
    else:
        assert False


# Generated at 2022-06-13 19:35:14.750828
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    dp = DocstringParam(
        ["param"], "description", "arg", "str", True, "1.3"
    )
    assert dp.args == ["param"]
    assert dp.description == "description"
    assert dp.arg_name == "arg"
    assert dp.type_name == "str"
    assert dp.is_optional == True
    assert dp.default == "1.3"

# Generated at 2022-06-13 19:35:20.590560
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    d=DocstringMeta(['param'], 'Test')

    if d.args==['param']:
        print('DocstringMeta constructor: args: Test passed')
    else:
        print('DocstringMeta constructor: args: Test failed')

    if d.description=='Test':
        print('DocstringMeta constructor: description: Test passed')
    else:
        print('DocstringMeta constructor: description: Test failed')


# Generated at 2022-06-13 19:35:23.083409
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    a = DocstringMeta(['hello world'], "hello world")
    assert a.args == ['hello world']
    assert a.description == "hello world"


# Generated at 2022-06-13 19:35:25.845661
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    meta = DocstringMeta(args=['parameter'], description='A parameter')
    assert isinstance(meta, DocstringMeta)


# Generated at 2022-06-13 19:35:32.910494
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    args = ['args']
    description = "test"
    type_name = 'type'
    is_generator = True
    return_name = 'return'
    docstring_returns = DocstringReturns(args, description, type_name, is_generator, return_name)
    assert docstring_returns.type_name == type_name
    assert docstring_returns.is_generator == is_generator
    assert docstring_returns.return_name == return_name

# Generated at 2022-06-13 19:35:35.313087
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    a = DocstringDeprecated(["deprecated"], "old", "new")
    assert a.description == "old"
    assert a.args == ["deprecated"]
    assert a.version == "new"


# Generated at 2022-06-13 19:35:51.541321
# Unit test for constructor of class Docstring
def test_Docstring():
    '''
    testing the initilization of DocString object
    '''
    ds = Docstring()
    for item in ds.meta:
        if(isinstance(item,DocstringParam)):
            raise ValueError('expected meta to be empty')
        elif(isinstance(item,DocstringRaises)):
            raise ValueError('expected meta to be empty')
        elif(isinstance(item,DocstringReturns)):
            raise ValueError('expected meta to be empty')
        elif(isinstance(item,DocstringDeprecated)):
            raise ValueError('expected meta to be empty')
    if(ds.short_description):
        raise ValueError('expected short description to be empty')
    if(ds.long_description):
        raise ValueError('expected long description to be empty')



# Generated at 2022-06-13 19:36:10.617180
# Unit test for constructor of class ParseError
def test_ParseError():
    try:
        raise ParseError("test")
    except ParseError as e:
        assert str(e) == "test"

# Generated at 2022-06-13 19:36:17.841630
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    """Test function for constructor of class DocstringParam."""
    param_args = ['param', 'arg']
    param_description = 'description of argument'
    param_arg_name = 'arg'
    param_type_name = 'str'
    param_is_optional = True
    param_default = 'arg_default'
    DocstringParam(param_args,
                       param_description,
                       param_arg_name,
                       param_type_name,
                       param_is_optional,
                       param_default)

# Generated at 2022-06-13 19:36:22.568337
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    args = ['deprecated',
            'version']
    description = 'this is a description'
    version = '2.0'
    doc = DocstringDeprecated(args, description, version)

    assert doc.description == description
    assert doc.version == version
    assert doc.args == args


# Generated at 2022-06-13 19:36:24.583004
# Unit test for constructor of class ParseError
def test_ParseError():
  err = ParseError("test")
  assert err != None


# Generated at 2022-06-13 19:36:30.232599
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    ds = DocstringReturns(args=None,description=None,type_name=None,is_generator=False,return_name=None)
    assert ds.type_name is None
    assert ds.description is None
    assert ds.return_name is None


# Generated at 2022-06-13 19:36:33.789795
# Unit test for constructor of class Docstring
def test_Docstring():
    doc=Docstring()
    assert doc.short_description==None
    assert doc.long_description==None
    assert doc.meta==[]
    assert doc.params==[]
    assert doc.raises==[]
    assert doc.returns==None
    assert doc.deprecation==None

# Generated at 2022-06-13 19:36:38.977361
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    m = DocstringRaises(["raises"], "if something happens", "ValueError")
    assert m.type_name == "ValueError"
    assert m.description == "if something happens"
    assert m.args == ["raises"]


# Generated at 2022-06-13 19:36:41.553232
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    docstring = DocstringMeta(["arg:","description:"], "a")
    assert docstring.args == ["arg:","description:"]
    assert docstring.description == "a"


# Generated at 2022-06-13 19:36:45.920175
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    """Test constructor of class DocstringParam."""
    obj = DocstringParam(["param"], "This is a test", "arg", None, None, None)
    assert obj.args == ["param"]
    assert obj.description == "This is a test"
    assert obj.arg_name == "arg"
    assert obj.type_name == None
    assert obj.is_optional == None
    assert obj.default == None


# Generated at 2022-06-13 19:36:47.211558
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    DocstringDeprecated()
    return True

# Generated at 2022-06-13 19:37:21.965977
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    aa = DocstringDeprecated(args=['aa'], description='aa', version='bb')
    assert aa.description == 'aa'
    assert aa.args == ['aa']



# Generated at 2022-06-13 19:37:25.454279
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    a = DocstringMeta([], 'This is a thing')
    assert a.args == []
    assert a.description == 'This is a thing'


# Generated at 2022-06-13 19:37:29.261898
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    args = ['arg', 'description']
    description = 'Description'
    a = DocstringMeta(args, description)
    assert a.args == args
    assert a.description == description


# Generated at 2022-06-13 19:37:32.443684
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    exception = DocstringRaises(['param'], 'description', 'exception')
    assert exception.args == ['param']
    assert exception.description == 'description'
    assert exception.type_name == 'exception'


# Generated at 2022-06-13 19:37:37.597289
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    args = ["param", "arg"]
    description = "description"
    arg_name = "arg_name"
    type_name = "type_name"
    is_optional = "is_optional"
    default = "default"
    test = DocstringParam(args, description, arg_name, type_name, is_optional, default)
    assert test.args == ["param", "arg"]
    assert test.description == "description"
    assert test.arg_name == "arg_name"
    assert test.type_name == "type_name"
    assert test.is_optional == "is_optional"
    assert test.default == "default"


# Generated at 2022-06-13 19:37:39.658476
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    """Unit test for DocstringDeprecated()."""
    DocstringDeprecated(['', ''], '', '1')



# Generated at 2022-06-13 19:37:42.433553
# Unit test for constructor of class ParseError
def test_ParseError():
    """Unit test for constructor of class ParseError."""
    error = ParseError()
    assert error

# Generated at 2022-06-13 19:37:43.327311
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    DocstringDeprecated(["deprecated"], None, None)

# Generated at 2022-06-13 19:37:48.341180
# Unit test for constructor of class Docstring
def test_Docstring():
    docstring = Docstring()
    assert docstring.short_description is None
    assert docstring.long_description is None
    assert docstring.blank_after_short_description is False
    assert docstring.blank_after_long_description is False
    assert docstring.meta == []


# Generated at 2022-06-13 19:37:51.385935
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    rais = DocstringRaises(['args'], 'description', 'type_name')
    assert rais != None

# Generated at 2022-06-13 19:38:59.000351
# Unit test for constructor of class ParseError
def test_ParseError():
    parseError=ParseError()
    assert isinstance(parseError,RuntimeError)
    assert parseError



# Generated at 2022-06-13 19:39:04.323259
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    """Test"""
    param_args = ['param', 'paramter']
    param_description = 'this is an optional parameter'
    param_arg_name = 'arg'
    param_type_name = 'int'
    param_is_optional = True
    param_default = '0'
    param_item = DocstringParam(param_args, param_description, param_arg_name, param_type_name, param_is_optional,
                                param_default)
    assert param_item.args == ['param', 'paramter']
    assert param_item.description == 'this is an optional parameter'
    assert param_item.arg_name == 'arg'
    assert param_item.type_name == 'int'
    assert param_item.is_optional == True
    assert param_item.default == '0'




# Generated at 2022-06-13 19:39:09.649642
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    test = DocstringParam(['param'], 'description', 'arg_name', None, True, 'default')
    assert test.args == ['param']
    assert test.description == 'description'
    assert test.arg_name == 'arg_name'
    assert test.type_name == None
    assert test.is_optional == True
    assert test.default == 'default'


# Generated at 2022-06-13 19:39:12.846143
# Unit test for constructor of class ParseError
def test_ParseError():
    try:
        raise ParseError("example")
    except ParseError as e:
        assert str(e) == "example"


# Generated at 2022-06-13 19:39:15.163235
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    a = DocstringMeta(["param", "arg"], "description")
    assert a.args == ["param", "arg"]
    assert a.description == "description"


# Generated at 2022-06-13 19:39:16.937878
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    DocstringReturns(args=[":return: test"], description="if something happens", type_name="str", is_generator=False, return_name=None)

# Generated at 2022-06-13 19:39:21.944611
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    a_args = ["arg"]
    a_description = "description"
    a_type_name = "type_name"
    test_object = DocstringRaises(a_args, a_description, a_type_name)
    assert test_object.args == a_args
    assert test_object.description == a_description
    assert test_object.type_name == a_type_name


# Generated at 2022-06-13 19:39:24.069274
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    dm = DocstringMeta([], "")
    assert dm.args == []
    assert dm.description == ""
    

# Generated at 2022-06-13 19:39:26.160862
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    assert DocstringRaises(["raises"], "description", "type_name")


# Generated at 2022-06-13 19:39:29.007377
# Unit test for constructor of class ParseError
def test_ParseError():
    # Test successful constructor
    try:
        raise ParseError
    except ParseError:
        pass
    # Test constructor with one argument
    try:
        raise ParseError("test")
    except ParseError:
        pass
