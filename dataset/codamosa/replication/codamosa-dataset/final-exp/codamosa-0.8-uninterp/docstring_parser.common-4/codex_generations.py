

# Generated at 2022-06-13 19:30:52.363357
# Unit test for constructor of class Docstring
def test_Docstring():
    c = Docstring()
    assert c.short_description is None
    assert c.long_description is None
    assert c.blank_after_short_description is False
    assert c.blank_after_long_description is False
    assert c.meta == []



# Generated at 2022-06-13 19:30:57.535190
# Unit test for constructor of class Docstring
def test_Docstring():
    docstring=Docstring()
    docstring.short_description="This is a test."
    print('Short description:', docstring.short_description)
    print('Long description:', docstring.long_description)
    print('Parameters:')
    for param in docstring.params:
        print(param)
    print('Exceptions:')
    for param in docstring.raises:
        print(param)
    print('Returns:')
    print(docstring.returns) # None
    print('Deprecation:')
    print(docstring.deprecation) # None

if __name__ == '__main__':
    test_Docstring()

# Generated at 2022-06-13 19:30:59.573657
# Unit test for constructor of class ParseError
def test_ParseError():
    try:
        raise ParseError("Test")
    except ParseError:
        pass
    return


# Generated at 2022-06-13 19:31:00.993046
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    dm = DocstringMeta()



# Generated at 2022-06-13 19:31:03.153987
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    assert isinstance(DocstringMeta(['param'], 'description'), DocstringMeta)


# Generated at 2022-06-13 19:31:09.880591
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    d = DocstringParam(['param'], 'description', 'arg', 'type', True, 'default')
    assert d.args == ['param']
    assert d.description == 'description'
    assert d.arg_name == 'arg'
    assert d.type_name == 'type'
    assert d.is_optional == True
    assert d.default == 'default'


# Unit test fo constructor of class DocstringReturns

# Generated at 2022-06-13 19:31:11.029836
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    DocstringRaises(["param, "], "test description", "test type name")

# Generated at 2022-06-13 19:31:14.086407
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    assert DocstringMeta(args=['parameter'], description='description').args == ['parameter']
    assert DocstringMeta(args=['parameter'], description='description').description == 'description'


# Generated at 2022-06-13 19:31:15.341146
# Unit test for constructor of class ParseError
def test_ParseError():
    try:
        raise ParseError("test")
    except ParseError:
        pass

# Generated at 2022-06-13 19:31:20.686379
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    p = DocstringParam(['param'], 'argument 1', 'Test', 'int', False, '5')
    assert p.args == ['param']
    assert p.description == 'argument 1'
    assert p.arg_name == 'Test'
    assert p.type_name == 'int'
    assert not p.is_optional
    assert p.default == '5'
    # Test __str__
    assert str(p) == "DocstringParam(['param'], 'argument 1', 'Test', 'int', False, '5')"

test_DocstringParam()


# Generated at 2022-06-13 19:31:24.921475
# Unit test for constructor of class ParseError
def test_ParseError():
    ParseError('a')


# Generated at 2022-06-13 19:31:31.279600
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    ex = DocstringRaises(args=[], description="test", type_name="test")
    print(ex)
    assert ex.type_name == "test", \
        "Invalid description"
    assert ex.args == [], \
        "Invalid args"
    assert ex.description == "test", \
        "Invalid description"
    print("DocstringRaises class constructor tests passed.")


# Generated at 2022-06-13 19:31:42.749913
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    ''' 
    Test if the constructor of class DocstringDeprecated is working properly
    ''' 
    # create an instance of the constructor 
    # Class: DocstringDeprecated
    # params: ["args": T.List[str], "description": T.Optional[str], "version": T.Optional[str]]

# Generated at 2022-06-13 19:31:44.378327
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    DocstringDeprecated(args="", description="", version="")

