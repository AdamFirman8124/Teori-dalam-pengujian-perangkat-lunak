

# Generated at 2022-06-13 19:30:55.458764
# Unit test for constructor of class Docstring
def test_Docstring():
    """Unit test for constructor of class Docstring."""
    d1 = Docstring()
    assert d1.short_description is None



# Generated at 2022-06-13 19:31:03.641574
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    args = ['Returns']
    description = 'This method returns something'
    type_name = 'str'
    is_generator = True
    return_name = 'method'

    expected = DocstringReturns(args, description, type_name, is_generator, return_name)

    assert type(expected) == DocstringReturns
    assert expected.type_name == type_name
    assert expected.description == description
    assert expected.is_generator == is_generator
    assert expected.return_name == return_name
    assert expected.args == args


# Generated at 2022-06-13 19:31:05.732951
# Unit test for constructor of class ParseError
def test_ParseError():
    assert ParseError('testing')

# Generated at 2022-06-13 19:31:13.015878
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    name = "DocstringReturns"
    args = ["raises", "raise", "except", "exception"]
    desc = "some description"
    tn = "type name"
    ig=True
    rn="return name"
    
    dr = DocstringReturns(args, desc, tn, ig, rn)

    assert(dr.description == desc)
    assert(dr.args == args)
    assert(dr.type_name == tn)
    assert(dr.is_generator == ig)
    assert(dr.return_name == rn)
    print("Successfully passed DocstringReturns class test")



# Generated at 2022-06-13 19:31:15.615148
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
  assert DocstringDeprecated(0, 0, 0).description == 0
  assert DocstringDeprecated(0, 0, 0).version == 0
  assert DocstringDeprecated(0, 0, 0).args == 0

# Generated at 2022-06-13 19:31:16.867859
# Unit test for constructor of class Docstring
def test_Docstring():
    Docstring()


# Generated at 2022-06-13 19:31:29.273086
# Unit test for constructor of class DocstringParam
def test_DocstringParam():

    #Test that init functions correctly when all params are None
    init_DocstringParam = DocstringParam(None, None,None,None,None,None)
    assert init_DocstringParam.args is None
    assert init_DocstringParam.description is None
    assert init_DocstringParam.arg_name is None
    assert init_DocstringParam.type_name is None
    assert init_DocstringParam.is_optional is None
    assert init_DocstringParam.default is None

    #Test that init functions correctly when all params are not empty
    init_DocstringParam2 = DocstringParam(['param'], "desc",'arg', 'int', False , 1)
    assert init_DocstringParam2.args == ['param']
    assert init_DocstringParam2.description == "desc"
    assert init_DocstringParam2.arg

# Generated at 2022-06-13 19:31:33.117344
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    args = ["param","name","type_name","description"]
    description = "this is description"
    type_name = "type name"
    r = DocstringRaises(args, description, type_name)
    print(r.args)
    print(r.description)
    print(r.type_name)

if __name__ == '__main__':
    test_DocstringRaises()

# Generated at 2022-06-13 19:31:35.647028
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    x = DocstringReturns([':raises'], 'description', 'type', False)
    assert x.description == 'description'
    print("Passed")

# Generated at 2022-06-13 19:31:40.229565
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    parameters = ["a", "b", "c"]
    description = "Valid description"
    doc_string_meta = DocstringMeta(parameters, description)

    assert doc_string_meta.args == parameters
    assert doc_string_meta.description == description


# Generated at 2022-06-13 19:31:54.872235
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    from typing import List
    from pyqpanda.utils import parse_docstring

    def test_function():
        """
        :param arg: test
        :return: test2
        :raises ValueError: test3
        """
        pass

    doc = parse_docstring(test_function)
    assert doc.short_description is None
    assert doc.long_description is None
    assert doc.blank_after_short_description is False
    assert doc.blank_after_long_description is False
    assert len(doc.meta) == 3
    assert isinstance(doc.meta[0], DocstringParam)
    assert isinstance(doc.meta[1], DocstringReturns)
    assert isinstance(doc.meta[2], DocstringRaises)
    
    