# Generated at 2022-06-13 19:31:49.150797
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    args = ["deprecated"]
    description = "This function is deprecated."
    version = "0.2.0"
    docstring_deprecation = DocstringDeprecated(args, description, version)
    assert isinstance(docstring_deprecation, DocstringDeprecated)
    assert docstring_deprecation.description == description
    assert docstring_deprecation.args == args
    assert docstring_deprecation.version == version
    
if __name__ == '__main__':
    test_DocstringDeprecated()

# Generated at 2022-06-13 19:31:54.414212
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    my_docstring = Docstring()
    assert my_docstring.short_description is None
    assert my_docstring.long_description is None
    assert my_docstring.blank_after_short_description == False
    assert my_docstring.blank_after_long_description == False
    assert my_docstring.meta == []

# Generated at 2022-06-13 19:31:56.470232
# Unit test for constructor of class ParseError
def test_ParseError():
    with pytest.raises(RuntimeError):
        raise ParseError()

# Generated at 2022-06-13 19:32:01.239502
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    docstring_meta = DocstringMeta(args = ['arg'], description = "description")
    assert type(docstring_meta) == DocstringMeta
    assert docstring_meta.args == ['arg']
    assert docstring_meta.description == "description"


# Generated at 2022-06-13 19:32:03.447564
# Unit test for constructor of class ParseError
def test_ParseError():
    try:
        raise ParseError('failed')
    except ParseError as e:
        assert True

# Generated at 2022-06-13 19:32:08.421453
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    test1 = DocstringDeprecated(['deprecated'], 'This function is deprecated', 'since v1.0')
    assert test1.version == 'since v1.0' and test1.description == test1.description



# Generated at 2022-06-13 19:32:17.715745
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    assert(DocstringReturns(["arg1"], "description", "type_name", True) 
            ==
           DocstringReturns(args = ["arg1"], 
                            description = "description", 
                            type_name = "type_name", 
                            is_generator = True))


# Generated at 2022-06-13 19:32:21.753093
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    args = ["arg"]
    description = "description"
    type_name = "type_name"
    DocstringRaises(args, description, type_name)

# Generated at 2022-06-13 19:32:23.841822
# Unit test for constructor of class ParseError
def test_ParseError():
    err = ParseError("test")
    assert str(err) == "test"
    assert repr(err) == "test"
    assert type(err) is ParseError


# Generated at 2022-06-13 19:32:26.702624
# Unit test for constructor of class Docstring
def test_Docstring():
    ds = Docstring()
    assert ds.short_description is None
    assert ds.long_description is None
    assert ds.blank_after_short_description is False
    assert ds.blank_after_long_description is False
    assert ds.meta == []



# Generated at 2022-06-13 19:32:31.936704
# Unit test for constructor of class Docstring
def test_Docstring():
    d = Docstring()

    assert(d.short_description is None)
    assert(d.long_description is None)
    assert(d.blank_after_short_description is False)
    assert(d.blank_after_long_description is False)
    assert(d.meta == [])



# Generated at 2022-06-13 19:32:43.620763
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    assert DocstringReturns([':returns', ':return', 'returns', 'return'], 'This is the return', 'This is the type', False).description == 'This is the return'
    assert DocstringReturns([':returns', ':return', 'returns', 'return'], 'This is the return', 'This is the type', False).type_name == 'This is the type'
    assert DocstringReturns([':returns', ':return', 'returns', 'return'], 'This is the return', 'This is the type', False).args == [':returns', ':return', 'returns', 'return']
    assert DocstringReturns([':returns', ':return', 'returns', 'return'], 'This is the return', 'This is the type', False).is_generator == False

# Generated at 2022-06-13 19:32:45.343892
# Unit test for constructor of class Docstring
def test_Docstring():
    doc = Docstring()
    assert isinstance(doc, Docstring)



# Generated at 2022-06-13 19:32:46.892639
# Unit test for constructor of class Docstring
def test_Docstring():
    docstring = Docstring()
    assert not docstring.short_description
    assert not docstring.long_description



# Generated at 2022-06-13 19:32:49.522854
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    dsd = DocstringDeprecated(["a"], "desc", "4")
    assert dsd.args == ["a"]
    assert dsd.description == "desc"
    assert dsd.version == "4"


# Generated at 2022-06-13 19:32:51.038067
# Unit test for constructor of class ParseError
def test_ParseError():
    print("Constructor of class ParseError")


#Unit test for constructor of class DocstringMeta

# Generated at 2022-06-13 19:33:00.059447
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    # pylint:disable=unused-variable
    t_list_str = [
        ["param", "arg", "type_name", "default"],
        None,
        "abc",
        "abc",
        None,
        None
    ]

    t_DocstringParam = DocstringParam(*t_list_str)

# Generated at 2022-06-13 19:33:04.284355
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    args = []
    description = "The given number is less than the lower bound."
    type_name = "ValueError"
    dsr = DocstringRaises(args, description, type_name)

    assert dsr.args == []
    assert dsr.description == description
    assert dsr.type_name == type_name



# Generated at 2022-06-13 19:33:07.637846
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    d=DocstringMeta(["param","test"], "An example")
    assert d.args==["param","test"]
    assert d.description=="An example"



# Generated at 2022-06-13 19:33:12.182629
# Unit test for constructor of class Docstring
def test_Docstring():
    ds = Docstring()
    assert(ds.short_description is None)
    assert(ds.long_description is None)
    assert(ds.blank_after_short_description is False)
    assert(ds.blank_after_long_description is False)
    assert(ds.meta == [])


# Generated at 2022-06-13 19:33:16.073631
# Unit test for constructor of class Docstring
def test_Docstring():
    doc = Docstring()
    print(doc.short_description)
    print(doc.long_description)
    print(doc.blank_after_short_description)
    print(doc.blank_after_long_description)
    print(doc.meta)

# Generated at 2022-06-13 19:33:18.194203
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    try:
        test = DocstringRaises([],None,None)
    except Exception:
        assert False
    assert True


# Generated at 2022-06-13 19:33:20.347087
# Unit test for constructor of class ParseError
def test_ParseError():
    error = ParseError("message")
    assert error.args[0] == "message"


# Generated at 2022-06-13 19:33:27.278978
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    docstring_param = DocstringParam(["param"], "description", 
    "arg_name", "type_name", True, "default")
    assert docstring_param.args == ["param"]
    assert docstring_param.description == "description"
    assert docstring_param.arg_name == "arg_name"
    assert docstring_param.type_name == "type_name"
    assert docstring_param.is_optional == True
    assert docstring_param.default == "default"


# Generated at 2022-06-13 19:33:31.918653
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    test_DocstringRaises = DocstringRaises(["raise","raises","except","exception"], "description", "type_name")
    assert test_DocstringRaises.args == ["raise","raises","except","exception"]
    assert test_DocstringRaises.description == "description"
    assert test_DocstringRaises.type_name == "type_name"


# Generated at 2022-06-13 19:33:36.765605
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    print("- Testing DocstringReturns class")

    # create instance
    ds = DocstringReturns(["returns"], "an example for a return value", None, None)

    # check if instance is created
    print("- check if instance is created")
    assert ds != None

    # check if args is set
    print("- check if args is set")
    assert ds.args != None

    # check if description is set
    print("- check if description is set")
    assert ds.description != None


# Generated at 2022-06-13 19:33:42.099361
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    docstringParam = DocstringParam(None, None, None, None, None, None)
    print(docstringParam)


# Generated at 2022-06-13 19:33:45.425665
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    DocstringParam(['param', 'arg', 'argument', 'attribute', 'key', 'keyword'], 'test description', 'arg_name', 'type_name', True, 'test default')


# Generated at 2022-06-13 19:33:47.337532
# Unit test for constructor of class ParseError
def test_ParseError():
    a = ParseError()
    str(a)


# Generated at 2022-06-13 19:33:51.330236
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
	args = ["test"]
	description = "Here is the description"
	doc_meta = DocstringMeta(args, description)
	assert doc_meta.args == ["test"]
	assert doc_meta.description == "Here is the description"