# Generated at 2022-06-13 19:31:59.080320
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    args = ['param', 'arg', 'argument']
    description = 'Description'
    dm = DocstringMeta(args, description)
    assert dm.args == args
    assert dm.description == description



# Generated at 2022-06-13 19:32:03.979459
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    a_DocstringRaises = DocstringRaises(args=[1], description="valueError", type_name='a type')
    a_DocstringRaises.description
    a_DocstringRaises.type_name
    a_DocstringRaises.args[0]


# Generated at 2022-06-13 19:32:09.723517
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    d = DocstringParam(["arg", "description"],"param", "name", "string", "false", "")
    assert d.descriptio == "description"
    assert d.arg_name == "name"
    assert d.type_name == "string"
    assert d.default == ""
    assert d.is_optional == "false"



# Generated at 2022-06-13 19:32:12.890068
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    obj = DocstringMeta(['arg'], 'description')
    assert obj.args == ['arg']
    assert obj.description == 'description'


# Generated at 2022-06-13 19:32:22.788373
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    args = ['param', 'description', 'type_name']
    description = 'description'
    type_name = 'type_name'
    docstringRaises = DocstringRaises(args, description, type_name)
    assert docstringRaises.args == ['param', 'description', 'type_name']
    assert docstringRaises.description == 'description'
    assert docstringRaises.type_name == 'type_name'

test_DocstringRaises()

# Generated at 2022-06-13 19:32:24.191134
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    DocstringMeta(["param"], "description")

# Unit test of constructor of class DocstringParam

# Generated at 2022-06-13 19:32:26.402582
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    args = ['Deprecated']
    desc = 'This is a deprecated feature.'
    version = '1.0.0'
    a = DocstringDeprecated(args, desc, version)


# Generated at 2022-06-13 19:32:30.072920
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    args = ['param']
    description = 'description'
    assert DocstringMeta(args, description) is not None


# Generated at 2022-06-13 19:32:31.001123
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    assert DocstringRaises


# Generated at 2022-06-13 19:32:43.749175
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    args = ['param', 'description']
    description = 'description'
    type_name = 'int'
    is_generator = False

    docstring_returns = DocstringReturns(args, description, type_name, is_generator)

    docstring_returns.args.should.be.equal(['param', 'description'])
    docstring_returns.description.should.be.equal('description')
    docstring_returns.type_name.should.be.equal('int')
    docstring_returns.is_generator.should.be.equal(False)



# Generated at 2022-06-13 19:32:51.193404
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    d = DocstringDeprecated(["deprecated"], "", "1.0")
    assert d.args == ["deprecated"]
    assert d.description == ""
    assert d.version == "1.0"
    assert not d.blank_after_long_description
    assert not d.blank_after_short_description
    assert not d.is_generator
    assert not d.is_optional
    assert not d.type_name
    assert not d.default
    assert not d.return_name
    assert not d.params
    assert not d.raises
    assert not d.returns
    assert not d.deprecation

# Generated at 2022-06-13 19:32:55.650375
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    print("\nTesting Constructor of class DocstringDeprecated\n")
    obj = DocstringDeprecated(['param', 'deprecated'], None, None)
    assert obj.args == ['param', 'deprecated']
    print("Test 1 passed.")
    obj = DocstringDeprecated(['deprecated'], 'Func is deprecated', '1.2.2')
    assert obj.args == ['deprecated']
    print("Test 2 passed.")


# Generated at 2022-06-13 19:33:03.544716
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    d = DocstringParam(
        ['arg'],
        description = 'description',
        arg_name = 'arg_name',
        type_name = 'type_name',
        is_optional = 'is_optional',
        default = 'default'
    )
    assert d.description == 'description'
    assert d.args == ['arg']
    assert d.arg_name == 'arg_name'
    assert d.type_name == 'type_name'
    assert d.is_optional == 'is_optional'
    assert d.default == 'default'