# Generated at 2022-06-13 19:33:54.002096
# Unit test for constructor of class Docstring
def test_Docstring():
    new_docstring = Docstring
    assert new_docstring != None
#result: PASS
#Unit test for return value of function __init__()

# Generated at 2022-06-13 19:33:59.645392
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    args = ['param']
    description = 'whatever'
    arg_name = 'x'
    type_name = 'str'
    is_optional = True
    default = 'blah'
    x = DocstringParam(args, description, arg_name, type_name, is_optional, default)
    assert x.arg_name == arg_name
    assert x.type_name == type_name
    assert x.is_optional == is_optional
    assert x.default == default


# Generated at 2022-06-13 19:34:02.373434
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    """Test if DocstringReturns is instantiated properly."""
    assert DocstringReturns(['returns'], "Returns the following", 'float', False)


# Generated at 2022-06-13 19:34:08.497920
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    args = ["param", "arg", "argument", "attribute", "key", "keyword"]
    description = "description"
    type_name = "type_name"
    is_generator = "is_generator"
    return_name = "return_name"
    a = DocstringReturns(args, description, type_name, is_generator, return_name)
    return a


# Generated at 2022-06-13 19:34:11.239140
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    l = list()
    d = str()
    a = str()
    t = None
    i = None
    de = None
    assert DocstringParam(l,d,a,t,i,de)


# Generated at 2022-06-13 19:34:13.920029
# Unit test for constructor of class ParseError
def test_ParseError():
    try:
        raise ParseError('my error text')
    except ParseError as e:
        assert e.args[0]=='my error text'

# Generated at 2022-06-13 19:34:21.970140
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    a = DocstringReturns(['raises', 'ValueError'], "if something happens", None)
    assert a.args == ['raises', 'ValueError']
    assert a.description == "if something happens"
    assert a.type_name == None
    assert a.is_generator == False
    assert a.return_name == None


# Generated at 2022-06-13 19:34:23.886624
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    assert DocstringDeprecated(['param', 'erro'], 'stuff', '3.2.2') is not None


# Generated at 2022-06-13 19:34:33.484049
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    assert DocstringReturns([], None, None, True).type_name is None
    assert DocstringReturns(["arg"], None, None, False).type_name is None
    assert DocstringReturns(["arg"], "description", None, True).type_name is None
    assert DocstringReturns(["arg"], "description", "name", False).type_name is None
    assert DocstringReturns(["arg"], None, "name", True).type_name is None
    assert DocstringReturns(["arg"], "description", None, False).type_name is None
    assert DocstringReturns(["arg"], None, "name", False).type_name is None
    assert DocstringReturns(["arg"], "description", "name", True).type_name is not None


# Generated at 2022-06-13 19:34:36.135604
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    args = ['arg', 'argument']
    description = 'desc'
    type_name = 'str'
    assert DocstringRaises(args, description, type_name) is not None


# Generated at 2022-06-13 19:34:38.473499
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    param = DocstringParam(["arg"], "description", "arg_name", "type_name", True, 2)
    assert param.is_optional == True
    assert param.default == 2


# Generated at 2022-06-13 19:34:39.694745
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
	d = DocstringDeprecated('test','test','test')
	assert d.args=='test'


# Generated at 2022-06-13 19:34:51.064326
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    # Given
    description = "This is a description"

    # When
    docstringParam = DocstringParam(["param"], description, "arg", "str", True, None)

    # Then
    assert docstringParam.args == ["param"]
    assert docstringParam.description == "This is a description"
    assert docstringParam.arg_name == "arg"
    assert docstringParam.type_name == "str"
    assert docstringParam.is_optional == True
    assert docstringParam.default == None

# Generated at 2022-06-13 19:34:57.412125
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    expected = """
    :deprecated (1.0)
    """
    version = "1.0"
    result = DocstringDeprecated(['deprecated'], None, version).description
    assert expected == result

if __name__ == '__main__':
    test_DocstringDeprecated()

# Generated at 2022-06-13 19:34:59.896555
# Unit test for constructor of class ParseError
def test_ParseError():
    raise ParseError("An error occured during parsing")
    print("test_ParseError passed")



# Generated at 2022-06-13 19:35:01.982325
# Unit test for constructor of class ParseError
def test_ParseError():
    with pytest.raises(RuntimeError):
        raise ParseError


# Generated at 2022-06-13 19:35:06.398982
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    args = []
    description = '''This is the descrition'''
    ds = DocstringMeta(args, description)
    assert ds.args == args
    assert ds.description == description


# Generated at 2022-06-13 19:35:07.188603
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    DocstringReturns(['arg'], 'description', 'type_name', True)

# Generated at 2022-06-13 19:35:10.143486
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    string = DocstringMeta(["string"], "This is a very, very long string.")
    assert string.args == ["string"]
    assert string.description == "This is a very, very long string."


# Generated at 2022-06-13 19:35:21.777639
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    args = ["a","b"]
    description = "desc"
    type_name = "int"
    is_generator = False
    return_name = "val"    
    
    p = DocstringReturns(args, description, type_name, is_generator, return_name)
    assert p.args == ["a", "b"]
    assert p.description == "desc"
    assert p.type_name == "int"
    assert p.is_generator == False
    assert p.return_name == "val"
    assert p.return_name is not None



# Generated at 2022-06-13 19:35:24.745554
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    item = DocstringMeta([], "")
    assert isinstance(item, DocstringMeta)


# Generated at 2022-06-13 19:35:33.481639
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    arg_name = "name"
    type_name = "type"
    is_optional = True
    default = "default"
    args = [arg_name, type_name, is_optional, default]
    description = "description"
    test_object =  DocstringParam(args, description, arg_name, type_name, is_optional, default)
    assert test_object.arg_name == "name"
    assert test_object.type_name == "type"
    assert test_object.description == "description"
    assert test_object.is_optional == True
    assert test_object.default == "default"


# Generated at 2022-06-13 19:35:36.363705
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    print("start to check DocstringReturns:")
    args = []
    desc = None
    type = None
    is_generator = False
    name = None
    dr = DocstringReturns(args,desc,type,is_generator,name)



# Generated at 2022-06-13 19:35:42.089181
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    ds = DocstringParam(["arg"], None, "arg", None, None, "")
    assert ds.description == ""
    assert ds.arg_name == "arg"
    assert ds.default == ""


# Generated at 2022-06-13 19:35:45.386420
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    value = DocstringReturns(list, str, str, bool, str)
    assert value.args == list
    assert value.description == str
    assert value.type_name == str
    assert value.is_generator == bool
    assert value.return_name == str

# Generated at 2022-06-13 19:35:55.465515
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    param = DocstringParam(["param"], None, 'arg', 'int', False, '1')
    assert param.args is ["param"]
    assert param.description is None
    assert param.arg_name is "arg"
    assert param.type_name is "int"
    assert param.is_optional is False
    assert param.default is "1"
    # Test for all other metas
    assert DocstringReturns(["returns"], None, 'int', False, None).args is ["returns"]
    assert DocstringRaises(["raise"], None, "IOError").args is ["raise"]
    assert DocstringDeprecated(["deprecated"], None, '1.0').args is ["deprecated"]

if __name__ == "__main__":
    test_DocstringParam()

# Generated at 2022-06-13 19:36:08.823351
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    Doc = DocstringReturns(
        args=["raises", "NameError"],
        description="This is a description",
        type_name = None,
        is_generator = False,
        return_name=None,
    )
    assert Doc.args == ["raises", "NameError"]
    assert Doc.description == "This is a description"
    assert Doc.type_name == None
    assert Doc.is_generator == False
    assert Doc.return_name == None



# Generated at 2022-06-13 19:36:13.571245
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    print("Testing constructor of class DocstringRaises")
    dr = DocstringRaises([], None, None)
    try:
        assert (isinstance(dr, DocstringRaises))
    except:
        print("Failed to test constructor of class DocstringRaises")
    else:
        print("Successfully tested constructor of class DocstringRaises")