# Generated at 2022-06-13 19:33:07.072285
# Unit test for constructor of class ParseError
def test_ParseError():
    """Test that the constructor of ParseError works as expected.

    See NAPALM-306
    """

    err = ParseError("A short description", "A long description")

    assert getattr(err, "args") == ("A short description", "A long description")

# Generated at 2022-06-13 19:33:14.470454
# Unit test for constructor of class Docstring
def test_Docstring():
    docstring = Docstring()
    assert (docstring.short_description is None)
    assert (docstring.long_description is None)
    assert (docstring.blank_after_short_description is False)
    assert (docstring.blank_after_long_description is False)
    assert (docstring.params == [])
    assert (docstring.raises == [])
    assert (docstring.returns is None)
    assert (docstring.deprecation is None)


# Generated at 2022-06-13 19:33:16.463046
# Unit test for constructor of class ParseError
def test_ParseError():
    A = ParseError("A")
    assert str(A) == "A"


# Generated at 2022-06-13 19:33:17.763357
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    assert isinstance(DocstringParam([], ""), DocstringMeta)


# Generated at 2022-06-13 19:33:23.496033
# Unit test for constructor of class Docstring
def test_Docstring():
    d = Docstring()
    assert d.short_description is None
    assert d.long_description is None
    assert d.blank_after_short_description is False
    assert d.blank_after_long_description is False
    assert d.meta == []
    assert d.params == []
    assert d.raises == []
    return



# Generated at 2022-06-13 19:33:29.671632
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    docstringParam = DocstringParam([],"","","",False,"")

    assert docstringParam
    assert len(docstringParam) == 0
    assert len(docstringParam.args) == 0
    assert len(docstringParam.description) == 0
    assert len(docstringParam.arg_name) == 0
    assert len(docstringParam.type_name) == 0
    assert len(docstringParam.is_optional) == 0
    assert len(docstringParam.default) == 0

# Generated at 2022-06-13 19:33:50.071565
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    dp = DocstringParam(['param'], 'This is the id of the ' +
                                    'representation of this table.',
                        'id', 'str', False, None)
    # Test for the args property
    args = dp.args
    assert args == ['param']
    # Test for the description property
    description = dp.description
    assert description == 'This is the id of the representation of this table.'
    # Test for the arg_name property
    arg_name = dp.arg_name
    assert arg_name == 'id'
    # Test for the type_name property
    type_name = dp.type_name
    assert type_name == 'str'
    # Test for the is_optional property
    is_optional = dp.is_optional
    assert is_optional == False
    # Test

# Generated at 2022-06-13 19:33:55.772284
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    args = ["param", "arg", "name"]
    description = "This is description of parameter."
    arg_name = "name"
    type_name = "int"
    is_optional = True
    default = None
    DocstringParam(args, description, arg_name, type_name, is_optional, default)


# Generated at 2022-06-13 19:34:01.176504
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    x = DocstringRaises(args = ['arg1', 'arg2'], description = "A description", type_name = 'string')
    assert x.args == ['arg1', 'arg2']
    assert x.description == "A description"
    assert x.type_name == 'string'


# Generated at 2022-06-13 19:34:06.309628
# Unit test for constructor of class Docstring
def test_Docstring():
    docstring = Docstring()
    assert docstring.short_description is None
    assert docstring.long_description is None
    assert docstring.blank_after_short_description is False
    assert docstring.blank_after_long_description is False
    assert docstring.meta == []