# Generated at 2022-06-13 19:36:21.680826
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    assert DocstringParam(1, 2, 3, 4, 5, 6).args == 1
    assert DocstringParam(1, 2, 3, 4, 5, 6).description == 2
    assert DocstringParam(1, 2, 3, 4, 5, 6).arg_name == 3
    assert DocstringParam(1, 2, 3, 4, 5, 6).type_name == 4
    assert DocstringParam(1, 2, 3, 4, 5, 6).is_optional == 5
    assert DocstringParam(1, 2, 3, 4, 5, 6).default == 6


# Generated at 2022-06-13 19:36:33.040971
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    # Arrange
    args = ["deprecated", "since", "1.0"]
    description = "Deprecated since version 1.0"
    version = "1.0"
    # Act
    actual = DocstringDeprecated(args, description, version)
    # Assert
    assert actual is not None
    assert actual.args == args
    assert actual.description == description
    assert actual.version == version
    assert actual.args[0] == args[0]
    assert actual.args[1] == args[1]
    assert actual.args[2] == args[2]


# Generated at 2022-06-13 19:36:35.529741
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    
    try:
        DocstringDeprecated( 
            args = 'args', 
            description = 'description',
            version = 'version'
        )
    except TypeError:
        assert(False)
    else:
        assert(True)


# Generated at 2022-06-13 19:36:41.313760
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    """Test constructor ,args,description"""
    args = ['arg1', 'arg2']
    description = "desc"
    assert DocstringMeta(args,description).description == "desc"
    assert DocstringMeta(args,description).args == ['arg1', 'arg2']


# Generated at 2022-06-13 19:36:42.348885
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    DocstringDeprecated(["deprecated"], "This method is deprecated.", "v3.2")


# Generated at 2022-06-13 19:36:45.450097
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    ds = DocstringReturns(args=[], description="", type_name=None, is_generator=False, return_name=None)
    print("end")


# Generated at 2022-06-13 19:36:47.278273
# Unit test for constructor of class ParseError
def test_ParseError():
    new = ParseError()
    assert new.args == ()


# Generated at 2022-06-13 19:36:57.872553
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    # given
    args = ["param"]
    description = "description"
    arg_name = "arg_name"
    type_name = "type_name"
    is_optional = True
    default = "default"
    # when
    result = DocstringParam(args, description, arg_name, type_name, is_optional, default)
    # then
    assert result.args == args
    assert result.description == description
    assert result.arg_name == arg_name
    assert result.type_name == type_name
    assert result.is_optional == is_optional
    assert result.default == default


# Generated at 2022-06-13 19:37:09.498422
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    assert DocstringMeta(['param', ':', 'test'], 'test')


# Generated at 2022-06-13 19:37:11.264489
# Unit test for constructor of class ParseError
def test_ParseError():
    """assert the constructor of ParseError."""
    err = ParseError('test-message')
    assert err.args == ('test-message',)



# Generated at 2022-06-13 19:37:21.261589
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
	args = ["param", "parameter", "arg", "argument", "attribute", "key", "keyword"]
	description = "desc"
	type_name = "type"
	is_generator = True
	return_name = "name"
	d = DocstringReturns(args, description, type_name, is_generator, return_name)
	print(d.args)
	print(d.description)
	print(d.type_name)
	print(d.is_generator)
	print(d.return_name)


if __name__ == "__main__":
	test_DocstringReturns()

# Generated at 2022-06-13 19:37:29.454499
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    docstring_param = DocstringParam(["Arguments:", "arg", "description"], "arg", "arg_name", "type_name", True, "default")
    assert docstring_param.is_optional == True
    assert docstring_param.type_name == "type_name"
    assert docstring_param.arg_name == "arg_name"
    assert docstring_param.default == "default"
    assert docstring_param.args == ["Arguments:", "arg", "description"]
    assert docstring_param.description == "arg"


# Generated at 2022-06-13 19:37:31.068988
# Unit test for constructor of class ParseError
def test_ParseError():
    try:
        raise ParseError
    except ParseError:
        return True


# Generated at 2022-06-13 19:37:39.829022
# Unit test for constructor of class Docstring
def test_Docstring():
    docstring = Docstring()
    assert docstring.short_description is None
    assert docstring.long_description is None
    assert docstring.blank_after_short_description == False
    assert docstring.blank_after_long_description == False
    assert docstring.params == []
    assert docstring.raises == []
    assert docstring.returns is None
    assert docstring.deprecation is None


# Generated at 2022-06-13 19:37:42.460790
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    returns = DocstringReturns(args=[], description="", type_name=None, is_generator=True)
    assert isinstance(returns, DocstringReturns)



# Generated at 2022-06-13 19:37:47.349279
# Unit test for constructor of class Docstring
def test_Docstring():
    docstring = Docstring()
    assert docstring.short_description is None
    assert docstring.long_description is None
    assert docstring.blank_after_short_description == False
    assert docstring.blank_after_long_description == False
    assert docstring.meta == []



# Generated at 2022-06-13 19:37:51.229644
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    assert test_df.meta == [
        DocstringDeprecated(
            args=['deprecated'],
            description='',
            version='1.0.0',
        ),
        DocstringReturns(
            args=['returns'],
            description='',
            type_name=None,
            is_generator=False,
        ),
    ]


# Generated at 2022-06-13 19:37:53.146135
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    DocstringParam.__init__(self, args, description, arg_name, type_name, is_optional, default)
    return

# Generated at 2022-06-13 19:38:19.494151
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    a = DocstringDeprecated(args=['a'], description='b', version='c')
    assert a.args == ['a']
    assert a.description == 'b'
    assert a.version == 'c'


# Generated at 2022-06-13 19:38:25.363502
# Unit test for constructor of class Docstring
def test_Docstring():
    docstring = Docstring()
    assert docstring.short_description is None
    assert docstring.long_description is None
    assert docstring.meta == []
    assert docstring.blank_after_short_description == False
    assert docstring.blank_after_long_description == False


# Generated at 2022-06-13 19:38:30.721256
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    args = list(range(5))
    description = "Description"
    test_obj1 = DocstringMeta(args, description)
    args_test = test_obj1.args
    description_test = test_obj1.description
    assert args == args_test
    assert description == description_test


# Generated at 2022-06-13 19:38:33.490493
# Unit test for constructor of class ParseError
def test_ParseError():
    error = ParseError("too many arguments")
    assert not error.args is None


# Generated at 2022-06-13 19:38:35.674104
# Unit test for constructor of class ParseError
def test_ParseError():
    t_instance = ParseError('error')
    assert t_instance._str == 'error'



# Generated at 2022-06-13 19:38:41.579564
# Unit test for constructor of class Docstring
def test_Docstring():
    ds = Docstring()
    assert(ds)
    assert(ds.short_description==None)
    assert(ds.long_description==None)
    assert(ds.blank_after_short_description==False)
    assert(ds.blank_after_long_description==False)
    assert(ds.meta==[])
    assert(ds.params==[])
    assert(ds.raises==[])
    assert(ds.returns==None)
    assert(ds.deprecation==None)

# Generated at 2022-06-13 19:38:55.720435
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    print('test_DocstringReturns')
    args = ['param', 'arg', 'argument', 'attribute', 'key', 'keyword']
    description = 'description of docstring'
    type_name = 'return_type'
    is_generator = False
    return_name = 'return_name'
    d = DocstringReturns(args, description, type_name, is_generator, return_name)
    print(d.args)
    print(d.description)
    print(d.type_name)
    print(d.is_generator)
    print(d.return_name)

if __name__ == "__main__":
    #test __init__ method of the class DocstringParam
    args = ['param', 'arg', 'argument', 'attribute', 'key', 'keyword']

# Generated at 2022-06-13 19:38:58.437052
# Unit test for constructor of class Docstring
def test_Docstring():
    docstring = Docstring()
    assert docstring.short_description is None
    assert docstring.long_description is None
    assert not docstring.blank_after_short_description
    assert not docstring.blank_after_long_description
    assert docstring.meta == []