# Generated at 2022-06-13 19:34:12.638569
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    myDocstringParam = DocstringParam(["param", "arg", "argument", "attribute", "key", "keyword"],
                                      "description", "arg_name", "type_name", True, "default")

    assert myDocstringParam.args == ["param", "arg", "argument", "attribute", "key", "keyword"]
    assert myDocstringParam.description == "description"
    assert myDocstringParam.arg_name == "arg_name"
    assert myDocstringParam.type_name == "type_name"
    assert myDocstringParam.is_optional == True
    assert myDocstringParam.default == "default"


# Generated at 2022-06-13 19:34:18.778390
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    params = DocstringParam(args=['param'], description="Description", arg_name="arg", type_name="type", is_optional=True, default="Default")
    assert params.args == ['param']
    assert params.description == "Description"
    assert params.arg_name == "arg"
    assert params.type_name == "type"
    assert params.is_optional == True
    assert params.default == "Default"


# Generated at 2022-06-13 19:34:27.307903
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    # Test case 1: normal input
    param = DocstringReturns(["returns"], "some text", "int", True, "my_return")
    assert param.args == ["returns"]
    assert param.description == "some text"
    assert param.type_name == "int"
    assert param.is_generator
    assert param.return_name == "my_return"
    
    # Test case 2: empty input
    param = DocstringReturns(["returns"], "", "", False)
    assert param.args == ["returns"]
    assert param.description == ""
    assert param.type_name == ""
    assert not param.is_generator
    assert param.return_name == None
    
    # Test case 3: type_name is None

# Generated at 2022-06-13 19:34:34.417249
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    a = DocstringParam(['param'], None, 'arg_name', 'type_name', 'is_optional', 'default')
    assert(a.args == ['param'])
    assert(a.description is None)
    assert(a.arg_name == 'arg_name')
    assert(a.type_name == 'type_name')
    assert(a.is_optional == 'is_optional')
    assert(a.default == 'default')
    print('Test for DocstringParam: pass.')

if __name__ == "__main__":
    test_DocstringParam()

# Generated at 2022-06-13 19:34:36.561973
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    with pytest.raises(TypeError):
        DocstringDeprecated()

    with pytest.raises(TypeError):
        DocstringDeprecated(1, 2)

# Generated at 2022-06-13 19:34:47.880599
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    # Testing class constructor with one argument
    test_item = DocstringDeprecated(["deprecated"], "description", "3.0")
    assert test_item.args == ["deprecated"]
    assert test_item.description == "description"
    assert test_item.version == "3.0"

    # Testing class constructor with no arguments
    test_item = DocstringDeprecated([], '', None)
    assert not test_item.args
    assert not test_item.description
    assert test_item.version == None



# Generated at 2022-06-13 19:35:08.200851
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    returns = DocstringReturns(args=[":returns"], description="a number",
                               type_name="int", is_generator=False,
                               return_name="the_number")


# Generated at 2022-06-13 19:35:11.821279
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    args = ["Lol", "Arg Name"]
    description = "A docstring for arg name Lol"
    type_name = "str"
    testRaises = DocstringRaises(args, description, type_name)


# Generated at 2022-06-13 19:35:15.744595
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    args = ["a", "b"]
    description = "test description"
    type_name = "test_typename"

    item = DocstringRaises(args, description, type_name)
    assert isinstance(item, DocstringRaises)
    assert item.args == args
    assert item.description == description
    assert item.type_name == type_name
    return True

# Generated at 2022-06-13 19:35:21.152781
# Unit test for constructor of class Docstring
def test_Docstring():
    s = Docstring()
    s.short_description = "Short description"
    s.long_description = "Long description"
    s.blank_after_short_description = True
    s.blank_after_long_description = True
    s.meta.append("This is a list")
    print("=======================Docstring=======================")
    print("Short description = ", s.short_description)
    print("Long description = ", s.long_description)
    print("Blank after short description = ", s.blank_after_short_description)
    print("Blank after long description = ", s.blank_after_long_description)
    print("Meta: ", s.meta)
    print("=======================Docstring=======================")