# Generated at 2022-06-13 19:39:03.915213
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    """Test constructor for DocstringReturns."""
    # Create list for the argument 'args'
    args = ['return', 'returns']
    # Create variable for the argument 'description'
    description = 'return a dictionary of information about the current platform.'
    # Create variable for the argument 'type_name'
    type_name = 'dict'
    # Create variable for the argument 'is_generator'
    is_generator = False
    # Create variable for the argument 'return name'
    return_name = 'sys'
    # Create object 'returns_object'
    returns_object = DocstringReturns(args, description, type_name, is_generator, return_name)
    # Test object 'returns_object'
    assert returns_object.args == ['return', 'returns']

# Generated at 2022-06-13 19:39:07.998504
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    a = DocstringReturns(["returns"], "this is a description", "type", True, "name")
    print(a.type_name)
    print(a.description)
    print(a.is_generator)
    print(a.args)


# Generated at 2022-06-13 19:39:57.803350
# Unit test for constructor of class Docstring
def test_Docstring():
    """Test Docstring constructor."""
    docstring = Docstring()
    assert docstring.short_description is None
    assert docstring.long_description is None
    assert not docstring.blank_after_short_description
    assert not docstring.blank_after_long_description
    assert docstring.params == []
    assert docstring.raises == []
    assert docstring.returns is None
    assert docstring.deprecation is None


# Generated at 2022-06-13 19:39:59.486403
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    args = ["test"]
    description = "testing"
    type_name = "test"
    DocstringRaises(args, description, type_name)

# Generated at 2022-06-13 19:40:02.132023
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    DocstringRaises.__init__(DocstringRaises, ["args"], "description", "type_name")



# Generated at 2022-06-13 19:40:07.047588
# Unit test for constructor of class Docstring
def test_Docstring():
    from pprint import pprint
    ds = Docstring()
    ds.short_description = 'this is short description'
    ds.long_description = 'this is long description'
    ds.blank_after_short_description = True
    ds.blank_after_long_description = False
    ds.meta = [1,2,3,4,5]
    pprint(ds.__dict__)

# Generated at 2022-06-13 19:40:10.678402
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    
    # create a new instance of class DocstringMeta
    dsm = DocstringMeta(["args"], "description")
    # check if the instance is not None
    assert dsm is not None



# Generated at 2022-06-13 19:40:18.122819
# Unit test for constructor of class Docstring
def test_Docstring():
    ds = Docstring()
    assert ds.short_description is None
    assert ds.long_description is None
    assert ds.blank_after_short_description is False
    assert ds.blank_after_long_description is False
    assert ds.meta == []
    assert ds.params == []
    assert ds.raises == []
    assert ds.returns is None
    assert ds.deprecation is None
    #assert ds._blank_after_short_description
    #assert ds._blank_after_long_description
    #assert ds._meta
    #assert ds._params
    #assert ds._raises
    #assert ds._returns
    #assert ds._deprecation

# Generated at 2022-06-13 19:40:19.963994
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    # Unit test is currently broken
    assert 1 == 0


# Generated at 2022-06-13 19:40:25.166708
# Unit test for constructor of class Docstring
def test_Docstring():
    d = Docstring()
    assert d.short_description is None
    assert d.long_description is None
    assert not d.blank_after_short_description
    assert not d.blank_after_long_description
    assert d.meta == []
    assert d.params == []
    assert d.raises == []
    assert d.returns is None
    assert d.deprecation is None



# Generated at 2022-06-13 19:40:31.086432
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    test_args = ['test', 'description']
    test_description = 'test description content'
    test_docstringmeta = DocstringMeta(test_args, test_description)
    assert(test_docstringmeta.args == test_args)
    assert(test_docstringmeta.description == test_description)


# Generated at 2022-06-13 19:40:34.078115
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    doc = DocstringRaises(["raises"], "description", "type")
    assert doc.description == "description"
    assert doc.type_name == "type"