# Generated at 2022-06-13 19:35:25.847262
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    args = ['param', 'description']
    description = 'description'
    type_name = 'description'
    assert not type_name
    assert type(args) is list
    assert type(description) is str
    assert type(type_name) is str
    assert type(DocstringRaises) is type



# Generated at 2022-06-13 19:35:30.631572
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    a = DocstringDeprecated(['v'], 'd', '0.0')
    assert a.args == ['v']
    assert a.description == 'd'
    assert a.version == '0.0'


# Generated at 2022-06-13 19:35:35.834619
# Unit test for constructor of class ParseError
def test_ParseError():
    """
    Test that the constructor of the class ParseError works as intended.
    """
    try:
        raise ParserError('Test')
    except ParseError:
        return
    except Exception:
        assert False



# Generated at 2022-06-13 19:35:44.205267
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    dr = DocstringReturns(["returns", "raises"], "description", "type_name", True, False)
    assert dr.args == ["returns", "raises"]
    assert dr.description == "description"
    assert dr.type_name == "type_name"
    assert dr.is_generator == True
    assert dr.return_name == None

# Generated at 2022-06-13 19:35:46.511938
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    args=['param']
    description = 'hi'
    d = DocstringMeta(args, description)
    assert d.args==['param']
    assert d.description=='hi'


# Generated at 2022-06-13 19:35:50.308738
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    returns = DocstringReturns(["a","b"], "description", "type", True, "name")
    assert returns.description == "description"
    assert returns.is_generator == True
    assert returns.return_name == "name"
    assert returns.type_name == "type"
    
    

# Generated at 2022-06-13 19:36:26.140327
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    """Test Construction of 'DocstringMeta'"""
    test = DocstringMeta(["param","arg"], "description")
    assert test.args == ["param","arg"]
    assert test.description == "description"


# Generated at 2022-06-13 19:36:28.701464
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    d = DocstringDeprecated(["param","key"], "desc", "1.0")



# Generated at 2022-06-13 19:36:30.153422
# Unit test for constructor of class Docstring
def test_Docstring():
    Docstring()

# Generated at 2022-06-13 19:36:41.514058
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    param1 = DocstringParam(
        args=['param'],
        description='blabla',
        arg_name='bla',
        type_name='param',
        is_optional=False,
        default= None,
    )
    assert isinstance(param1, DocstringMeta)
    assert param1.args == ['param']
    assert param1.description == 'blabla'
    assert param1.arg_name == 'bla'
    assert param1.type_name == 'param'
    assert param1.is_optional == False
    assert param1.default == None


# Generated at 2022-06-13 19:36:43.661849
# Unit test for constructor of class ParseError
def test_ParseError():
    try:
        raise ParseError()
    except ParseError:
        pass
    else:
        print("ParseError constructor test failed")


# Generated at 2022-06-13 19:36:51.196156
# Unit test for constructor of class ParseError
def test_ParseError():
    try:
        raise ParseError("blah")
    except ParseError as e:
        assert(e.args[0] == "blah")
    try:
        raise ParseError("foo", "bar")
    except ParseError as e:
        assert(e.args[0] == "foo")
        assert(e.args[1] == "bar")


# Generated at 2022-06-13 19:36:53.199367
# Unit test for constructor of class ParseError
def test_ParseError():
    try:
        p = ParseError("ok")
    except:
        pass



# Generated at 2022-06-13 19:37:00.456305
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    doc_param= DocstringParam(args=["arg","description"],description="dasdasdasd",arg_name=arg, type_name=None, is_optional=False, default=None)
    assert doc_param.args==["arg","description"]
    assert doc_param.description == "dasdasdasd"
    assert doc_param.arg_name == "arg"
    assert doc_param.type_name == None
    assert doc_param.is_optional == False
    assert doc_param.default == None


# Generated at 2022-06-13 19:37:09.018420
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    # test1
    args = ['args']
    description = 'description'
    type_name = 'type_name'
    is_generator = 'is_generator'
    return_name = 'return_name'
    assert str(DocstringReturns(args, description, type_name, is_generator, return_name)) == "args, description, type_name, is_generator, return_name"
    # test2
    args = ['args']
    description = 'description'
    type_name = 'type_name'
    is_generator = 'is_generator'
    assert str(
        DocstringReturns(args, description, type_name, is_generator)) == "args, description, type_name, is_generator"
    # test3
    args = ['args']
    description = 'description'

# Generated at 2022-06-13 19:37:12.577412
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    obj1 = DocstringParam(['param', 'arg'], 'description', 'arg', 'str', True, 'None')
    assert obj1.args == ['param', 'arg']
    assert obj1.description == 'description'
    assert obj1.arg_name == 'arg'
    assert obj1.type_name == 'str'
    assert obj1.is_optional == True
    assert obj1.default == 'None'


# Generated at 2022-06-13 19:38:24.301686
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    a = DocstringMeta("a", "b")
    assert a.args == "a"
    assert a.description == "b"


# Generated at 2022-06-13 19:38:26.672743
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    try:
        d = DocstringRaises(['raises'], 'raises an exception', 'ValueError')
    except (TypeError, NameError, ValueError, SyntaxError) as error:
        print(error)
    return

test_DocstringRaises()

# Generated at 2022-06-13 19:38:39.412127
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    """
    Create a test instance of DocstringParam to verify that the constructor is working properly.
    """
    # define input values
    args = ["param", "parameter", "arg", "argument"]
    description = "The description"
    arg_name = "argu"
    type_name = "typ"
    is_optional = True
    default = None

    # construct the instance to test
    test_instance = DocstringParam(args, description, arg_name, type_name, is_optional, default)

    # verify that the constructed instance has expected values
    assert(args == test_instance.args)
    assert(description == test_instance.description)
    assert(arg_name == test_instance.arg_name)
    assert(type_name == test_instance.type_name)

# Generated at 2022-06-13 19:38:46.310831
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    sample_args = ["Deprecated:", "param1", "param2", "param3"]
    sample_description = "Testing"
    sample_version = "3.3"
    sample_object = DocstringDeprecated(sample_args, sample_description, sample_version)

    assert sample_object.args == sample_args
    assert sample_object.description == sample_description
    assert sample_object.version == sample_version


# Generated at 2022-06-13 19:38:54.541593
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    # Create object of type DocstringParam
    param = DocstringParam(["param", "arg"], "description", "arg", None, None, None)

    # Assert that all of the parameters were set properly
    assert param.args == ["param", "arg"]
    assert param.description == "description"
    assert param.arg_name == "arg"
    assert param.type_name is None
    assert param.is_optional is None
    assert param.default is None


# Generated at 2022-06-13 19:38:56.540963
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    assert DocstringRaises([], "", "").args == []
    assert DocstringRaises([], "", "").description == ""
    assert DocstringRaises([], "", "").type_name 

# Generated at 2022-06-13 19:38:59.209715
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    def show():
        pass
    d = DocstringRaises(['raises', 'exception'], 'exception description', 'Exception')
    show.__name__ = 'show'
    show.__doc__ = str(d)
    print(show.__doc__)

# Generated at 2022-06-13 19:38:59.863148
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    DocstringReturns([], "", "", True)

# Generated at 2022-06-13 19:39:05.286992
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    """Unit test for constructor of class DocstringReturns."""
    params = ["param", "description"]
    description = ["description"]
    type_name = ["typename"]
    is_generator = True
    return_name = "return_name"
    DocstringReturns(params, description, type_name, is_generator, return_name)



# Generated at 2022-06-13 19:39:08.913359
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    d = DocstringDeprecated(['deprecated'], 'test', 'test')
    assert d.args == ['deprecated']
    assert d.description == 'test'
    assert d.version == 'test'
